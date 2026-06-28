from .lesson_page import LessonPage


class HomeworkPage(LessonPage):
    def complete_homework_flow(self) -> None:
        self.open_tab("assignments")
        self.mark_homework_done()
