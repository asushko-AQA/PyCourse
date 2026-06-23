# 16 — Course 3: Game Dev (Pygame) Rollout

## Goal
Author Course 3 (Game Dev with Pygame) to schema v2, built **block by block with a verification gate per block**, bilingual (EN/RU), and integrated into the frontend parser/map/locks and the DB index. Follows the CURRICULUM.md Course 3 outline (3 blocks, capstone "Catch the Falling Stars").

## Architectural decisions in effect

> 1. **Stack** — content-only; integrates with the Next.js parser and is re-indexed into the FastAPI DB.
> 2. **Lesson storage** — new lessons are **canonical markdown** (schema v2); sync job (05) indexes metadata.
> 3. **Gamification** — Course 3 lessons earn stars/streaks like all others (reading/homework/quiz).
> 4. **Homework checking** — Pygame tasks are hard to autograde headlessly; default to quiz + self-mark homework, and only add `checker_ref` for logic that runs without a display.

## Dependencies
- **01** (schema v2), **05** (index new lessons). Wave 5 — can overlap 15 and late platform work.
- Follows `CURRICULUM.md` Course 3 blocks.

## Block-by-block plan (verify after each block)
- [ ] **Block 1 — Getting Started with Pygame**: install + game loop, window/colors, shapes/coordinates, delta-time movement.
- [ ] **Block 2 — Player Controls & Animations**: keyboard events, images/sprites, score/text rendering, game states.
- [ ] **Block 3 — Physics & Collisions (Final Project)**: collision detection, "Catch the Falling Stars" capstone, polish (sound/high score/difficulty).

## Per-block steps
- [ ] Author bilingual `en.md`/`ru.md` to schema v2 with starter/solution Pygame scripts (60–100 lines per CURRICULUM pacing).
- [ ] Quick Check quizzes; wire `course-3-game-dev/` README, STUDENT-MAP, next-links.
- [ ] Update `courseParser.ts` if Course 3 introduces any new structural cases; run `validate-content`.
- [ ] Run `verify-lesson-in-block` per block; file ideas/issues to `documents/`.
- [ ] Re-index via sync job (05).

## Verification
- [ ] Each block's lessons run (`python starter/game.py`) and pass `verify-lesson-in-block`.
- [ ] `npm run validate-content` passes; Course 3 appears in the CourseMap with correct locks.
- [ ] Sync `--check` clean after each block.
- [ ] EN/RU parity holds across all Course 3 lessons.

## Out of scope
- Migrating Course 1/2 lessons (15).
- Pygame Zero alternative track (backlog note in CURRICULUM).
