"""Production email adapter stub (SMTP).

Wired but intentionally minimal: it sends a plaintext message over SMTP using the
configured credentials. Choosing/optimising a transactional provider is out of
scope for plan 06 — the abstraction is what matters.
"""

from __future__ import annotations

import smtplib
from email.message import EmailMessage as MimeMessage

from app.core.config import Settings
from app.services.email.base import EmailMessage


class SmtpEmailSender:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    def send(self, message: EmailMessage) -> None:
        s = self._settings
        mime = MimeMessage()
        mime["From"] = s.email_from
        mime["To"] = message.to
        mime["Subject"] = message.subject
        mime.set_content(message.text_body)

        with smtplib.SMTP(s.smtp_host, s.smtp_port) as server:
            if s.smtp_use_tls:
                server.starttls()
            if s.smtp_user and s.smtp_password:
                server.login(s.smtp_user, s.smtp_password)
            server.send_message(mime)
