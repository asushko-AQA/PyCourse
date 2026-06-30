"""Shared FastAPI dependencies."""

from __future__ import annotations

from collections.abc import Generator

from fastapi import Depends
from sqlmodel import Session

from app.core.config import Settings, get_settings
from app.core.db import get_session
from app.repositories.email_verification_repo import EmailVerificationTokenRepo
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
        email_sender=sender,
        settings=settings,
    )
