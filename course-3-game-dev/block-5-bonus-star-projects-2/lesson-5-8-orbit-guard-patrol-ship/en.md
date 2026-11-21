# Lesson 5.8: Patrol Ship & Blasters

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~32 min**  
> [Choose language](README.md) · **[Русский →](ru.md)**

<!-- meta
homework: starter/game.py
minutes: 32
-->

---

## Title

**Level ★20 — Patrol Bolt**

---

## Explanation

- Slide `ship_x` along the bottom with arrow keys; clamp inside margins.
- `player_bolts` is a **list of dicts** with `x`, `y`, `vy` (negative = up).
- `COOLDOWN` timer so SPACE cannot spray infinite bolts.
- List comprehension cleanup: drop bolts above `PLAY_TOP` or below `HEIGHT`.

---

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-8-orbit-guard-patrol-ship
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
player_bolts.append({"x": ship_x, "y": SHIP_Y, "vy": -BOLT_SPEED})
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-8-orbit-guard-patrol-ship
python solution\game.py
```

**Expected output (visual):** Runnable Orbit Guard milestone for lesson 5.8.

---

## Quick Drills

1. Print `len(player_bolts)` after each shot.
2. Log `formation_x` when the grid steps down.
3. Skim [solution/game.py](solution/game.py) for orbit colors.

---

## Practice Task

**Quest name:** Patrol Bolt

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

1. `player_bolts` stores…
   - **a)** A list of bolt dicts
   - **b)** Only one integer
   - **c)** Flask routes
   - **d)** PNG filenames

2. Negative `vy` means the bolt moves…
   - **a)** Up the screen
   - **b)** Only sideways
   - **c)** Into the ship
   - **d)** Never

3. `COOLDOWN` prevents…
   - **a)** Spam firing every frame
   - **b)** Drawing stars
   - **c)** Installing pygame
   - **d)** Reading keyboard

4. You remove off-screen bolts by…
   - **a)** Filtering the list by y range
   - **b)** Deleting pygame
   - **c)** Renaming files
   - **d)** Using Turtle

5. Lesson 5.9 adds…
   - **a)** Invader grid marching
   - **b)** Flask forms
   - **c)** Turtle art
   - **d)** pip uninstall


---

<details><summary>Click to reveal answers</summary>

1. **a)** Each bolt is a small dict in a list.
2. **a)** Upward motion in screen coordinates.
3. **a)** Cooldown spaces out shots.
4. **a)** Keep only bolts between top and bottom.
5. **a)** Enemy formation next.

</details>


## What's Next

→ [Lesson 5.9 — Invader Formation](../lesson-5-9-orbit-guard-invader-formation/README.md)

---

*Defend the orbit with code.*

[← Choose language](README.md)
