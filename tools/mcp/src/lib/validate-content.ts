import { getCourses } from "../../../../frontend/src/lib/courseParser.js";
import { LANGS } from "../../../../frontend/src/lib/types.js";

export interface ValidateContentOptions {
  course?: string;
  block?: string;
  lesson?: string;
}

export interface ValidateContentResult {
  coursesParsed: number;
  lessonsChecked: number;
  filesChecked: number;
  problems: string[];
  warnings: string[];
  ok: boolean;
}

function matchesFilter(
  courseSlug: string,
  blockSlug: string,
  lessonSlug: string,
  opts: ValidateContentOptions,
): boolean {
  if (opts.course && !courseSlug.includes(opts.course)) return false;
  if (opts.block && !blockSlug.includes(opts.block)) return false;
  if (opts.lesson && !lessonSlug.includes(opts.lesson)) return false;
  return true;
}

export function validateContent(
  opts: ValidateContentOptions = {},
): ValidateContentResult {
  const problems: string[] = [];
  const warnings: string[] = [];
  let lessonCount = 0;
  let fileCount = 0;

  const courses = getCourses().filter((course) =>
    opts.course ? course.slug.includes(opts.course) : true,
  );

  for (const course of courses) {
    for (const block of course.blocks) {
      if (opts.block && !block.slug.includes(opts.block)) continue;

      for (const lesson of block.lessons) {
        if (
          !matchesFilter(course.slug, block.slug, lesson.slug, opts)
        ) {
          continue;
        }

        lessonCount++;
        const enQuizLen = lesson.content.en.quiz.length;

        for (const lang of LANGS) {
          fileCount++;
          const content = lesson.content[lang];
          const where = `${course.slug}/${block.slug}/${lesson.slug}/${lang}.md`;

          if (!content.title || content.title === "Untitled") {
            problems.push(`${where}: missing H1 title`);
          }
          if (content.theory.trim().length < 100) {
            problems.push(`${where}: theory section looks empty`);
          }
          if (content.assignments.trim().length < 50) {
            problems.push(`${where}: assignments section looks empty`);
          }
          if (content.quiz.length === 0) {
            problems.push(`${where}: no quiz parsed`);
          }
          if (content.quiz.length > 0 && content.quiz.length < 3) {
            problems.push(`${where}: only ${content.quiz.length} quiz questions`);
          }

          for (const [index, question] of content.quiz.entries()) {
            if (question.options.length < 2) {
              problems.push(`${where}: question ${index + 1} has <2 options`);
            }
            if (
              question.correctIndex < 0 ||
              question.correctIndex >= question.options.length
            ) {
              problems.push(`${where}: question ${index + 1} bad correctIndex`);
            }
            if (!question.explanation) {
              problems.push(`${where}: question ${index + 1} missing explanation`);
            }
          }

          if (!content.present.codeExample) {
            warnings.push(
              `${where}: missing "## Code Example" section (schema v2)`,
            );
          }
          if (!content.present.codeExecution) {
            warnings.push(
              `${where}: missing "## Code Execution" section (schema v2)`,
            );
          }

          if (lang === "ru" && content.quiz.length !== enQuizLen) {
            warnings.push(
              `${where}: quiz count ${content.quiz.length} ≠ en ${enQuizLen} (parity)`,
            );
          }
        }
      }
    }
  }

  return {
    coursesParsed: courses.length,
    lessonsChecked: lessonCount,
    filesChecked: fileCount,
    problems,
    warnings,
    ok: problems.length === 0,
  };
}
