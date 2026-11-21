# Урок 5.23: Победные линии и счёт

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~32 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 32
-->

---

## Title

**Уровень ★35 — Схема победы**

---

## Объяснение

**Tic-Tac-Bot** — Block 5 ★ project **#7** — is a factory-themed **tic-tac-toe** board where **bolt X** and **gear O** marks are drawn with Pygame shapes only (no image files).

The board is a **list of 9 cells** (`None`, `"X"`, or `"O"`). Index `0` is top-left; `8` is bottom-right.

This lesson focuses on: **список `WIN_LINES`, победа + подсветка, ничья, счёт, R — новый раунд.**

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-23-tic-tac-bot-win-score
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Dark robot-factory window; finish TODOs for this lesson's goal.

---

### Step 2: Compare the solution

Study [solution/game.py](solution/game.py) for the full pattern. Loop lines; draw pink highlight across winners.

---

## Пример кода

**File: [solution/game.py](solution/game.py)**:

```python
WIN_LINES = [(0, 1, 2), (3, 4, 5), …]
```

---

## Запуск кода

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-23-tic-tac-bot-win-score
python solution\game.py
```

**Expected output (visual):** Runnable Tic-Tac-Bot milestone for lesson 5.23.

---

## Быстрые упражнения

1. Print `board` after three clicks — how many `None` values remain?
2. Change one neon color and rerun.
3. Say aloud which `WIN_LINES` triple is a diagonal (lesson 5.23+).

---

## Задание для практики

**Quest name:** Схема счёта

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

1. There are … winning lines on a 3×3 board
   - **a)** 8
   - **b)** 3
   - **c)** 12
   - **d)** 1
2. A draw happens when…
   - **a)** Board full and no winner
   - **b)** pygame.QUIT
   - **c)** First move is O
   - **d)** Score is 99
3. Highlighting the win line helps…
   - **a)** Players see which triple matched
   - **b)** Delete the list
   - **c)** Install Flask
   - **d)** Skip events
4. Session scores should reset when…
   - **a)** You only reset the round board, not lifetime menu stats (this lesson)
   - **b)** Never
   - **c)** Every frame
   - **d)** On import
5. Next lesson adds…
   - **a)** The Tic-Tac-Bot AI
   - **b)** Django
   - **c)** Minesweeper flood fill
   - **d)** 2048 slide
---

<details><summary>Click to reveal answers</summary>

1. **a)** 8 lines

2. **a)** Full board, no winner.

3. **a)** Shows the triple.

4. **a)** Round vs session (see lesson).

5. **a)** Bot AI.

</details>

## Что дальше

→ [Урок 5.24 — Tic-Tac-Bot целиком](../lesson-5-24-tic-tac-bot-complete/README.md)

---

*Circuits aligned!*

[Choose language](README.md)
