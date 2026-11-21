# Lesson 5.31: Shadow Spawns & HP

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~34 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 34
-->

---

## Title

**Level ★43 — Shadow Tide**

---

## Explanation

**Night Swarm** — Block 5 ★ project **#9** — is a calm **top-down lantern keeper** game: you repel soft **shadow creatures** with **light orbs** (shapes only, no violence graphics).

This lesson focuses on: **timer spawns at screen edges, `direction_toward` chase, contact damage, HP bar.**

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-31-night-swarm-shadow-spawns
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Twilight arena window; finish TODOs for this lesson's goal.

---

### Step 2: Compare the solution

Study [solution/game.py](solution/game.py) for the full pattern.

---

## Code Example

**File: [solution/game.py](solution/game.py)**:

```python
d = direction_toward(ex, ey, px, py)
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-31-night-swarm-shadow-spawns
python solution\game.py
```

**Mac/Linux:** `python solution/game.py`

**Expected output (visual):** Runnable Night Swarm milestone for lesson 5.31.

---

## Quick Drills

1. Print your move vector before `normalize()` — when is length > 1?
2. Change `PLAYER_SPEED` and feel the difference with the same `dt`.
3. Name one upgrade key from `UPGRADE_POOL` and what it boosts.

---

## Practice Task

**Quest name:** Edge Warden

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: does the window match this lesson's goal?
3. **Bonus stretch:** tint the arena grid a new colour.

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Diagonal movement feels faster than cardinal directions

**Cause:** Adding `(1,1)` without normalizing makes length √2.

**Fix:** Call `move.normalize()` whenever `move.length_squared() > 0`.

---

## Quick Check

1. Enemies should spawn…
   - **a)** Just outside screen edges
   - **b)** Only in the centre
   - **c)** From PNG files
   - **d)** Inside the HUD
2. Chase uses a vector…
   - **a)** Toward the player each frame
   - **b)** Random teleport
   - **c)** Toward mouse only
   - **d)** Without dt
3. Contact damage needs…
   - **a)** A short hurt cooldown
   - **b)** Infinite instant kill
   - **c)** No player HP
   - **d)** Flask session
4. Capping `MAX_ENEMIES` helps…
   - **a)** Performance stay smooth
   - **b)** Delete shadows
   - **c)** Disable draw
   - **d)** Skip input
5. Next lesson adds…
   - **a)** auto light orbs
   - **b)** Breakout paddle
   - **c)** Tic-tac grid
   - **d)** Mine flood-fill

---

<details><summary>Click to reveal answers</summary>

1. **a)** Just outside screen edges
2. **a)** Toward the player each frame
3. **a)** A short hurt cooldown
4. **a)** Performance stay smooth
5. **a)** auto light orbs

</details>

## What's Next

→ [Lesson 5.32 — Light Orbs Auto-Fire](../lesson-5-32-night-swarm-light-orbs/README.md)

---

*Keep the lantern bright!*

[Choose language](README.md)
