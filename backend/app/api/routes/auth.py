"""Registration + email-verification endpoints (plan 06).

Sign-in / session issuance is plan 07; these endpoints only create accounts and
confirm email ownership.
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps import auth_service
from app.schemas.auth import (
    RegisterRequest,
    RegisterResponse,
    VerifyRequest,
    VerifyResponse,
)
from app.services.auth_service import (
    AuthService,
    EmailAlreadyRegistered,
    InvalidVerificationToken,
    ParentalConsentRequired,
    VerificationTokenExpired,
    VerificationTokenUsed,
    WeakPassword,
)

router = APIRouter(prefix="/auth", tags=["auth"])


def _error(status_code: int, code: str, message: str) -> HTTPException:
    return HTTPException(status_code=status_code, detail={"code": code, "message": message})


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
