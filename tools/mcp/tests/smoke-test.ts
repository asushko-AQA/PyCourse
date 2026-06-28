/**
 * Smoke test for MCP tool handlers (run from repo root):
 *   npx tsx tools/mcp/tests/smoke-test.ts
 */

import { inspectLesson } from "../src/lib/inspect-lesson.js";
import { quizHash } from "../src/lib/quiz-hash.js";
import { validateContent } from "../src/lib/validate-content.js";
import { getLogFilePath, logToolCall } from "../src/logger.js";
import { assertRepoRoot, getRepoRoot } from "../src/repo-root.js";

function assert(condition: boolean, message: string): void {
  if (!condition) throw new Error(message);
}

async function main(): Promise<void> {
  const root = getRepoRoot();
  process.chdir(root);
  assertRepoRoot(root);
  console.log("Repo root:", root);

  const validation = validateContent({ course: "course-1-python-basics" });
  assert(validation.lessonsChecked > 0, "validate_content returned no lessons");
  console.log(
    `validate_content: ${validation.lessonsChecked} lessons, ${validation.problems.length} problems`,
  );

  const lesson = inspectLesson({
    lessonPath:
      "course-1-python-basics/block-1-meeting-your-computer/lesson-1-1-installing-python",
  });
  assert(lesson.lessonId === "lesson-1-1", "inspect_lesson wrong lesson id");
  console.log(`inspect_lesson: ${lesson.lessonId} ok`);

  const hashes = await quizHash("lesson-1-1-installing-python");
  assert(hashes.hashed >= 2, "quiz_hash expected en+ru hashes");
  console.log(`quiz_hash: ${hashes.hashed} hashed`);

  let negativePassed = false;
  try {
    inspectLesson({ lessonPath: "lesson-does-not-exist-xyz" });
  } catch (error) {
    negativePassed = true;
    logToolCall({
      timestamp: new Date().toISOString(),
      tool: "inspect_lesson",
      args: { lesson_path: "lesson-does-not-exist-xyz" },
      status: "error",
      durationMs: 0,
      summary: error instanceof Error ? error.message : String(error),
      error: error instanceof Error ? error.message : String(error),
    });
  }
  assert(negativePassed, "negative-path inspect_lesson should throw");
  console.log("negative-path inspect_lesson: logged error as expected");
  console.log("Log file:", getLogFilePath());
  console.log("Smoke test passed.");
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
