# 04 — SQLite Schema & Migrations (FastAPI core)

## Goal
Stand up the FastAPI backend's persistent data layer: SQLModel/SQLAlchemy models, an initial migration, and repository interfaces for all **metadata + user data** tables. This is the split of the old `sqlite-core-model` plan that owns *schema*; the indexer that fills lesson metadata is plan 05. Per decision 2, **no full lesson bodies are stored** — only ids, ordering, refs, and hashes.

## Architectural decisions in effect

> 1. **Stack** — FastAPI + **SQLModel** (SQLAlchemy core) in `backend/`; single SQLite file (WAL), Postgres-ready abstraction. FastAPI is the only DB writer.
> 2. **Lesson storage** — tables store lesson **metadata only**: ids, course/block refs, ordering, `quiz_hash`, `homework_ref`/`checker_ref`. Bodies stay in markdown.
> 3. **Gamification** — schema includes user data tables that stars/streaks (09) extend; no XP columns (XP is legacy, migrated in 09).
> 4. **Homework checking** — schema reserves `submission`/`checker` references; execution lives in the external executor (10), not in tables.

## Dependencies
- **00** (backend skeleton), **01** (schema v2 defines extractable metadata). Wave 1.
- Consumed by: 05 (fills lesson tables), 06/07 (auth tables), 08 (progress), 09 (stars/streaks), 10 (submissions), 12 (external identities).

## Tables (initial)
- `courses`, `blocks`, `lessons` — metadata + ordering + `slug`, `path`, `quiz_hash`, `homework_ref`, `checker_ref`, `content_hash`.
- `users` — id, email, `email_verified_at`, `password_hash`, timestamps.
- `email_verification_tokens`, `sessions` (server-side session rows for cookie transport).
- `progress` — per user/lesson state + last-position cursor (filled by 08).
- `star_events`, `achievements`, `user_achievements`, `streak_snapshots` (defined here, driven by 09).
- `submissions` (homework, by 10), `external_identities` (by 12) — created as empty schema or deferred to their plans; reserve FK shape here.

## Deliverables / Steps
- [ ] Add FastAPI app skeleton (`backend/app`), `pyproject.toml`, uvicorn entrypoint, settings (env: `DATABASE_URL`, etc.).
- [ ] Define SQLModel models for the tables above (metadata-only for lessons).
- [ ] Choose + wire migrations (Alembic) with an initial migration; enable WAL + busy-timeout.
- [ ] Repository interfaces (`LessonRepo`, `UserRepo`, `SessionRepo`, `ProgressRepo`, ...) — thin, testable, used by routers/services and the bot-facing APIs.
- [ ] Health endpoint + DB connectivity check.

## Verification
- [ ] `alembic upgrade head` creates `pycourse.db` with all tables; downgrade works.
- [ ] Repository unit tests: create/read a course+lesson metadata row; no body column exists on `lessons`.
- [ ] Health endpoint returns DB-ok; WAL confirmed via `PRAGMA journal_mode`.

## Out of scope
- Populating lesson rows from markdown (05).
- Auth/progress/stars/homework business logic (06–10).
- Postgres migration (design-compatible only).
