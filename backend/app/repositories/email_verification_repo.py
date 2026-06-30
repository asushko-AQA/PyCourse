from datetime import datetime

from sqlmodel import select

from app.models.tables import EmailVerificationToken, now_utc
from app.repositories.base import BaseRepo


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

    def consume(self, row: EmailVerificationToken, *, when: datetime | None = None) -> EmailVerificationToken:
        row.consumed_at = when or now_utc()
        self.session.add(row)
        self.session.commit()
        self.session.refresh(row)
        return row
