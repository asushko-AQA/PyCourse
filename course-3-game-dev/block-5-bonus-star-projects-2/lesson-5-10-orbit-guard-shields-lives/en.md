# Lesson 5.10: Shields, Lives & Score

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~36 min**  
> [Choose language](README.md) · **[Русский →](ru.md)**

<!-- meta
homework: starter/game.py
minutes: 36
-->

---

## Title

**Level ★22 — Shield Wall**

---

## Explanation

- Player bolt hits invader → remove both, `score += 100`.
- Random invader fires `enemy_bolts` downward on a timer.
- Ship hit → `lives -= 1`; shields are block grids with HP that wear down.
- `collidepoint` on small shield blocks eats bolts before they reach the ship.

---

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-10-orbit-guard-shields-lives
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Orbit window; finish TODOs to match the lesson goal.

---

### Step 2: Compare the solution

Study [solution/game.py](solution/game.py) for patrol ship, formation march, shields, or full waves — depending on this lesson.

---

## Code Example

**File: [solution/game.py](solution/game.py)** — key pattern from this lesson:

```python
if inv.collidepoint(bx, by): invaders.remove(inv); score += 100
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-10-orbit-guard-shields-lives
python solution\game.py
```

**Expected output (visual):** Runnable Orbit Guard milestone for lesson 5.10.

---

## Quick Drills

1. Print `len(player_bolts)` after each shot.
2. Log `formation_x` when the grid steps down.
3. Skim [solution/game.py](solution/game.py) for orbit colors.

---

## Practice Task

**Quest name:** Shield Wall

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: does the orbit window behave like the lesson goal?
3. **Bonus stretch:** add an extra star twinkle on the background (see solution).

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Bolts never disappear.

**Cause:** Forgot to filter `player_bolts` after moving.

**Fix:** Reassign the list with a comprehension checking `PLAY_TOP < y < HEIGHT`.

**Problem:** Formation teleports off-screen.

**Cause:** Not flipping `march_dir` at margins.

**Fix:** When `formation_x` passes margin, multiply `march_dir` by -1 and add `step_down`.


---

## Quick Check

1. Enemy bolts move with…
   - **a)** Positive vy (down)
   - **b)** Only vx
   - **c)** Turtle degrees
   - **d)** Flask POST

2. Shields wear down when…
   - **a)** Bolt collidepoint hits a block
   - **b)** Player scores 100
   - **c)** Window closes
   - **d)** Stars spawn

3. `lives` drops when…
   - **a)** Enemy bolt hits the ship rect
   - **b)** You shoot a shield
   - **c)** Formation marches
   - **d)** You win

4. Removing a hit invader uses…
   - **a)** list.remove on invaders
   - **b)** pip uninstall
   - **c)** Deleting pygame
   - **d)** Renaming ru.md

5. Lesson 5.11 adds…
   - **a)** Waves, UFO bonus, full states
   - **b)** Only one enemy
   - **c)** No score
   - **d)** Flask deploy


---

<details><summary>Click to reveal answers</summary>

1. **a)** Downward motion like falling shots.
2. **a)** HP on each shield cell decreases.
3. **a)** Ship rectangle collision with enemy bolt.
4. **a)** Mutate the invader list in place.
5. **a)** Full Orbit Guard polish next.

</details>


## What's Next

→ [Lesson 5.11 — Orbit Guard Complete](../lesson-5-11-orbit-guard-complete/README.md)

---

*Defend the orbit with code.*

[← Choose language](README.md)
