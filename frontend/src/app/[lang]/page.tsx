import { notFound } from "next/navigation";
import { getCourses } from "@/lib/courseParser";
import { getDict } from "@/lib/i18n";
import { isLang } from "@/lib/types";
import CourseCard from "@/components/CourseCard";

export default async function HomePage({
  params,
}: {
  params: Promise<{ lang: string }>;
}) {
  const { lang } = await params;
  if (!isLang(lang)) notFound();
  const dict = getDict(lang);
  const courses = getCourses();

  return (
    <div className="flex flex-col gap-8">
      <div className="text-center">
        <h1 className="text-3xl font-black text-slate-800 sm:text-4xl">
          {dict.home.welcome}
        </h1>
        <p className="mt-2 font-semibold text-slate-500">
          {dict.home.subtitle}
        </p>
      </div>

      <div className="grid gap-6 sm:grid-cols-2">
        {courses.map((course, i) => {
          const meta = dict.courses[course.id] ?? {
            title: course.slug,
            description: "",
            emoji: "📚",
          };
          const lessonKeys = course.blocks.flatMap((b) =>
            b.lessons.map((l) => l.key),
          );
          return (
            <CourseCard
              key={course.id}
              index={i}
              href={`/${lang}/${course.id}`}
              emoji={meta.emoji}
              title={meta.title}
              description={meta.description}
              lessonKeys={lessonKeys}
              lessonsLabel={dict.home.lessons}
              completedLabel={dict.home.completed}
              startLabel={dict.home.start}
              continueLabel={dict.home.continue}
            />
          );
        })}
      </div>
    </div>
  );
}
