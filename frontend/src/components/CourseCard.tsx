"use client";

/**
 * Home-page course card with live progress (completed lessons / total)
 * read from the persisted store after hydration.
 */

import Link from "next/link";
import { motion } from "framer-motion";
import { useHydrated, useProgressStore } from "@/stores/progressStore";

interface CourseCardProps {
  href: string;
  emoji: string;
  title: string;
  description: string;
  /** Progress keys of all lessons in this course. */
  lessonKeys: string[];
  lessonsLabel: string;
  completedLabel: string;
  startLabel: string;
  continueLabel: string;
  index: number;
}

export default function CourseCard({
  href,
  emoji,
  title,
  description,
  lessonKeys,
  lessonsLabel,
  completedLabel,
  startLabel,
  continueLabel,
  index,
}: CourseCardProps) {
  const hydrated = useHydrated();
  const completedLessons = useProgressStore((s) => s.completedLessons);
  const done = hydrated
    ? lessonKeys.filter((k) => completedLessons.includes(k)).length
    : 0;
  const total = lessonKeys.length;
  const pct = total === 0 ? 0 : Math.round((done / total) * 100);

  return (
    <motion.div
      initial={{ opacity: 0, y: 24 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, delay: index * 0.1 }}
    >
      <Link
        href={href}
        className="group flex h-full flex-col gap-3 rounded-3xl bg-white p-6 shadow-sm ring-1 ring-slate-100 transition-all hover:-translate-y-1 hover:shadow-xl hover:ring-violet-200"
      >
        <div className="text-5xl" aria-hidden>
          {emoji}
        </div>
        <h2 className="text-xl font-extrabold text-slate-800">{title}</h2>
        <p className="flex-1 text-sm font-semibold text-slate-500">
          {description}
        </p>
        <div className="flex items-center justify-between text-xs font-bold text-slate-400">
          <span>
            {total} {lessonsLabel}
          </span>
          <span>
            {done}/{total} {completedLabel}
          </span>
        </div>
        <div className="h-2.5 overflow-hidden rounded-full bg-slate-100">
          <div
            className="h-full rounded-full bg-gradient-to-r from-emerald-400 to-teal-400 transition-all duration-700"
            style={{ width: `${pct}%` }}
          />
        </div>
        <span className="mt-1 self-start rounded-full bg-violet-500 px-5 py-2 text-sm font-extrabold text-white shadow transition-transform group-hover:scale-105">
          {done > 0 ? continueLabel : startLabel} →
        </span>
      </Link>
    </motion.div>
  );
}
