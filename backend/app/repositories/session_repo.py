from datetime import datetime

from sqlmodel import select

from app.models.tables import SessionRow
from app.repositories.base import BaseRepo


class SessionRepo(BaseRepo):
    def create_session(self, *, user_id: str, session_token_hash: str, expires_at: datetime) -> SessionRow:
        row = SessionRow(
            user_id=user_id,
            session_token_hash=session_token_hash,
            expires_at=expires_at,
        )
        self.session.add(row)
        self.session.commit()
        self.session.refresh(row)
        return row

    def get_by_token_hash(self, token_hash: str) -> SessionRow | None:
        stmt = select(SessionRow).where(SessionRow.session_token_hash == token_hash)
        return self.session.exec(stmt).first()
