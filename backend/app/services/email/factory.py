"""Select the email adapter from configuration (plan 06)."""

from __future__ import annotations

from app.core.config import Settings, get_settings
from app.services.email.base import EmailSender
from app.services.email.console import ConsoleEmailSender
from app.services.email.smtp import SmtpEmailSender


def get_email_sender(settings: Settings | None = None) -> EmailSender:
    settings = settings or get_settings()
    backend = settings.email_backend.lower()
    if backend == "smtp":
        return SmtpEmailSender(settings)
    if backend == "console":
        return ConsoleEmailSender()
    raise ValueError(f"Unknown EMAIL_BACKEND: {settings.email_backend!r}")
