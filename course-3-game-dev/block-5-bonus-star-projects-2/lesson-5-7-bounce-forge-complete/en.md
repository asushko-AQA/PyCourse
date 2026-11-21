# Lesson 5.7: Bounce Forge Complete

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~40 min**  
> [Choose language](README.md) · **[Русский →](ru.md)**

<!-- meta
homework: starter/game.py
minutes: 40
-->

---

## Title

**Level ★19 — Bounce Forge Pro**

---

## Explanation

Chain lessons 5.4–5.6. On clear level, load next pattern or `WIN`. Speed scales with level and score. Title: SPACE = Breakout, P = Pong.

- `LEVEL_PATTERNS` list of string rows
- `state` like Glow Worm 5.3
- `high_score` on breakout runs
- `P` toggles Pong: two anvil paddles, first to 5

---

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-7-bounce-forge-complete
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Forge window; finish TODOs to match the lesson goal.

---

### Step 2: Compare the solution

Study [solution/game.py](solution/game.py) for wall bounce, paddle angle, bricks, or full states — depending on this lesson.

---

## Code Example

**File: [solution/game.py](solution/game.py)** — key pattern from this lesson:

```python
ball_x += ball_vx * dt
ball_y += ball_vy * dt
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-7-bounce-forge-complete
python solution\game.py
```

**Expected output (visual):** Runnable Bounce Forge milestone for lesson 5.7.

---

## Quick Drills

1. Slow `ball_vx` to half — still bounces?
2. Log `hit_frac` when the paddle strikes.
3. Count bricks left on the HUD.

---

## Practice Task

**Quest name:** Bounce Forge Pro

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: does the forge window behave like the lesson goal?
3. **Bonus stretch:** extra spark particles on bounce (see 5.4 solution).

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Ball sticks inside a brick.

**Cause:** No position nudge after flipping velocity.

**Fix:** Move ball one pixel out along the normal after bounce.

**Problem:** Paddle teleports off-screen.

**Cause:** Forgetting `paddle.clamp_ip(screen.get_rect())`.

**Fix:** Clamp after every movement step.

---

## Quick Check

1. `LEVEL_PATTERNS` holds…
   - **a)** Strings of 0/1 for brick rows
   - **b)** PNG filenames
   - **c)** Flask URLs
   - **d)** Turtle angles only

2. Session `high_score` should update…
   - **a)** Every pygame.init
   - **b)** When current score beats it
   - **c)** Only on WIN
   - **d)** Never

3. Optional Pong mode uses…
   - **a)** Two paddles; Q/E for top player
   - **b)** Mouse only
   - **c)** No ball
   - **d)** HTTP GET

4. When all levels clear you set…
   - **a)** GAME_OVER always
   - **b)** Flask debug
   - **c)** state = WIN
   - **d)** score = 0

5. Next ★ roadmap project is…
   - **a)** Orbit Guard (coming soon)
   - **b)** Course 2 calculator
   - **c)** Block 0 pen paper
   - **d)** Removing pygame

---

<details><summary>Click to reveal answers</summary>

1. **a)** ASCII maps for bricks.
2. **b)** Track best during play.
3. **a)** Second paddle on title P.
4. **c)** Victory state.
5. **a)** See block README.
</details>


## What's Next

→ [Lesson 5.8 — Patrol Ship & Blasters](../lesson-5-8-orbit-guard-patrol-ship/README.md) — **Orbit Guard** ★ project #3!

---

*Sparks fly in the forge.*

[← Choose language](README.md)
