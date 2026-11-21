# Lesson 5.17: Slide & Merge

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~36 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 36
-->

---

## Title

**Level ★29 — Rune Slide**

---

## Explanation

The core move is **slide + merge one row to the left** as a **pure function** `merge_row`.

Pipeline for one row:

1. **`compress`** — push non-zero values left, pad with `0`.
2. **Merge once** — if neighbors match, combine into double value; each pair merges **at most once** per move.
3. **`compress`** again.

Other directions reuse the same logic:

| Direction | Trick |
|-----------|-------|
| Right | reverse row → merge left → reverse |
| Up | transpose → merge left → transpose |
| Down | transpose → reverse → merge → reverse → transpose |

Call **`spawn_rune()` only when the board actually changed.**

---

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-17-merge-magic-slide-merge
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
merged, gained = merge_row(board[row])
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-17-merge-magic-slide-merge
python solution\game.py
```

**Expected output (visual):** Runnable Merge Magic milestone for lesson 5.17.

---

## Quick Drills

1. `print(merge_row([2, 2, 4, 4]))` — what row and score?
2. Try move_up on a column of twos.
3. Skim [solution/game.py](solution/game.py) for transpose helpers.


---

## Practice Task

**Quest name:** One Row Left

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: does the window match this lesson's goal?
3. **Bonus stretch:** add a tiny HUD label with score or hint text.

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Score jumps too fast

**Cause:** Adding gain outside merge_row loop.

**Fix:** Return gained points from merge_row and add once per successful move.


---

## Quick Check

1. `merge_row` merges each equal pair…
   - **a)** At most once per move
   - **b)** Forever in a loop
   - **c)** Only on diagonals
   - **d)** Never

2. Move right reuses left by…
   - **a)** Reversing the row first
   - **b)** Using Flask
   - **c)** Deleting the grid
   - **d)** Printing Turtle

3. Spawn after arrow key when…
   - **a)** Board changed
   - **b)** Always every frame
   - **c)** Never
   - **d)** Score is 0

4. `transpose` swaps…
   - **a)** Rows and columns
   - **b)** RGB and HSL
   - **c)** pip and venv
   - **d)** mouse buttons

5. Lesson 5.18 adds…
   - **a)** Win 2048, undo, game over
   - **b)** Only install Python
   - **c)** Course 1 lists
   - **d)** Removing score

---

<details><summary>Click to reveal answers</summary>


1. **a)** At most once per move.


2. **a)** Reversing the row first.


3. **a)** Board changed.


4. **a)** Rows and columns.


5. **a)** Win 2048, undo, game over.


</details>



## What's Next

→ [Lesson 5.18 — Merge Magic Complete](../lesson-5-18-merge-magic-complete/README.md)

---

*Forge brighter runes.*

[Choose language](README.md)
