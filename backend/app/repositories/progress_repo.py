from __future__ import annotations

from sqlmodel import select

from app.models.tables import Progress, now_utc
from app.repositories.base import BaseRepo


class ProgressRepo(BaseRepo):
    def list_by_user(self, *, user_id: str) -> list[Progress]:
        stmt = select(Progress).where(Progress.user_id == user_id).order_by(Progress.updated_at)
        return list(self.session.exec(stmt).all())

    def get_progress(self, *, user_id: str, lesson_id: str) -> Progress | None:
        stmt = select(Progress).where(Progress.user_id == user_id, Progress.lesson_id == lesson_id)
        return self.session.exec(stmt).first()

    def get_last_position(self, *, user_id: str) -> str | None:
        stmt = (
            select(Progress)
            .where(Progress.user_id == user_id, Progress.last_position.is_not(None))  # type: ignore[union-attr]
            .order_by(Progress.updated_at.desc())  # type: ignore[attr-defined]
        )
        row = self.session.exec(stmt).first()
        return row.last_position if row else None

    def set_last_position(self, *, user_id: str, last_position: str | None) -> None:
        if last_position is None:
            return
        stmt = select(Progress).where(Progress.user_id == user_id).order_by(Progress.updated_at.desc())  # type: ignore[attr-defined]
        row = self.session.exec(stmt).first()
        if row is None:
            return
        row.last_position = last_position
        row.updated_at = now_utc()
        self.session.add(row)
        self.session.commit()

    def patch_progress(
        self,
        *,
        user_id: str,
        lesson_id: str,
        reading_done: bool | None = None,
        homework_done: bool | None = None,
        quiz_perfect: bool | None = None,
        last_position: str | None = None,
    ) -> Progress:
        row = self.get_progress(user_id=user_id, lesson_id=lesson_id)
        if row is None:
            row = Progress(
                user_id=user_id,
                lesson_id=lesson_id,
                reading_done=reading_done or False,
                homework_done=homework_done or False,
                quiz_perfect=quiz_perfect or False,
                last_position=last_position,
            )
            self.session.add(row)
        else:
            if reading_done is not None:
                row.reading_done = reading_done
            if homework_done is not None:
                row.homework_done = homework_done
            if quiz_perfect is not None:
                row.quiz_perfect = quiz_perfect
            if last_position is not None:
                row.last_position = last_position
            row.updated_at = now_utc()
        self.session.commit()
        self.session.refresh(row)
        return row

    def merge_progress(
        self,
        *,
        user_id: str,
        lesson_id: str,
        reading_done: bool,
        homework_done: bool,
        quiz_perfect: bool,
    ) -> Progress:
        row = self.get_progress(user_id=user_id, lesson_id=lesson_id)
        if row is None:
            row = Progress(
                user_id=user_id,
                lesson_id=lesson_id,
                reading_done=reading_done,
                homework_done=homework_done,
                quiz_perfect=quiz_perfect,
            )
            self.session.add(row)
        else:
            row.reading_done = row.reading_done or reading_done
            row.homework_done = row.homework_done or homework_done
            row.quiz_perfect = row.quiz_perfect or quiz_perfect
            row.updated_at = now_utc()
        self.session.commit()
        self.session.refresh(row)
        return row

    def upsert_progress(
        self,
        *,
        user_id: str,
        lesson_id: str,
        reading_done: bool,
        homework_done: bool,
        quiz_perfect: bool,
        stars_earned: int,
        last_position: str | None = None,
    ) -> Progress:
        row = self.get_progress(user_id=user_id, lesson_id=lesson_id)
        if row is None:
            row = Progress(
                user_id=user_id,
                lesson_id=lesson_id,
                reading_done=reading_done,
                homework_done=homework_done,
                quiz_perfect=quiz_perfect,
                stars_earned=stars_earned,
                last_position=last_position,
            )
            self.session.add(row)
        else:
            row.reading_done = reading_done
            row.homework_done = homework_done
            row.quiz_perfect = quiz_perfect
            row.stars_earned = stars_earned
            row.last_position = last_position
            row.updated_at = now_utc()
        self.session.commit()
        self.session.refresh(row)
        return row
