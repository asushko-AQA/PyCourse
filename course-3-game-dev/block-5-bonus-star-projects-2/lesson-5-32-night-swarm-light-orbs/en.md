# Lesson 5.32: Light Orbs Auto-Fire

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~36 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 36
-->

---

## Title

**Level ★44 — Orb Sentinel**

---

## Explanation

**Night Swarm** — Block 5 ★ project **#9** — is a calm **top-down lantern keeper** game: you repel soft **shadow creatures** with **light orbs** (shapes only, no violence graphics).

This lesson focuses on: **nearest-enemy targeting, projectile list, enemy HP, XP gem drops.**

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-32-night-swarm-light-orbs
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
idx = nearest_enemy_index(px, py, enemies)
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-32-night-swarm-light-orbs
python solution\game.py
```

**Mac/Linux:** `python solution/game.py`

**Expected output (visual):** Runnable Night Swarm milestone for lesson 5.32.

---

## Quick Drills

1. Print your move vector before `normalize()` — when is length > 1?
2. Change `PLAYER_SPEED` and feel the difference with the same `dt`.
3. Name one upgrade key from `UPGRADE_POOL` and what it boosts.

---

## Practice Task

**Quest name:** Orb Archer

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

1. Auto-attack should target…
   - **a)** The nearest living shadow
   - **b)** A random corner
   - **c)** The HUD text
   - **d)** Oldest coin
2. Projectiles are usually stored in…
   - **a)** A list of dicts
   - **b)** A SQL table
   - **c)** One global int
   - **d)** A Flask route
3. When enemy HP hits 0…
   - **a)** Drop an XP gem
   - **b)** Spawn a brick
   - **c)** End the course
   - **d)** Delete pygame
4. Orb motion uses…
   - **a)** pos += vel * dt
   - **b)** Only while loops in turtle
   - **c)** CSS flex
   - **d)** HTML forms
5. Next lesson adds…
   - **a)** level-up upgrade picks
   - **b)** Pong paddle
   - **c)** 2048 merge
   - **d)** Glyph shuffle

---

<details><summary>Click to reveal answers</summary>

1. **a)** The nearest living shadow
2. **a)** A list of dicts
3. **a)** Drop an XP gem
4. **a)** pos += vel * dt
5. **a)** level-up upgrade picks

</details>

## What's Next

→ [Lesson 5.33 — XP & Level-Up Choices](../lesson-5-33-night-swarm-level-up/README.md)

---

*Keep the lantern bright!*

[Choose language](README.md)
