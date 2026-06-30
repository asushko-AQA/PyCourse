from datetime import datetime

from sqlmodel import select

from app.models.tables import User, now_utc
from app.repositories.base import BaseRepo


class UserRepo(BaseRepo):
    def create_user(
        self,
        *,
        email: str,
        password_hash: str,
        is_minor: bool = False,
        guardian_email: str | None = None,
        parental_consent: bool = False,
    ) -> User:
        row = User(
            email=email,
            password_hash=password_hash,
            is_minor=is_minor,
            guardian_email=guardian_email,
            parental_consent=parental_consent,
            parental_consent_at=now_utc() if parental_consent else None,
        )
        self.session.add(row)
        self.session.commit()
        self.session.refresh(row)
        return row

    def get_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        return self.session.exec(stmt).first()

    def get(self, user_id: str) -> User | None:
        return self.session.get(User, user_id)

    def mark_email_verified(self, user: User, *, when: datetime | None = None) -> User:
        user.email_verified_at = when or now_utc()
        user.updated_at = now_utc()
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
