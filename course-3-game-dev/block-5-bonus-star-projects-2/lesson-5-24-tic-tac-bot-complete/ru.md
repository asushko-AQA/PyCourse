# Урок 5.24: Tic-Tac-Bot целиком

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~35 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 35
-->

---

## Title

**Уровень ★36 — Tic-Tac-Bot Pro**

---

## Объяснение

**Tic-Tac-Bot** — Block 5 ★ project **#7** — is a factory-themed **tic-tac-toe** board where **bolt X** and **gear O** marks are drawn with Pygame shapes only (no image files).

The board is a **list of 9 cells** (`None`, `"X"`, or `"O"`). Index `0` is top-left; `8` is bottom-right.

This lesson focuses on: **бот Easy/Medium/Hard, задержка хода, кто начинаёт, сессия П/Пр/Н, minimax на Hard.**

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-24-tic-tac-bot-complete
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Dark robot-factory window; finish TODOs for this lesson's goal.

---

### Step 2: Compare the solution

Study [solution/game.py](solution/game.py) for the full pattern. Medium: win → block → centre → corner → any. Hard: minimax lookahead.

---

## Пример кода

**File: [solution/game.py](solution/game.py)**:

```python
bot_timer -= dt
if bot_timer <= 0:
    bot_move()
```

---

## Запуск кода

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-24-tic-tac-bot-complete
python solution\game.py
```

**Expected output (visual):** Runnable Tic-Tac-Bot milestone for lesson 5.24.

---

## Быстрые упражнения

1. Print `board` after three clicks — how many `None` values remain?
2. Change one neon color and rerun.
3. Say aloud which `WIN_LINES` triple is a diagonal (lesson 5.23+).

---

## Задание для практики

**Quest name:** Tic-Tac-Bot Pro

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

1. Easy bot picks…
   - **a)** A random empty cell
   - **b)** Always centre
   - **c)** Never moves
   - **d)** Deletes board
2. Medium bot should first…
   - **a)** Take a winning move if possible
   - **b)** Pick TOP-LEFT always
   - **c)** Quit
   - **d)** Shuffle WIN_LINES
3. Hard minimax means…
   - **a)** Look ahead at future moves to play best
   - **b)** Only random
   - **c)** No draws possible ever
   - **d)** Uses image sprites
4. `bot_timer` avoids…
   - **a)** Instant robot moves — feels like thinking
   - **b)** All drawing
   - **c)** pygame.init
   - **d)** Lists
5. Next ★ project on the roadmap is…
   - **a)** Leap Lands
   - **b)** Twin Cards
   - **c)** Sky Hopper
   - **d)** Flask forms
---

<details><summary>Click to reveal answers</summary>

1. **a)** Random empty.

2. **a)** Win if you can.

3. **a)** Look ahead.

4. **a)** Short delay.

5. **a)** Leap Lands.

</details>

## Что дальше

→ [Урок 5.25 — Игрок и прыжок](../lesson-5-25-leap-lands-player-jump/README.md) — **Leap Lands** ★ №8!

---

*Bots + brains!*

[Choose language](README.md)
