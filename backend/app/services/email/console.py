"""Development email adapter: prints the message (including the verification
link) to the application log instead of sending it. Never used in production.
"""

from __future__ import annotations

import logging

from app.services.email.base import EmailMessage

logger = logging.getLogger("app.email")


def _format_console_message(message: EmailMessage) -> str:
    return (
        "\n--- DEV EMAIL (not actually sent) ---\n"
        f"To: {message.to}\n"
        f"Subject: {message.subject}\n\n"
        f"{message.text_body}"
        "-------------------------------------"
    )


class ConsoleEmailSender:
    def send(self, message: EmailMessage) -> None:
        formatted = _format_console_message(message)
        # Railway/container logs capture stdout reliably; logger output may be filtered.
        print(formatted, flush=True)
        logger.info("%s", formatted)
