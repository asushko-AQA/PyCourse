"""Progress sync business logic (plan 08)."""

from __future__ import annotations

from app.models.tables import Progress, now_utc
from app.repositories.lesson_repo import LessonRepo
from app.repositories.progress_repo import ProgressRepo
from app.schemas.progress import (
    LessonProgressItem,
    ProgressMergeLesson,
    ProgressSnapshot,
    ProgressUpsertRequest,
)


class InvalidLessonKey(Exception):
    code = "invalid_lesson_key"

    def __init__(self, lesson_key: str) -> None:
        super().__init__(f"Unknown lesson key: {lesson_key}")
        self.lesson_key = lesson_key


class ProgressService:
    def __init__(self, *, progress: ProgressRepo, lessons: LessonRepo) -> None:
        self.progress = progress
        self.lessons = lessons

    def _resolve_lesson_id(self, lesson_key: str) -> str:
        lesson = self.lessons.get_lesson_by_key(lesson_key)
        if lesson is None:
            raise InvalidLessonKey(lesson_key)
        return lesson.id

    @staticmethod
    def _to_item(row: Progress, *, lesson_key: str) -> LessonProgressItem:
        return LessonProgressItem(
            lesson_key=lesson_key,
            reading_done=row.reading_done,
            homework_done=row.homework_done,
            quiz_perfect=row.quiz_perfect,
            last_position=row.last_position,
            updated_at=row.updated_at,
        )

    def _lesson_key_for_row(self, row: Progress) -> str:
        lesson = self.lessons.get_lesson(row.lesson_id)
        if lesson is None:
            return row.lesson_id
        if "/" in lesson.id:
            return lesson.id
        return f"{lesson.course_id}/{lesson.id}"

    def get_snapshot(self, *, user_id: str) -> ProgressSnapshot:
        rows = self.progress.list_by_user(user_id=user_id)
        items = [self._to_item(row, lesson_key=self._lesson_key_for_row(row)) for row in rows]
        last_position = self.progress.get_last_position(user_id=user_id)
        return ProgressSnapshot(lessons=items, last_position=last_position)

    def upsert(self, *, user_id: str, payload: ProgressUpsertRequest) -> LessonProgressItem:
        lesson_id = self._resolve_lesson_id(payload.lesson_key)
        row = self.progress.patch_progress(
            user_id=user_id,
            lesson_id=lesson_id,
            reading_done=payload.reading_done,
            homework_done=payload.homework_done,
            quiz_perfect=payload.quiz_perfect,
            last_position=payload.last_position,
        )
        if payload.last_position is not None:
            self.progress.set_last_position(user_id=user_id, last_position=payload.last_position)
        return self._to_item(row, lesson_key=payload.lesson_key)

    def merge_local(
        self,
        *,
        user_id: str,
        lessons: list[ProgressMergeLesson],
        last_position: str | None,
    ) -> tuple[int, ProgressSnapshot]:
        merged = 0
        for item in lessons:
            try:
                lesson_id = self._resolve_lesson_id(item.lesson_key)
            except InvalidLessonKey:
                continue
            self.progress.merge_progress(
                user_id=user_id,
                lesson_id=lesson_id,
                reading_done=item.reading_done,
                homework_done=item.homework_done,
                quiz_perfect=item.quiz_perfect,
            )
            merged += 1

        if last_position is not None:
            existing = self.progress.get_last_position(user_id=user_id)
            if existing is None:
                self.progress.set_last_position(user_id=user_id, last_position=last_position)

        return merged, self.get_snapshot(user_id=user_id)
