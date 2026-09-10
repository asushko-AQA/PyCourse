from datetime import datetime, timezone

from sqlmodel import select

from app.models.tables import EmailVerificationToken, now_utc
from app.repositories.base import BaseRepo


def _as_utc(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value


class EmailVerificationTokenRepo(BaseRepo):
    def create(self, *, user_id: str, token: str, expires_at: datetime) -> EmailVerificationToken:
        row = EmailVerificationToken(user_id=user_id, token=token, expires_at=expires_at)
        self.session.add(row)
        self.session.commit()
        self.session.refresh(row)
        return row

    def get_by_token(self, token: str) -> EmailVerificationToken | None:
        stmt = select(EmailVerificationToken).where(EmailVerificationToken.token == token)
        return self.session.exec(stmt).first()

    def get_latest_active_for_user(
        self,
        user_id: str,
        *,
        when: datetime | None = None,
    ) -> EmailVerificationToken | None:
        """Return the newest unused, non-expired token for a user, if any."""
        cutoff = when or now_utc()
        stmt = (
            select(EmailVerificationToken)
            .where(EmailVerificationToken.user_id == user_id)
            .where(EmailVerificationToken.consumed_at.is_(None))
            .order_by(EmailVerificationToken.created_at.desc())
        )
        for row in self.session.exec(stmt).all():
            if _as_utc(row.expires_at) > cutoff:
                return row
        return None

    def consume(self, row: EmailVerificationToken, *, when: datetime | None = None) -> EmailVerificationToken:
        row.consumed_at = when or now_utc()
        self.session.add(row)
        self.session.commit()
        self.session.refresh(row)
        return row
