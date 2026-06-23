# 02 — Frontend MVP (Local / localStorage)

## Goal
Promote and finish the existing Next.js MVP described in `.cursor/plans/gamified_next.js_course_app_e9e5bc50.plan.md` into a build-clean, demoable web baseline **before any backend wiring**. The app parses canonical course markdown at build time, renders lessons in Theory / Assignments / Quiz tabs, and tracks progress locally. This is the web baseline that plans 07–09 later migrate onto the FastAPI backend.

## Architectural decisions in effect

> 1. **Stack** — Next.js frontend in `frontend/`; FastAPI backend comes later. This MVP is intentionally backend-free.
> 2. **Lesson storage** — Frontend reads **canonical markdown** at build time via `courseParser.ts`; no DB.
> 3. **Gamification** — MVP ships the legacy XP/levels store **as a temporary placeholder**; it is explicitly slated for migration to stars in 09. Do not deepen XP semantics.
> 4. **Homework checking** — Out of scope here; Assignments tab is read + self-mark only.

## Dependencies
- **00** (layout). Benefits from **01** (schema v2) but can proceed on current lesson format; runs in parallel in Wave 0.
- Consumed by: 08 (progress migration off localStorage), 09 (XP→stars), 14 (resume UX hooks).

## Deliverables / Steps (from the existing MVP plan — preserve these todos)
- [ ] Scaffold Next.js 15 + TS + Tailwind + shadcn in `frontend/`; install `react-markdown`, `remark-gfm`, `rehype-raw`, `framer-motion`, `canvas-confetti`, `lucide-react`, `zustand`.
- [ ] `[lang]` routing (`en`/`ru`), root redirect, i18n dictionaries, `LanguageToggle`.
- [ ] `courseParser.ts`: scan `course-*/block-*/lesson-*`, split sections, extract quizzes; typed model in `types.ts`; `npm run validate-content`.
- [ ] Home + `CourseMap` with locked/unlocked/completed node states (lesson N unlocks when N−1 completed).
- [ ] Lesson player: Theory / Assignments / Quiz tabs; `QuizEngine`, `ConfettiTrigger`, `ChimePlayer`, `XPBadge`, `LessonLockGuard`.
- [ ] Zustand `progressStore` with `persist` (localStorage key `pyquest-progress`), hydration-safe.
- [ ] Build-clean gate: `npm run build` generates all static lesson pages with zero TS/build errors.

## Verification
- [ ] `npm run build` passes clean; all lesson pages statically generated.
- [ ] Dev smoke test: roadmap lock/unlock, quiz flow + confetti, RU/EN toggle preserves progress, localStorage persists across reload.
- [ ] `npm run validate-content` reports no lesson missing a quiz/section.

## Out of scope
- Any auth, accounts, or server APIs (06/07).
- Server-backed progress (08).
- Replacing XP with stars (09) — only flagged here.
