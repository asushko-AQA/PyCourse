# Course 3 Block 2 — Draft Notes

**Authoring agent:** executor (teacher support draft)  
**Date:** 2026-09-22 (Europe/Minsk)  
**Path:** `/workspace/course-3-draft/` (copy into repo `course-3-game-dev/` later)  
**Status:** Complete draft of Block 2 — not committed  
**Do not modify:** `/workspace/PyCourse-tmp/` (read-only reference)

---

## What was authored

- Block folder: `course-3-game-dev/block-2-player-controls-animations/`
- Block README + lessons **2.1–2.4** each with `README.md`, `en.md`, `ru.md`, `starter/game.py`, `solution/game.py`
- Lesson 2.2 includes generated `player.png` (48×48 teal ship) in both starter/ and solution/
- Schema v2 section order; Pygame homework = self-mark + quiz (no `checker` meta key)
- Course README / STUDENT-MAP EN+RU updated for Block 2 draft status
- Block 1 README + Lesson 1.4 What's Next / chooser now link into 2.1

### Level names (Course 3 Levels 5–8)

| Lesson | EN | RU |
|--------|----|----|
| 2.1 | Level 5 — Key Captain | Уровень 5 — Капитан клавиш |
| 2.2 | Level 6 — Sprite Summoner | Уровень 6 — Призыватель спрайтов |
| 2.3 | Level 7 — Score Scribbler | Уровень 7 — Писарь очков |
| 2.4 | Level 8 — Stage Director | Уровень 8 — Режиссёр сцен |

---

## Assumptions

1. Continues Block 1 conventions: `game.py`, Windows-first CLI with Mac/Linux notes, `dt` from Lesson 1.4.
2. Levels continue **5–8** (Course 3 fresh numbering; Block 1 was 1–4).
3. Lesson 2.1 teaches **`get_pressed()`** for continuous move (not only KEYDOWN).
4. Lesson 2.2 prefers a tiny PNG asset over Surface-only drawing; path via `os.path` next to script.
5. Lesson 2.3 works **without** copying `player.png` (rect fallback); optional sprite if student copies from 2.2.
6. Lesson 2.4 uses an **8-second** timed round so Game Over is easy to reach in class (not collision-based — that is Block 3).
7. 2.4 What's Next → Block 2 README (Block 3 not authored yet).
8. Relative links assume final home under repo root beside other courses.
9. RU Practice heading: **`## Задание для практики`**; both languages keep `## Title` for the level line.

---

## Known gaps / follow-ups for Helper QA

- [ ] Run all `starter/game.py` and `solution/game.py` on a machine **with a display** + pygame installed (draft box may be headless).
- [ ] Confirm EN/RU Quick Check counts match (**5** each for all four lessons).
- [ ] Confirm schema v2 headings present in both languages.
- [ ] Decide if Lesson 2.3 should **ship** `player.png` copies (currently optional / fallback rect).
- [ ] Decide if 2.4 timer (8s) is the right classroom length vs longer / collision trigger later in Block 3.
- [ ] Optional: `pygame.sprite.Sprite` class — intentionally **not** introduced (blit + Rect only); teacher may want a stretch note.
- [ ] Russian fun names for Levels 5–8 — easy rename if teacher prefers alternatives.
- [ ] No `exercises/` extras; no screenshots/GIFs yet.
- [ ] Wire into frontend CourseMap / locks / DB sync only after copy into git repo.
- [ ] Block 3 not started.

---

## Helper QA checklist (copy)

1. Tree matches `course-3-game-dev/block-2-player-controls-animations/`
2. Every lesson: README + en + ru + starter + solution (+ `player.png` for 2.2)
3. Starter has `# TODO`; solution complete; filename `game.py`
4. EN/RU section parity + same Quick Check question count (5)
5. What's Next → next lesson **README.md** (2.4 → block README)
6. Pedagogy: ~30–40 min, visible window every lesson, playful tone
7. No platform/frontend edits; no edits under `PyCourse-tmp/`
8. `python -m py_compile` on all `game.py`; no `__pycache__` left in tree
9. Do not commit from scratch path without teacher approval

---

## Open questions for the teacher (Учитель)

1. Keep Level names **Key Captain / Sprite Summoner / Score Scribbler / Stage Director** (and RU equivalents), or prefer different fun names?
2. Should Lesson 2.3 bundle `player.png` like 2.2, or keep the rect fallback (current)?
3. Is the **8-second** demo timer in 2.4 OK for class, or prefer 15–30s / no auto game-over until Block 3 collisions?
4. Introduce `pygame.sprite.Sprite` / Group as optional stretch in 2.2, or leave for a later polish lesson?
5. When copying into the repo: merge Block 2 beside existing Block 1; course README already says Blocks 1–2 draft — confirm replace/merge strategy with Helper.
6. Any preferred scoring fiction for 2.3 (RIGHT-to-earn vs time-based only vs Space-to-add-1)?

---

Ready for @Helper content check (do not commit until after QA).

---

## Teacher decisions (Учитель, 2026-09-22)

1. **Level names 5–8** — keep (Key Captain / Sprite Summoner / Score Scribbler / Stage Director + RU).
2. **2.3 player.png** — keep rect fallback (optional copy from 2.2); do not bundle.
3. **2.4 timer** — default **15s** (was 8s); stretch drill → try 30s.
4. **pygame.sprite.Sprite** — leave for later; blit + Rect only in Block 2.
5. **Merge** — copy Block 2 beside Block 1; update course README/maps (same as Block 1 flow).
6. **2.3 score fiction** — keep hold-RIGHT-to-earn (simple continuous feedback).

Ready for @Helper content check.
