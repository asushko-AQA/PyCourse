from .pages.course_map_page import CourseMapPage
from .pages.home_page import HomePage


def test_course_page_navigation_from_home(page, base_url: str) -> None:
    home = HomePage(page, base_url)
    home.goto_home("en")
    home.open_course("course-1")
    home.expect_url_path("/en/course-1")

    course = CourseMapPage(page, base_url)
    course.expect_course_title("Python Basics")
    course.back_to_all_courses()
    course.expect_url_path("/en")


def test_course_page_lesson_node_navigation(page, base_url: str) -> None:
    course = CourseMapPage(page, base_url)
    course.goto("/en/course-1")
    course.open_lesson_node("course-1", "lesson-0-1")
    course.expect_url_path("/en/course-1/block-0/lesson-0-1")
