# 01 — Lesson Structure Refresh (Schema v2)

## Goal
Define and approve a canonical **lesson schema v2** so every lesson across all courses follows one comprehensive, machine-friendly, bilingual format. Schema v2 is the contract that the markdown→DB sync job (05), the frontend parser, and the bot all rely on. This plan produces the schema document plus the explicit update hooks needed in the two existing tools that parse lessons, and the bilingual-parity rules.

## Architectural decisions in effect

> 1. **Stack** — FastAPI backend + Next.js frontend; bot is a separate HTTP client.
> 2. **Lesson storage** — Markdown stays **canonical**; SQLite holds only metadata (incl. quiz hashes, homework/checker refs). Schema v2 defines exactly what metadata is extractable.
> 3. **Gamification** — Stars + streaks; the three star sources (reading/homework/quiz) must be derivable from lesson structure.
> 4. **Homework checking** — External executor; each lesson may declare a `homework`/`checker` reference that schema v2 must accommodate.

## Dependencies
- **00** (layout + decisions). Can run in parallel with 02 in Wave 0.
- Consumed by: 04/05 (sync indexes schema v2 metadata), 09 (star sources), 10 (checker refs), 15 (migration batches), 16 (Course 3 authored to v2).

## Schema v2 — required structure
- `README.md` = language chooser only.
- `en.md` / `ru.md` section order (matching headings in RU):
  1. Title + intro
  2. Numbered tutorial steps
  3. **Code Example** + **Code Execution** (NEW required sections — Course 2 Flask lessons currently miss these)
  4. Quick Drills / Быстрые упражнения
  5. Practice Task / Задание для практики
  6. Debug Corner / Уголок отладки
  7. Quick Check / Проверь себя (3–5 MCQ, collapsible answers)
  8. What's Next / Что дальше → links to **next lesson's `README.md`**
- Optional declared metadata block (HTML comment, not rendered) for: `homework` ref, `checker` ref, estimated minutes. Kept out of visible body; canonical content unaffected.

## Bilingual parity rules
- `en.md` and `ru.md` MUST have the same section set and the same number of Quick Check questions.
- Heading variants normalized (`Practice Task` vs `Try it yourself`; Block 1 RU `## Дальше` → `## Что дальше`).
- Quiz options `a)–d)` and `<details>` answer block format identical across languages → enables stable quiz hashing in 05.

## Deliverables / Steps
- [ ] Write `documents/plans/lesson-schema-v2.md` (canonical schema doc) with mandatory/optional sections and the metadata-comment format.
- [ ] Update `AGENTS.md` lesson section + `.cursor/skills/write-lesson/SKILL.md` + `.cursor/skills/review-lesson/SKILL.md` to enforce v2.
- [ ] **Update hook — `frontend/src/lib/courseParser.ts`**: document exactly which regex/section splits change for the new Code Example/Code Execution sections and optional metadata comment; add to its parse + `validate-content` script.
- [ ] **Update hook — `tools/apply_lesson_quizzes.py`**: ensure quiz insertion stays idempotent under v2 headings and emits the quiz hash format used by 05.
- [ ] Produce a per-block gap list (existing 32 lessons vs v2) — feeds 15.

## Verification
- [ ] Schema doc approved and linked from `AGENTS.md`.
- [ ] `courseParser.ts` parses one converted sample lesson (EN+RU) with no missing-section warnings; `npm run validate-content` passes.
- [ ] `apply_lesson_quizzes.py` re-run on a v2 lesson is a no-op (idempotent) and prints a stable quiz hash.
- [ ] EN/RU parity check passes on the sample lesson.

## Out of scope
- Actually migrating all 32 lessons (that is 15).
- DB tables/sync implementation (04/05).
- Authoring new Course 3 lessons (16).
