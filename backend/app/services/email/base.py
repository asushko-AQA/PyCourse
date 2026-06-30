"""Email-sender abstraction (plan 06).

The backend never hard-codes an email vendor. Business logic depends only on the
`EmailSender` protocol; the concrete adapter (console for dev, SMTP for prod) is
selected by environment via `get_email_sender()`.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class EmailMessage:
    to: str
    subject: str
    text_body: str


class EmailSender(Protocol):
    def send(self, message: EmailMessage) -> None:
        """Deliver `message`. Implementations must not raise on transient
        delivery issues being unknown; they may raise on hard misconfiguration."""
        ...


def render_verification_email(to: str, verify_url: str) -> EmailMessage:
    """Build the verification email body shared by every adapter."""
    text_body = (
        "Welcome to PyCourse!\n\n"
        "Please confirm your email address to activate your account:\n\n"
        f"    {verify_url}\n\n"
        "This link expires soon and can be used only once.\n"
        "If you did not create a PyCourse account, you can ignore this email.\n"
    )
    return EmailMessage(to=to, subject="Confirm your PyCourse email", text_body=text_body)
