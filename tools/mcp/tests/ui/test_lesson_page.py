from playwright.sync_api import expect

from .pages.lesson_page import LessonPage


def test_lesson_page_tabs_and_back_navigation(page, base_url: str) -> None:
    lesson = LessonPage(page, base_url)
    lesson.goto("/en/course-1/block-0/lesson-0-1")

    lesson.open_tab("theory")
    lesson.open_tab("assignments")
    lesson.open_tab("quiz")

    lesson.back_to_block()
    lesson.expect_url_path("/en/course-1")


def test_lesson_files_tab_shows_starter(page, base_url: str) -> None:
    lesson = LessonPage(page, base_url)
    lesson.goto("/en/course-1/block-1/lesson-1-1")
    lesson.open_tab("files")
    expect(page.locator("#lesson-file-starter-hello-py")).to_contain_text("Hello, World!")
