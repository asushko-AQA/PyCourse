/**
 * Content validation: parses every lesson markdown file and reports lessons
 * with missing/empty sections or unparseable quizzes.
 *
 * Run from frontend/:  npm run validate-content
 */

import { getCourses } from "../src/lib/courseParser";
import { LANGS } from "../src/lib/types";

let lessonCount = 0;
let fileCount = 0;

// Fatal problems (exit 1) — structural breakage the app cannot render.
const problems: string[] = [];
// Non-fatal warnings (exit 0) — schema-v2 gaps tracked for the migration (plan 15).
const warnings: string[] = [];

const courses = getCourses();

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
    }
  }
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
