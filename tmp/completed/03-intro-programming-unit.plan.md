# 03 — Intro Programming Unit ("What is a programming language?")

## Goal
Add a foundational, pre-syntax unit that explains what a programming language is, what an interpreter/runtime does, and how code becomes behavior — for absolute beginners (age 11+) before Course 1 Block 1's tooling lessons. This plan decides placement (pre-course vs Block 0) and its impact on the CourseMap unlock chain, then authors the bilingual lesson(s) to schema v2.

## Architectural decisions in effect

> 1. **Stack** — content-only; consumed by the Next.js frontend via the markdown parser.
> 2. **Lesson storage** — new lessons are **canonical markdown**; sync (05) indexes their metadata.
> 3. **Gamification** — the intro unit participates in stars/streaks like any lesson (reading star; quiz star; homework star only if a task exists).
> 4. **Homework checking** — keep any practice trivially self-checkable or executor-optional (concept-first unit).

## Dependencies
- **00**, and **01** (author directly to schema v2). Wave 1.
- Affects: 02/08 (CourseMap unlock chain + progress), 15 (counts toward lesson inventory).

## Placement decision
- **Recommendation:** a **pre-course intro unit** rendered before Course 1 Block 1, authored as `course-1-python-basics/block-0-getting-started/` (mirrors Course 2's `block-0`). Rationale: keeps Block 1 focused on tooling; gives the CourseMap a gentle on-ramp node.
- CourseMap impact: the first intro lesson becomes the new **root unlocked node**; lesson 1.1 unlocks after the intro's quiz/reading. Document the prerequisite-id shift in `courseParser.ts` ordering.

## Deliverables / Steps
- [ ] Decide and record placement (pre-course Block 0 vs inside Block 1) — default above.
- [ ] Author 1–2 bilingual lessons (EN/RU) to schema v2: e.g. `what-is-a-programming-language`, `how-code-runs` (interpreter/runtime mental model, tiny runnable `hello.py`).
- [ ] Visual mental models (analogy: recipe → kitchen → dish) age-appropriate per youth-python-pedagogy skill.
- [ ] Quick Check (3–5 MCQ) + minimal Practice; starter/solution if a runnable result fits.
- [ ] Update `CURRICULUM.md`, course/block `README.md`, `STUDENT-MAP(.ru).md`, and next-links.
- [ ] Update `courseParser.ts` ordering so the intro node is first and 1.1's prerequisite points to it.

## Verification
- [ ] `verify-lesson-in-block` subagent run; findings filed to `documents/ideas` / `documents/issues`.
- [ ] `npm run validate-content` passes; CourseMap shows intro as the first unlockable node and 1.1 gated behind it.
- [ ] EN/RU parity holds.

## Out of scope
- Deepening later Block 1 lessons (15).
- Any backend/progress wiring beyond CourseMap ordering.
