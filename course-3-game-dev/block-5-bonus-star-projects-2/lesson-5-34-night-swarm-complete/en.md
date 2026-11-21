# Lesson 5.34: Night Swarm Complete

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~38 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 38
-->

---

## Title

**Level ★46 — Night Swarm Pro**

---

## Explanation

**Night Swarm** — Block 5 ★ project **#9** — is a calm **top-down lantern keeper** game: you repel soft **shadow creatures** with **light orbs** (shapes only, no violence graphics).

This lesson focuses on: **harder waves over time, 3-minute survive goal, menu/level-up/pause/win/loss, session best time.**

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-34-night-swarm-complete
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
state = "MENU"
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-34-night-swarm-complete
python solution\game.py
```

**Mac/Linux:** `python solution/game.py`

**Expected output (visual):** Runnable Night Swarm milestone for lesson 5.34.

---

## Quick Drills

1. Print your move vector before `normalize()` — when is length > 1?
2. Change `PLAYER_SPEED` and feel the difference with the same `dt`.
3. Name one upgrade key from `UPGRADE_POOL` and what it boosts.

---

## Practice Task

**Quest name:** Night Swarm Pro

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

1. Win condition in this build is…
   - **a)** Survive about 180 seconds
   - **b)** Collect one coin
   - **c)** Merge to 2048
   - **d)** Clear mines only
2. Difficulty ramp can…
   - **a)** Shorten spawn interval over time
   - **b)** Remove all enemies
   - **c)** Disable dt forever
   - **d)** Skip drawing
3. Session best should store…
   - **a)** Longest survive time
   - **b)** Only window title
   - **c)** Student .env
   - **d)** Git hash
4. Pause uses…
   - **a)** ESC toggles while playing
   - **b)** Only mouse right-click
   - **c)** Flask POST
   - **d)** pip uninstall
5. Roadmap next is…
   - **a)** Lane Rush top-down dodge
   - **b)** Course 1 install
   - **c)** Django deploy
   - **d)** Only Turtle

---

<details><summary>Click to reveal answers</summary>

1. **a)** Survive about 180 seconds
2. **a)** Shorten spawn interval over time
3. **a)** Longest survive time
4. **a)** ESC toggles while playing
5. **a)** Lane Rush top-down dodge

</details>

## What's Next

→ [Block 5 — Lane Rush (coming soon)](../../README.md) — **Lane Rush** ★ project #10 on the roadmap

---

*Keep the lantern bright!*

[Choose language](README.md)
