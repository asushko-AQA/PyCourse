# Lesson 5.30: Lantern Keeper Move

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~32 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 32
-->

---

## Title

**Level ★42 — Lantern Step**

---

## Explanation

**Night Swarm** — Block 5 ★ project **#9** — is a calm **top-down lantern keeper** game: you repel soft **shadow creatures** with **light orbs** (shapes only, no violence graphics).

This lesson focuses on: **`pygame.Vector2` eight-way input, `.normalize()`, arena bounds with `dt`.**

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-30-night-swarm-lantern-move
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
move = move.normalize()
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-30-night-swarm-lantern-move
python solution\game.py
```

**Mac/Linux:** `python solution/game.py`

**Expected output (visual):** Runnable Night Swarm milestone for lesson 5.30.

---

## Quick Drills

1. Print your move vector before `normalize()` — when is length > 1?
2. Change `PLAYER_SPEED` and feel the difference with the same `dt`.
3. Name one upgrade key from `UPGRADE_POOL` and what it boosts.

---

## Practice Task

**Quest name:** Lantern Drift

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

1. `Vector2.normalize()` helps because…
   - **a)** Diagonal speed matches cardinals
   - **b)** It removes pygame
   - **c)** It disables dt
   - **d)** It loads PNGs
2. Eight-way movement builds input from…
   - **a)** WASD and arrow keys combined
   - **b)** Only mouse clicks
   - **c)** SQL queries
   - **d)** pip list
3. Arena clamping keeps the lantern…
   - **a)** Inside margin borders
   - **b)** Off-screen forever
   - **c)** In Flask only
   - **d)** Without colors
4. `dt` in `pos += move * SPEED * dt` means…
   - **a)** Frame-rate independent motion
   - **b)** Delete timer
   - **c)** Only Windows
   - **d)** Turtle pen
5. Next lesson adds…
   - **a)** shadow spawns and HP
   - **b)** Flask templates
   - **c)** Course 1 Turtle
   - **d)** Breakout bricks

---

<details><summary>Click to reveal answers</summary>

1. **a)** Diagonal speed matches cardinals
2. **a)** WASD and arrow keys combined
3. **a)** Inside margin borders
4. **a)** Frame-rate independent motion
5. **a)** shadow spawns and HP

</details>

## What's Next

→ [Lesson 5.31 — Shadow Spawns & HP](../lesson-5-31-night-swarm-shadow-spawns/README.md)

---

*Keep the lantern bright!*

[Choose language](README.md)
