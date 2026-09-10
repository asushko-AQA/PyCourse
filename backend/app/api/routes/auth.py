"""Auth endpoints (plans 06 + 07): register, verify, sign-in, sign-out, session."""

from __future__ import annotations

from collections import deque
from datetime import datetime, timedelta
from threading import Lock

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from sqlmodel import Session

from app.api.deps import auth_service, current_user, db_session
from app.core.config import Settings, get_settings
from app.models.tables import User, now_utc
from app.repositories.email_verification_repo import EmailVerificationTokenRepo
from app.repositories.user_repo import UserRepo
from app.schemas.auth import (
    DevVerificationLinkResponse,
    RegisterRequest,
    RegisterResponse,
    SessionResponse,
    SessionUser,
    SignInRequest,
    VerifyRequest,
    VerifyResponse,
)
from app.services.auth_service import (
    AuthService,
    EmailNotVerified,
    EmailAlreadyRegistered,
    InvalidCredentials,
    InvalidVerificationToken,
    ParentalConsentRequired,
    VerificationTokenExpired,
    VerificationTokenUsed,
    WeakPassword,
)

router = APIRouter(prefix="/auth", tags=["auth"])

_signin_failures: dict[str, deque[datetime]] = {}
_signin_lock = Lock()


def _error(status_code: int, code: str, message: str) -> HTTPException:
    return HTTPException(status_code=status_code, detail={"code": code, "message": message})


def _session_payload(user: User) -> SessionResponse:
    assert user.email_verified_at is not None
    return SessionResponse(
        user=SessionUser(
            id=user.id,
            email=user.email,
            email_verified_at=user.email_verified_at,
        )
    )


def _signin_key(request: Request, email: str) -> str:
    ip = request.client.host if request.client else "unknown"
    return f"{email.lower()}::{ip}"


def _is_rate_limited(key: str, *, now: datetime, settings: Settings) -> bool:
    cutoff = now - timedelta(seconds=settings.signin_rate_limit_window_seconds)
    with _signin_lock:
        q = _signin_failures.setdefault(key, deque())
        while q and q[0] < cutoff:
            q.popleft()
        return len(q) >= settings.signin_rate_limit_attempts


def _record_signin_failure(key: str, *, now: datetime, settings: Settings) -> None:
    cutoff = now - timedelta(seconds=settings.signin_rate_limit_window_seconds)
    with _signin_lock:
        q = _signin_failures.setdefault(key, deque())
        while q and q[0] < cutoff:
            q.popleft()
        q.append(now)


def _clear_signin_failures(key: str) -> None:
    with _signin_lock:
        _signin_failures.pop(key, None)


@router.post("/register", response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
def register(payload: RegisterRequest, service: AuthService = Depends(auth_service)) -> RegisterResponse:
    try:
        user = service.register(
            email=payload.email,
            password=payload.password,
            is_minor=payload.is_minor,
            guardian_email=payload.guardian_email,
            parental_consent=payload.parental_consent,
        )
    except EmailAlreadyRegistered as exc:
        raise _error(status.HTTP_409_CONFLICT, exc.code, str(exc)) from exc
    except WeakPassword as exc:
        raise _error(status.HTTP_422_UNPROCESSABLE_ENTITY, exc.code, str(exc)) from exc
    except ParentalConsentRequired as exc:
        raise _error(status.HTTP_422_UNPROCESSABLE_ENTITY, exc.code, str(exc)) from exc

    return RegisterResponse(
        user_id=user.id,
        email=user.email,
        verification_required=True,
        is_minor=user.is_minor,
    )


def _do_verify(token: str, service: AuthService) -> VerifyResponse:
    try:
        user = service.verify(token=token)
    except VerificationTokenUsed as exc:
        raise _error(status.HTTP_410_GONE, exc.code, str(exc)) from exc
    except VerificationTokenExpired as exc:
        raise _error(status.HTTP_410_GONE, exc.code, str(exc)) from exc
    except InvalidVerificationToken as exc:
        raise _error(status.HTTP_404_NOT_FOUND, exc.code, str(exc)) from exc

    assert user.email_verified_at is not None
    return VerifyResponse(email=user.email, email_verified_at=user.email_verified_at)


@router.post("/verify", response_model=VerifyResponse)
def verify(payload: VerifyRequest, service: AuthService = Depends(auth_service)) -> VerifyResponse:
    return _do_verify(payload.token, service)


@router.get("/verify", response_model=VerifyResponse)
def verify_via_link(token: str, service: AuthService = Depends(auth_service)) -> VerifyResponse:
    return _do_verify(token, service)


@router.post("/sign-in", response_model=SessionResponse)
def sign_in(
    payload: SignInRequest,
    response: Response,
    request: Request,
    service: AuthService = Depends(auth_service),
    settings: Settings = Depends(get_settings),
) -> SessionResponse:
    key = _signin_key(request, payload.email)
    now = now_utc()
    if _is_rate_limited(key, now=now, settings=settings):
        raise _error(status.HTTP_429_TOO_MANY_REQUESTS, "too_many_attempts", "Too many sign-in attempts.")

    try:
        result = service.sign_in(email=payload.email, password=payload.password)
    except InvalidCredentials as exc:
        _record_signin_failure(key, now=now, settings=settings)
        raise _error(status.HTTP_401_UNAUTHORIZED, exc.code, str(exc)) from exc
    except EmailNotVerified as exc:
        _record_signin_failure(key, now=now, settings=settings)
        raise _error(status.HTTP_403_FORBIDDEN, exc.code, str(exc)) from exc

    _clear_signin_failures(key)
    max_age = int(timedelta(hours=settings.session_ttl_hours).total_seconds())
    response.set_cookie(
        key=settings.session_cookie_name,
        value=result.session_token,
        httponly=True,
        secure=settings.session_cookie_secure,
        samesite="lax",
        max_age=max_age,
        path="/",
    )
    return _session_payload(result.user)


@router.post("/sign-out", status_code=status.HTTP_204_NO_CONTENT)
def sign_out(
    response: Response,
    request: Request,
    service: AuthService = Depends(auth_service),
    settings: Settings = Depends(get_settings),
) -> Response:
    service.sign_out(session_token=request.cookies.get(settings.session_cookie_name))
    response.status_code = status.HTTP_204_NO_CONTENT
    response.delete_cookie(
        key=settings.session_cookie_name,
        path="/",
        httponly=True,
        secure=settings.session_cookie_secure,
        samesite="lax",
    )
    return response


@router.get("/session", response_model=SessionResponse)
def session_bootstrap(user: User = Depends(current_user)) -> SessionResponse:
    return _session_payload(user)


@router.get(
    "/dev/verification-link",
    response_model=DevVerificationLinkResponse,
    tags=["auth", "dev"],
    summary="DEV/console-only: fetch the latest verification link for smoke testing",
)
def dev_verification_link(
    email: str,
    settings: Settings = Depends(get_settings),
    session: Session = Depends(db_session),
) -> DevVerificationLinkResponse:
    """Retrieve the latest unused verification token when ``EMAIL_BACKEND=console``.

    Disabled (404) for any other email backend so production SMTP deployments
    never expose verification links over HTTP.
    """
    if settings.email_backend.lower() != "console":
        raise _error(status.HTTP_404_NOT_FOUND, "not_found", "Not found.")

    normalized = email.strip().lower()
    user = UserRepo(session).get_by_email(normalized)
    if user is None:
        raise _error(status.HTTP_404_NOT_FOUND, "not_found", "No pending verification for this email.")

    token_row = EmailVerificationTokenRepo(session).get_latest_active_for_user(user.id)
    if token_row is None:
        raise _error(status.HTTP_404_NOT_FOUND, "not_found", "No pending verification for this email.")

    return DevVerificationLinkResponse(
        email=normalized,
        verify_url=settings.build_verify_url(token_row.token),
        token=token_row.token,
    )
