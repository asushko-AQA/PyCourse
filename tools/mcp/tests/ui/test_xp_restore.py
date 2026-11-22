"""XP comes back from the server snapshot when a signed-in learner opens the app."""

import json

from playwright.sync_api import expect

from .pages.course_map_page import CourseMapPage


def test_sign_in_restores_xp_from_server_progress(page, base_url: str) -> None:
    snapshot = {
        "lessons": [
            {
                "lesson_key": "course-1/lesson-0-1",
                "reading_done": True,
                "homework_done": False,
                "quiz_perfect": False,
                "last_position": None,
                "updated_at": None,
            },
            {
                "lesson_key": "course-1/lesson-0-2",
                "reading_done": True,
                "homework_done": False,
                "quiz_perfect": True,
                "last_position": None,
                "updated_at": None,
            },
        ],
        "last_position": None,
    }

    def fulfill_backend(route) -> None:
        url = route.request.url.split("?", 1)[0].rstrip("/")
        if url.endswith("/auth/session"):
            route.fulfill(
                status=200,
                content_type="application/json",
                body=json.dumps(
                    {
                        "user": {
                            "id": "user-restore",
                            "email": "ada@example.com",
                            "email_verified_at": "2026-01-01T00:00:00Z",
                        }
                    }
                ),
            )
            return
        if url.endswith("/progress") and route.request.method == "GET":
            route.fulfill(
                status=200,
                content_type="application/json",
                body=json.dumps(snapshot),
            )
            return
        route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps({"snapshot": snapshot, "merged_count": 0, "lesson": snapshot["lessons"][0]}),
        )

    page.route("http://localhost:8000/**", fulfill_backend)
    page.route("http://127.0.0.1:8000/**", fulfill_backend)

    course = CourseMapPage(page, base_url)
    course.goto("/en/course-1")
    page.evaluate("localStorage.removeItem('pyquest-progress')")
    page.reload()

    expect(page.get_by_test_id("xp-badge")).to_contain_text("20")
    raw = page.evaluate("localStorage.getItem('pyquest-progress')")
    state = json.loads(raw)["state"]
    assert state["xp"] == 20
    assert state["completedLessons"] == [
        "course-1/lesson-0-1",
        "course-1/lesson-0-2",
    ]
    assert state["completedQuizzes"] == ["course-1/lesson-0-2"]
