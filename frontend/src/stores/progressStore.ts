"use client";

/**
 * Gamification progress store (Zustand + localStorage persist).
 *
 * Keys are lesson progress keys like "course-1/lesson-2-1" (globally unique).
 *
 * When signed in, progress syncs to the FastAPI backend (plan 08). localStorage
 * remains the offline fallback with optimistic updates and a pending queue.
 *
 * Hydration: SSR and the first client render always see the initial state.
 * Use `useHydrated()` before reading persisted values to avoid mismatches.
 */

import { useSyncExternalStore } from "react";
import { create } from "zustand";
import { persist } from "zustand/middleware";

import {
  fetchProgress,
  mergeProgress,
  ProgressApiError,
  upsertProgress,
  type ProgressSnapshot,
  type ProgressUpsertInput,
} from "@/lib/progressClient";

export const XP_PER_QUIZ = 10;
export const XP_PER_LESSON = 5;
export const XP_PER_LEVEL = 50;

/**
 * XP is derived from progress, never accumulated separately, so it can always be
 * rebuilt from a server snapshot: every completed lesson is worth XP_PER_LESSON,
 * every perfect quiz adds XP_PER_QUIZ (a perfect quiz also completes its lesson).
 */
export function computeXp(completedLessons: string[], completedQuizzes: string[]): number {
  const lessons = new Set([...completedLessons, ...completedQuizzes]);
  return lessons.size * XP_PER_LESSON + new Set(completedQuizzes).size * XP_PER_QUIZ;
}

/** A quiz counts (XP, `quizPerfect`, lesson completion) only when every answer was right on the first try. */
export function isPerfectQuiz(firstTryCount: number, total: number): boolean {
  return total > 0 && firstTryCount >= total;
}

export function getLevel(xp: number): number {
  return Math.floor(xp / XP_PER_LEVEL) + 1;
}

/** 0..1 progress toward the next level. */
export function getLevelProgress(xp: number): number {
  return (xp % XP_PER_LEVEL) / XP_PER_LEVEL;
}

export interface PendingProgressUpdate extends ProgressUpsertInput {
  id: string;
}

type SyncStatus = "idle" | "syncing" | "offline" | "error";

interface ProgressState {
  xp: number;
  completedLessons: string[];
  completedQuizzes: string[];
  hasMergedLocal: boolean;
  mergedForUserId: string | null;
  pendingUpdates: PendingProgressUpdate[];
  syncStatus: SyncStatus;
  isSignedIn: boolean;

  completeLesson: (key: string) => void;
  /**
   * Record a finished quiz. Returns true when this attempt earned the reward
   * (perfect score and not collected before); imperfect attempts change nothing.
   */
  completeQuiz: (key: string, firstTryCount: number, total: number) => boolean;
  setLastPosition: (position: string) => void;
  reset: () => void;

  setSignedIn: (signedIn: boolean, userId?: string) => void;
  syncWithServer: (userId?: string) => Promise<void>;
  flushPending: () => Promise<void>;
}

let syncChain: Promise<void> = Promise.resolve();

function enqueueSync(task: () => Promise<void>): void {
  syncChain = syncChain.then(task).catch(() => undefined);
}

/** Rebuild local progress, including XP, from a server snapshot (PL-05). */
export function progressFromSnapshot(
  snapshot: ProgressSnapshot,
): Pick<ProgressState, "completedLessons" | "completedQuizzes" | "xp"> {
  return snapshotToLocal(snapshot);
}

function snapshotToLocal(
  snapshot: ProgressSnapshot,
): Pick<ProgressState, "completedLessons" | "completedQuizzes" | "xp"> {
  const completedLessons = new Set<string>();
  const completedQuizzes = new Set<string>();

  for (const lesson of snapshot.lessons) {
    if (lesson.readingDone || lesson.homeworkDone || lesson.quizPerfect) {
      completedLessons.add(lesson.lessonKey);
    }
    if (lesson.quizPerfect) {
      completedQuizzes.add(lesson.lessonKey);
    }
  }

  return {
    completedLessons: [...completedLessons],
    completedQuizzes: [...completedQuizzes],
    xp: computeXp([...completedLessons], [...completedQuizzes]),
  };
}

function buildMergePayload(state: ProgressState) {
  const keys = new Set([...state.completedLessons, ...state.completedQuizzes]);
  return [...keys].map((lessonKey) => ({
    lessonKey,
    readingDone: state.completedLessons.includes(lessonKey),
    quizPerfect: state.completedQuizzes.includes(lessonKey),
  }));
}

function queueOrSync(
  get: () => ProgressState,
  set: (partial: Partial<ProgressState> | ((s: ProgressState) => Partial<ProgressState>)) => void,
  update: ProgressUpsertInput,
): void {
  if (!get().isSignedIn) return;

  const pending: PendingProgressUpdate = {
    ...update,
    id: `${update.lessonKey}:${Date.now()}:${Math.random().toString(36).slice(2)}`,
  };

  if (typeof navigator !== "undefined" && !navigator.onLine) {
    set((s) => ({
      pendingUpdates: [...s.pendingUpdates, pending],
      syncStatus: "offline",
    }));
    return;
  }

  enqueueSync(async () => {
    set({ syncStatus: "syncing" });
    try {
      await upsertProgress(update);
      set({ syncStatus: "idle" });
    } catch (err) {
      if (err instanceof ProgressApiError && err.code === "unauthorized") {
        set({ isSignedIn: false, syncStatus: "idle" });
        return;
      }
      set((s) => ({
        pendingUpdates: [...s.pendingUpdates, pending],
        syncStatus: "offline",
      }));
    }
  });
}

export const useProgressStore = create<ProgressState>()(
  persist(
    (set, get) => ({
      xp: 0,
      completedLessons: [],
      completedQuizzes: [],
      hasMergedLocal: false,
      mergedForUserId: null,
      pendingUpdates: [],
      syncStatus: "idle",
      isSignedIn: false,

      completeLesson: (key) => {
        set((s) => {
          if (s.completedLessons.includes(key)) return s;
          const completedLessons = [...s.completedLessons, key];
          return {
            completedLessons,
            xp: computeXp(completedLessons, s.completedQuizzes),
          };
        });
        queueOrSync(get, set, { lessonKey: key, readingDone: true });
      },

      completeQuiz: (key, firstTryCount, total) => {
        if (!isPerfectQuiz(firstTryCount, total)) return false;
        if (get().completedQuizzes.includes(key)) return false;
        set((s) => {
          const completedQuizzes = [...s.completedQuizzes, key];
          const completedLessons = s.completedLessons.includes(key)
            ? s.completedLessons
            : [...s.completedLessons, key];
          return {
            completedQuizzes,
            completedLessons,
            xp: computeXp(completedLessons, completedQuizzes),
          };
        });
        queueOrSync(get, set, { lessonKey: key, quizPerfect: true, readingDone: true });
        return true;
      },

      setLastPosition: (position) => {
        const parts = position.split("/");
        const lessonKey =
          parts.length >= 3 ? `${parts[0]}/${parts[2]}` : parts.slice(0, 2).join("/");
        queueOrSync(get, set, { lessonKey, lastPosition: position });
      },

      reset: () =>
        set({
          xp: 0,
          completedLessons: [],
          completedQuizzes: [],
          hasMergedLocal: false,
          mergedForUserId: null,
          pendingUpdates: [],
          syncStatus: "idle",
        }),

      setSignedIn: (signedIn, userId) => {
        // Header components call this on mount, before localStorage has been
        // read. A set() that early would persist the empty initial state and
        // wipe saved progress, so wait until rehydration has finished.
        const apply = () => {
          set({ isSignedIn: signedIn });
          if (!signedIn) return;
          if (userId && get().mergedForUserId !== userId) {
            set({ hasMergedLocal: false });
          }
          enqueueSync(() => get().syncWithServer(userId));
        };
        if (useProgressStore.persist.hasHydrated()) apply();
        else useProgressStore.persist.onFinishHydration(() => apply());
      },

      flushPending: async () => {
        const { pendingUpdates, isSignedIn } = get();
        if (!isSignedIn || pendingUpdates.length === 0) return;

        set({ syncStatus: "syncing" });
        const remaining: PendingProgressUpdate[] = [];

        for (const update of pendingUpdates) {
          try {
            await upsertProgress(update);
          } catch (err) {
            if (err instanceof ProgressApiError && err.code === "unauthorized") {
              set({ isSignedIn: false, syncStatus: "idle", pendingUpdates: [] });
              return;
            }
            remaining.push(update);
          }
        }

        set({
          pendingUpdates: remaining,
          syncStatus: remaining.length > 0 ? "offline" : "idle",
        });
      },

      syncWithServer: async (userId) => {
        if (!get().isSignedIn) return;

        set({ syncStatus: "syncing" });

        try {
          const state = get();
          const needsMerge =
            Boolean(userId && state.mergedForUserId !== userId) ||
            (!state.hasMergedLocal && state.mergedForUserId === null);
          const hasLocal =
            state.completedLessons.length > 0 ||
            state.completedQuizzes.length > 0 ||
            state.pendingUpdates.length > 0;

          if (hasLocal && needsMerge) {
            const snapshot = await mergeProgress(buildMergePayload(state));
            set({
              ...snapshotToLocal(snapshot),
              hasMergedLocal: true,
              mergedForUserId: userId ?? state.mergedForUserId,
              syncStatus: "idle",
            });
          } else {
            const snapshot = await fetchProgress();
            set({
              ...snapshotToLocal(snapshot),
              hasMergedLocal: true,
              mergedForUserId: userId ?? state.mergedForUserId,
              syncStatus: "idle",
            });
          }

          await get().flushPending();
        } catch (err) {
          if (err instanceof ProgressApiError && err.code === "unauthorized") {
            set({ isSignedIn: false, syncStatus: "idle" });
            return;
          }
          set({ syncStatus: "offline" });
        }
      },
    }),
    {
      name: "pyquest-progress",
      // Older builds stored an accumulated XP counter; always re-derive it.
      merge: (persisted, current) => {
        const merged = { ...current, ...(persisted as Partial<ProgressState>) };
        return {
          ...merged,
          xp: computeXp(merged.completedLessons ?? [], merged.completedQuizzes ?? []),
        };
      },
      partialize: (state) => ({
        xp: state.xp,
        completedLessons: state.completedLessons,
        completedQuizzes: state.completedQuizzes,
        hasMergedLocal: state.hasMergedLocal,
        mergedForUserId: state.mergedForUserId,
        pendingUpdates: state.pendingUpdates,
      }),
    },
  ),
);

const subscribeNoop = () => () => {};

/**
 * True once the component is mounted on the client (and the persisted store
 * has therefore been rehydrated).
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

/** Re-sync queued progress when the browser comes back online. */
if (typeof window !== "undefined") {
  window.addEventListener("online", () => {
    const { isSignedIn, flushPending, syncWithServer } = useProgressStore.getState();
    if (!isSignedIn) return;
    void flushPending().then(() => syncWithServer());
  });
}
