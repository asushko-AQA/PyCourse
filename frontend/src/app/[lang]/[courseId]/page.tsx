import Link from "next/link";
import { notFound } from "next/navigation";
import { getCourse, getCourses } from "@/lib/courseParser";
import { getDict } from "@/lib/i18n";
import { isLang, LANGS } from "@/lib/types";
import CourseMap, { type MapBlock } from "@/components/CourseMap";

export function generateStaticParams() {
  return LANGS.flatMap((lang) =>
    getCourses().map((course) => ({ lang, courseId: course.id })),
  );
}

export const dynamicParams = false;

/** "lesson-2-1" → "2.1" */
function lessonNum(lessonId: string): string {
  const m = lessonId.match(/^lesson-(\d+)-(\d+)$/);
  return m ? `${m[1]}.${m[2]}` : lessonId;
}

export default async function CoursePage({
  params,
}: {
  params: Promise<{ lang: string; courseId: string }>;
}) {
  const { lang, courseId } = await params;
  if (!isLang(lang)) notFound();
  const course = getCourse(courseId);
  if (!course) notFound();

  const dict = getDict(lang);
  const courseMeta = dict.courses[course.id];

  const blocks: MapBlock[] = course.blocks.map((block) => {
    const blockMeta = dict.blocks[`${course.id}/${block.id}`] ?? {
      title: block.slug,
      emoji: "📦",
    };
    return {
      id: block.id,
      title: blockMeta.title,
      emoji: blockMeta.emoji,
      lessons: block.lessons.map((lesson) => ({
        key: lesson.key,
        prerequisiteKey: lesson.prerequisiteKey,
        href: `/${lang}/${course.id}/${block.id}/${lesson.id}`,
        num: lessonNum(lesson.id),
        title: lesson.content[lang].title,
        levelTitle: lesson.content[lang].levelTitle,
      })),
    };
  });

  return (
    <div className="flex flex-col gap-6">
      <div>
        <Link
          href={`/${lang}`}
          className="text-sm font-bold text-sky-600 hover:underline"
        >
          ← {dict.map.backHome}
        </Link>
        <h1 className="mt-2 flex items-center gap-3 text-3xl font-black text-slate-800">
          <span aria-hidden>{courseMeta?.emoji}</span>
          {courseMeta?.title ?? course.slug}
        </h1>
      </div>

      <CourseMap
        blocks={blocks}
        lockedLabel={dict.map.locked}
        lockedHintTemplate={dict.map.lockedHint}
      />
    </div>
  );
}
