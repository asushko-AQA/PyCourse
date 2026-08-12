/**
 * Thin client for the FastAPI progress endpoints (plan 08).
 *
 * The typed, generated client arrives in plan 11; until then this hand-written
 * wrapper covers fetch/upsert/merge.
 */

const BACKEND_URL = (
  process.env.NEXT_PUBLIC_BACKEND_URL ?? "http://localhost:8000"
).replace(/\/$/, "");

export type ProgressErrorCode =
  | "generic"
  | "unauthorized"
  | "invalid_lesson_key";

export class ProgressApiError extends Error {
  code: ProgressErrorCode;
  constructor(code: ProgressErrorCode, message?: string) {
    super(message ?? code);
    this.code = code;
  }
}

export interface LessonProgressItem {
  lessonKey: string;
  readingDone: boolean;
  homeworkDone: boolean;
  quizPerfect: boolean;
  lastPosition: string | null;
  updatedAt: string | null;
}

export interface ProgressSnapshot {
  lessons: LessonProgressItem[];
  lastPosition: string | null;
}

export interface ProgressUpsertInput {
  lessonKey: string;
  readingDone?: boolean;
  homeworkDone?: boolean;
  quizPerfect?: boolean;
  lastPosition?: string | null;
}

export interface ProgressMergeLesson {
  lessonKey: string;
  readingDone?: boolean;
  homeworkDone?: boolean;
  quizPerfect?: boolean;
}

async function parseErrorCode(res: Response): Promise<ProgressErrorCode> {
  try {
    const data = await res.json();
    const code = data?.detail?.code;
    if (typeof code === "string") return code as ProgressErrorCode;
  } catch {
    // fall through
  }
  return "generic";
}

function mapLessonItem(raw: Record<string, unknown>): LessonProgressItem {
  return {
    lessonKey: String(raw.lesson_key),
    readingDone: Boolean(raw.reading_done),
    homeworkDone: Boolean(raw.homework_done),
    quizPerfect: Boolean(raw.quiz_perfect),
    lastPosition: raw.last_position == null ? null : String(raw.last_position),
    updatedAt: raw.updated_at == null ? null : String(raw.updated_at),
  };
}

function mapSnapshot(raw: Record<string, unknown>): ProgressSnapshot {
  const lessonsRaw = Array.isArray(raw.lessons) ? raw.lessons : [];
  return {
    lessons: lessonsRaw.map((item) => mapLessonItem(item as Record<string, unknown>)),
    lastPosition: raw.last_position == null ? null : String(raw.last_position),
  };
}

export async function fetchProgress(): Promise<ProgressSnapshot> {
  let res: Response;
  try {
    res = await fetch(`${BACKEND_URL}/progress`, {
      method: "GET",
      credentials: "include",
    });
  } catch {
    throw new ProgressApiError("generic", "network error");
  }

  if (!res.ok) throw new ProgressApiError(await parseErrorCode(res));
  return mapSnapshot(await res.json());
}

export async function upsertProgress(input: ProgressUpsertInput): Promise<LessonProgressItem> {
  let res: Response;
  try {
    res = await fetch(`${BACKEND_URL}/progress`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify({
        lesson_key: input.lessonKey,
        reading_done: input.readingDone,
        homework_done: input.homeworkDone,
        quiz_perfect: input.quizPerfect,
        last_position: input.lastPosition,
      }),
    });
  } catch {
    throw new ProgressApiError("generic", "network error");
  }

  if (!res.ok) throw new ProgressApiError(await parseErrorCode(res));
  const data = await res.json();
  return mapLessonItem(data.lesson as Record<string, unknown>);
}

export async function mergeProgress(
  lessons: ProgressMergeLesson[],
  lastPosition?: string | null,
): Promise<ProgressSnapshot> {
  let res: Response;
  try {
    res = await fetch(`${BACKEND_URL}/progress/merge`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify({
        lessons: lessons.map((lesson) => ({
          lesson_key: lesson.lessonKey,
          reading_done: lesson.readingDone ?? false,
          homework_done: lesson.homeworkDone ?? false,
          quiz_perfect: lesson.quizPerfect ?? false,
        })),
        last_position: lastPosition ?? null,
      }),
    });
  } catch {
    throw new ProgressApiError("generic", "network error");
  }

  if (!res.ok) throw new ProgressApiError(await parseErrorCode(res));
  const data = await res.json();
  return mapSnapshot(data.snapshot as Record<string, unknown>);
}
