# 17 — Bridge Course "Leveling Up Python" (Course 1.5)

## Goal
Author a short bridge course that sits **between Course 1 (Basics) and Course 2 (Web Apps)** and also serves as the prerequisite for **Course 3 (Game Dev)**. It closes the language-maturity gap: Course 1 ends at lists/dicts/turtle and never teaches error handling, files, own modules, or classes — yet Course 2 (Flask multi-file apps, decorators, dicts → templates) and Course 3 (sprites as classes) both assume that maturity. Built to schema v2, bilingual (EN/RU), block-by-block with a verification gate per block.

## Architectural decisions in effect

> 1. **Stack** — content-only; integrates with the Next.js parser/map/locks and is re-indexed into the FastAPI DB.
> 2. **Lesson storage** — new lessons are **canonical markdown** (schema v2); sync job (05) indexes metadata + quiz hashes.
> 3. **Gamification** — bridge lessons earn stars/streaks like all others (reading / homework / perfect-quiz; 12h replay).
> 4. **Homework checking** — `try/except`, files, modules, and class logic are easy to autograde headlessly; add `checker_ref` + hidden tests (10) per practice task.

## Dependencies
- **01** (schema v2 + authoring rules), **05** (index new lessons). Wave 5 — content-only.
- Requires `CURRICULUM.md` to gain a Course 1.5 section (add as a deliverable here).
- **Sequencing:** should land **before 16** (Pygame leans on classes). Course 2 does not hard-require it, but it is the recommended path.

## Course shape (proposed — confirm during 01 gap pass)
New course folder `course-1_5-leveling-up/` (slug avoids clashing with `course-1`/`course-2` ordering). Two blocks, ~5–6 lessons + capstone.

### Block 1 — Stronger Programs
- [ ] **L1 — Catching errors (`try`/`except`)**: stop crashes on bad `input()`; "errors as detective work" tone. Result: a calculator that never crashes.
- [ ] **L2 — Saving & loading files**: read/write text; save a high score / saved game. Result: a score that persists between runs.
- [ ] **L3 — Your own modules (`import`)**: split helpers across files; prepares for Flask's multi-file layout. Result: a `main.py` that imports `helpers.py`.

### Block 2 — Objects (Intro to OOP)
- [ ] **L4 — Classes & objects**: "your own custom data type / a recipe for making objects" (extends the existing functions=recipes analogy). Model a `Pet` or `Player`. Result: create and interact with two objects.
- [ ] **L5 — Methods & state**: objects that hold data and do things (`pet.feed()`, `player.take_damage()`). Result: a tiny stateful object.
- [ ] **Capstone — `my_creature/creature.py`** (root-level student folder, per AGENTS.md convention): a save-able creature/RPG tying together classes + files + error handling.

## Per-block steps
- [ ] Author bilingual `en.md`/`ru.md` to schema v2 section order, 15–50 line programs, one concept per lesson.
- [ ] Quick Check (3–5 MCQ) + practice task with `checker_ref` + hidden tests (10) per lesson.
- [ ] Create `course-1_5-leveling-up/` README, STUDENT-MAP.md/.ru.md, block READMEs; wire next-links (Course 1 Block 5 → here → Course 2 Block 0).
- [ ] Add Course 1.5 to `CURRICULUM.md` and update the Development Order; add the student capstone folder note (`my_creature/`).
- [ ] Update `courseParser.ts` only if a new structural case appears; update CourseMap unlock chain so 1.5 unlocks after Course 1 and gates Course 2/3.
- [ ] Run `verify-lesson-in-block` per block; file ideas/issues to `documents/`.
- [ ] Re-index via sync job (05).

## Verification
- [ ] Every lesson runs (`python starter/...`) and passes `verify-lesson-in-block`.
- [ ] `npm run validate-content` passes; Course 1.5 appears in CourseMap between Courses 1 and 2 with correct locks.
- [ ] EN/RU parity holds across all bridge lessons.
- [ ] Sync `--check` clean after each block; DB metadata matches markdown.
- [ ] Capstone earns 3 stars (reading + homework checker + perfect quiz) end-to-end.

## Out of scope
- Migrating existing Course 1/2 lessons (15) and Course 3 authoring (16).
- Advanced OOP (inheritance, dunder beyond `__init__`/`__str__`, decorators) — keep to a beginner-friendly subset; note deeper topics as a CURRICULUM backlog item.
