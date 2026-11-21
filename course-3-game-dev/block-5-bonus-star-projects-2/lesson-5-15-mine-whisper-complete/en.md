# Lesson 5.15: Mine Whisper Complete

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~40 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 40
-->

---

## Title

**Level ★27 — Mine Whisper Pro**

---

## Explanation

Polish the cavern into a full loop:

| Phase | `state` | Player action |
|-------|---------|---------------|
| Title | `START` | **1/2/3** pick difficulty |
| Play | `PLAYING` | reveal + flag; timer runs |
| Win | `WON` | all safe cells open — save **best time** |
| Lose | `LOST` | hit a mine — show all mines |

**HUD:** `Mines: MINE_COUNT - flags` and `Time: elapsed`.

**Difficulty presets** in `DIFFICULTIES` adjust `COLS`, `ROWS`, `MINE_COUNT`.

---

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-15-mine-whisper-complete
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
if player_won(grid):
    state = WON
    record_best()
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-15-mine-whisper-complete
python solution\game.py
```

**Expected output (visual):** Runnable Mine Whisper milestone for lesson 5.15.

---

## Quick Drills

1. Print the picked `(col, row)` each click.
2. Change `CELL` — does the board still align with clicks?
3. Skim [solution/game.py](solution/game.py) for whisper colors.

---

## Practice Task

**Quest name:** Mine Whisper Pro

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: does the window match this lesson's goal?
3. **Bonus stretch:** add a tiny HUD label with grid size.

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Timer never moves

**Cause:** `elapsed` only grows when state is PLAYING.

**Fix:** Add `if state == PLAYING: elapsed += dt`.


---

## Quick Check

1. `best_times` stores…
   - **a)** Fastest clear per difficulty
   - **b)** pip cache
   - **c)** Only block 1
   - **d)** Nothing

2. Win condition checks…
   - **a)** All non-mine cells revealed
   - **b)** Every cell flagged
   - **c)** Score > 9999
   - **d)** Flask session

3. Keys 1/2/3 on title…
   - **a)** Start easy/medium/hard
   - **b)** Quit pygame
   - **c)** Delete grid
   - **d)** Open browser

4. Mine counter shows…
   - **a)** MINE_COUNT minus flags placed
   - **b)** FPS
   - **c)** Random seed
   - **d)** Lesson slug

5. Next ★ roadmap game is…
   - **a)** Merge Magic (coming soon)
   - **b)** Course 2 only
   - **c)** Block 0 essay
   - **d)** Removing pygame

---

<details><summary>Click to reveal answers</summary>


1. **a)** Fastest clear per difficulty.

2. **a)** All non-mine cells revealed.

3. **a)** Start easy/medium/hard.

4. **a)** MINE_COUNT minus flags placed.

5. **a)** Merge Magic (coming soon).


</details>



## What's Next

→ [Block 5 — Merge Magic (coming soon)](../README.md)

---

*Listen to the crystals.*

[Choose language](README.md)
