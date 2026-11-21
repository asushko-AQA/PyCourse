# Lesson 5.16: Rune Lattice & Spawn

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~32 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 32
-->

---

## Title

**Level ★28 — Rune Lattice**

---

## Explanation

Block 5 ★ project **#5** is **Merge Magic** — a glowing **rune forge** puzzle (our own art; shapes + numbers only).

The board is a **4×4 list of lists** of integers:

```python
board[row][col] = 0  # 0 = empty rune slot
```

- **`col`** counts sideways (0 = left). **`row`** counts down (0 = top).
- `spawn_rune()` picks a random empty cell and places **2** (90%) or **4** (10%).
- `RUNE_COLORS[value]` tints each tile; draw the number in the center.

---

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-16-merge-magic-rune-board
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Glowing rune board; finish TODOs for this lesson's goal.

---

### Step 2: Compare the solution

Study [solution/game.py](solution/game.py) for the full pattern.

---

## Code Example

**File: [solution/game.py](solution/game.py)**:

```python
board[r][c] = 2 if random.random() < 0.9 else 4
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-16-merge-magic-rune-board
python solution\game.py
```

**Expected output (visual):** Runnable Merge Magic milestone for lesson 5.16.

---

## Quick Drills

1. Print `empty_cells()` after each spawn.
2. Change a color in `RUNE_COLORS` — does the tile update?
3. Skim [solution/game.py](solution/game.py) for the rune theme.


---

## Practice Task

**Quest name:** Rune Forge Grid

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: does the window match this lesson's goal?
3. **Bonus stretch:** add a tiny HUD label with score or hint text.

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Tiles all look the same

**Cause:** Drawing uses `value` but board never gets spawns.

**Fix:** Call `spawn_rune()` after reset and press **S** to test.


---

## Quick Check

1. `board[row][col]` uses…
   - **a)** Row index first, then column
   - **b)** Only Flask
   - **c)** File paths
   - **d)** Turtle pens

2. `spawn_rune` needs…
   - **a)** At least one cell with value 0
   - **b)** A mine
   - **c)** HTTP GET
   - **d)** Turtle done()

3. Empty cells are value…
   - **a)** 0
   - **b)** 2 only
   - **c)** 2048 always
   - **d)** None type

4. RUNE_COLORS maps…
   - **a)** Number value → RGB tuple
   - **b)** Score → Flask
   - **c)** Mouse → SQL
   - **d)** Grid → pip

5. Lesson 5.17 adds…
   - **a)** merge_row slide algorithm
   - **b)** Only Turtle
   - **c)** Deleting pygame
   - **d)** Course 2 only

---

<details><summary>Click to reveal answers</summary>


1. **a)** Row index first, then column.


2. **a)** At least one cell with value 0.


3. **a)** 0.


4. **a)** Number value → RGB tuple.


5. **a)** merge_row slide algorithm.


</details>



## What's Next

→ [Lesson 5.17 — Slide & Merge](../lesson-5-17-merge-magic-slide-merge/README.md)

---

*Forge brighter runes.*

[Choose language](README.md)
