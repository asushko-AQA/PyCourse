# PyCourse Platform — Atomic Plan Index

These plans turn PyCourse from a markdown-only course repo into a gamified, multi-channel learning platform. They are **atomic** and executed **one at a time with step-by-step verification**, in the numbered order below.

## Binding architectural decisions (apply to every plan)

1. **Stack** — Python **FastAPI** backend (shared core) + existing **Next.js** frontend in `frontend/`. Web app and Telegram bot both consume the backend over HTTP; the bot runs as a separate process.
2. **Lesson storage** — Markdown in git is **canonical**. SQLite stores only **metadata** (lesson ids, ordering, block/course refs, quiz hashes, homework/checker refs) + user data. No lesson bodies in the DB; a sync job indexes markdown → DB.
3. **Gamification** — **Stars + streaks** are primary (3 stars/lesson: reading/homework/perfect-quiz; 12h replay cooldown; 3/5/7-day streaks). Legacy XP/levels is migrated and retired.
4. **Homework checking** — Student `.py` runs on an **external executor** (self-hosted **Piston** default, Judge0 CE alternative). Never executed in the FastAPI process.

## Execution order & dependencies

| # | Plan | One-line description | Depends on |
|---|------|----------------------|------------|
| 00 | app-stack-architecture-decision | Records the 4 decisions, monorepo layout, process topology, session transport, SQLite persistence | — |
| 01 | lesson-structure-refresh | Lesson schema v2 + update hooks for `courseParser.ts` & `apply_lesson_quizzes.py`; bilingual parity | 00 |
| 02 | frontend-mvp-local | Finish the Next.js localStorage MVP; build-clean web baseline | 00 (01) |
| 03 | intro-programming-unit | "What is a programming language" pre-Block-1 unit + CourseMap unlock impact | 00, 01 |
| 04 | sqlite-schema-migrations | FastAPI + SQLModel tables, migrations, repository interfaces (metadata-only) | 00, 01 |
| 05 | markdown-sync-job | Idempotent markdown→DB indexer, drift detection, CI hook | 01, 04 |
| 06 | email-registration-flow | Register + email verification + password hashing; email adapter; COPPA note | 00, 04 |
| 07 | signin-signout-sessions | Login/logout/session bootstrap + end-to-end auth checkpoint | 04, 06 |
| 08 | progress-sync-engine | Server progress APIs; migrate off localStorage; first-login merge; offline fallback | 02, 05, 07 |
| 09 | achievements-stars-system | Stars (primary) + streaks + 12h cooldown; absorbs XP→stars migration | 04, 05, 08 |
| 10 | homework-checking-judge | Piston/Judge0 executor; checker contract, hidden tests, submission API; homework star | 04, 05, 09 |
| 11 | shared-api-contracts | OpenAPI from FastAPI + typed clients for frontend and bot | 04–10 |
| 12 | cross-channel-identity | `external_identities` schema + link/unlink APIs (before the bot) | 04, 07, 11 |
| 13 | telegram-bot-channel | `bot/` package consuming shared contracts + APIs; learning flows; linking | 11, 12 |
| 14 | cross-channel-resume-ux | Last-position cursor, "continue where you left off", web↔TG deep-link handoff | 08, 12, 13 |
| 15 | lesson-migration-batches | Migrate/deepen 32 lessons to v2 in per-block batches + verify each (incl. HTML/CSS primer addendum) | 01, 05 (10) |
| 16 | course3-gamedev-rollout | Pygame Course 3, block-by-block with verification gates, bilingual | 01, 05, 17 |
| 17 | bridge-course-leveling-up-python | Course 1.5 bridge: try/except, files, modules, classes/OOP — between Courses 1 and 2; prereq for Course 3 | 01, 05 |

## Recommended waves (parallelization)

- **Wave 0** — `00`, `01`, `02` in parallel (decisions, schema, web baseline).
- **Wave 1** — `03`, `04`, `05` (intro unit; DB schema then indexer).
- **Wave 2** — `06`, `07` (registration then sign-in/sessions).
- **Wave 3** — `08` first, then `09` and `10` in parallel (progress, then stars + homework).
- **Wave 4** — `11` and `12` in parallel, then `13`, then `14`.
- **Wave 5** — `15`, `17`, then `16` (content). All can **overlap late platform work** (Waves 3–4) since they are content-only and gated by 01 + 05. Sequence `17` (bridge course, teaches classes) **before** `16` (Pygame relies on classes).

## Notes
- Each plan file is self-contained: Goal, architectural-decisions callout, dependencies, deliverables checklist, verification, out-of-scope.
- Plans produce **markdown only**; application code is written when a plan is executed, not here.
