# Lesson 5.13: Mines & Neighbor Numbers

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~34 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 34
-->

---

## Title

**Level ★25 — Hidden Echo**

---

## Explanation

After the first **left click**, call `place_mines` so the clicked **safe zone** (cell + 8 neighbors) never contains a mine.

Then loop every cell and set `neighbors` with `count_neighbor_mines`.

On reveal: show a tinted digit `1`–`8`, or a red crystal if you hit a mine.

---

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-13-mine-whisper-mines-numbers
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
board[r][c]["neighbors"] = count_neighbor_mines(board, c, r)
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-13-mine-whisper-mines-numbers
python solution\game.py
```

**Expected output (visual):** Runnable Mine Whisper milestone for lesson 5.13.

---

## Quick Drills

1. Print the picked `(col, row)` each click.
2. Change `CELL` — does the board still align with clicks?
3. Skim [solution/game.py](solution/game.py) for whisper colors.

---

## Practice Task

**Quest name:** Echo Counter

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: does the window match this lesson's goal?
3. **Bonus stretch:** add a tiny HUD label with grid size.

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Every cell shows 0

**Cause:** Mines placed but neighbors not computed.

**Fix:** After placing mines, loop all cells and call `count_neighbor_mines`.


---

## Quick Check

1. Mines are placed…
   - **a)** After the first safe click
   - **b)** Before pygame.init
   - **c)** On import only
   - **d)** Never

2. `neighbors` counts…
   - **a)** Mines in 8 surrounding cells
   - **b)** FPS only
   - **c)** Keyboard keys
   - **d)** Flask routes

3. First-click safety means…
   - **a)** That cell (and neighbors) are mine-free
   - **b)** No random module
   - **c)** No grid
   - **d)** Infinite lives

4. A revealed mine shows…
   - **a)** Red crystal shape
   - **b)** HTML form
   - **c)** pip logo
   - **d)** Nothing

5. Lesson 5.14 adds…
   - **a)** Flood-fill open areas + right-click flags
   - **b)** Only print()
   - **c)** Course 1 turtle only
   - **d)** Removing dicts

---

<details><summary>Click to reveal answers</summary>


1. **a)** After the first safe click.

2. **a)** Mines in 8 surrounding cells.

3. **a)** That cell (and neighbors) are mine-free.

4. **a)** Red crystal shape.

5. **a)** Flood-fill open areas + right-click flags.


</details>



## What's Next

→ [Lesson 5.14 — Flood Reveal & Flags](../lesson-5-14-mine-whisper-flood-flags/README.md)

---

*Listen to the crystals.*

[Choose language](README.md)
