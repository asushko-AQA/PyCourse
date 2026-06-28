"use client";

/**
 * One-question-at-a-time quiz with progress dots, confetti + chime on
 * correct answers, gentle hints on wrong answers (no penalty), and an XP
 * reward on completion (awarded once per lesson via the progress store).
 */

import { useMemo, useState } from "react";
import Link from "next/link";
import { motion, AnimatePresence } from "framer-motion";
import type { QuizQuestion } from "@/lib/types";
import type { Dict } from "@/lib/i18n";
import { fill } from "@/lib/i18n";
import { useProgressStore, XP_PER_QUIZ } from "@/stores/progressStore";
import { fireConfettiBurst, fireConfettiCelebration } from "./ConfettiTrigger";
import { playChime } from "./ChimePlayer";

interface QuizEngineProps {
  /** Progress key of the lesson, e.g. "course-1/lesson-2-1". */
  lessonKey: string;
  questions: QuizQuestion[];
  dict: Dict;
  /** Course map URL (results screen navigation). */
  courseHref: string;
  /** Next lesson URL or null when this is the last lesson of the course. */
  nextHref: string | null;
}

const LETTERS = ["a", "b", "c", "d", "e", "f"];

export default function QuizEngine({
  lessonKey,
  questions,
  dict,
  courseHref,
  nextHref,
}: QuizEngineProps) {
  const completeQuiz = useProgressStore((s) => s.completeQuiz);
  const completedQuizzes = useProgressStore((s) => s.completedQuizzes);

  const [index, setIndex] = useState(0);
  const [solvedSet, setSolvedSet] = useState<Set<number>>(new Set());
  const [wrongPicks, setWrongPicks] = useState<number[]>([]);
  const [firstTryCount, setFirstTryCount] = useState(0);
  const [finished, setFinished] = useState(false);
  const [earnedNow, setEarnedNow] = useState(false);
  const [feedback, setFeedback] = useState<string | null>(null);

  const question = questions[index];
  const solved = solvedSet.has(index);

  const pick = useMemo(
    () => (list: string[]) => list[Math.floor(Math.random() * list.length)],
    [],
  );

  function choose(optionIndex: number) {
    if (solved || finished) return;
    if (optionIndex === question.correctIndex) {
      setSolvedSet((s) => new Set(s).add(index));
      if (wrongPicks.length === 0) setFirstTryCount((n) => n + 1);
      setFeedback(pick(dict.quiz.correct));
      playChime("correct");
      fireConfettiBurst();
    } else {
      setWrongPicks((w) => (w.includes(optionIndex) ? w : [...w, optionIndex]));
      setFeedback(pick(dict.quiz.wrong));
      playChime("wrong");
    }
  }

  function advance() {
    if (index + 1 < questions.length) {
      setIndex(index + 1);
      setWrongPicks([]);
      setFeedback(null);
    } else {
      const isFirstCompletion = !completedQuizzes.includes(lessonKey);
      setEarnedNow(isFirstCompletion);
      completeQuiz(lessonKey);
      setFinished(true);
      playChime("finish");
      fireConfettiCelebration();
    }
  }

  function replay() {
    setIndex(0);
    setSolvedSet(new Set());
    setWrongPicks([]);
    setFirstTryCount(0);
    setFinished(false);
    setFeedback(null);
  }

  if (finished) {
    const stars =
      firstTryCount >= questions.length
        ? 3
        : firstTryCount >= Math.ceil(questions.length * 0.6)
          ? 2
          : 1;
    return (
      <motion.div
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        className="flex flex-col items-center gap-4 rounded-3xl bg-gradient-to-b from-amber-50 to-orange-50 p-8 text-center ring-2 ring-amber-200"
      >
        <div className="text-6xl">🏆</div>
        <h2 className="text-2xl font-extrabold text-amber-700">
          {dict.quiz.resultsTitle}
        </h2>
        <div className="text-3xl" aria-label={`${stars}/3`}>
          {"⭐".repeat(stars)}
          <span className="opacity-25">{"⭐".repeat(3 - stars)}</span>
        </div>
        <p className="font-semibold text-amber-800">
          {fill(dict.quiz.resultsBody, {
            score: firstTryCount,
            total: questions.length,
          })}
        </p>
        <div
          className={`rounded-full px-4 py-1.5 text-sm font-extrabold ${
            earnedNow
              ? "bg-violet-500 text-white shadow-lg"
              : "bg-slate-200 text-slate-500"
          }`}
        >
          {earnedNow
            ? fill(dict.quiz.xpEarned, { xp: XP_PER_QUIZ })
            : dict.quiz.alreadyEarned}
        </div>
        <div className="mt-2 flex flex-wrap justify-center gap-3">
          {nextHref && (
            <Link
              href={nextHref}
              data-automation-id="quiz-next-lesson"
              className="rounded-full bg-emerald-500 px-6 py-2.5 font-extrabold text-white shadow transition-transform hover:scale-105"
            >
              {dict.quiz.nextLesson}
            </Link>
          )}
          <Link
            href={courseHref}
            data-automation-id="quiz-back-to-map"
            className="rounded-full bg-sky-100 px-6 py-2.5 font-extrabold text-sky-700 transition-transform hover:scale-105"
          >
            {dict.quiz.backToMap}
          </Link>
          <button
            data-automation-id="quiz-replay"
            onClick={replay}
            className="rounded-full bg-white px-6 py-2.5 font-extrabold text-slate-500 ring-1 ring-slate-200 transition-transform hover:scale-105"
          >
            {dict.quiz.replay}
          </button>
        </div>
      </motion.div>
    );
  }

  return (
    <div className="flex flex-col gap-5">
      {/* Progress dots */}
      <div className="flex items-center justify-between">
        <span className="text-sm font-bold text-slate-500">
          {fill(dict.quiz.questionOf, {
            current: index + 1,
            total: questions.length,
          })}
        </span>
        <div className="flex gap-1.5">
          {questions.map((_, i) => (
            <span
              key={i}
              className={`h-2.5 w-2.5 rounded-full transition-colors ${
                solvedSet.has(i)
                  ? "bg-emerald-400"
                  : i === index
                    ? "bg-violet-400"
                    : "bg-slate-200"
              }`}
            />
          ))}
        </div>
      </div>

      <AnimatePresence mode="wait">
        <motion.div
          key={index}
          initial={{ opacity: 0, x: 24 }}
          animate={{ opacity: 1, x: 0 }}
          exit={{ opacity: 0, x: -24 }}
          transition={{ duration: 0.2 }}
          className="flex flex-col gap-4"
        >
          <h3 className="text-lg font-extrabold text-slate-800">
            {question.question}
          </h3>

          <div className="flex flex-col gap-2.5">
            {question.options.map((option, i) => {
              const isCorrectPick = solved && i === question.correctIndex;
              const isWrongPick = wrongPicks.includes(i);
              return (
                <motion.button
                  key={i}
                  data-automation-id={`quiz-option-${i}`}
                  onClick={() => choose(i)}
                  disabled={solved}
                  whileTap={solved ? undefined : { scale: 0.98 }}
                  animate={
                    isWrongPick && !solved ? { x: [0, -6, 6, -4, 4, 0] } : {}
                  }
                  className={`flex items-start gap-3 rounded-2xl border-2 p-3.5 text-left font-semibold transition-colors ${
                    isCorrectPick
                      ? "border-emerald-400 bg-emerald-50 text-emerald-800"
                      : isWrongPick
                        ? "border-rose-300 bg-rose-50 text-rose-700"
                        : "border-slate-200 bg-white text-slate-700 hover:border-violet-300 hover:bg-violet-50"
                  } ${solved && !isCorrectPick ? "opacity-50" : ""}`}
                >
                  <span
                    className={`flex h-7 w-7 shrink-0 items-center justify-center rounded-full text-sm font-extrabold ${
                      isCorrectPick
                        ? "bg-emerald-400 text-white"
                        : isWrongPick
                          ? "bg-rose-300 text-white"
                          : "bg-slate-100 text-slate-500"
                    }`}
                  >
                    {isCorrectPick ? "✓" : LETTERS[i]}
                  </span>
                  <span className="pt-0.5">{option}</span>
                </motion.button>
              );
            })}
          </div>

          {feedback && (
            <motion.div
              initial={{ opacity: 0, y: 8 }}
              animate={{ opacity: 1, y: 0 }}
              className={`rounded-2xl p-3.5 text-sm font-bold ${
                solved
                  ? "bg-emerald-50 text-emerald-700"
                  : "bg-amber-50 text-amber-800"
              }`}
            >
              <p>{feedback}</p>
              {!solved && question.explanation && (
                <p className="mt-1.5 font-medium text-amber-700">
                  💡 {dict.quiz.hint}: {question.explanation}
                </p>
              )}
            </motion.div>
          )}

          {solved && (
            <motion.button
              initial={{ opacity: 0, y: 8 }}
              animate={{ opacity: 1, y: 0 }}
              data-automation-id="quiz-advance"
              onClick={advance}
              className="self-end rounded-full bg-violet-500 px-7 py-2.5 font-extrabold text-white shadow-lg transition-transform hover:scale-105"
            >
              {index + 1 < questions.length ? dict.quiz.next : dict.quiz.finish}
            </motion.button>
          )}
        </motion.div>
      </AnimatePresence>
    </div>
  );
}
