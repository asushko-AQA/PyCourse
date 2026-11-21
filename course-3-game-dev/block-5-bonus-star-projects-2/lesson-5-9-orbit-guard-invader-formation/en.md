# Lesson 5.9: Invader Formation

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~34 min**  
> [Choose language](README.md) · **[Русский →](ru.md)**

<!-- meta
homework: starter/game.py
minutes: 34
-->

---

## Title

**Level ★21 — Invader March**

---

## Explanation

- `formation_x`, `formation_y` offset the whole grid; rebuild `invaders` each step.
- `march_dir` is `1` or `-1`; flip at margins and add `step_down` to `formation_y`.
- Grid: `COLS` × `ROWS` of `pygame.Rect` invader shapes (ellipses only).
- Bolts still pass through — collisions arrive in lesson 5.10.

---

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-9-orbit-guard-invader-formation
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
formation_x += march_dir * march_speed * dt
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-9-orbit-guard-invader-formation
python solution\game.py
```

**Expected output (visual):** Runnable Orbit Guard milestone for lesson 5.9.

---

## Quick Drills

1. Print `len(player_bolts)` after each shot.
2. Log `formation_x` when the grid steps down.
3. Skim [solution/game.py](solution/game.py) for orbit colors.

---

## Practice Task

**Quest name:** Invader March

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

1. When the formation hits the side you…
   - **a)** Flip march_dir and step down
   - **b)** Delete pygame
   - **c)** Stop the clock
   - **d)** Hide the ship

2. `build_invaders()` should run…
   - **a)** After formation offsets change
   - **b)** Only once per game ever
   - **c)** Before pygame.init
   - **d)** Never

3. `march_dir` is typically…
   - **a)** 1 or -1 for left/right
   - **b)** A pygame Surface
   - **c)** Player score
   - **d)** A file path

4. Invaders are drawn as…
   - **a)** Original ellipse shapes
   - **b)** Copyrighted bitmaps
   - **c)** HTML tables
   - **d)** Flask templates

5. Lesson 5.10 adds…
   - **a)** Collisions, shields, enemy fire
   - **b)** Only Turtle
   - **c)** Database queries
   - **d)** Removing lists


---

<details><summary>Click to reveal answers</summary>

1. **a)** Classic Space Invaders sidestep + drop.
2. **a)** Rects must follow the marching offset.
3. **a)** Sign tells which way the block slides.
4. **a)** Shape-only art — no stolen sprites.
5. **a)** Combat layer next.

</details>


## What's Next

→ [Lesson 5.10 — Shields, Lives & Score](../lesson-5-10-orbit-guard-shields-lives/README.md)

---

*Defend the orbit with code.*

[← Choose language](README.md)
