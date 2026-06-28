# 05 — Markdown → DB Sync Job (Indexer)

## Goal
Implement an idempotent indexer that reads canonical lesson markdown (schema v2) and upserts **metadata only** into the SQLite tables from plan 04: lesson ids, course/block refs, ordering, quiz hashes, and homework/checker references. Includes drift detection (DB vs markdown) and a CI hook so the index can never silently diverge from the source of truth.

## Architectural decisions in effect

> 1. **Stack** — runs as a FastAPI management command / script in `backend/`; the only writer to lesson tables.
> 2. **Lesson storage** — markdown is **canonical**; this job indexes metadata into the DB and **never** copies bodies. `content_hash`/`quiz_hash` detect changes.
> 3. **Gamification** — `quiz_hash` lets 09 detect quiz changes that may reset/regrant quiz stars.
> 4. **Homework checking** — extracts `homework_ref`/`checker_ref` from the v2 metadata comment for 10.

## Dependencies
- **01** (schema v2 + parser/quiz-hash format), **04** (tables/repos). Wave 1 (after/with 04).
- Consumed by: 08 (progress references valid lesson ids), 09 (quiz hashes), 10 (checker refs), 15 (re-index after each migration batch).

## Deliverables / Steps
- [ ] Indexer command (e.g. `python -m app.sync.index_lessons`) that walks `course-*/block-*/lesson-*`, derives ids/ordering, computes `content_hash` + `quiz_hash`, upserts metadata.
- [ ] Idempotency: re-running with no markdown changes performs **zero writes** (hash compare).
- [ ] Drift detection mode (`--check`): exits non-zero if DB metadata differs from markdown (missing lessons, stale hashes, ordering mismatch).
- [ ] Reuse the same parsing rules as `frontend/src/lib/courseParser.ts` (document the shared contract from 01 so EN/RU and quiz hashing match the frontend).
- [ ] CI hook: run `--check` in CI to fail PRs that change lessons without re-indexing (or auto-index on deploy).

## Verification
- [ ] First run populates lesson/quiz metadata for all current lessons; second run writes nothing.
- [ ] Editing one lesson's quiz changes only that lesson's `quiz_hash`; `--check` flags it until re-index.
- [ ] Deleting/reordering a lesson is detected by `--check`.
- [ ] CI fails on intentional drift, passes after re-index.

## Out of scope
- Defining schema v2 (01) or tables (04).
- Serving lesson content to clients (frontend reads markdown directly; bot reads via API in 13).
- Migrating lesson content depth (15).
