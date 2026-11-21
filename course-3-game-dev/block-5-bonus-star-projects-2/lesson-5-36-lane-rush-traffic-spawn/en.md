# Lesson 5.36: Traffic Spawns & Distance

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~36 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 36
-->

---

## Title

**Level ★48 — Traffic Tide**

---

## Explanation

**Lane Rush** — Block 5 ★ project **#10** — is a **top-down dodge racer** on scrolling neon lanes.

This lesson focuses on: **traffic cars spawning in random lanes on a timer, moving down, `colliderect` crash ends the run, distance score from scroll speed.**

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-36-lane-rush-traffic-spawn
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

---

### Step 2: Compare the solution

Study [solution/game.py](solution/game.py).

---

## Code Example

**File: [solution/game.py](solution/game.py)**:

```python
if pr.colliderect(tr):
    game_over = True
```

---

## Code Execution

```text
python solution\game.py
```

**Expected output (visual):** Traffic streams down; crash shows game over; `R` restarts.

---

## Quick Drills

1. What dict keys does each traffic car need?
2. Why remove cars when `cy > HEIGHT`?
3. How does `distance_m` grow each frame?

---

## Practice Task

**Quest name:** Traffic Tide

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: dodge at least one car before a crash.
3. **Bonus stretch:** draw traffic with a second accent colour.

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Cars stack on top of each other

**Cause:** Spawning every frame instead of on a timer.

**Fix:** Only append when `spawn_timer <= 0`, then reset to `SPAWN_EVERY`.

---

## Quick Check

1. Traffic spawn lane is picked with…
   - **a)** `rng.randint(0, NUM_LANES - 1)`
   - **b)** Only mouse X
   - **c)** Flask session
   - **d)** Turtle heading
2. Cars move…
   - **a)** Down the screen each frame with `TRAFFIC_SPEED * dt`
   - **b)** Only left on the title screen
   - **c)** Never
   - **d)** Only in JSON
3. Crash detection uses…
   - **a)** `Rect.colliderect`
   - **b)** `pip list`
   - **c)** SQL joins
   - **d)** HTML forms
4. Distance score rises because…
   - **a)** Scroll speed accumulates over time
   - **b)** Window title changes
   - **c)** Git push
   - **d)** Mines explode
5. Next lesson adds…
   - **a)** Fuel, coins, near-miss, session best, Block 5 finale
   - **b)** Course 2 deploy
   - **c)** Shard Stack rotate
   - **d)** Only Block 0 warm-up

---

<details><summary>Click to reveal answers</summary>

1. **a)** `rng.randint(0, NUM_LANES - 1)`
2. **a)** Down the screen each frame with `TRAFFIC_SPEED * dt`
3. **a)** `Rect.colliderect`
4. **a)** Scroll speed accumulates over time
5. **a)** Fuel, coins, near-miss, session best, Block 5 finale

</details>

## What's Next

→ [Lesson 5.37 — Lane Rush Complete](../lesson-5-37-lane-rush-complete/README.md)

---

*Thread the traffic!*

[Choose language](README.md)