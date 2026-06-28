import pytest

from .pages.quiz_page import QuizPage


def test_quiz_flow_to_results_and_back_to_map(page, base_url: str) -> None:
    quiz = QuizPage(page, base_url)
    quiz.goto("/en/course-1/block-0/lesson-0-1")
    try:
        quiz.complete_quiz()
    except pytest.skip.Exception:
        raise

    quiz.page.get_by_test_id("quiz-back-to-map").click()
    quiz.expect_url_path("/en/course-1")
