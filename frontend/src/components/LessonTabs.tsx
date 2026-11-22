"use client";

/**
 * Lesson player: Theory / Assignments / Quiz / Files tabs.
 *  - Theory & Assignments render markdown.
 *  - Assignments tab has a "mark done" button that completes the lesson.
 *  - Quiz tab hosts the QuizEngine (XP + confetti + completion).
 *  - Files tab shows the lesson folder files (starter, exercises, solution);
 *    links to those files in the markdown switch to it.
 * Panels stay mounted (hidden when inactive) so quiz progress survives tab switches.
 */

import { useState } from "react";
import Link from "next/link";
import { motion } from "framer-motion";
import type { LessonFile, QuizQuestion } from "@/lib/types";
import type { Dict } from "@/lib/i18n";
import { useHydrated, useProgressStore } from "@/stores/progressStore";
import MarkdownView from "./MarkdownView";
import QuizEngine from "./QuizEngine";
import LessonFiles, { lessonFileAnchorId } from "./LessonFiles";
import { fireConfettiBurst } from "./ConfettiTrigger";
import { playChime } from "./ChimePlayer";

interface LessonTabsProps {
  lessonKey: string;
  theory: string;
  assignments: string;
  quiz: QuizQuestion[];
  files: LessonFile[];
  dict: Dict;
  courseHref: string;
  nextHref: string | null;
}

type TabId = "theory" | "assignments" | "quiz" | "files";

export default function LessonTabs({
  lessonKey,
  theory,
  assignments,
  quiz,
  files,
  dict,
  courseHref,
  nextHref,
}: LessonTabsProps) {
  const [tab, setTab] = useState<TabId>("theory");
  const hydrated = useHydrated();
  const completedLessons = useProgressStore((s) => s.completedLessons);
  const completeLesson = useProgressStore((s) => s.completeLesson);
  const lessonDone = hydrated && completedLessons.includes(lessonKey);

  const tabs: { id: TabId; label: string }[] = [
    { id: "theory", label: dict.tabs.theory },
    { id: "assignments", label: dict.tabs.assignments },
    { id: "quiz", label: dict.tabs.quiz },
    ...(files.length > 0 ? [{ id: "files" as const, label: dict.tabs.files }] : []),
  ];

  function openFile(filePath: string) {
    setTab("files");
    requestAnimationFrame(() => {
      if (filePath.startsWith("solution")) {
        document
          .querySelector<HTMLDetailsElement>('[data-automation-id="lesson-solution"]')
          ?.setAttribute("open", "");
      }
      document
        .getElementById(lessonFileAnchorId(filePath))
        ?.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  }

  function markAssignmentsDone() {
    if (lessonDone) return;
    completeLesson(lessonKey);
    playChime("correct");
    fireConfettiBurst();
  }

  return (
    <div className="flex flex-col gap-6">
      {/* Tab bar */}
      <div className="flex flex-wrap gap-1.5 self-start rounded-3xl bg-slate-100 p-1.5" role="tablist">
        {tabs.map((t) => (
          <button
            key={t.id}
            data-automation-id={`lesson-tab-${t.id}`}
            onClick={() => setTab(t.id)}
            className={`relative rounded-full px-4 py-2 text-sm font-extrabold transition-colors sm:px-5 ${
              tab === t.id ? "text-white" : "text-slate-500 hover:text-slate-700"
            }`}
            aria-selected={tab === t.id}
            role="tab"
          >
            {tab === t.id && (
              <motion.span
                layoutId="tab-pill"
                className="absolute inset-0 rounded-full bg-gradient-to-r from-violet-500 to-fuchsia-500 shadow"
                transition={{ type: "spring", duration: 0.4 }}
              />
            )}
            <span className="relative">{t.label}</span>
          </button>
        ))}
      </div>

      {/* Tab content */}
      <div className="rounded-3xl bg-white p-5 shadow-sm ring-1 ring-slate-100 sm:p-8">
        <div hidden={tab !== "theory"}>
          <MarkdownView markdown={theory} onFileLink={openFile} />
        </div>

        <div hidden={tab !== "assignments"}>
          <div className="flex flex-col gap-6">
            <MarkdownView markdown={assignments} onFileLink={openFile} />
            <button
              data-automation-id="lesson-mark-done"
              onClick={markAssignmentsDone}
              disabled={lessonDone}
              className={`self-start rounded-full px-6 py-2.5 font-extrabold transition-transform ${
                lessonDone
                  ? "bg-emerald-100 text-emerald-700"
                  : "bg-emerald-500 text-white shadow-lg hover:scale-105"
              }`}
            >
              {lessonDone ? dict.lesson.markedDone : dict.lesson.markDone}
            </button>
          </div>
        </div>

        <div hidden={tab !== "quiz"}>
          {quiz.length > 0 ? (
            <QuizEngine
              lessonKey={lessonKey}
              questions={quiz}
              dict={dict}
              courseHref={courseHref}
              nextHref={nextHref}
            />
          ) : (
            <p className="font-semibold text-slate-500">{dict.lesson.noQuiz}</p>
          )}
        </div>

        {files.length > 0 && (
          <div hidden={tab !== "files"}>
            <LessonFiles files={files} dict={dict} onFileLink={openFile} />
          </div>
        )}
      </div>

      {/* Footer nav */}
      <div className="flex items-center justify-between">
        <Link
          href={courseHref}
          data-automation-id="lesson-back-to-map"
          className="font-bold text-sky-600 hover:underline"
        >
          {dict.lesson.backToMap}
        </Link>
        {nextHref && lessonDone && (
          <Link
            href={nextHref}
            data-automation-id="lesson-next"
            className="rounded-full bg-emerald-500 px-5 py-2 font-extrabold text-white shadow transition-transform hover:scale-105"
          >
            {dict.lesson.nextLesson}
          </Link>
        )}
      </div>
    </div>
  );
}
