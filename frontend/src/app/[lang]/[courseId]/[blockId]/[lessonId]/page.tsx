import Link from "next/link";
import { notFound } from "next/navigation";
import {
  getCourses,
  getCourseLessons,
  getLesson,
} from "@/lib/courseParser";
import { getDict } from "@/lib/i18n";
import { isLang, LANGS, type Lesson } from "@/lib/types";
import LessonLockGuard from "@/components/LessonLockGuard";
import LessonTabs from "@/components/LessonTabs";

export function generateStaticParams() {
  return LANGS.flatMap((lang) =>
    getCourses().flatMap((course) =>
      course.blocks.flatMap((block) =>
        block.lessons.map((lesson) => ({
          lang,
          courseId: course.id,
          blockId: block.id,
          lessonId: lesson.id,
        })),
      ),
    ),
  );
}

export const dynamicParams = false;

function lessonHref(lang: string, lesson: Lesson): string {
  return `/${lang}/${lesson.courseId}/${lesson.blockId}/${lesson.id}`;
}

export default async function LessonPage({
  params,
}: {
  params: Promise<{
    lang: string;
    courseId: string;
    blockId: string;
    lessonId: string;
  }>;
}) {
  const { lang, courseId, blockId, lessonId } = await params;
  if (!isLang(lang)) notFound();
  const lesson = getLesson(courseId, blockId, lessonId);
  if (!lesson) notFound();

  const dict = getDict(lang);
  const content = lesson.content[lang];

  // Neighbors in the flattened course sequence (for prereq lock + next nav).
  const sequence = getCourseLessons(courseId);
  const idx = sequence.findIndex((l) => l.key === lesson.key);
  const prereq = idx > 0 ? sequence[idx - 1] : null;
  const next = idx >= 0 ? (sequence[idx + 1] ?? null) : null;

  const courseHref = `/${lang}/${courseId}`;
  const blockMeta = dict.blocks[`${courseId}/${blockId}`];

  return (
    <LessonLockGuard
      prerequisiteKey={lesson.prerequisiteKey}
      prerequisiteTitle={prereq ? prereq.content[lang].title : null}
      prerequisiteHref={prereq ? lessonHref(lang, prereq) : null}
      courseHref={courseHref}
      lockedTitle={dict.lesson.lockedTitle}
      lockedBodyTemplate={dict.lesson.lockedBody}
      backToMapLabel={dict.lesson.backToMap}
      goToPrereqLabel={dict.lesson.goToPrereq}
    >
      <div className="flex flex-col gap-6">
        <div>
          <Link
            href={courseHref}
            data-automation-id="lesson-block-back"
            className="text-sm font-bold text-sky-600 hover:underline"
          >
            ← {blockMeta?.emoji} {blockMeta?.title}
          </Link>
          <h1 className="mt-2 text-3xl font-black text-slate-800">
            {content.title}
          </h1>
          {content.levelTitle && (
            <p className="mt-1.5 inline-block rounded-full bg-amber-100 px-3 py-1 text-sm font-extrabold text-amber-700">
              🏅 {content.levelTitle}
            </p>
          )}
        </div>

        <LessonTabs
          lessonKey={lesson.key}
          theory={content.theory}
          assignments={content.assignments}
          quiz={content.quiz}
          dict={dict}
          courseHref={courseHref}
          nextHref={next ? lessonHref(lang, next) : null}
        />
      </div>
    </LessonLockGuard>
  );
}
