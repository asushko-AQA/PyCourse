/**
 * Content-quality checks used by validate-content.ts (beyond "does it parse"):
 * starter vs solution, EN/RU parity, quiz answer-letter balance, relative links.
 *
 * Strict courses (1–2) report these as problems (exit 1); other courses get
 * warnings so the build keeps passing while their gaps are tracked.
 */

import fs from "node:fs";
import path from "node:path";
import type { Course, Lesson } from "../src/lib/types";

export const STRICT_COURSES = new Set(["course-1", "course-2"]);

/**
 * Block 1 of Course 1 is "run-only": the learner runs a finished script and
 * writes their own file (my_intro.py, launch.py…), so starter == solution there
 * on purpose (audit C1-25 tracks whether to keep the duplicate solution/).
 */
const RUN_ONLY_LESSONS = new Set([
  "course-1/lesson-1-1",
  "course-1/lesson-1-2",
  "course-1/lesson-1-3",
  "course-1/lesson-1-4",
]);

export interface Report {
  problem: (msg: string) => void;
  warning: (msg: string) => void;
}

function reportFor(courseId: string, r: Report): (msg: string) => void {
  return STRICT_COURSES.has(courseId) ? r.problem : r.warning;
}

// ---------------------------------------------------------------------------
// starter vs solution
// ---------------------------------------------------------------------------

/** Strip a trailing `# comment` unless the `#` sits inside a string literal. */
function stripInlineComment(line: string): string {
  let quote: string | null = null;
  for (let i = 0; i < line.length; i++) {
    const ch = line[i];
    if (quote) {
      if (ch === "\\") i++;
      else if (ch === quote) quote = null;
    } else if (ch === '"' || ch === "'") {
      quote = ch;
    } else if (ch === "#") {
      return line.slice(0, i);
    }
  }
  return line;
}

/** Executable Python lines: no comments, no blank lines, trimmed. */
export function pythonCode(source: string): string[] {
  return source
    .split(/\r?\n/)
    .map((l) => stripInlineComment(l).trim())
    .filter((l) => l.length > 0);
}

function listPyFiles(dir: string): string[] {
  if (!fs.existsSync(dir)) return [];
  const out: string[] = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name === "__pycache__") continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) out.push(...listPyFiles(full));
    else if (entry.name.endsWith(".py")) out.push(full);
  }
  return out;
}

export function checkStarterVsSolution(
  lesson: Lesson,
  lessonDir: string,
  where: string,
  r: Report,
): void {
  if (RUN_ONLY_LESSONS.has(lesson.key)) return;
  const report = reportFor(lesson.courseId, r);
  const starterDir = path.join(lessonDir, "starter");
  const solutionDir = path.join(lessonDir, "solution");
  for (const starter of listPyFiles(starterDir)) {
    const rel = path.relative(starterDir, starter);
    const starterSrc = fs.readFileSync(starter, "utf-8");
    if (!/\bTODO\b/.test(starterSrc)) {
      report(`${where}/starter/${rel}: starter has no "# TODO" for the learner`);
    }
    const solution = path.join(solutionDir, rel);
    if (!fs.existsSync(solution)) continue;
    const a = pythonCode(starterSrc).join("\n");
    const b = pythonCode(fs.readFileSync(solution, "utf-8")).join("\n");
    if (a === b) {
      report(
        `${where}/starter/${rel}: code (comments ignored) is identical to solution/${rel} — the starter must not contain the solution`,
      );
    }
  }
}

// ---------------------------------------------------------------------------
// EN/RU parity
// ---------------------------------------------------------------------------

const LETTERS = "abcd";

function countMatches(md: string, re: RegExp): number {
  return md.match(re)?.length ?? 0;
}

function fenceCount(md: string): number {
  return Math.floor(countMatches(md, /^\s*```/gm) / 2);
}

export function checkLessonParity(
  lesson: Lesson,
  lessonDir: string,
  where: string,
  r: Report,
): void {
  const report = reportFor(lesson.courseId, r);
  const en = lesson.content.en;
  const ru = lesson.content.ru;

  if (en.quiz.length !== ru.quiz.length) {
    report(`${where}: quiz has ${en.quiz.length} questions in en.md but ${ru.quiz.length} in ru.md`);
  } else {
    en.quiz.forEach((q, i) => {
      const rq = ru.quiz[i];
      if (q.correctIndex !== rq.correctIndex) {
        report(
          `${where}: quiz Q${i + 1} correct answer is ${LETTERS[q.correctIndex]}) in en.md but ${LETTERS[rq.correctIndex]}) in ru.md`,
        );
      }
      if (q.options.length !== rq.options.length) {
        report(`${where}: quiz Q${i + 1} has ${q.options.length} options in en.md but ${rq.options.length} in ru.md`);
      }
    });
  }

  for (const key of Object.keys(en.present) as (keyof typeof en.present)[]) {
    if (en.present[key] !== ru.present[key]) {
      report(`${where}: section "${key}" is ${en.present[key] ? "missing from ru.md" : "missing from en.md"}`);
    }
  }

  const enMd = fs.readFileSync(path.join(lessonDir, "en.md"), "utf-8");
  const ruMd = fs.readFileSync(path.join(lessonDir, "ru.md"), "utf-8");
  const enSteps = countMatches(enMd, /^### (Step|Шаг)\s+\d+/gm);
  const ruSteps = countMatches(ruMd, /^### (Step|Шаг)\s+\d+/gm);
  if (enSteps !== ruSteps) {
    report(`${where}: ${enSteps} numbered steps in en.md but ${ruSteps} in ru.md`);
  }
  const enFences = fenceCount(enMd);
  const ruFences = fenceCount(ruMd);
  if (enFences !== ruFences) {
    r.warning(`${where}: ${enFences} code blocks in en.md but ${ruFences} in ru.md (parity)`);
  }
}

// ---------------------------------------------------------------------------
// Quiz answer-letter balance
// ---------------------------------------------------------------------------

export function checkQuizBalance(course: Course, r: Report): void {
  const report = reportFor(course.id, r);
  const totals = new Map<string, number>();
  let questions = 0;

  for (const block of course.blocks) {
    for (const lesson of block.lessons) {
      const quiz = lesson.content.en.quiz;
      const counts = new Map<string, number>();
      for (const q of quiz) {
        const letter = LETTERS[q.correctIndex] ?? "?";
        counts.set(letter, (counts.get(letter) ?? 0) + 1);
        totals.set(letter, (totals.get(letter) ?? 0) + 1);
        questions++;
      }
      const max = Math.max(0, ...counts.values());
      if (quiz.length >= 3 && max > Math.ceil(quiz.length / 2)) {
        const pattern = quiz.map((q) => LETTERS[q.correctIndex]).join("");
        report(
          `${course.slug}/${block.slug}/${lesson.slug}: quiz answers "${pattern}" — one letter is correct in ${max} of ${quiz.length} questions; spread answers over a–d`,
        );
      }
    }
  }

  if (questions < 20) return;
  for (const letter of LETTERS) {
    const share = (totals.get(letter) ?? 0) / questions;
    if (share < 0.15 || share > 0.35) {
      report(
        `${course.slug}: correct answer ${letter}) is used in ${Math.round(share * 100)}% of ${questions} quiz questions (expected 15–35%)`,
      );
    }
  }
}

// ---------------------------------------------------------------------------
// Relative links and anchors
// ---------------------------------------------------------------------------

/** GitHub-style heading anchor. */
export function githubSlug(heading: string): string {
  return heading
    .replace(/\[([^\]]*)\]\([^)]*\)/g, "$1")
    .replace(/[*_`~]/g, "")
    .trim()
    .toLowerCase()
    .replace(/[^\p{L}\p{M}\p{N}\s-]/gu, "")
    .replace(/\s/g, "-");
}

const anchorCache = new Map<string, Set<string>>();

function anchorsOf(file: string): Set<string> {
  const cached = anchorCache.get(file);
  if (cached) return cached;
  const seen = new Map<string, number>();
  const anchors = new Set<string>();
  let inFence = false;
  for (const line of fs.readFileSync(file, "utf-8").split(/\r?\n/)) {
    if (/^\s*```/.test(line)) inFence = !inFence;
    if (inFence) continue;
    const m = line.match(/^#{1,6}\s+(.+?)\s*#*\s*$/);
    if (!m) continue;
    const base = githubSlug(m[1]);
    const n = seen.get(base) ?? 0;
    seen.set(base, n + 1);
    anchors.add(n === 0 ? base : `${base}-${n}`);
  }
  for (const m of fs.readFileSync(file, "utf-8").matchAll(/<a\s+(?:name|id)="([^"]+)"/g)) {
    anchors.add(m[1]);
  }
  anchorCache.set(file, anchors);
  return anchors;
}

function listMarkdown(dir: string): string[] {
  const out: string[] = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name.startsWith(".") || entry.name === "node_modules") continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) out.push(...listMarkdown(full));
    else if (entry.name.endsWith(".md")) out.push(full);
  }
  return out;
}

export function checkRelativeLinks(root: string, course: Course, r: Report): void {
  const report = reportFor(course.id, r);
  const courseDir = path.join(root, course.slug);
  for (const file of listMarkdown(courseDir)) {
    const rel = path.relative(root, file);
    const text = fs.readFileSync(file, "utf-8").replace(/^\s*```[\s\S]*?^\s*```/gm, "");
    for (const m of text.matchAll(/\[[^\]]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)/g)) {
      const target = m[1];
      if (/^(https?:|mailto:)/.test(target)) continue;
      const [rawPath, anchor] = target.split("#");
      const resolved = rawPath ? path.resolve(path.dirname(file), decodeURI(rawPath)) : file;
      if (!fs.existsSync(resolved)) {
        report(`${rel}: broken link "${target}" (no such file)`);
        continue;
      }
      if (anchor && resolved.endsWith(".md")) {
        if (!anchorsOf(resolved).has(decodeURIComponent(anchor).toLowerCase())) {
          report(`${rel}: link "${target}" points to a missing heading anchor`);
        }
      }
    }
  }
}
