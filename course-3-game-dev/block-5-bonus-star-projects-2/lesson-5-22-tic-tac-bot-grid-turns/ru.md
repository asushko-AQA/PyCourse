# Урок 5.22: Сетка и ходы по очереди

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~30 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 30
-->

---

## Title

**Уровень ★34 — Робо-сетка**

---

## Объяснение

**Tic-Tac-Bot** — Block 5 ★ project **#7** — is a factory-themed **tic-tac-toe** board where **bolt X** and **gear O** marks are drawn with Pygame shapes only (no image files).

The board is a **list of 9 cells** (`None`, `"X"`, or `"O"`). Index `0` is top-left; `8` is bottom-right.

This lesson focuses on: **доска из 9 клеток, сетка, болт X / шестерня O, клик → клетка, два игрока.**

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-22-tic-tac-bot-grid-turns
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Dark robot-factory window; finish TODOs for this lesson's goal.

---

### Step 2: Compare the solution

Study [solution/game.py](solution/game.py) for the full pattern. Finish drawing functions and hot-seat turn swap.

---

## Пример кода

**File: [solution/game.py](solution/game.py)**:

```python
board = [None] * 9
current = 'X'
```

---

## Запуск кода

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-22-tic-tac-bot-grid-turns
python solution\game.py
```

**Expected output (visual):** Runnable Tic-Tac-Bot milestone for lesson 5.22.

---

## Быстрые упражнения

1. Print `board` after three clicks — how many `None` values remain?
2. Change one neon color and rerun.
3. Say aloud which `WIN_LINES` triple is a diagonal (lesson 5.23+).

---

## Задание для практики

**Quest name:** Неоновая фабрика

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: does the window match this lesson's goal?
3. **Bonus stretch:** draw a tiny robot head above the grid (rectangles + circles only).

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Уголок отладки

**Problem:** Clicks land on the wrong cell

**Cause:** `mouse_to_cell` forgot `collidepoint` or mixed up `col`/`row` math.

**Fix:** Loop indices `0…8`, build `cell_rect(i)`, test `rect.collidepoint(pos)`.

---

## Проверь себя

1. A 3×3 board stored as a list has…
   - **a)** 9 cells
   - **b)** 3 cells only
   - **c)** 81 cells
   - **d)** One string
2. Hot-seat means…
   - **a)** Players share one keyboard, taking turns
   - **b)** Only the bot plays
   - **c)** No mouse
   - **d)** Flask routes
3. `None` in a cell means…
   - **a)** Empty — free to click
   - **b)** Always X wins
   - **c)** Quit pygame
   - **d)** HTTP 404
4. Bolt X is drawn with…
   - **a)** Two crossing lines
   - **b)** pygame.image.load only
   - **c)** Turtle forward()
   - **d)** SQL INSERT
5. Next lesson adds…
   - **a)** Win lines and a score table
   - **b)** pip uninstall
   - **c)** Course 1 Turtle
   - **d)** Breakout bricks
---

<details><summary>Click to reveal answers</summary>

1. **a)** 9 cells

2. **a)** Players share one keyboard.

3. **a)** Empty cell.

4. **a)** Two crossing lines.

5. **a)** Win lines and score.

</details>

## Что дальше

→ [Урок 5.23 — Победные линии и счёт](../lesson-5-23-tic-tac-bot-win-score/README.md)

---

*Factory sparks!*

[Choose language](README.md)
