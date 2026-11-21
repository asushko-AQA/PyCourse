# Lesson 5.18: Merge Magic Complete

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~40 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 40
-->

---

## Title

**Level ★30 — Merge Magic Pro**

---

## Explanation

Polish the forge into a full loop:

| Phase | `state` | Player action |
|-------|---------|---------------|
| Title | `START` | **SPACE** begins |
| Play | `PLAYING` / `WON` | arrows slide runes; **U** = one undo |
| Win | `WON` | tile **2048** — **C** continue or **SPACE** restart |
| Over | `OVER` | no legal moves — **SPACE** restart |

**Session `best_score`** tracks your highest merge total.

Store **`undo_snapshot`** (board copy + score) before each successful move — only **one** undo step back.

---

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-18-merge-magic-complete
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
if not can_move(board): state = OVER
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-18-merge-magic-complete
python solution\game.py
```

**Expected output (visual):** Runnable Merge Magic milestone for lesson 5.18.

---

## Quick Drills

1. Force `state = OVER` and test SPACE restart.
2. Reach 2048 in debug — does **C** continue?
3. Skim [solution/game.py](solution/game.py) for undo_snapshot.


---

## Practice Task

**Quest name:** Merge Magic Pro

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: does the window match this lesson's goal?
3. **Bonus stretch:** add a tiny HUD label with score or hint text.

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Undo does nothing

**Cause:** Snapshot never saved before move.

**Fix:** Set undo_snapshot = (deepcopy(board), score) when changed is True.


---

## Quick Check

1. `best_score` stores…
   - **a)** Highest score this session
   - **b)** pip cache
   - **c)** Only block 1
   - **d)** Nothing

2. Game over when…
   - **a)** No move changes the board
   - **b)** Score hits 0
   - **c)** Window closes
   - **d)** Flask restarts

3. Win at 2048 — key **C**…
   - **a)** Continue playing after win banner
   - **b)** Deletes board
   - **c)** Quits pygame
   - **d)** Opens browser

4. `undo_snapshot` allows…
   - **a)** One step back
   - **b)** Infinite history
   - **c)** Only mines
   - **d)** Course 2

5. Next ★ roadmap game is…
   - **a)** Twin Cards (coming soon)
   - **b)** Course 2 only
   - **c)** Block 0 essay
   - **d)** Removing pygame

---

<details><summary>Click to reveal answers</summary>


1. **a)** Highest score this session.


2. **a)** No move changes the board.


3. **a)** Continue playing after win banner.


4. **a)** One step back.


5. **a)** Twin Cards (coming soon).


</details>



## What's Next

→ [Block 5 — Twin Cards (coming soon)](../README.md)

---

*Forge brighter runes.*

[Choose language](README.md)
