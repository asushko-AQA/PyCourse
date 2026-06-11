/**
 * Shared content-model types for the gamified course app.
 *
 * The hierarchy mirrors the repo layout: Course → Block → Lesson.
 * All content is parsed from markdown at build time (see courseParser.ts).
 */

export type Lang = "en" | "ru";

export const LANGS: Lang[] = ["en", "ru"];

export function isLang(value: string): value is Lang {
  return value === "en" || value === "ru";
}

/** One multiple-choice question parsed from a "Quick Check" section. */
export interface QuizQuestion {
  /** Question text (markdown inline formatting allowed). */
  question: string;
  /** Answer options in order a, b, c, d. */
  options: string[];
  /** Index into `options` of the correct answer. */
  correctIndex: number;
  /** Explanation shown as a hint / after answering. */
  explanation: string;
}

/** Language-specific content of a single lesson. */
export interface LessonContent {
  /** Human title, e.g. "Variables, Strings, Integers" (number prefix stripped). */
  title: string;
  /** Fun level name from the "## Title" section, e.g. "Level 6 — Magic Boxes for Your Data". */
  levelTitle: string | null;
  /** Markdown for the Theory tab (intro + numbered steps + code examples). */
  theory: string;
  /** Markdown for the Assignments tab (drills, practice task, debug corner). */
  assignments: string;
  /** Structured quiz for the Quiz tab. */
  quiz: QuizQuestion[];
}

export interface Lesson {
  /** Short id used in URLs, e.g. "lesson-2-1". */
  id: string;
  /** Full folder name, e.g. "lesson-2-1-variables". */
  slug: string;
  /** Short course id, e.g. "course-1". */
  courseId: string;
  /** Short block id, e.g. "block-2". */
  blockId: string;
  /**
   * Globally unique progress key, e.g. "course-1/lesson-2-1".
   * Used in the progress store (lesson ids alone repeat across courses).
   */
  key: string;
  /** Position in the flattened course sequence (0-based). */
  order: number;
  /** Progress key of the lesson that must be completed first, or null for the first lesson of a course. */
  prerequisiteKey: string | null;
  content: Record<Lang, LessonContent>;
}

export interface Block {
  /** Short id used in URLs, e.g. "block-2" (Course 2 starts at "block-0"). */
  id: string;
  /** Full folder name, e.g. "block-2-talking-to-python". */
  slug: string;
  courseId: string;
  lessons: Lesson[];
}

export interface Course {
  /** Short id used in URLs, e.g. "course-1". */
  id: string;
  /** Full folder name, e.g. "course-1-python-basics". */
  slug: string;
  blocks: Block[];
}
