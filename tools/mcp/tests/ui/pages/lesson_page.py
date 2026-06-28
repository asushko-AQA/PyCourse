from playwright.sync_api import expect

from .app_shell_page import AppShellPage


class LessonPage(AppShellPage):
    def open_tab(self, tab_id: str) -> None:
        self.page.get_by_test_id(f"lesson-tab-{tab_id}").click()

    def back_to_map(self) -> None:
        self.page.get_by_test_id("lesson-back-to-map").click()

    def back_to_block(self) -> None:
        self.page.get_by_test_id("lesson-block-back").click()

    def mark_homework_done(self) -> None:
        self.page.get_by_test_id("lesson-mark-done").click()

    def expect_next_visible(self) -> None:
        expect(self.page.get_by_test_id("lesson-next")).to_be_visible()

    def open_next(self) -> None:
        self.page.get_by_test_id("lesson-next").click()
