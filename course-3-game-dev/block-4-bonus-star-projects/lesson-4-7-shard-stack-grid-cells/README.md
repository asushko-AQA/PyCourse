# Lesson 4.7: Grid & Cells

> **Course:** Game Development with Python  
> **Block:** Bonus ★ Star Projects *(optional)*  
> **Time:** ~30–35 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level ★7 — Crystal Well |
| **[Русский →](ru.md)** | Уровень ★7 — Кристальная яма |

---

## What you'll build / Что ты создашь

**EN:** **Shard Stack** starts here — a falling-block puzzle with **procedural colored squares** (our own name; not “Tetris”). Today you draw the **playfield** as a **2D list** and paint each cell.

**RU:** **Shard Stack** начинается здесь — падающие блоки из **цветных квадратов**. Сегодня ты рисуешь **поле** как **двумерный список** и закрашиваешь клетки.

## What you'll learn / Что ты узнаешь

- `grid[row][col]` — list inside a list (rows × columns)
- Map grid math → pixel `Rect`s with `CELL`, `BOARD_X`, `BOARD_Y`
- A **shard** as a list of `(row, col)` offsets from an anchor

## Before you start / Перед стартом

- [ ] [Lesson 4.6](../lesson-4-6-prism-dash-complete/README.md) — finished ★ project #2 *(recommended)*
- [ ] [Course 1 Lists](../../../../course-1-python-basics/block-4-organizing-code/lesson-4-2-lists/README.md) — 1D lists refresh

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | Empty grid TODOs |
| [solution/game.py](solution/game.py) | Drawn grid + demo T shard |

## Quick drills / Быстрые упражнения

1. Set `COLS = 8` — how does the well feel?
2. Fill row 19 with `1` — only the bottom row locked?
3. Change `CELL` to `28` and re-center `BOARD_X`.

---

**Previous / Предыдущий урок:** [Lesson 4.6 — Prism Dash Complete](../lesson-4-6-prism-dash-complete/README.md)

**Next / Дальше:** [Lesson 4.8 — Falling Pieces & Controls](../lesson-4-8-shard-stack-falling-pieces/README.md)