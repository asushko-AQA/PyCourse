"use client";

/**
 * Adventure map for one course: blocks as themed zones, lessons as nodes on
 * a winding path. Node states come from the progress store:
 *   locked (padlock, muted) / unlocked (vibrant, pulsing) / completed (star).
 */

import Link from "next/link";
import { motion } from "framer-motion";
import { isUnlocked, useHydrated, useProgressStore } from "@/stores/progressStore";

export interface MapLesson {
  /** Progress key, e.g. "course-1/lesson-2-1". */
  key: string;
  prerequisiteKey: string | null;
  href: string;
  /** Display number, e.g. "2.1". */
  num: string;
  title: string;
  levelTitle: string | null;
}

export interface MapBlock {
  id: string;
  title: string;
  emoji: string;
  lessons: MapLesson[];
}

interface CourseMapProps {
  blocks: MapBlock[];
  lockedLabel: string;
  /** "{lesson}" placeholder = prerequisite lesson title. */
  lockedHintTemplate: string;
}

/** Pastel zone backgrounds, cycled per block. */
const ZONE_STYLES = [
  "from-sky-50 to-indigo-50 ring-sky-200",
  "from-emerald-50 to-teal-50 ring-emerald-200",
  "from-amber-50 to-orange-50 ring-amber-200",
  "from-fuchsia-50 to-pink-50 ring-fuchsia-200",
  "from-violet-50 to-purple-50 ring-violet-200",
];

/** Horizontal offset of a node along the winding path. */
function pathOffset(i: number): number {
  return Math.round(Math.sin(i * 1.1) * 70);
}

export default function CourseMap({
  blocks,
  lockedLabel,
  lockedHintTemplate,
}: CourseMapProps) {
  const hydrated = useHydrated();
  const completedLessons = useProgressStore((s) => s.completedLessons);
  const completed = hydrated ? completedLessons : [];

  // Map prerequisite key → title for lock hints.
  const titleByKey = new Map<string, string>();
  for (const block of blocks)
    for (const lesson of block.lessons) titleByKey.set(lesson.key, lesson.title);

  let nodeIndex = 0;

  return (
    <div className="flex flex-col gap-8">
      {blocks.map((block, blockIdx) => (
        <motion.section
          key={block.id}
          initial={{ opacity: 0, y: 24 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-40px" }}
          transition={{ duration: 0.4 }}
          className={`rounded-3xl bg-gradient-to-b p-6 ring-2 sm:p-8 ${
            ZONE_STYLES[blockIdx % ZONE_STYLES.length]
          }`}
        >
          <h2 className="mb-6 flex items-center gap-3 text-xl font-extrabold text-slate-700 sm:text-2xl">
            <span className="text-3xl" aria-hidden>
              {block.emoji}
            </span>
            {block.title}
          </h2>

          <div className="relative mx-auto flex max-w-md flex-col items-center gap-7">
            {/* Dashed path behind the nodes */}
            <div
              aria-hidden
              className="absolute inset-y-4 left-1/2 w-1 -translate-x-1/2 border-l-4 border-dashed border-white/80"
            />

            {block.lessons.map((lesson) => {
              const i = nodeIndex++;
              const done = completed.includes(lesson.key);
              const unlocked = isUnlocked(lesson.prerequisiteKey, completed);
              const offset = pathOffset(i);

              const circle = (
                <span
                  className={`flex h-16 w-16 items-center justify-center rounded-full text-xl font-extrabold shadow-lg ring-4 transition-transform ${
                    done
                      ? "bg-gradient-to-b from-amber-300 to-yellow-400 text-white ring-amber-200"
                      : unlocked
                        ? "map-node-pulse bg-gradient-to-b from-violet-400 to-fuchsia-500 text-white ring-violet-200 group-hover:scale-110"
                        : "bg-slate-200 text-slate-400 ring-slate-100"
                  }`}
                >
                  {done ? "⭐" : unlocked ? lesson.num : "🔒"}
                </span>
              );

              const label = (
                <span className="max-w-44 text-center">
                  <span
                    className={`block text-sm font-extrabold ${
                      unlocked || done ? "text-slate-700" : "text-slate-400"
                    }`}
                  >
                    {lesson.num} · {lesson.title}
                  </span>
                  {!unlocked && !done && lesson.prerequisiteKey && (
                    <span className="mt-0.5 block text-xs font-medium text-slate-400">
                      {lockedHintTemplate.replace(
                        "{lesson}",
                        titleByKey.get(lesson.prerequisiteKey) ?? "…",
                      )}
                    </span>
                  )}
                </span>
              );

              return (
                <motion.div
                  key={lesson.key}
                  initial={{ opacity: 0, scale: 0.7 }}
                  whileInView={{ opacity: 1, scale: 1 }}
                  viewport={{ once: true, margin: "-20px" }}
                  transition={{ duration: 0.3, delay: 0.05 }}
                  className="relative z-10"
                  style={{ transform: `translateX(${offset}px)` }}
                >
                  {unlocked || done ? (
                    <Link
                      href={lesson.href}
                      className="group flex flex-col items-center gap-2"
                    >
                      {circle}
                      {label}
                    </Link>
                  ) : (
                    <div
                      className="flex cursor-not-allowed flex-col items-center gap-2"
                      title={lockedLabel}
                    >
                      {circle}
                      {label}
                    </div>
                  )}
                </motion.div>
              );
            })}
          </div>
        </motion.section>
      ))}
    </div>
  );
}
