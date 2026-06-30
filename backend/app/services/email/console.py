"""Development email adapter: prints the message (including the verification
link) to the application log instead of sending it. Never used in production.
"""

from __future__ import annotations

import logging

from app.services.email.base import EmailMessage

logger = logging.getLogger("app.email")


class ConsoleEmailSender:
    def send(self, message: EmailMessage) -> None:
        logger.info(
            "\n--- DEV EMAIL (not actually sent) ---\n"
            "To: %s\nSubject: %s\n\n%s"
            "-------------------------------------",
            message.to,
            message.subject,
            message.text_body,
        )
