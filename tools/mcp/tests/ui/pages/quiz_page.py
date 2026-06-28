import pytest
from playwright.sync_api import expect

from .lesson_page import LessonPage


class QuizPage(LessonPage):
    def open_quiz(self) -> None:
        self.open_tab("quiz")

    def _advance_visible(self) -> bool:
        return self.page.get_by_test_id("quiz-advance").count() > 0

    def answer_until_advance(self, max_options: int = 6) -> None:
        for i in range(max_options):
            opt = self.page.get_by_test_id(f"quiz-option-{i}")
            if opt.count() == 0:
                break
            opt.click()
            if self._advance_visible():
                return
        raise AssertionError("Could not find correct quiz option for current question")

    def complete_quiz(self, max_questions: int = 10) -> None:
        self.open_quiz()
        if self.page.get_by_text("No quiz in this lesson").count() > 0:
            pytest.skip("Lesson has no quiz")

        for _ in range(max_questions):
            self.answer_until_advance()
            self.page.get_by_test_id("quiz-advance").click()
            if self.page.get_by_test_id("quiz-back-to-map").count() > 0:
                expect(self.page.get_by_test_id("quiz-replay")).to_be_visible()
                return

        raise AssertionError("Quiz did not reach results screen within expected question count")
