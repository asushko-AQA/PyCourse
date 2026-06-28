from datetime import datetime, timedelta, timezone

from sqlalchemy import inspect

from app.repositories.lesson_repo import LessonRepo
from app.repositories.progress_repo import ProgressRepo
from app.repositories.session_repo import SessionRepo
from app.repositories.user_repo import UserRepo


def test_lesson_metadata_repositories_roundtrip(session) -> None:
    lesson_repo = LessonRepo(session)
    lesson_repo.create_course(
        course_id="course-1",
        slug="course-1-python-basics",
        title="Python Basics",
        path="course-1-python-basics",
        order_index=1,
    )
    lesson_repo.create_block(
        block_id="block-1",
        course_id="course-1",
        slug="block-1-meeting-your-computer",
        title="Meeting Your Computer",
        path="course-1-python-basics/block-1-meeting-your-computer",
        order_index=1,
    )
    lesson = lesson_repo.create_lesson(
        lesson_id="lesson-1-1",
        course_id="course-1",
        block_id="block-1",
        slug="lesson-1-1-installing-python",
        title="Installing Python",
        path="course-1-python-basics/block-1-meeting-your-computer/lesson-1-1-installing-python",
        order_index=1,
        quiz_hash="abc123",
        homework_ref="starter/install.py",
        checker_ref="checker/install",
        content_hash="hash-1",
    )
    fetched = lesson_repo.get_lesson(lesson.id)
    assert fetched is not None
    assert fetched.quiz_hash == "abc123"
    assert fetched.homework_ref == "starter/install.py"

    columns = {col["name"] for col in inspect(session.connection()).get_columns("lessons")}
    assert "body" not in columns
    assert "markdown" not in columns


def test_user_session_and_progress_repositories(session) -> None:
    lesson_repo = LessonRepo(session)
    lesson_repo.create_course(
        course_id="course-1",
        slug="course-1-python-basics",
        title="Python Basics",
        path="course-1-python-basics",
        order_index=1,
    )
    lesson_repo.create_block(
        block_id="block-1",
        course_id="course-1",
        slug="block-1-meeting-your-computer",
        title="Meeting Your Computer",
        path="course-1-python-basics/block-1-meeting-your-computer",
        order_index=1,
    )
    lesson = lesson_repo.create_lesson(
        lesson_id="lesson-1-1",
        course_id="course-1",
        block_id="block-1",
        slug="lesson-1-1-installing-python",
        title="Installing Python",
        path="course-1-python-basics/block-1-meeting-your-computer/lesson-1-1-installing-python",
        order_index=1,
    )

    user_repo = UserRepo(session)
    user = user_repo.create_user(email="kid@example.com", password_hash="hash")
    assert user_repo.get_by_email("kid@example.com") is not None

    session_repo = SessionRepo(session)
    row = session_repo.create_session(
        user_id=user.id,
        session_token_hash="token-hash",
        expires_at=datetime.now(timezone.utc) + timedelta(days=7),
    )
    assert row.session_token_hash == "token-hash"
    assert session_repo.get_by_token_hash("token-hash") is not None

    progress_repo = ProgressRepo(session)
    first = progress_repo.upsert_progress(
        user_id=user.id,
        lesson_id=lesson.id,
        reading_done=True,
        homework_done=False,
        quiz_perfect=False,
        stars_earned=1,
        last_position="line:100",
    )
    assert first.stars_earned == 1

    second = progress_repo.upsert_progress(
        user_id=user.id,
        lesson_id=lesson.id,
        reading_done=True,
        homework_done=True,
        quiz_perfect=True,
        stars_earned=3,
        last_position="line:220",
    )
    assert second.id == first.id
    assert second.stars_earned == 3
    assert progress_repo.get_progress(user_id=user.id, lesson_id=lesson.id) is not None
