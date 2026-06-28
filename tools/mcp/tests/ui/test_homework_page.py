from .pages.homework_page import HomeworkPage


def test_homework_completion_unlocks_next_lesson(page, base_url: str) -> None:
    homework = HomeworkPage(page, base_url)
    homework.goto("/en/course-1/block-0/lesson-0-1")
    homework.complete_homework_flow()
    homework.expect_next_visible()
    homework.open_next()
    homework.expect_url_path("/en/course-1/block-0/lesson-0-2")
