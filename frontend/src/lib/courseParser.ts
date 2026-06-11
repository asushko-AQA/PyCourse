/**
 * Build-time course content parser.
 *
 * Scans course/block/lesson folders for en.md + ru.md in the repo root (one
 * level above frontend), splits each lesson markdown into Theory, Assignments
 * and Quiz by `## ` headings, and parses Quick Check sections into structured
 * quiz questions.
 *
 * Server-only: uses `fs`. Import from server components or scripts only.
 */

import fs from "node:fs";
import path from "node:path";
import type {
  Block,
  Course,
  Lang,
  Lesson,
  LessonContent,
  QuizQuestion,
} from "./types";
import { LANGS } from "./types";

// ---------------------------------------------------------------------------
// Content root resolution
// ---------------------------------------------------------------------------

/** Find the repo root containing `course-*` folders (frontend/.. or cwd). */
function resolveContentRoot(): string {
  const candidates = [path.resolve(process.cwd(), ".."), process.cwd()];
  for (const dir of candidates) {
    try {
      const entries = fs.readdirSync(dir);
      if (entries.some((e) => /^course-\d+-/.test(e))) return dir;
    } catch {
      // try next candidate
    }
  }
  throw new Error(
    `Could not locate course content. Looked in: ${candidates.join(", ")}`,
  );
}

function listDirs(parent: string, pattern: RegExp): string[] {
  return fs
    .readdirSync(parent, { withFileTypes: true })
    .filter((e) => e.isDirectory() && pattern.test(e.name))
    .map((e) => e.name);
}

// ---------------------------------------------------------------------------
// Markdown section splitting
// ---------------------------------------------------------------------------

interface Section {
  heading: string;
  body: string;
}

/** Split markdown into the preamble (before the first `## `) and `## ` sections. */
function splitSections(md: string): { preamble: string; sections: Section[] } {
  const lines = md.split(/\r?\n/);
  const sections: Section[] = [];
  const preambleLines: string[] = [];
  let current: Section | null = null;
  let inCodeFence = false;

  for (const line of lines) {
    if (/^```/.test(line.trim())) inCodeFence = !inCodeFence;
    if (!inCodeFence && /^## (?!#)/.test(line)) {
      if (current) sections.push(current);
      current = { heading: line.slice(3).trim(), body: "" };
      continue;
    }
    if (current) current.body += line + "\n";
    else preambleLines.push(line);
  }
  if (current) sections.push(current);
  return { preamble: preambleLines.join("\n"), sections };
}

type SectionCategory = "title" | "theory" | "assignments" | "quiz" | "next";

/** Classify a `## ` heading into a lesson tab. Unknown headings go to theory. */
function categorize(heading: string): SectionCategory {
  const h = heading
    .toLowerCase()
    .replace(/[*_`]/g, "")
    .trim();

  if (/^(title|заголовок)$/.test(h)) return "title";
  if (/^(quick check|проверь себя)/.test(h)) return "quiz";
  if (/^(what'?s next|что дальше|дальше)$/.test(h)) return "next";
  if (/capstone|капстоун/.test(h)) return "assignments";
  if (
    /^(quick drills|быстрые упражнения|practice task|практическое задание|задание для практики|try it yourself|попробуй сам|debug corner|уголок отладки|отладка|разбор ошибок)/.test(
      h,
    )
  ) {
    return "assignments";
  }
  return "theory";
}

/**
 * Replace relative markdown links (starter/…, ../lesson-…, README.md) with
 * their plain text — those targets don't exist as routes in the app.
 * Absolute http(s) links are kept.
 */
function stripRelativeLinks(md: string): string {
  return md.replace(
    /\[([^\]]+)\]\((?!https?:\/\/|#)[^)]+\)/g,
    (_m, text: string) => `**${text}**`,
  );
}

// ---------------------------------------------------------------------------
// Quiz parsing
// ---------------------------------------------------------------------------

const OPTION_RE = /^\s*-\s+\*\*([a-d])\)\*\*\s*(.*)$/;
const QUESTION_RE = /^(\d+)\.\s+(.*)$/;
const ANSWER_RE = /^\s*(\d+)\.\s+\*\*([a-d])\)\*\*\s*(.*)$/;

/**
 * Parse a "Quick Check" section body into structured questions.
 *
 * Expected shape (uniform across the repo):
 *   1. Question text?
 *      - **a)** Option
 *      - **b)** Option
 *   …
 *   <details><summary>…</summary>
 *   1. **b)** Explanation.
 *   </details>
 */
function parseQuiz(body: string): QuizQuestion[] {
  const detailsIdx = body.search(/<details/i);
  const questionsPart = detailsIdx === -1 ? body : body.slice(0, detailsIdx);
  const answersPart = detailsIdx === -1 ? "" : body.slice(detailsIdx);

  // Parse answers: number → { letter, explanation }
  const answers = new Map<number, { letter: string; explanation: string }>();
  for (const line of answersPart.split(/\r?\n/)) {
    const m = line.match(ANSWER_RE);
    if (m) {
      answers.set(Number(m[1]), { letter: m[2], explanation: m[3].trim() });
    }
  }

  // Parse questions and options.
  interface Draft {
    num: number;
    question: string;
    options: string[];
  }
  const drafts: Draft[] = [];
  let current: Draft | null = null;

  for (const line of questionsPart.split(/\r?\n/)) {
    const opt = line.match(OPTION_RE);
    if (opt && current) {
      current.options.push(opt[2].trim());
      continue;
    }
    const q = line.match(QUESTION_RE);
    if (q) {
      if (current) drafts.push(current);
      current = { num: Number(q[1]), question: q[2].trim(), options: [] };
      continue;
    }
    // Continuation of a multi-line question (before its options start).
    if (current && current.options.length === 0 && line.trim() !== "") {
      current.question += " " + line.trim();
    }
  }
  if (current) drafts.push(current);

  return drafts
    .filter((d) => d.options.length >= 2)
    .map((d) => {
      const answer = answers.get(d.num);
      const correctIndex = answer
        ? answer.letter.charCodeAt(0) - "a".charCodeAt(0)
        : 0;
      return {
        question: d.question,
        options: d.options,
        correctIndex: Math.min(Math.max(correctIndex, 0), d.options.length - 1),
        explanation: answer?.explanation ?? "",
      };
    });
}

// ---------------------------------------------------------------------------
// Lesson parsing
// ---------------------------------------------------------------------------

/** Strip the "Lesson 2.1:" / "Урок 2.1:" prefix from the H1 title. */
function extractTitle(preamble: string): string {
  const h1 = preamble.match(/^#\s+(.+)$/m);
  if (!h1) return "Untitled";
  return h1[1].replace(/^(Lesson|Урок)\s+[\d.]+\s*[:.]?\s*/i, "").trim();
}

/** Pull the bold level name out of the "## Title" section body. */
function extractLevelTitle(body: string): string | null {
  const m = body.match(/\*\*([\s\S]+?)\*\*/);
  return m ? m[1].trim() : null;
}

function parseLessonFile(filePath: string): LessonContent {
  const md = fs.readFileSync(filePath, "utf-8");
  const { preamble, sections } = splitSections(md);

  let levelTitle: string | null = null;
  const theoryParts: string[] = [];
  const assignmentParts: string[] = [];
  let quiz: QuizQuestion[] = [];

  for (const section of sections) {
    const category = categorize(section.heading);
    const chunk = `## ${section.heading}\n${section.body}`;
    switch (category) {
      case "title":
        levelTitle = extractLevelTitle(section.body);
        break;
      case "quiz":
        quiz = parseQuiz(section.body);
        break;
      case "assignments":
        assignmentParts.push(chunk);
        break;
      case "next":
        break; // navigation handled by the app itself
      case "theory":
        theoryParts.push(chunk);
        break;
    }
  }

  return {
    title: extractTitle(preamble),
    levelTitle,
    theory: stripRelativeLinks(theoryParts.join("\n").trim()),
    assignments: stripRelativeLinks(assignmentParts.join("\n").trim()),
    quiz,
  };
}

// ---------------------------------------------------------------------------
// Course tree assembly
// ---------------------------------------------------------------------------

/** "lesson-2-1-variables" → [2, 1] for ordering. */
function lessonOrderKey(slug: string): [number, number] {
  const m = slug.match(/^lesson-(\d+)-(\d+)-/);
  return m ? [Number(m[1]), Number(m[2])] : [99, 99];
}

function buildCourse(root: string, courseSlug: string): Course | null {
  const courseDir = path.join(root, courseSlug);
  const courseId = courseSlug.match(/^(course-\d+)/)![1];

  const blockSlugs = listDirs(courseDir, /^block-\d+-/).sort((a, b) => {
    const na = Number(a.match(/^block-(\d+)/)![1]);
    const nb = Number(b.match(/^block-(\d+)/)![1]);
    return na - nb;
  });
  if (blockSlugs.length === 0) return null; // e.g. course-3 placeholder

  const blocks: Block[] = [];
  let order = 0;
  let prevKey: string | null = null;

  for (const blockSlug of blockSlugs) {
    const blockId = blockSlug.match(/^(block-\d+)/)![1];
    const blockDir = path.join(courseDir, blockSlug);

    const lessonSlugs = listDirs(blockDir, /^lesson-\d+-\d+-/).sort((a, b) => {
      const [a1, a2] = lessonOrderKey(a);
      const [b1, b2] = lessonOrderKey(b);
      return a1 - b1 || a2 - b2;
    });

    const lessons: Lesson[] = [];
    for (const lessonSlug of lessonSlugs) {
      const lessonId = lessonSlug.match(/^(lesson-\d+-\d+)/)![1];
      const lessonDir = path.join(blockDir, lessonSlug);

      const enPath = path.join(lessonDir, "en.md");
      const ruPath = path.join(lessonDir, "ru.md");
      if (!fs.existsSync(enPath) || !fs.existsSync(ruPath)) continue;

      const key = `${courseId}/${lessonId}`;
      lessons.push({
        id: lessonId,
        slug: lessonSlug,
        courseId,
        blockId,
        key,
        order,
        prerequisiteKey: prevKey,
        content: {
          en: parseLessonFile(enPath),
          ru: parseLessonFile(ruPath),
        },
      });
      prevKey = key;
      order++;
    }

    blocks.push({ id: blockId, slug: blockSlug, courseId, lessons });
  }

  return { id: courseId, slug: courseSlug, blocks };
}

// ---------------------------------------------------------------------------
// Public API (cached for the duration of the build)
// ---------------------------------------------------------------------------

let cache: Course[] | null = null;

export function getCourses(): Course[] {
  if (cache) return cache;
  const root = resolveContentRoot();
  const courseSlugs = listDirs(root, /^course-\d+-/).sort();
  cache = courseSlugs
    .map((slug) => buildCourse(root, slug))
    .filter((c): c is Course => c !== null);
  return cache;
}

export function getCourse(courseId: string): Course | undefined {
  return getCourses().find((c) => c.id === courseId);
}

export function getLesson(
  courseId: string,
  blockId: string,
  lessonId: string,
): Lesson | undefined {
  return getCourse(courseId)
    ?.blocks.find((b) => b.id === blockId)
    ?.lessons.find((l) => l.id === lessonId);
}

/** Flattened, ordered lessons of one course. */
export function getCourseLessons(courseId: string): Lesson[] {
  return getCourse(courseId)?.blocks.flatMap((b) => b.lessons) ?? [];
}

/** Find a lesson by its progress key, plus the next lesson in sequence. */
export function getLessonByKey(
  key: string,
): { lesson: Lesson; next: Lesson | null } | undefined {
  const courseId = key.split("/")[0];
  const lessons = getCourseLessons(courseId);
  const idx = lessons.findIndex((l) => l.key === key);
  if (idx === -1) return undefined;
  return { lesson: lessons[idx], next: lessons[idx + 1] ?? null };
}

export { LANGS };
