"use client";

/**
 * Client-side lock screen for lessons whose prerequisite is not completed.
 * Pages are statically generated, so locking must happen on the client where
 * localStorage progress lives. Renders a skeleton until the store hydrates
 * to avoid flashing locked content.
 */

import type { ReactNode } from "react";
import Link from "next/link";
import { isUnlocked, useHydrated, useProgressStore } from "@/stores/progressStore";

interface LessonLockGuardProps {
  prerequisiteKey: string | null;
  prerequisiteTitle: string | null;
  /** URL of the prerequisite lesson. */
  prerequisiteHref: string | null;
  courseHref: string;
  lockedTitle: string;
  /** "{lesson}" placeholder = prerequisite title. */
  lockedBodyTemplate: string;
  backToMapLabel: string;
  goToPrereqLabel: string;
  children: ReactNode;
}

export default function LessonLockGuard({
  prerequisiteKey,
  prerequisiteTitle,
  prerequisiteHref,
  courseHref,
  lockedTitle,
  lockedBodyTemplate,
  backToMapLabel,
  goToPrereqLabel,
  children,
}: LessonLockGuardProps) {
  const hydrated = useHydrated();
  const completedLessons = useProgressStore((s) => s.completedLessons);

  if (!hydrated) {
    return (
      <div className="flex flex-col gap-4 py-8" aria-busy>
        <div className="h-8 w-2/3 animate-pulse rounded-full bg-slate-200" />
        <div className="h-4 w-full animate-pulse rounded-full bg-slate-100" />
        <div className="h-4 w-5/6 animate-pulse rounded-full bg-slate-100" />
        <div className="h-64 w-full animate-pulse rounded-3xl bg-slate-100" />
      </div>
    );
  }

  if (!isUnlocked(prerequisiteKey, completedLessons)) {
    return (
      <div className="flex flex-col items-center gap-5 rounded-3xl bg-slate-50 p-10 text-center ring-2 ring-slate-200">
        <div className="text-6xl" aria-hidden>
          🔒
        </div>
        <h1 className="text-2xl font-extrabold text-slate-700">{lockedTitle}</h1>
        <p className="font-semibold text-slate-500">
          {lockedBodyTemplate.replace("{lesson}", prerequisiteTitle ?? "…")}
        </p>
        <div className="flex flex-wrap justify-center gap-3">
          {prerequisiteHref && (
            <Link
              href={prerequisiteHref}
              className="rounded-full bg-violet-500 px-6 py-2.5 font-extrabold text-white shadow transition-transform hover:scale-105"
            >
              {goToPrereqLabel}
            </Link>
          )}
          <Link
            href={courseHref}
            className="rounded-full bg-sky-100 px-6 py-2.5 font-extrabold text-sky-700 transition-transform hover:scale-105"
          >
            {backToMapLabel}
          </Link>
        </div>
      </div>
    );
  }

  return <>{children}</>;
}
