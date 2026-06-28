# 08 — Progress Sync Engine

## Goal
Move lesson/quiz progress from the frontend's localStorage (`pyquest-progress`) to DB-backed server APIs, with a first-login merge from local state, an offline fallback, and preserved unlock logic. This is the bridge from the local MVP (02) to a multi-device, multi-channel platform.

## Architectural decisions in effect

> 1. **Stack** — progress APIs in FastAPI; frontend store syncs over HTTP; bot (13) uses the same APIs.
> 2. **Lesson storage** — progress references **lesson ids/metadata** from the synced DB (05); content stays in markdown.
> 3. **Gamification** — progress events are the substrate stars/streaks (09) are computed from; do not duplicate star logic here.
> 4. **Homework checking** — homework completion arrives from 10; this plan only stores the resulting progress/state.

## Dependencies
- **02** (frontend MVP + local store), **05** (valid lesson ids), **07** (authenticated session). Wave 3 — **08 before 09/10**.
- Consumed by: 09 (stars), 10 (homework state), 14 (last-position cursor resume).

## Deliverables / Steps
- [ ] Define progress contract: per user/lesson state (read, quiz result, homework state) + **last-position cursor** (`course/block/lesson/tab`); idempotent update semantics.
- [ ] `GET /progress` and `POST /progress` (upsert) endpoints; validation against synced lesson ids.
- [ ] Refactor `frontend/src/stores/progressStore.ts` to sync with server when authenticated; keep `persist` as **offline fallback** + optimistic updates.
- [ ] **First-login merge**: one-time reconciliation of localStorage `pyquest-progress` into server state (union of completions; server wins on conflict, document policy).
- [ ] Preserve CourseMap/`LessonLockGuard` unlock behavior against server data.

## Verification
- [ ] Completing a lesson while signed in persists server-side; reload on another device shows it.
- [ ] First sign-in merges existing local progress without loss or duplication.
- [ ] Offline: updates queue locally and sync on reconnect; no data loss.
- [ ] Unlock logic identical to MVP behavior.

## Out of scope
- Star/streak computation (09) and XP retirement.
- Homework execution (10).
- Cross-channel handoff UX (14) — only the cursor field is defined here.
