import re
from pathlib import Path

import pytest

from .pages.quiz_page import QuizPage

REPO = Path(__file__).resolve().parents[4]


def _correct_indexes(course_id: str, block_id: str, lesson_id: str) -> list[int]:
    matches = list(REPO.glob(f"{course_id}-*/{block_id}-*/{lesson_id}-*/en.md"))
    assert matches, f"no lesson markdown for {course_id}/{block_id}/{lesson_id}"
    text = matches[0].read_text(encoding="utf-8")
    body = text[text.lower().find("<details") :]
    letters = re.findall(r"^\d+\.\s+\*\*([a-d])\)", body, re.M)
    return [ord(letter) - ord("a") for letter in letters]


def _progress(page) -> dict:
    raw = page.evaluate("localStorage.getItem('pyquest-progress')")
    assert raw, "progress was not stored"
    return __import__("json").loads(raw)["state"]


def test_quiz_flow_to_results_and_back_to_map(page, base_url: str) -> None:
    quiz = QuizPage(page, base_url)
    quiz.goto("/en/course-1/block-0/lesson-0-1")
    try:
        quiz.complete_quiz()
    except pytest.skip.Exception:
        raise

    quiz.page.get_by_test_id("quiz-back-to-map").click()
    quiz.expect_url_path("/en/course-1")


def test_imperfect_quiz_earns_no_xp_and_does_not_complete_lesson(page, base_url: str) -> None:
    quiz = QuizPage(page, base_url)
    quiz.goto("/en/course-1/block-0/lesson-0-1")
    quiz.open_quiz()

    missed = False
    for _ in range(6):
        if page.get_by_test_id("quiz-back-to-map").count() > 0:
            break
        # A wrong first click (when option 0 is not the answer) makes the run imperfect.
        page.get_by_test_id("quiz-option-0").click()
        if page.get_by_test_id("quiz-advance").count() == 0:
            missed = True
            quiz.answer_until_advance()
        page.get_by_test_id("quiz-advance").click()

    assert missed, "every first option was correct, so the run was not imperfect"
    reward = page.get_by_test_id("quiz-reward")
    assert reward.get_attribute("data-reward") == "none"
    assert "earned!" not in reward.inner_text()
    state = _progress(page)
    assert state["xp"] == 0
    assert state["completedQuizzes"] == []
    assert "course-1/lesson-0-1" not in state["completedLessons"]


def _answer_perfect(quiz: QuizPage, indexes: list[int]) -> None:
    quiz.open_quiz()
    for index in indexes:
        quiz.page.get_by_test_id(f"quiz-option-{index}").click()
        quiz.page.get_by_test_id("quiz-advance").click()


def test_perfect_quiz_earns_xp_once(page, base_url: str) -> None:
    quiz = QuizPage(page, base_url)
    page.goto(f"{base_url}/en")
    page.evaluate("localStorage.clear()")
    quiz.goto("/en/course-1/block-0/lesson-0-1")
    indexes = _correct_indexes("course-1", "block-0", "lesson-0-1")
    _answer_perfect(quiz, indexes)
    reward = quiz.page.get_by_test_id("quiz-reward")
    assert reward.get_attribute("data-reward") == "earned"
    assert "+10 XP" in reward.inner_text()
    state = _progress(quiz.page)
    assert state["xp"] == 15  # lesson + perfect quiz
    assert "course-1/lesson-0-1" in state["completedQuizzes"]
    assert "course-1/lesson-0-1" in state["completedLessons"]

    quiz.page.get_by_test_id("quiz-replay").click()
    quiz.complete_quiz()
    assert quiz.page.get_by_test_id("quiz-reward").get_attribute("data-reward") == "collected"
    assert _progress(quiz.page)["xp"] == 15


def test_xp_is_restored_from_saved_progress(page, base_url: str) -> None:
    """A stored snapshot with xp 0 is rebuilt from completed lessons and quizzes."""
    page.goto(f"{base_url}/en")
    # Let the first (empty) persist finish, then plant a snapshot with xp 0.
    page.wait_for_function("() => localStorage.getItem('pyquest-progress')")
    page.evaluate(
        """() => localStorage.setItem('pyquest-progress', JSON.stringify({
          state: {
            xp: 0,
            completedLessons: ['course-1/lesson-0-1', 'course-1/lesson-0-2'],
            completedQuizzes: ['course-1/lesson-0-1'],
            hasMergedLocal: true,
            mergedForUserId: null,
            pendingUpdates: []
          },
          version: 0
        }))"""
    )
    page.reload()
    page.wait_for_timeout(1500)
    # The header badge is for signed-in learners. The stored XP is rebuilt on
    # load: 2 lessons × 5 + 1 perfect quiz × 10.
    raw = page.evaluate("localStorage.getItem('pyquest-progress')")
    assert raw and __import__("json").loads(raw)["state"]["xp"] == 20, raw
