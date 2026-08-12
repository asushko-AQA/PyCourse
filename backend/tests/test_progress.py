"""Plan 08 verification: progress sync API."""

from __future__ import annotations

import re

from app.repositories.lesson_repo import LessonRepo

GOOD_PASSWORD = "snakes123"


def _token_from_link(text_body: str) -> str:
    match = re.search(r"token=([^\s&]+)", text_body)
    assert match, f"no token in email body:\n{text_body}"
    return match.group(1)


def _register_verify_sign_in(client, mailer, *, email: str = "kid@example.com") -> None:
    register = client.post("/auth/register", json={"email": email, "password": GOOD_PASSWORD})
    assert register.status_code == 201
    token = _token_from_link(mailer.last.text_body)
    verify = client.post("/auth/verify", json={"token": token})
    assert verify.status_code == 200
    sign_in = client.post("/auth/sign-in", json={"email": email, "password": GOOD_PASSWORD})
    assert sign_in.status_code == 200


def _seed_lesson(session) -> str:
    repo = LessonRepo(session)
    repo.create_course(
        course_id="course-1",
        slug="course-1-python-basics",
        title="Python Basics",
        path="course-1-python-basics",
        order_index=1,
    )
    repo.create_block(
        block_id="course-1/block-0",
        course_id="course-1",
        slug="block-0-getting-started",
        title="Getting Started",
        path="course-1-python-basics/block-0-getting-started",
        order_index=0,
    )
    lesson_key = "course-1/lesson-0-1"
    repo.create_lesson(
        lesson_id=lesson_key,
        course_id="course-1",
        block_id="course-1/block-0",
        slug="lesson-0-1-what-is-a-programming-language",
        title="What Is a Programming Language?",
        path="course-1-python-basics/block-0-getting-started/lesson-0-1-what-is-a-programming-language",
        order_index=0,
    )
    return lesson_key


def test_progress_requires_auth(client):
    resp = client.get("/progress")
    assert resp.status_code == 401
    assert resp.json()["detail"]["code"] == "unauthorized"


def test_progress_upsert_and_fetch(client, engine, mailer, session):
    lesson_key = _seed_lesson(session)
    _register_verify_sign_in(client, mailer)

    upsert = client.post(
        "/progress",
        json={
            "lesson_key": lesson_key,
            "reading_done": True,
            "last_position": "course-1/block-0/lesson-0-1/read",
        },
    )
    assert upsert.status_code == 200, upsert.text
    body = upsert.json()
    assert body["lesson"]["lesson_key"] == lesson_key
    assert body["lesson"]["reading_done"] is True

    snapshot = client.get("/progress")
    assert snapshot.status_code == 200
    data = snapshot.json()
    assert len(data["lessons"]) == 1
    assert data["lessons"][0]["lesson_key"] == lesson_key
    assert data["last_position"] == "course-1/block-0/lesson-0-1/read"


def test_progress_merge_unions_local_completions(client, engine, mailer, session):
    lesson_key = _seed_lesson(session)
    _register_verify_sign_in(client, mailer, email="merge@example.com")

    server = client.post("/progress", json={"lesson_key": lesson_key, "reading_done": True})
    assert server.status_code == 200

    merge = client.post(
        "/progress/merge",
        json={
            "lessons": [
                {"lesson_key": lesson_key, "reading_done": True, "quiz_perfect": True},
            ],
            "last_position": "course-1/block-0/lesson-0-1/quiz",
        },
    )
    assert merge.status_code == 200, merge.text
    merged = merge.json()
    assert merged["merged_count"] == 1
    lesson = merged["snapshot"]["lessons"][0]
    assert lesson["reading_done"] is True
    assert lesson["quiz_perfect"] is True


def test_progress_invalid_lesson_key(client, mailer, session):
    _seed_lesson(session)
    _register_verify_sign_in(client, mailer, email="invalid@example.com")

    resp = client.post("/progress", json={"lesson_key": "course-9/lesson-9-9", "reading_done": True})
    assert resp.status_code == 404
    assert resp.json()["detail"]["code"] == "invalid_lesson_key"
