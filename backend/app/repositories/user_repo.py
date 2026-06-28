from sqlmodel import select

from app.models.tables import User
from app.repositories.base import BaseRepo


class UserRepo(BaseRepo):
    def create_user(self, *, email: str, password_hash: str) -> User:
        row = User(email=email, password_hash=password_hash)
        self.session.add(row)
        self.session.commit()
        self.session.refresh(row)
        return row

    def get_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        return self.session.exec(stmt).first()

    def get(self, user_id: str) -> User | None:
        return self.session.get(User, user_id)
