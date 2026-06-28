# 15 — Lesson Migration Batches (to Schema v2)

## Goal
Execution plan to migrate and deepen the existing ~32 lessons (Course 1: 21, Course 2: 11) to schema v2 (01), in **per-block batches**, each followed by a `verify-lesson-in-block` subagent pass and a markdown re-index (05). This is the concrete "more comprehensive/detailed lessons" work, sequenced so the platform always has consistent, indexable content.

## Architectural decisions in effect

> 1. **Stack** — content-only; verified against `courseParser.ts` and re-indexed into the FastAPI DB.
> 2. **Lesson storage** — lessons stay **canonical markdown**; after each batch, run the sync job (05) so DB metadata + quiz hashes track changes.
> 3. **Gamification** — adding/clarifying homework + quizzes during migration enables the homework/quiz stars (09/10).
> 4. **Homework checking** — where a lesson gains a practice task, add a `checker_ref` + hidden tests (10) during its batch.

## Dependencies
- **01** (schema v2 + gap list), **05** (re-index), and benefits from **10** (add checkers). Wave 5 — overlaps late platform work; can run alongside 16.
- Uses the per-block gap list produced in 01.

## Batch order (one block per batch; verify after each)
- [ ] Batch A — Course 1 Block 1 (+ intro unit from 03 if placed here)
- [ ] Batch B — Course 1 Block 2
- [ ] Batch C — Course 1 Block 3
- [ ] Batch D — Course 1 Block 4
- [ ] Batch E — Course 1 Block 5 (Turtle)
- [ ] Batch F — Course 2 Block 0
- [ ] Batch G — Course 2 Block 1
- [ ] Batch H — Course 2 Block 2 (add missing Code Example/Code Execution to Flask lessons)
- [ ] Batch I — **HTML/CSS primer** (new lessons, see addendum below)

## Addendum — HTML/CSS primer (Course 2)
Course 2 jumps to Jinja templates (`2.1 HTML templates`) without teaching HTML/CSS first. Add **1–2 short, Flask-contextual lessons** at the **start of Course 2 Block 2** (before `lesson-2-1-html-templates`), e.g. `lesson-2-0a-html-basics` and `lesson-2-0b-css-basics`.
- [ ] **HTML basics**: just-enough structure (headings, paragraphs, lists, links, a form) — framed as "what your Flask templates are made of," not web design.
- [ ] **CSS basics**: selectors, colors, spacing; link via `url_for('static', ...)` so it dovetails with `2.4 static-files-css`.
- [ ] Keep strictly inside `AGENTS.md` boundaries: simple HTML/CSS only — **no JavaScript, no frameworks**.
- [ ] Renumber/relink Block 2 next-links to insert the primer before `2.1`; update block README + STUDENT-MAP.
- [ ] Same per-block steps + verification as other batches (schema v2, EN/RU parity, Quick Check, `verify-lesson-in-block`, re-index via 05).

## Per-batch steps
- [ ] Bring each lesson's `en.md`/`ru.md` to v2 section order; fill missing Code Example/Code Execution; deepen explanations per youth-python-pedagogy.
- [ ] Ensure EN/RU parity + Quick Check completeness; add/adjust homework + `checker_ref` where applicable.
- [ ] Run `verify-lesson-in-block`; file ideas/issues to `documents/`.
- [ ] Re-run the sync job (05) `--check` then index; confirm quiz hashes update.

## Verification
- [ ] Every migrated block passes `verify-lesson-in-block` and `npm run validate-content`.
- [ ] Sync `--check` is clean after each batch; DB metadata matches markdown.
- [ ] No EN/RU parity gaps remain in migrated blocks.

## Out of scope
- Defining schema v2 (01) or the sync job (05).
- Course 3 authoring (16).
