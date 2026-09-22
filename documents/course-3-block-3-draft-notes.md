# Course 3 Block 3 — Draft Notes

**Authoring agent:** executor (teacher support draft)  
**Date:** 2026-09-22 (Europe/Minsk)  
**Path:** `/workspace/course-3-draft/` (copy into repo `course-3-game-dev/` later)  
**Status:** Complete draft of Block 3 — not committed  
**Do not modify:** `/workspace/PyCourse-tmp/` (read-only reference)

---

## What was authored

- Block folder: `course-3-game-dev/block-3-physics-collisions-final-project/`
- Block README + lessons **3.1–3.3** each with `README.md`, `en.md`, `ru.md`, `starter/game.py`, `solution/game.py`
- Assets:
  - 3.1: `coin.png` (starter + solution)
  - 3.2: `star.png` (starter + solution)
  - 3.3: `star.png`, `catch.wav`, `miss.wav` (starter + solution) — tiny generated tones via `wave`
- Schema v2 section order; Pygame homework = self-mark + quiz (no `checker` meta key)
- Course README / STUDENT-MAP EN+RU updated for Block 3 draft status
- Block 2 README + Lesson 2.4 What's Next / chooser now link into 3.1

### Level names (Course 3 Levels 9–11)

| Lesson | EN | RU |
|--------|----|----|
| 3.1 | Level 9 — Coin Collector | Уровень 9 — Сборщик монет |
| 3.2 | Level 10 — Star Catcher | Уровень 10 — Ловец звёзд |
| 3.3 | Level 11 — Polish Pro | Уровень 11 — Мастер полировки |

---

## Assumptions

1. Continues Blocks 1–2 conventions: `game.py`, Windows-first CLI with Mac/Linux notes, `dt`, `get_pressed`, states, score HUD.
2. Levels continue **9–11** (Course 3 numbering; Blocks 1–2 were 1–8).
3. Lesson 3.1 teaches **`rect.colliderect()`** with relocate-after-hit (avoid multi-frame score spam).
4. Lesson 3.2 is the **capstone** (~45–50 min): one falling star at a time, paddle catch, 3 misses → game over, SPACE restart via title. Intentionally **not** introducing `pygame.sprite.Group` (blit + Rect only).
5. Lesson 3.3 polishes 3.2: **in-memory** `high_score` (no file required), difficulty ramp `BASE + score * 12`, optional `mixer.Sound` with try/except.
6. Tiny WAV beeps ship with 3.3; if audio fails on a machine, game still runs.
7. 3.2 solution includes a *tiny* fall_speed bump on catch as a preview; 3.3 makes ramp the explicit `BASE + score * k` formula.
8. Relative links assume final home under repo root beside other courses.
9. RU Practice heading: **`## Задание для практики`**; both languages keep `## Title` for the level line.
10. No automated checker for display games.

---

## Known gaps / follow-ups for Helper QA

- [ ] Run all `starter/game.py` and `solution/game.py` on a machine **with a display** + pygame + (for 3.3) working speakers.
- [ ] Confirm EN/RU Quick Check counts match (**5** each for all three lessons).
- [ ] Confirm schema v2 headings present in both languages.
- [ ] Decide if 3.2 should allow **multiple stars** on screen (currently one-at-a-time for clarity).
- [ ] Decide if high score should persist to `highscore.txt` in the main path (currently bonus only).
- [ ] Optional: `pygame.sprite.Sprite` / Group — still deferred; teacher may want a stretch note in Block 3 README.
- [ ] Russian fun names for Levels 9–11 — easy rename if teacher prefers alternatives.
- [ ] No `exercises/` extras; no screenshots/GIFs yet.
- [ ] Wire into frontend CourseMap / locks / DB sync only after copy into git repo.
- [ ] Capstone length (~120 lines) — confirm OK for age 11+ with TODOs scaffolded.

---

## Helper QA checklist (copy)

1. Tree matches `course-3-game-dev/block-3-physics-collisions-final-project/`
2. Every lesson: README + en + ru + starter + solution (+ assets as listed)
3. Starter has `# TODO`; solution complete; filename `game.py`
4. EN/RU section parity + same Quick Check question count (5)
5. What's Next → next lesson **README.md** (3.3 → block README; 2.4 → 3.1)
6. Pedagogy: ~30–40 min (3.2 ~45–50), visible window every lesson, playful tone
7. No platform/frontend edits; no edits under `PyCourse-tmp/`
8. `python -m py_compile` on all `game.py`; no `__pycache__` left in tree
9. Do not commit from scratch path without teacher approval

---

## Open questions for the teacher (Учитель)

1. Keep Level names **Coin Collector / Star Catcher / Polish Pro** (and RU equivalents), or prefer different fun names?
2. Is **one star at a time** the right capstone complexity, or should 3.2 introduce a small list of concurrent stars?
3. Keep **in-memory high score** as the default for 3.3, or require `highscore.txt` in the main Practice Task?
4. Is **3 misses → game over** the right difficulty for class demos, or prefer a timed round / lives = 5?
5. Should catch/miss WAV files stay bundled, or teach generating a beep with `wave` / numpy as a drill?
6. When copying into the repo: merge Block 3 beside Blocks 1–2; confirm replace/merge strategy with Helper (same as prior blocks).
7. Any preferred fiction for the paddle (basket / spaceship / net) vs generic cyan bar?

---

Ready for @Helper content check (do not commit until after QA).

---

## Teacher decisions (Учитель, 2026-09-22)

1. **Level names 9–11** — keep Coin Collector / Star Catcher / Polish Pro (+ RU).
2. **Capstone stars** — keep **one star at a time** (clarity for class); multi-star = stretch only.
3. **High score** — **in-memory** as main path; `highscore.txt` = stretch in 3.3.
4. **Lives** — keep **3 misses → game over**.
5. **WAV files** — keep bundled `catch.wav` / `miss.wav` with try/except.
6. **Merge** — copy Block 3 beside Blocks 1–2 (same flow as before).
7. **Paddle fiction** — keep cyan bar (optional rename to “basket” in student prose later if desired).

Ready for @Helper content check.
