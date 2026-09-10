"""Request/response models for the progress sync API (plan 08)."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class LessonProgressItem(BaseModel):
    """Per-lesson progress state returned to clients."""

    lesson_key: str
    reading_done: bool = False
    homework_done: bool = False
    quiz_perfect: bool = False
    last_position: str | None = None
    updated_at: datetime | None = None


class ProgressSnapshot(BaseModel):
    """Full progress snapshot for the authenticated user."""

    lessons: list[LessonProgressItem]
    last_position: str | None = None


class ProgressUpsertRequest(BaseModel):
    """Idempotent single-lesson upsert. Omitted booleans are left unchanged."""

    lesson_key: str = Field(min_length=1)
    reading_done: bool | None = None
    homework_done: bool | None = None
    quiz_perfect: bool | None = None
    last_position: str | None = None


class ProgressMergeLesson(BaseModel):
    lesson_key: str = Field(min_length=1)
    reading_done: bool = False
    homework_done: bool = False
    quiz_perfect: bool = False


class ProgressMergeRequest(BaseModel):
    """Bulk merge for first-login localStorage reconciliation (union of completions)."""

    lessons: list[ProgressMergeLesson] = Field(default_factory=list)
    last_position: str | None = None


class ProgressUpsertResponse(BaseModel):
    lesson: LessonProgressItem


class ProgressMergeResponse(BaseModel):
    merged_count: int
    snapshot: ProgressSnapshot
