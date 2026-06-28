import fs from "node:fs";
import path from "node:path";
import { getCourses } from "../../../../frontend/src/lib/courseParser.js";
import type { LessonMeta } from "../../../../frontend/src/lib/types.js";
import { LANGS } from "../../../../frontend/src/lib/types.js";
import { getRepoRoot } from "../repo-root.js";

export interface InspectLessonOptions {
  lessonPath: string;
}

export interface LessonLanguageReport {
  title: string;
  levelTitle: string | null;
  theoryChars: number;
  assignmentsChars: number;
  quizCount: number;
  meta: LessonMeta | null;
  sectionsPresent: {
    codeExample: boolean;
    codeExecution: boolean;
    practiceTask: boolean;
    debugCorner: boolean;
  };
  issues: string[];
}

export interface InspectLessonResult {
  lessonPath: string;
  course: string;
  block: string;
  lesson: string;
  lessonId: string;
  files: Record<string, string>;
  languages: Record<string, LessonLanguageReport>;
  starterFiles: string[];
  solutionFiles: string[];
  parityIssues: string[];
}

function normalizeLessonPath(input: string): string {
  return input.replace(/\\/g, "/").replace(/\/+$/, "");
}

function resolveLessonDir(lessonPath: string): string {
  const root = getRepoRoot();
  const normalized = normalizeLessonPath(lessonPath);

  const candidates = [
    path.isAbsolute(normalized) ? normalized : path.join(root, normalized),
    path.join(root, ...normalized.split("/")),
  ];

  for (const candidate of candidates) {
    if (fs.existsSync(path.join(candidate, "en.md"))) {
      return candidate;
    }
  }

  const slug = path.basename(normalized);
  for (const course of getCourses()) {
    for (const block of course.blocks) {
      for (const lesson of block.lessons) {
        if (
          lesson.slug === slug ||
          lesson.slug.includes(slug) ||
          normalized.endsWith(lesson.slug)
        ) {
          return path.join(root, course.slug, block.slug, lesson.slug);
        }
      }
    }
  }

  throw new Error(
    `Lesson not found for path "${lessonPath}". Use a folder like course-1-python-basics/block-1-meeting-your-computer/lesson-1-1-installing-python`,
  );
}

function listFiles(dir: string): string[] {
  if (!fs.existsSync(dir)) return [];
  return fs
    .readdirSync(dir, { withFileTypes: true })
    .filter((entry) => entry.isFile())
    .map((entry) => entry.name)
    .sort();
}

function buildLanguageReport(
  lang: string,
  content: ReturnType<typeof getCourses>[number]["blocks"][number]["lessons"][number]["content"]["en"],
): LessonLanguageReport {
  const issues: string[] = [];

  if (!content.title || content.title === "Untitled") {
    issues.push("missing H1 title");
  }
  if (content.theory.trim().length < 100) {
    issues.push("theory section looks empty");
  }
  if (content.assignments.trim().length < 50) {
    issues.push("assignments section looks empty");
  }
  if (content.quiz.length === 0) {
    issues.push("no quiz parsed");
  } else if (content.quiz.length < 3) {
    issues.push(`only ${content.quiz.length} quiz questions`);
  }

  for (const [index, question] of content.quiz.entries()) {
    if (question.options.length < 2) {
      issues.push(`question ${index + 1} has <2 options`);
    }
    if (
      question.correctIndex < 0 ||
      question.correctIndex >= question.options.length
    ) {
      issues.push(`question ${index + 1} has bad correctIndex`);
    }
    if (!question.explanation) {
      issues.push(`question ${index + 1} missing explanation`);
    }
  }

  if (!content.present.codeExample) {
    issues.push('missing "## Code Example" (schema v2)');
  }
  if (!content.present.codeExecution) {
    issues.push('missing "## Code Execution" (schema v2)');
  }

  return {
    title: content.title,
    levelTitle: content.levelTitle,
    theoryChars: content.theory.trim().length,
    assignmentsChars: content.assignments.trim().length,
    quizCount: content.quiz.length,
    meta: content.meta,
    sectionsPresent: content.present,
    issues,
  };
}

export function inspectLesson(opts: InspectLessonOptions): InspectLessonResult {
  const lessonDir = resolveLessonDir(opts.lessonPath);
  const rel = normalizeLessonPath(path.relative(getRepoRoot(), lessonDir));
  const parts = rel.split("/");
  const course = parts[0] ?? "";
  const block = parts[1] ?? "";
  const lesson = parts[2] ?? "";

  const courses = getCourses();
  const match = courses
    .flatMap((c) =>
      c.blocks.flatMap((b) =>
        b.lessons.map((l) => ({
          course: c,
          block: b,
          lesson: l,
        })),
      ),
    )
    .find((item) => item.lesson.slug === lesson);

  if (!match) {
    throw new Error(`Parsed lesson metadata not found for ${rel}`);
  }

  const languages: Record<string, LessonLanguageReport> = {};
  const files: Record<string, string> = {};

  for (const lang of LANGS) {
    const filePath = path.join(lessonDir, `${lang}.md`);
    files[lang] = path.relative(getRepoRoot(), filePath).replace(/\\/g, "/");
    languages[lang] = buildLanguageReport(lang, match.lesson.content[lang]);
  }

  const parityIssues: string[] = [];
  const enQuiz = languages.en?.quizCount ?? 0;
  const ruQuiz = languages.ru?.quizCount ?? 0;
  if (enQuiz !== ruQuiz) {
    parityIssues.push(`quiz count en=${enQuiz} ru=${ruQuiz}`);
  }

  return {
    lessonPath: rel,
    course,
    block,
    lesson,
    lessonId: match.lesson.id,
    files,
    languages,
    starterFiles: listFiles(path.join(lessonDir, "starter")),
    solutionFiles: listFiles(path.join(lessonDir, "solution")),
    parityIssues,
  };
}
