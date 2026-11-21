# Lesson 5.25: Player & Jump

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~32 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 32
-->

---

## Title

**Level ★37 — Crystal Hop**

---

## Explanation

**Leap Lands** — Block 5 ★ project **#8** — is a twilight **mini platformer** with shape-only art (no image files).

Maps are **lists of strings**: `#` ground, `=` platform, `C` coin, `S` spawn, `F` flag, `^` spike, `E` enemy patrol (later lessons).

This lesson focuses on: **player `Rect`, left/right with `dt`, gravity + jump only when grounded.**

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-25-leap-lands-player-jump
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Night-sky window; finish TODOs for this lesson's goal.

---

### Step 2: Compare the solution

Study [solution/game.py](solution/game.py) for the full pattern.

---

## Code Example

**File: [solution/game.py](solution/game.py)**:

```python
vel_y += GRAVITY * dt
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-25-leap-lands-player-jump
python solution\game.py
```

**Mac/Linux:** `python solution/game.py`

**Expected output (visual):** Runnable Leap Lands milestone for lesson 5.25.

---

## Quick Drills

1. Print `grounded` when moving — when is it `True`?
2. Tweak `GRAVITY` or `JUMP_V` and rerun.
3. Name three map characters and what they mean.

---

## Practice Task

**Quest name:** Crystal Hopper

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: does the window match this lesson's goal?
3. **Bonus stretch:** draw a faint starfield behind the tiles.

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Player falls through the floor

**Cause:** Skipping axis-separated collision or never setting `grounded`.

**Fix:** After moving on **Y**, push the player up to `tile.top` when landing.

---

## Quick Check

1. `dt` keeps motion smooth because…
   - **a)** Speed scales with frame time
   - **b)** It disables input
   - **c)** It only works on Linux
   - **d)** It removes gravity
2. Jump should happen only when…
   - **a)** `grounded` is True
   - **b)** In the air always
   - **c)** `vel_y < 0`
   - **d)** On Flask server
3. `#` in the map is…
   - **a)** Solid ground
   - **b)** A coin
   - **c)** A flag
   - **d)** Background JPG
4. Axis-separated collision is…
   - **a)** Move X, resolve, move Y, resolve
   - **b)** Random teleport
   - **c)** Turtle only
   - **d)** SQL DELETE
5. Next lesson adds…
   - **a)** a map from strings
   - **b)** pip freeze
   - **c)** Course 1 Turtle
   - **d)** Only print()

---

<details><summary>Click to reveal answers</summary>

1. **a)** Speed scales with frame time.

2. **a)** On the ground.

3. **a)** Solid ground.

4. **a)** Separate X then Y.

5. **a)** Next arc step.

</details>

## What's Next

→ [Lesson 5.26 — Text Map & Tiles](../lesson-5-26-leap-lands-text-map/README.md)

---

*Float on!*

[Choose language](README.md)
