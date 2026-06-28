from sqlmodel import select

from app.models.tables import Progress
from app.repositories.base import BaseRepo


class ProgressRepo(BaseRepo):
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
        stmt = select(Progress).where(Progress.user_id == user_id, Progress.lesson_id == lesson_id)
        row = self.session.exec(stmt).first()
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
        self.session.commit()
        self.session.refresh(row)
        return row

    def get_progress(self, *, user_id: str, lesson_id: str) -> Progress | None:
        stmt = select(Progress).where(Progress.user_id == user_id, Progress.lesson_id == lesson_id)
        return self.session.exec(stmt).first()
