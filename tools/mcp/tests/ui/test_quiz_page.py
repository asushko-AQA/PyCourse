import json
import re
from pathlib import Path

import pytest
from playwright.sync_api import expect

from .pages.quiz_page import QuizPage

LESSON_0_1 = (
    Path(__file__).resolve().parents[4]
    / "course-1-python-basics"
    / "block-0-getting-started"
    / "lesson-0-1-what-is-a-programming-language"
    / "en.md"
)


def _correct_indices(markdown: str) -> list[int]:
    details = markdown.split("<details", 1)[-1]
    letters = re.findall(r"^\s*\d+\.\s+\*\*([a-d])\)\*\*", details, flags=re.M)
    if len(letters) < 3:
        raise AssertionError("could not read quiz answer letters")
    return [ord(letter) - ord("a") for letter in letters]


def _progress(page) -> dict:
    raw = page.evaluate("localStorage.getItem('pyquest-progress')")
    if not raw:
        return {}
    return json.loads(raw).get("state", {})


def test_quiz_flow_to_results_and_back_to_map(page, base_url: str) -> None:
    quiz = QuizPage(page, base_url)
    quiz.goto("/en/course-1/block-0/lesson-0-1")
    try:
        quiz.complete_quiz()
    except pytest.skip.Exception:
        raise

    quiz.page.get_by_test_id("quiz-back-to-map").click()
    quiz.expect_url_path("/en/course-1")


def test_imperfect_quiz_does_not_award_xp(page, base_url: str) -> None:
    quiz = QuizPage(page, base_url)
    quiz.goto("/en/course-1/block-0/lesson-0-1")
    page.evaluate("localStorage.removeItem('pyquest-progress')")
    page.reload()
    quiz.open_quiz()

    for _ in range(6):
        if page.get_by_test_id("quiz-back-to-map").count() > 0:
            break
        # Option 0 is not the answer for every question in lesson 0.1.
        page.get_by_test_id("quiz-option-0").click()
        if page.get_by_test_id("quiz-advance").count() == 0:
            quiz.answer_until_advance()
        page.get_by_test_id("quiz-advance").click()

    expect(page.get_by_test_id("quiz-xp")).to_be_visible()
    expect(page.get_by_test_id("quiz-xp")).not_to_contain_text("+10")
    state = _progress(page)
    assert "course-1/lesson-0-1" not in state.get("completedQuizzes", [])
    assert state.get("xp", 0) == 0
    assert "course-1/lesson-0-1" not in state.get("completedLessons", [])


def test_perfect_quiz_awards_xp_without_completing_the_lesson(page, base_url: str) -> None:
    indices = _correct_indices(LESSON_0_1.read_text(encoding="utf-8"))
    quiz = QuizPage(page, base_url)
    quiz.goto("/en/course-1/block-0/lesson-0-1")
    page.evaluate("localStorage.removeItem('pyquest-progress')")
    page.reload()
    quiz.open_quiz()

    for index in indices:
        page.get_by_test_id(f"quiz-option-{index}").click()
        expect(page.get_by_test_id("quiz-advance")).to_be_visible()
        page.get_by_test_id("quiz-advance").click()

    expect(page.get_by_test_id("quiz-xp")).to_contain_text("+10")
    state = _progress(page)
    assert "course-1/lesson-0-1" in state.get("completedQuizzes", [])
    assert state.get("xp") == 10
    assert "course-1/lesson-0-1" not in state.get("completedLessons", [])
