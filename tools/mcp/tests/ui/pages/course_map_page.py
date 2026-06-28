from playwright.sync_api import expect

from .app_shell_page import AppShellPage


class CourseMapPage(AppShellPage):
    def open_lesson_node(self, course_id: str, lesson_id: str) -> None:
        self.page.get_by_test_id(f"lesson-node-{course_id}-{lesson_id}").click()

    def back_to_all_courses(self) -> None:
        self.page.get_by_role("link", name="← All courses").click()

    def expect_course_title(self, title: str) -> None:
        expect(self.page.get_by_role("heading", name=title)).to_be_visible()
