# Lesson 5.1: Grid & Segments

> **Course:** Game Development with Python  
> **Block:** Bonus ★ Star Projects II *(optional)*  
> **Time:** ~30–35 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level ★13 — Neon Trail |
| **[Русский →](ru.md)** | Уровень ★13 — Неоновый след |

---

## What you'll build / Что ты создашь

**EN:** **Glow Worm** — project **#1** in Block 5 — is our own **grid snake** with **glowing circle segments** (original art; no borrowed sprites). Today you draw the board, store the worm as a **list of cells**, and move **one step per timer tick** with arrow keys.

**RU:** **Glow Worm** — проект **№1** в Блоке 5 — своя **змейка на сетке** со **светящимися кружками**. Сегодня ты рисуешь поле, хранишь тело в **списке клеток** и двигаешься **раз в тик таймера** стрелками.

## What you'll learn / Что ты узнаешь

- `COLS`, `ROWS`, and pixel math with `CELL`, `BOARD_X`, `BOARD_Y`
- `segments` as `(col, row)` cells — index `0` is the **head**
- `direction` / `pending_dir` as `(dc, dr)` tuples; **no instant U-turn**
- `move_timer` + `MOVE_INTERVAL` — grid steps, not every frame
- `draw_glow_segment` — neon head vs body circles

## Before you start / Перед стартом

- [ ] [Block 5 overview](../README.md) — Glow Worm roadmap
- [ ] [Lesson 4.12 — Glyph Grove Complete](../../block-4-bonus-star-projects/lesson-4-12-glyph-grove-complete/README.md) — finished Block 4 ★ *(recommended)*
- [ ] [Course 1 Lists](../../../../course-1-python-basics/block-4-organizing-code/lesson-4-2-lists/README.md) — list refresh

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | Grid + glow art; movement TODOs |
| [solution/game.py](solution/game.py) | Timer move + arrows (wall bounce for now) |

## Quick drills / Быстрые упражнения

1. Start with four segments — does the tail follow smoothly?
2. Print `segments[0]` on the HUD each step.
3. Slow `MOVE_INTERVAL` to `0.35` — easier steering practice.

---

**Previous / Предыдущее:** [Block 5 ★ II](../README.md) · [Glyph Grove 4.12](../../block-4-bonus-star-projects/lesson-4-12-glyph-grove-complete/README.md)

**Next / Дальше:** [Lesson 5.2 — Food, Growth & Collisions](../lesson-5-2-glow-worm-food-growth/README.md)