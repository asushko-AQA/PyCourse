/**
 * Reward rules for quizzes and XP restored from a server snapshot.
 * Run: npx tsx scripts/progress-rules.test.ts
 */
import {
  computeXp,
  isPerfectQuiz,
  progressFromSnapshot,
  XP_PER_LESSON,
  XP_PER_QUIZ,
} from "../src/stores/progressStore";

function check(name: string, ok: boolean): void {
  if (!ok) {
    console.error("FAIL", name);
    process.exitCode = 1;
  } else {
    console.log("ok", name);
  }
}

check("perfect only when every answer is first-try", isPerfectQuiz(4, 4) && !isPerfectQuiz(3, 4) && !isPerfectQuiz(0, 4));
check("empty quiz is not perfect", !isPerfectQuiz(0, 0));

check(
  "xp is lessons × 5 plus perfect quizzes × 10",
  computeXp(["course-1/lesson-0-1", "course-1/lesson-0-2"], ["course-1/lesson-0-1"]) ===
    2 * XP_PER_LESSON + XP_PER_QUIZ,
);

const restored = progressFromSnapshot({
  lastPosition: null,
  lessons: [
    {
      lessonKey: "course-1/lesson-0-1",
      readingDone: true,
      homeworkDone: false,
      quizPerfect: true,
      lastPosition: null,
      updatedAt: null,
    },
    {
      lessonKey: "course-1/lesson-0-2",
      readingDone: true,
      homeworkDone: false,
      quizPerfect: false,
      lastPosition: null,
      updatedAt: null,
    },
  ],
});
check("snapshot restores both lessons", restored.completedLessons.length === 2);
check("snapshot restores only the perfect quiz", restored.completedQuizzes.join() === "course-1/lesson-0-1");
check("snapshot xp is 20, not the stale local 0", restored.xp === 20);

if (process.exitCode) process.exit(process.exitCode);
