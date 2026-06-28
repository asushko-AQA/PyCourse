from playwright.sync_api import expect

from .app_shell_page import AppShellPage


class HomePage(AppShellPage):
    def open_course(self, course_id: str) -> None:
        self.page.get_by_test_id(f"course-card-{course_id}").click()

    def expect_welcome(self) -> None:
        expect(self.page.get_by_role("heading", name="Welcome back, Creator!")).to_be_visible()
