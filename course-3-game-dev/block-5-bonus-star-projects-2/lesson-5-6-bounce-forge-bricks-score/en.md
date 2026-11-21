# Lesson 5.6: Bricks & Score

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~36 min**  
> [Choose language](README.md) · **[Русский →](ru.md)**

<!-- meta
homework: starter/game.py
minutes: 36
-->

---

## Title

**Level ★18 — Ember Bricks**

---

## Explanation

Loop `bricks[:]` and test collision. Compare penetration from previous position to pick **left/right vs top/bottom**, then remove the brick.

- Build rows from string patterns (`"1110101"`)
- Save `prev_ball_x/y` before moving — better side guess
- Flip `vx` on left/right hits; flip `vy` on top/bottom
- `score += 10` per brick

---

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-6-bounce-forge-bricks-score
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
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-6-bounce-forge-bricks-score
python solution\game.py
```

**Expected output (visual):** Runnable Bounce Forge milestone for lesson 5.6.

---

## Quick Drills

1. Slow `ball_vx` to half — still bounces?
2. Log `hit_frac` when the paddle strikes.
3. Count bricks left on the HUD.

---

## Practice Task

**Quest name:** Ember Bricks

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

1. Bricks are stored as…
   - **a)** A list of `pygame.Rect`
   - **b)** A Flask route table
   - **c)** Turtle pens
   - **d)** Only tuples of RGB

2. Why keep `prev_ball_x`?
   - **a)** Guess collision side (top vs side)
   - **b)** Store PNG paths
   - **c)** Replace dt
   - **d)** Render quiz HTML

3. Hitting the top face usually flips…
   - **a)** Only score
   - **b)** `ball_vy` sign
   - **c)** Window width
   - **d)** paddle.x

4. After removing a brick you should…
   - **a)** Break after first hit per frame
   - **b)** Remove every brick always
   - **c)** Never change vx
   - **d)** Skip score

5. Lesson 5.7 adds…
   - **a)** Full game: levels, states, session best
   - **b)** Course 0 warm-up
   - **c)** pip install django
   - **d)** Only one wall

---

<details><summary>Click to reveal answers</summary>

1. **a)** Rects for draw + collide.
2. **a)** Side detection needs last frame.
3. **b)** Vertical bounce off brick.
4. **c)** One brick per frame is enough.
5. **a)** Complete forge game.
</details>


## What's Next

→ [Lesson 5.7 — Bounce Forge Complete](../lesson-5-7-bounce-forge-complete/README.md)

---

*Sparks fly in the forge.*

[← Choose language](README.md)
