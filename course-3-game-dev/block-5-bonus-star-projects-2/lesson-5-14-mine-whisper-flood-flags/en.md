# Lesson 5.14: Flood Reveal & Flags

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~36 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 36
-->

---

## Title

**Level ★26 — Whisper Flood**

---

## Explanation

When you reveal a cell with `neighbors == 0`, the cavern **whispers open** — all connected zero cells flip to revealed.

**Recursion picture:** imagine whispering in a cave — the echo bounces to each open tunnel mouth, and each mouth echoes to its neighbors:

```text
You → neighbor A → neighbor B → …
```

**Gentle recursion** (read the solution):

```python
def flood_reveal_recursive(board, col, row):
    # reveal this cell; if neighbors==0, visit each neighbor
```

**Iterative stack** (same result, often safer in games):

```python
stack = [(col, row)]
while stack:
    c, r = stack.pop()
    ...
```

**Flags:** `MOUSEBUTTONDOWN` button **3** (right click) toggles `flagged` on hidden cells.

---

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-14-mine-whisper-flood-flags
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
while stack:
    c, r = stack.pop()
    # reveal zero cells and push neighbors
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-14-mine-whisper-flood-flags
python solution\game.py
```

**Expected output (visual):** Runnable Mine Whisper milestone for lesson 5.14.

---

## Quick Drills

1. Print the picked `(col, row)` each click.
2. Change `CELL` — does the board still align with clicks?
3. Skim [solution/game.py](solution/game.py) for whisper colors.

---

## Practice Task

**Quest name:** Whisper Flood

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: does the window match this lesson's goal?
3. **Bonus stretch:** add a tiny HUD label with grid size.

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Only one zero opens

**Cause:** Flood stopped after first cell.

**Fix:** When neighbors==0, push all 8 neighbors onto the stack.


---

## Quick Check

1. Flood-fill runs when…
   - **a)** Revealed cell has neighbors==0
   - **b)** Game quits
   - **c)** Score is None
   - **d)** Never

2. A stack version uses…
   - **a)** pop/push on a list
   - **b)** Only Turtle
   - **c)** SQL joins
   - **d)** HTML

3. Right-click toggles…
   - **a)** flagged on hidden cells
   - **b)** Window size
   - **c)** pip
   - **d)** Course 2 routes

4. Recursion and stack versions should…
   - **a)** Reveal the same cells
   - **b)** Always differ
   - **c)** Delete the grid
   - **d)** Skip mines

5. Lesson 5.15 adds…
   - **a)** Timer, difficulty, win/lose
   - **b)** Only one cell
   - **c)** No pygame
   - **d)** Flask only

---

<details><summary>Click to reveal answers</summary>


1. **a)** Revealed cell has neighbors==0.

2. **a)** pop/push on a list.

3. **a)** flagged on hidden cells.

4. **a)** Reveal the same cells.

5. **a)** Timer, difficulty, win/lose.


</details>



## What's Next

→ [Lesson 5.15 — Mine Whisper Complete](../lesson-5-15-mine-whisper-complete/README.md)

---

*Listen to the crystals.*

[Choose language](README.md)
