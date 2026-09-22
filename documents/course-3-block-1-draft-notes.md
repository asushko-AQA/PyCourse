# Course 3 Block 1 — Draft Notes

**Authoring agent:** executor (teacher support draft)  
**Date:** 2026-09-22 (Europe/Minsk)  
**Path:** `/workspace/course-3-draft/` (copy into repo `course-3-game-dev/` later)  
**Status:** Complete draft of Block 1 only — not committed

---

## What was authored

- Course README (status **Draft Block 1**), EN/RU STUDENT-MAP
- Block 1 README + readiness checklist stub
- Lessons **1.1–1.4** each with `README.md`, `en.md`, `ru.md`, `starter/game.py`, `solution/game.py`
- Schema v2 section order; Pygame homework = self-mark + quiz (no `checker` meta key)

### Level names (fresh Course 3 Levels 1–4)

| Lesson | EN | RU |
|--------|----|----|
| 1.1 | Level 1 — Window Wizard | Уровень 1 — Мастер окна |
| 1.2 | Level 2 — Color Caster | Уровень 2 — Заклинатель цвета |
| 1.3 | Level 3 — Box Voyager | Уровень 3 — Капитан координат |
| 1.4 | Level 4 — Time Slider | Уровень 4 — Ползунок времени |

---

## Assumptions

1. Students may reuse Course 2 `.venv` or create a new one; Lesson 1.1 documents both.
2. Windows-first CLI (`\`) with Mac/Linux forward-slash notes (matches Turtle 5.1).
3. One main file per lesson: `game.py`.
4. Lesson 1.1 starter is **nearly complete** (runnable window + quit) with instructional `# TODO` comments — same spirit as Turtle 5.1. Lessons 1.2–1.4 leave critical lines for students to fill (`fill`/`nudge`, `x`+`draw.rect`, `dt`+`speed*dt`).
5. RU Practice heading uses canonical **`## Задание для практики`** (schema v2), not legacy `## Практическое задание`.
6. RU/EN both use `## Title` for the level-name section (per schema table).
7. Lesson 1.4 "What's Next" points to Block 1 README (Block 2 not authored yet).
8. Relative links assume final home under repo root beside `course-1-…` / `course-2-…` (same as placeholder).

---

## Known gaps / follow-ups for Helper QA

- [ ] Run all `starter/game.py` and `solution/game.py` on a machine **with a display** + pygame installed (this draft box may be headless).
- [ ] Confirm EN/RU Quick Check counts match (target: **5** each for all four lessons).
- [ ] Confirm schema v2 headings present in both languages (`Code Example` / `Пример кода`, etc.).
- [ ] Decide whether Lesson 1.1 starter should leave `QUIT` as a hard TODO (currently instructional TODO on working quit — aligns with Turtle sample).
- [ ] Optional block-level `STUDENT-MAP.md` was **not** added (course-level maps only; block README links to course maps).
- [ ] Wire into frontend CourseMap / locks / DB sync only after copy into git repo (out of scope for this draft).
- [ ] Block 2/3 not started.
- [ ] Russian level name for 1.3 ("Капитан координат") — teacher may prefer "Повелитель фигур" or "Капитан координат"; easy rename.
- [ ] No `exercises/` extras (optional per schema).
- [ ] No screenshots/GIFs yet — ASCII sketches only.
- [ ] Verify `pip install pygame` version note if curriculum pins a version later.

---

## Helper QA checklist (copy)

1. Tree matches layout under `course-3-game-dev/block-1-…`
2. Every lesson: README + en + ru + starter + solution
3. Starter has `# TODO`; solution complete; same filename `game.py`
4. EN/RU section parity + same Quick Check question count
5. What's Next → next lesson **README.md** (1.4 → block README until Block 2 exists)
6. Pedagogy: ~30–40 min, visible window every lesson, playful tone
7. No platform/frontend edits in this draft
8. Do not commit from scratch path without teacher approval

---

## Open questions for the teacher (Учитель)

1. Keep Course 3 levels numbered **1–4** (fresh) or continue from Course 2’s last level number?
2. Prefer harder 1.1 starter (broken quit until student fixes) vs Turtle-style guided complete starter?
3. Any preferred Russian fun names for Levels 2–4?
4. Should Block 1 get its own `STUDENT-MAP.md` pair for consistency with Course 1 blocks?
5. When copying into the repo: replace placeholder `course-3-game-dev/README.md` entirely with this draft’s README?

---

## Teacher decisions (Учитель, 2026-09-22)

1. **Levels 1–4 fresh** — keep (Course 2 also restarts at Level 1 per course).
2. **Lesson 1.1 starter** — keep Turtle-style guided/complete + instructional TODOs (not a broken-quit hard starter).
3. **RU 1.3 name** — renamed **Капитан коробки → Капитан координат**.
4. **Block-level STUDENT-MAP** — skip for now; course-level maps are enough for Block 1 gate.
5. **Copy-in README** — yes, fully replace placeholder `course-3-game-dev/README.md` when merging to repo.

Ready for @Helper content check (do not commit until after QA).
