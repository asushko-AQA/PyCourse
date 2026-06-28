from .pages.lesson_page import LessonPage


def test_lesson_page_tabs_and_back_navigation(page, base_url: str) -> None:
    lesson = LessonPage(page, base_url)
    lesson.goto("/en/course-1/block-0/lesson-0-1")

    lesson.open_tab("theory")
    lesson.open_tab("assignments")
    lesson.open_tab("quiz")

    lesson.back_to_block()
    lesson.expect_url_path("/en/course-1")
