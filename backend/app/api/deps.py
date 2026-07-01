"""Shared FastAPI dependencies."""

from __future__ import annotations

from collections.abc import Generator

from fastapi import Depends, HTTPException, Request, status
from sqlmodel import Session

from app.core.config import Settings, get_settings
from app.core.security import hash_session_token
from app.core.db import get_session
from app.models.tables import User, now_utc
from app.repositories.email_verification_repo import EmailVerificationTokenRepo
from app.repositories.session_repo import SessionRepo
from app.repositories.user_repo import UserRepo
from app.services.auth_service import AuthService
from app.services.email.base import EmailSender
from app.services.email.factory import get_email_sender


def db_session() -> Generator[Session, None, None]:
    yield from get_session()


def email_sender(settings: Settings = Depends(get_settings)) -> EmailSender:
    return get_email_sender(settings)


def auth_service(
    session: Session = Depends(db_session),
    sender: EmailSender = Depends(email_sender),
    settings: Settings = Depends(get_settings),
) -> AuthService:
    return AuthService(
        users=UserRepo(session),
        tokens=EmailVerificationTokenRepo(session),
        sessions=SessionRepo(session),
        email_sender=sender,
        settings=settings,
    )


def _as_utc(value):
    if value.tzinfo is None:
        from datetime import timezone

        return value.replace(tzinfo=timezone.utc)
    return value


def _unauthorized() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={"code": "unauthorized", "message": "Authentication required."},
    )


def current_user(
    request: Request,
    session: Session = Depends(db_session),
    settings: Settings = Depends(get_settings),
) -> User:
    token = request.cookies.get(settings.session_cookie_name)
    if not token:
        raise _unauthorized()

    sessions = SessionRepo(session)
    users = UserRepo(session)
    row = sessions.get_by_token_hash(hash_session_token(token))
    if row is None:
        raise _unauthorized()

    if _as_utc(row.expires_at) < now_utc():
        sessions.delete(row)
        raise _unauthorized()

    user = users.get(row.user_id)
    if user is None:
        sessions.delete(row)
        raise _unauthorized()

    sessions.touch(row)
    return user
