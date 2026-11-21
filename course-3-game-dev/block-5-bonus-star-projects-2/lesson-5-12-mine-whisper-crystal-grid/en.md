# Lesson 5.12: Crystal Grid & Clicks

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~32 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 32
-->

---

## Title

**Level ★24 — Crystal Lattice**

---

## Explanation

Block 5 ★ project **#4** is **Mine Whisper** — a calm **crystal cavern** puzzle (our own art; shapes + numbers only).

The board is a **2D list** (`grid`) of **cell dicts**:

```python
grid[row][col] = {"revealed": False, "peek": False}
```

- **`col`** counts sideways (0 = left). **`row`** counts down (0 = top).
- `mouse_to_cell(event.pos)` turns pixels into `(col, row)` using `BOARD_X`, `BOARD_Y`, and `CELL`.

**Drawing:** Each hidden crystal is a rounded purple tile with a tiny shine rect. A **peek** highlights the cell you clicked.

---

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-12-mine-whisper-crystal-grid
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Purple crystal board; finish TODOs for this lesson's goal.

---

### Step 2: Compare the solution

Study [solution/game.py](solution/game.py) for the full pattern.

---

## Code Example

**File: [solution/game.py](solution/game.py)**:

```python
col = (mx - BOARD_X) // CELL
row = (my - BOARD_Y) // CELL
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-12-mine-whisper-crystal-grid
python solution\game.py
```

**Expected output (visual):** Runnable Mine Whisper milestone for lesson 5.12.

---

## Quick Drills

1. Print the picked `(col, row)` each click.
2. Change `CELL` — does the board still align with clicks?
3. Skim [solution/game.py](solution/game.py) for whisper colors.

---

## Practice Task

**Quest name:** Crystal Click Map

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: does the window match this lesson's goal?
3. **Bonus stretch:** add a tiny HUD label with grid size.

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** HUD always says (0, 0)

**Cause:** Forgot to store `picked` from `mouse_to_cell`.

**Fix:** Assign `picked = mouse_to_cell(event.pos)` and blit `col, row`.


---

## Quick Check

1. `grid[row][col]` uses…
   - **a)** Row index first, then column
   - **b)** Only Flask sessions
   - **c)** File paths
   - **d)** Turtle pens

2. `mouse_to_cell` returns None when…
   - **a)** Click is outside the board
   - **b)** Score is zero
   - **c)** pygame missing
   - **d)** Always

3. Cell dicts in 5.12 track…
   - **a)** revealed / peek flags
   - **b)** HTTP cookies
   - **c)** SQL tables
   - **d)** Only audio

4. BOARD_X and CELL help…
   - **a)** Map pixels → grid coords
   - **b)** Install pip
   - **c)** Deploy Docker
   - **d)** Print quizzes

5. Lesson 5.13 adds…
   - **a)** Random mines + neighbor counts
   - **b)** Only Turtle
   - **c)** Deleting lists
   - **d)** Course 2 Flask

---

<details><summary>Click to reveal answers</summary>


1. **a)** Row index first, then column.

2. **a)** Click is outside the board.

3. **a)** revealed / peek flags.

4. **a)** Map pixels → grid coords.

5. **a)** Random mines + neighbor counts.


</details>



## What's Next

→ [Lesson 5.13 — Mines & Neighbor Numbers](../lesson-5-13-mine-whisper-mines-numbers/README.md)

---

*Listen to the crystals.*

[Choose language](README.md)
