from __future__ import annotations

from datetime import date, datetime, timezone
from uuid import uuid4

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, SQLModel


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


class Timestamped(SQLModel):
    created_at: datetime = Field(default_factory=now_utc, nullable=False)
    updated_at: datetime = Field(default_factory=now_utc, nullable=False)


class Course(SQLModel, table=True):
    __tablename__ = "courses"

    id: str = Field(primary_key=True)
    slug: str = Field(index=True, unique=True, nullable=False)
    title: str = Field(nullable=False)
    path: str = Field(nullable=False, unique=True)
    order_index: int = Field(nullable=False, default=0)
    content_hash: str | None = Field(default=None)


class Block(SQLModel, table=True):
    __tablename__ = "blocks"

    id: str = Field(primary_key=True)
    course_id: str = Field(foreign_key="courses.id", index=True, nullable=False)
    slug: str = Field(index=True, nullable=False)
    title: str = Field(nullable=False)
    path: str = Field(nullable=False, unique=True)
    order_index: int = Field(nullable=False, default=0)
    content_hash: str | None = Field(default=None)

    __table_args__ = (UniqueConstraint("course_id", "slug", name="uq_blocks_course_slug"),)


class Lesson(SQLModel, table=True):
    __tablename__ = "lessons"

    id: str = Field(primary_key=True)
    course_id: str = Field(foreign_key="courses.id", index=True, nullable=False)
    block_id: str = Field(foreign_key="blocks.id", index=True, nullable=False)
    slug: str = Field(index=True, nullable=False)
    title: str = Field(nullable=False)
    path: str = Field(nullable=False, unique=True)
    order_index: int = Field(nullable=False, default=0)
    quiz_hash: str | None = Field(default=None, index=True)
    homework_ref: str | None = Field(default=None)
    checker_ref: str | None = Field(default=None)
    content_hash: str | None = Field(default=None)

    __table_args__ = (
        UniqueConstraint("block_id", "slug", name="uq_lessons_block_slug"),
        UniqueConstraint("course_id", "order_index", name="uq_lessons_course_order"),
    )


class User(Timestamped, table=True):
    __tablename__ = "users"

    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    email: str = Field(index=True, unique=True, nullable=False)
    email_verified_at: datetime | None = Field(default=None)
    password_hash: str = Field(nullable=False)

    # COPPA / parental-consent (plan 06). `is_minor` is a self-declared under-13
    # gate; when set, a guardian email and explicit consent are required before
    # the account is usable.
    is_minor: bool = Field(default=False, nullable=False)
    guardian_email: str | None = Field(default=None)
    parental_consent: bool = Field(default=False, nullable=False)
    parental_consent_at: datetime | None = Field(default=None)


class EmailVerificationToken(SQLModel, table=True):
    __tablename__ = "email_verification_tokens"

    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    user_id: str = Field(foreign_key="users.id", index=True, nullable=False)
    token: str = Field(nullable=False, unique=True, index=True)
    expires_at: datetime = Field(nullable=False)
    created_at: datetime = Field(default_factory=now_utc, nullable=False)
    # Single-use: set when the token is redeemed so it cannot be reused.
    consumed_at: datetime | None = Field(default=None)


class SessionRow(SQLModel, table=True):
    __tablename__ = "sessions"

    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    user_id: str = Field(foreign_key="users.id", index=True, nullable=False)
    session_token_hash: str = Field(nullable=False, unique=True, index=True)
    expires_at: datetime = Field(nullable=False)
    created_at: datetime = Field(default_factory=now_utc, nullable=False)
    last_seen_at: datetime = Field(default_factory=now_utc, nullable=False)


class Progress(Timestamped, table=True):
    __tablename__ = "progress"

    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    user_id: str = Field(foreign_key="users.id", index=True, nullable=False)
    lesson_id: str = Field(foreign_key="lessons.id", index=True, nullable=False)
    reading_done: bool = Field(default=False, nullable=False)
    homework_done: bool = Field(default=False, nullable=False)
    quiz_perfect: bool = Field(default=False, nullable=False)
    stars_earned: int = Field(default=0, nullable=False)
    last_position: str | None = Field(default=None)

    __table_args__ = (UniqueConstraint("user_id", "lesson_id", name="uq_progress_user_lesson"),)


class StarEvent(SQLModel, table=True):
    __tablename__ = "star_events"

    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    user_id: str = Field(foreign_key="users.id", index=True, nullable=False)
    lesson_id: str | None = Field(default=None, foreign_key="lessons.id", index=True)
    event_type: str = Field(nullable=False)
    stars_delta: int = Field(default=0, nullable=False)
    created_at: datetime = Field(default_factory=now_utc, nullable=False)


class Achievement(SQLModel, table=True):
    __tablename__ = "achievements"

    id: str = Field(primary_key=True)
    code: str = Field(nullable=False, unique=True, index=True)
    title: str = Field(nullable=False)
    description: str = Field(nullable=False)
    stars_reward: int = Field(default=0, nullable=False)
    created_at: datetime = Field(default_factory=now_utc, nullable=False)


class UserAchievement(SQLModel, table=True):
    __tablename__ = "user_achievements"

    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    user_id: str = Field(foreign_key="users.id", index=True, nullable=False)
    achievement_id: str = Field(foreign_key="achievements.id", index=True, nullable=False)
    achieved_at: datetime = Field(default_factory=now_utc, nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "achievement_id",
            name="uq_user_achievements_user_achievement",
        ),
    )


class StreakSnapshot(SQLModel, table=True):
    __tablename__ = "streak_snapshots"

    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    user_id: str = Field(foreign_key="users.id", index=True, unique=True, nullable=False)
    current_streak_days: int = Field(default=0, nullable=False)
    best_streak_days: int = Field(default=0, nullable=False)
    last_activity_date: date | None = Field(default=None)
    updated_at: datetime = Field(default_factory=now_utc, nullable=False)


class Submission(SQLModel, table=True):
    __tablename__ = "submissions"

    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    user_id: str = Field(foreign_key="users.id", index=True, nullable=False)
    lesson_id: str = Field(foreign_key="lessons.id", index=True, nullable=False)
    status: str = Field(nullable=False, default="pending")
    checker_ref: str | None = Field(default=None)
    executor_job_ref: str | None = Field(default=None, index=True)
    submitted_at: datetime = Field(default_factory=now_utc, nullable=False)
    checked_at: datetime | None = Field(default=None)


class ExternalIdentity(SQLModel, table=True):
    __tablename__ = "external_identities"

    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    user_id: str = Field(foreign_key="users.id", index=True, nullable=False)
    provider: str = Field(nullable=False)
    provider_user_id: str = Field(nullable=False)
    linked_at: datetime = Field(default_factory=now_utc, nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "provider",
            "provider_user_id",
            name="uq_external_identities_provider_user",
        ),
    )
