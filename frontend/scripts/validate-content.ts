/**
 * Content validation: parses every lesson markdown file and reports lessons
 * with missing/empty sections or unparseable quizzes.
 *
 * Run from frontend/:  npm run validate-content
 */

import path from "node:path";
import { getContentRoot, getCourses } from "../src/lib/courseParser";
import { getDict } from "../src/lib/i18n";
import { LANGS } from "../src/lib/types";
import {
  checkLessonParity,
  checkQuizBalance,
  checkRelativeLinks,
  checkStarterVsSolution,
} from "./content-checks";

let lessonCount = 0;
let fileCount = 0;

// Fatal problems (exit 1) — structural breakage the app cannot render.
const problems: string[] = [];
// Non-fatal warnings (exit 0) — schema-v2 gaps tracked for the migration (plan 15).
const warnings: string[] = [];

const courses = getCourses();
const contentRoot = getContentRoot();
const SLUG_TITLE_RE = /^course-\d+(?:-[a-z0-9-]+)?$/i;

const report = {
  problem: (msg: string) => problems.push(msg),
  warning: (msg: string) => warnings.push(msg),
};

for (const course of courses) {
  for (const lang of LANGS) {
    const dict = getDict(lang);
    const meta = dict.courses[course.id];
    const where = `i18n/${lang}.ts courses["${course.id}"]`;

    if (!meta) {
      problems.push(`${where}: missing course metadata (card would show slug "${course.slug}")`);
      continue;
    }
    if (!meta.title.trim()) {
      problems.push(`${where}: empty title`);
    } else if (meta.title === course.slug || SLUG_TITLE_RE.test(meta.title)) {
      problems.push(
        `${where}: title "${meta.title}" looks like a raw slug; add a human-readable title`,
      );
    }
    if (!meta.description.trim()) {
      problems.push(`${where}: empty description`);
    }
  }

  for (const block of course.blocks) {
    const blockKey = `${course.id}/${block.id}`;
    for (const lang of LANGS) {
      const blockMeta = getDict(lang).blocks[blockKey];
      if (!blockMeta) {
        problems.push(
          `i18n/${lang}.ts blocks["${blockKey}"]: missing block metadata`,
        );
      }
    }
  }
}

for (const course of courses) {
  for (const block of course.blocks) {
    for (const lesson of block.lessons) {
      lessonCount++;
      const enQuizLen = lesson.content.en.quiz.length;
      for (const lang of LANGS) {
        fileCount++;
        const c = lesson.content[lang];
        const where = `${course.slug}/${block.slug}/${lesson.slug}/${lang}.md`;

        if (!c.title || c.title === "Untitled")
          problems.push(`${where}: missing H1 title`);
        if (c.theory.trim().length < 100)
          problems.push(`${where}: theory section looks empty`);
        if (c.assignments.trim().length < 50)
          problems.push(`${where}: assignments section looks empty`);
        if (c.quiz.length === 0) problems.push(`${where}: no quiz parsed`);
        if (c.quiz.length > 0 && c.quiz.length < 3)
          problems.push(`${where}: only ${c.quiz.length} quiz questions`);

        for (const [i, q] of c.quiz.entries()) {
          if (q.options.length < 2)
            problems.push(`${where}: question ${i + 1} has <2 options`);
          if (q.correctIndex < 0 || q.correctIndex >= q.options.length)
            problems.push(`${where}: question ${i + 1} bad correctIndex`);
          if (!q.explanation)
            problems.push(`${where}: question ${i + 1} missing explanation`);
        }

        // Schema v2 — warn (non-fatal) until migration (plan 15) closes these.
        if (!c.present.codeExample)
          warnings.push(`${where}: missing "## Code Example" section (schema v2)`);
        if (!c.present.codeExecution)
          warnings.push(`${where}: missing "## Code Execution" section (schema v2)`);

        // Bilingual parity: EN and RU should have the same number of quiz questions.
        if (lang === "ru" && c.quiz.length !== enQuizLen)
          warnings.push(
            `${where}: quiz count ${c.quiz.length} ≠ en ${enQuizLen} (parity)`,
          );
      }

      if (course.id === "course-1" || course.id === "course-2") {
        const lessonDir = path.join(
          contentRoot,
          course.slug,
          block.slug,
          lesson.slug,
        );
        const whereLesson = `${course.slug}/${block.slug}/${lesson.slug}`;
        checkStarterVsSolution(lesson, lessonDir, whereLesson, report);
        checkLessonParity(lesson, lessonDir, whereLesson, report);
      }
    }
  }
}

for (const course of courses) {
  // These checks are enforced for Courses 1–2 (the audited courses). Course 3
  // keeps the original parse-only checks while its own gaps are tracked separately.
  if (course.id !== "course-1" && course.id !== "course-2") continue;
  checkQuizBalance(course, report);
  checkRelativeLinks(contentRoot, course, report);
}

console.log(
  `Parsed ${courses.length} courses, ${lessonCount} lessons, ${fileCount} files.`,
);

if (warnings.length > 0) {
  console.warn(`\n${warnings.length} schema-v2 warning(s) (non-fatal):`);
  for (const w of warnings) console.warn(`  - ${w}`);
}

if (problems.length > 0) {
  console.error(`\n${problems.length} problem(s):`);
  for (const p of problems) console.error(`  - ${p}`);
  process.exit(1);
} else {
  console.log("\nAll content parsed cleanly (no fatal problems). ✅");
}
