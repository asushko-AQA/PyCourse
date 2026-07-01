"use client";

/**
 * Gamification progress store (Zustand + localStorage persist).
 *
 * Keys are lesson progress keys like "course-1/lesson-2-1" (globally unique —
 * lesson ids alone repeat across courses).
 *
 * XP rules:
 *  - finishing a lesson quiz (first time): +XP_PER_QUIZ, also completes the lesson
 *  - completing a lesson (first time, via quiz or "mark done"): +XP_PER_LESSON
 *  - level = floor(xp / XP_PER_LEVEL) + 1
 *
 * Hydration: SSR and the first client render always see the initial state.
 * Use `useHydrated()` before reading persisted values to avoid mismatches.
 */

import { useSyncExternalStore } from "react";
import { create } from "zustand";
import { persist } from "zustand/middleware";

export const XP_PER_QUIZ = 10;
export const XP_PER_LESSON = 5;
export const XP_PER_LEVEL = 50;

export function getLevel(xp: number): number {
  return Math.floor(xp / XP_PER_LEVEL) + 1;
}

/** 0..1 progress toward the next level. */
export function getLevelProgress(xp: number): number {
  return (xp % XP_PER_LEVEL) / XP_PER_LEVEL;
}

interface ProgressState {
  xp: number;
  completedLessons: string[];
  completedQuizzes: string[];
  addXp: (amount: number) => void;
  /** Mark a lesson complete (idempotent). Awards XP_PER_LESSON the first time. */
  completeLesson: (key: string) => void;
  /** Mark a quiz complete (idempotent). Awards XP and completes the lesson. */
  completeQuiz: (key: string) => void;
  /** Clear all local progress (used on sign-out before server sync exists). */
  reset: () => void;
}

export const useProgressStore = create<ProgressState>()(
  persist(
    (set) => ({
      xp: 0,
      completedLessons: [],
      completedQuizzes: [],

      addXp: (amount) => set((s) => ({ xp: s.xp + amount })),

      completeLesson: (key) =>
        set((s) => {
          if (s.completedLessons.includes(key)) return s;
          return {
            completedLessons: [...s.completedLessons, key],
            xp: s.xp + XP_PER_LESSON,
          };
        }),

      completeQuiz: (key) =>
        set((s) => {
          if (s.completedQuizzes.includes(key)) return s;
          const lessonAlreadyDone = s.completedLessons.includes(key);
          return {
            completedQuizzes: [...s.completedQuizzes, key],
            completedLessons: lessonAlreadyDone
              ? s.completedLessons
              : [...s.completedLessons, key],
            xp: s.xp + XP_PER_QUIZ + (lessonAlreadyDone ? 0 : XP_PER_LESSON),
          };
        }),

      reset: () =>
        set({
          xp: 0,
          completedLessons: [],
          completedQuizzes: [],
        }),
    }),
    { name: "pyquest-progress" },
  ),
);

const subscribeNoop = () => () => {};

/**
 * True once the component is mounted on the client (and the persisted store
 * has therefore been rehydrated). Render default/skeleton state until then.
 *
 * Uses `useSyncExternalStore` so the server/first-paint snapshot is `false` and
 * the client snapshot is `true` — the React-recommended hydration pattern, with
 * no `setState` inside an effect.
 */
export function useHydrated(): boolean {
  return useSyncExternalStore(
    subscribeNoop,
    () => true,
    () => false,
  );
}

/** Is a lesson unlocked given the completed-lessons list? */
export function isUnlocked(
  prerequisiteKey: string | null,
  completedLessons: string[],
): boolean {
  return prerequisiteKey === null || completedLessons.includes(prerequisiteKey);
}
