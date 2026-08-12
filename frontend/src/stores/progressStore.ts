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

  addXp: (amount: number) => void;
  completeLesson: (key: string) => void;
  completeQuiz: (key: string) => void;
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

function snapshotToLocal(snapshot: ProgressSnapshot): Pick<ProgressState, "completedLessons" | "completedQuizzes"> {
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

      addXp: (amount) => set((s) => ({ xp: s.xp + amount })),

      completeLesson: (key) => {
        set((s) => {
          if (s.completedLessons.includes(key)) return s;
          return {
            completedLessons: [...s.completedLessons, key],
            xp: s.xp + XP_PER_LESSON,
          };
        });
        queueOrSync(get, set, { lessonKey: key, readingDone: true });
      },

      completeQuiz: (key) => {
        set((s) => {
          if (s.completedQuizzes.includes(key)) return s;
          const lessonAlreadyDone = s.completedLessons.includes(key);
          return {
            completedQuizzes: [...s.completedQuizzes, key],
            completedLessons: lessonAlreadyDone ? s.completedLessons : [...s.completedLessons, key],
            xp: s.xp + XP_PER_QUIZ + (lessonAlreadyDone ? 0 : XP_PER_LESSON),
          };
        });
        queueOrSync(get, set, { lessonKey: key, quizPerfect: true, readingDone: true });
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
        set({ isSignedIn: signedIn });
        if (signedIn) {
          if (userId && get().mergedForUserId !== userId) {
            set({ hasMergedLocal: false });
          }
          enqueueSync(() => get().syncWithServer(userId));
        }
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
