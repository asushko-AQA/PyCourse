"""Registration + session-auth business logic (plans 06 and 07).

The service is transport-agnostic: routers translate its domain errors into HTTP
responses. It depends only on repositories, the email-sender abstraction, and
settings — never on FastAPI or the request object.
"""

from __future__ import annotations

import re
from datetime import datetime, timedelta
from dataclasses import dataclass

from app.core.config import Settings
from app.core.security import (
    generate_session_token,
    generate_verification_token,
    hash_session_token,
    hash_password,
    verify_password,
)
from app.models.tables import User, now_utc
from app.repositories.email_verification_repo import EmailVerificationTokenRepo
from app.repositories.session_repo import SessionRepo
from app.repositories.user_repo import UserRepo
from app.services.email.base import EmailSender, render_verification_email


class AuthError(Exception):
    """Base class for registration/verification domain errors."""

    code = "auth_error"


class EmailAlreadyRegistered(AuthError):
    code = "email_already_registered"


class WeakPassword(AuthError):
    code = "weak_password"


class ParentalConsentRequired(AuthError):
    code = "parental_consent_required"


class InvalidVerificationToken(AuthError):
    code = "invalid_token"


class VerificationTokenExpired(AuthError):
    code = "token_expired"


class VerificationTokenUsed(AuthError):
    code = "token_used"


class InvalidCredentials(AuthError):
    code = "invalid_credentials"


class EmailNotVerified(AuthError):
    code = "email_not_verified"


@dataclass(frozen=True)
class SignInResult:
    user: User
    session_token: str
    expires_at: datetime


# A small blacklist of obvious choices; the length + character rules do the
# heavy lifting. Kept deliberately short — this is a kids' learning platform,
# not a bank.
_COMMON_PASSWORDS = frozenset(
    {
        "password",
        "12345678",
        "123456789",
        "qwertyui",
        "password1",
        "iloveyou",
        "letmein1",
    }
)


def validate_password_strength(password: str, *, min_length: int) -> None:
    """Raise WeakPassword with a clear, friendly message if too weak."""
    if len(password) < min_length:
        raise WeakPassword(f"Password must be at least {min_length} characters long.")
    if not re.search(r"[A-Za-z]", password):
        raise WeakPassword("Password must include at least one letter.")
    if not re.search(r"\d", password):
        raise WeakPassword("Password must include at least one number.")
    if password.lower() in _COMMON_PASSWORDS:
        raise WeakPassword("That password is too common — please pick another.")


class AuthService:
    def __init__(
        self,
        *,
        users: UserRepo,
        tokens: EmailVerificationTokenRepo,
        sessions: SessionRepo,
        email_sender: EmailSender,
        settings: Settings,
    ) -> None:
        self._users = users
        self._tokens = tokens
        self._sessions = sessions
        self._email = email_sender
        self._settings = settings

    def register(
        self,
        *,
        email: str,
        password: str,
        is_minor: bool = False,
        guardian_email: str | None = None,
        parental_consent: bool = False,
    ) -> User:
        normalized_email = email.strip().lower()

        if self._users.get_by_email(normalized_email) is not None:
            raise EmailAlreadyRegistered("An account with this email already exists.")

        validate_password_strength(password, min_length=self._settings.password_min_length)

        # COPPA gate: a self-declared under-13 user must supply a guardian email
        # and an explicit consent checkbox before the account can be created.
        if is_minor:
            if not guardian_email:
                raise ParentalConsentRequired(
                    "A parent or guardian email is required for users under 13."
                )
            if not parental_consent:
                raise ParentalConsentRequired(
                    "A parent or guardian must confirm consent for users under 13."
                )

        user = self._users.create_user(
            email=normalized_email,
            password_hash=hash_password(password),
            is_minor=is_minor,
            guardian_email=(guardian_email.strip().lower() if guardian_email else None),
            parental_consent=parental_consent if is_minor else False,
        )

        self._issue_and_send_token(user)
        return user

    def _issue_and_send_token(self, user: User) -> str:
        token = generate_verification_token()
        expires_at = now_utc() + timedelta(hours=self._settings.email_verification_ttl_hours)
        self._tokens.create(user_id=user.id, token=token, expires_at=expires_at)

        verify_url = self._settings.build_verify_url(token)
        # For minors, the confirmation goes to the guardian's inbox.
        recipient = user.guardian_email if (user.is_minor and user.guardian_email) else user.email
        self._email.send(render_verification_email(recipient, verify_url))
        return token

    def verify(self, *, token: str) -> User:
        row = self._tokens.get_by_token(token)
        if row is None:
            raise InvalidVerificationToken("This verification link is not valid.")
        if row.consumed_at is not None:
            raise VerificationTokenUsed("This verification link has already been used.")
        if _aware(row.expires_at) < now_utc():
            raise VerificationTokenExpired("This verification link has expired.")

        user = self._users.get(row.user_id)
        if user is None:
            raise InvalidVerificationToken("This verification link is not valid.")

        self._tokens.consume(row)
        if user.email_verified_at is None:
            user = self._users.mark_email_verified(user)
        return user

    def sign_in(self, *, email: str, password: str) -> SignInResult:
        normalized_email = email.strip().lower()
        user = self._users.get_by_email(normalized_email)
        if user is None or not verify_password(password, user.password_hash):
            raise InvalidCredentials("Email or password is incorrect.")
        if user.email_verified_at is None:
            raise EmailNotVerified("Please verify your email before signing in.")

        session_token = generate_session_token()
        expires_at = now_utc() + timedelta(hours=self._settings.session_ttl_hours)
        self._sessions.create_session(
            user_id=user.id,
            session_token_hash=hash_session_token(session_token),
            expires_at=expires_at,
        )
        return SignInResult(user=user, session_token=session_token, expires_at=expires_at)

    def sign_out(self, *, session_token: str | None) -> None:
        if not session_token:
            return
        self._sessions.delete_by_token_hash(hash_session_token(session_token))


def _aware(value):
    """SQLite may return naive datetimes; treat them as UTC for comparison."""
    if value.tzinfo is None:
        from datetime import timezone

        return value.replace(tzinfo=timezone.utc)
    return value
