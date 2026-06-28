from __future__ import annotations

from typing import Literal

from sqlmodel import select

from app.models.tables import Block, Course, Lesson
from app.repositories.base import BaseRepo

UpsertAction = Literal["created", "updated", "unchanged"]


class LessonRepo(BaseRepo):
    def create_course(self, *, course_id: str, slug: str, title: str, path: str, order_index: int) -> Course:
        row = Course(id=course_id, slug=slug, title=title, path=path, order_index=order_index)
        self.session.add(row)
        self.session.commit()
        self.session.refresh(row)
        return row

    def create_block(
        self,
        *,
        block_id: str,
        course_id: str,
        slug: str,
        title: str,
        path: str,
        order_index: int,
    ) -> Block:
        row = Block(
            id=block_id,
            course_id=course_id,
            slug=slug,
            title=title,
            path=path,
            order_index=order_index,
        )
        self.session.add(row)
        self.session.commit()
        self.session.refresh(row)
        return row

    def create_lesson(
        self,
        *,
        lesson_id: str,
        course_id: str,
        block_id: str,
        slug: str,
        title: str,
        path: str,
        order_index: int,
        quiz_hash: str | None = None,
        homework_ref: str | None = None,
        checker_ref: str | None = None,
        content_hash: str | None = None,
    ) -> Lesson:
        row = Lesson(
            id=lesson_id,
            course_id=course_id,
            block_id=block_id,
            slug=slug,
            title=title,
            path=path,
            order_index=order_index,
            quiz_hash=quiz_hash,
            homework_ref=homework_ref,
            checker_ref=checker_ref,
            content_hash=content_hash,
        )
        self.session.add(row)
        self.session.commit()
        self.session.refresh(row)
        return row

    def get_lesson(self, lesson_id: str) -> Lesson | None:
        return self.session.get(Lesson, lesson_id)

    def get_course(self, course_id: str) -> Course | None:
        return self.session.get(Course, course_id)

    def get_block(self, block_id: str) -> Block | None:
        return self.session.get(Block, block_id)

    def get_lesson_by_path(self, lesson_path: str) -> Lesson | None:
        stmt = select(Lesson).where(Lesson.path == lesson_path)
        return self.session.exec(stmt).first()

    def list_courses(self) -> list[Course]:
        stmt = select(Course).order_by(Course.order_index, Course.slug)
        return list(self.session.exec(stmt).all())

    def list_blocks(self) -> list[Block]:
        stmt = select(Block).order_by(Block.course_id, Block.order_index, Block.slug)
        return list(self.session.exec(stmt).all())

    def list_lessons(self) -> list[Lesson]:
        stmt = select(Lesson).order_by(Lesson.course_id, Lesson.order_index, Lesson.slug)
        return list(self.session.exec(stmt).all())

    def upsert_course(
        self,
        *,
        course_id: str,
        slug: str,
        title: str,
        path: str,
        order_index: int,
        content_hash: str | None = None,
    ) -> tuple[UpsertAction, Course]:
        row = self.get_course(course_id)
        if row is None:
            row = Course(
                id=course_id,
                slug=slug,
                title=title,
                path=path,
                order_index=order_index,
                content_hash=content_hash,
            )
            self.session.add(row)
            self.session.commit()
            self.session.refresh(row)
            return ("created", row)

        changed = False
        if row.slug != slug:
            row.slug = slug
            changed = True
        if row.title != title:
            row.title = title
            changed = True
        if row.path != path:
            row.path = path
            changed = True
        if row.order_index != order_index:
            row.order_index = order_index
            changed = True
        if row.content_hash != content_hash:
            row.content_hash = content_hash
            changed = True

        if not changed:
            return ("unchanged", row)

        self.session.commit()
        self.session.refresh(row)
        return ("updated", row)

    def upsert_block(
        self,
        *,
        block_id: str,
        course_id: str,
        slug: str,
        title: str,
        path: str,
        order_index: int,
        content_hash: str | None = None,
    ) -> tuple[UpsertAction, Block]:
        row = self.get_block(block_id)
        if row is None:
            row = Block(
                id=block_id,
                course_id=course_id,
                slug=slug,
                title=title,
                path=path,
                order_index=order_index,
                content_hash=content_hash,
            )
            self.session.add(row)
            self.session.commit()
            self.session.refresh(row)
            return ("created", row)

        changed = False
        if row.course_id != course_id:
            row.course_id = course_id
            changed = True
        if row.slug != slug:
            row.slug = slug
            changed = True
        if row.title != title:
            row.title = title
            changed = True
        if row.path != path:
            row.path = path
            changed = True
        if row.order_index != order_index:
            row.order_index = order_index
            changed = True
        if row.content_hash != content_hash:
            row.content_hash = content_hash
            changed = True

        if not changed:
            return ("unchanged", row)

        self.session.commit()
        self.session.refresh(row)
        return ("updated", row)

    def upsert_lesson(
        self,
        *,
        lesson_id: str,
        course_id: str,
        block_id: str,
        slug: str,
        title: str,
        path: str,
        order_index: int,
        quiz_hash: str | None = None,
        homework_ref: str | None = None,
        checker_ref: str | None = None,
        content_hash: str | None = None,
    ) -> tuple[UpsertAction, Lesson]:
        row = self.get_lesson(lesson_id)
        if row is None:
            row = Lesson(
                id=lesson_id,
                course_id=course_id,
                block_id=block_id,
                slug=slug,
                title=title,
                path=path,
                order_index=order_index,
                quiz_hash=quiz_hash,
                homework_ref=homework_ref,
                checker_ref=checker_ref,
                content_hash=content_hash,
            )
            self.session.add(row)
            self.session.commit()
            self.session.refresh(row)
            return ("created", row)

        changed = False
        if row.course_id != course_id:
            row.course_id = course_id
            changed = True
        if row.block_id != block_id:
            row.block_id = block_id
            changed = True
        if row.slug != slug:
            row.slug = slug
            changed = True
        if row.title != title:
            row.title = title
            changed = True
        if row.path != path:
            row.path = path
            changed = True
        if row.order_index != order_index:
            row.order_index = order_index
            changed = True
        if row.quiz_hash != quiz_hash:
            row.quiz_hash = quiz_hash
            changed = True
        if row.homework_ref != homework_ref:
            row.homework_ref = homework_ref
            changed = True
        if row.checker_ref != checker_ref:
            row.checker_ref = checker_ref
            changed = True
        if row.content_hash != content_hash:
            row.content_hash = content_hash
            changed = True

        if not changed:
            return ("unchanged", row)

        self.session.commit()
        self.session.refresh(row)
        return ("updated", row)
