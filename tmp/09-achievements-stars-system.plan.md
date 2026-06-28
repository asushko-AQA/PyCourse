# 09 — Achievements: Stars & Streaks System

## Goal
Implement the primary gamification model — **stars + streaks** — on top of progress (08), and **migrate/retire the legacy XP/levels system**. Three stars per lesson (reading=1, homework=1, perfect quiz=1), a 12-hour replay cooldown for improving stars, and 3/5/7-day streak achievements. The migration from `frontend/src/stores/progressStore.ts` XP/levels must be documented so the app never shows two competing metaphors.

## Architectural decisions in effect

> 1. **Stack** — star/streak evaluator + APIs in FastAPI; frontend and bot render stars from the same endpoints.
> 2. **Lesson storage** — stars key off lesson metadata + `quiz_hash` from synced DB (05).
> 3. **Gamification** — **stars + streaks are primary.** XP/levels are **migrated and removed**, not kept alongside.
> 4. **Homework checking** — the homework star is granted when 10 reports a passing submission.

## Dependencies
- **08** (progress events), **04** (`star_events`/`achievements`/`streak_snapshots`), **05** (`quiz_hash`). Wave 3 — after 08; parallel with 10.
- Consumed by: 13 (bot shows stars/streaks), 14 (resume surfaces streak nudges).

## Star & streak rules
- Stars per lesson (max 3): `lesson_read` (open/complete), `homework_done` (passing check from 10), `quiz_perfect` (zero mistakes).
- **Replay cooldown**: recompute/improve stars only after `last_attempt_at + 12h`.
- Streaks: daily-activity tracking; achievements at 3/5/7 consecutive days (extensible).

## XP → stars migration (must document)
- Map: derive each user's earned stars from existing completion records; XP/level no longer displayed.
- Replace `XPBadge.tsx` with a stars/streak badge; remove `xp`/`level` from the store (or freeze + hide) — single metaphor only.
- Record the one-time backfill: existing completed lessons → `lesson_read` (+`quiz_perfect` where quiz was perfect).

## Deliverables / Steps
- [ ] Star evaluator service + `GET /stars` / achievement APIs; compute current stars + eligibility window.
- [ ] Streak engine: daily activity rollup → grant 3/5/7-day achievements.
- [ ] Frontend: per-lesson star indicators, achievement badges, streak display; retire XP UI.
- [ ] One-time XP→stars backfill migration + documented mapping.

## Verification
- [ ] Reading grants 1 star; perfect quiz grants the quiz star; homework pass (10) grants the homework star.
- [ ] Re-attempt before 12h does not change stars; after 12h it can improve them.
- [ ] 3/5/7-day streaks grant achievements; gaps reset the streak.
- [ ] No XP/level UI remains; backfill produced correct stars for existing users.

## Out of scope
- Homework execution mechanics (10).
- Progress storage/merge (08).
- New achievement types beyond 3/5/7-day (backlog).
