# Lesson 5.4: Ball & Wall Bounces

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~32 min**  
> [Choose language](README.md) · **[Русский →](ru.md)**

<!-- meta
homework: starter/game.py
minutes: 32
-->

---

## Title

**Level ★16 — Spark Ball**

---

## Explanation

Store `ball_x`, `ball_y`, `ball_vx`, `ball_vy`. Each frame:

```python
ball_x += ball_vx * dt
ball_y += ball_vy * dt
bounce_walls()
```

Inside `bounce_walls()`, clamp position and use `abs()` so velocity always points **away** from the wall:

```python
if ball_x - BALL_R <= 0:
    ball_x = BALL_R
    ball_vx = abs(ball_vx)
```

- `ball_vx`, `ball_vy` as floats; position += velocity * `dt`
- Flip velocity sign when the circle touches an edge
- `BALL_R` radius — bounce when center is `R` pixels from the wall
- Forge palette: dark background + orange spark circles

---

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-4-bounce-forge-ball-walls
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
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-4-bounce-forge-ball-walls
python solution\game.py
```

**Expected output (visual):** Runnable Bounce Forge milestone for lesson 5.4.

---

## Quick Drills

1. Slow `ball_vx` to half — still bounces?
2. Log `hit_frac` when the paddle strikes.
3. Count bricks left on the HUD.

---

## Practice Task

**Quest name:** Spark Ball

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

1. `ball_vx` and `ball_vy` together are…
   - **a)** A 2D velocity vector
   - **b)** Flask secret key
   - **c)** Turtle pen width
   - **d)** Only the y position

2. Bouncing off the right wall usually means…
   - **a)** Set `ball_vy = 0` only
   - **b)** Make `ball_vx` negative (point left)
   - **c)** Delete pygame
   - **d)** Skip `dt`

3. Why multiply by `dt`?
   - **a)** Frame-rate independent motion
   - **b)** Install pygame twice
   - **c)** Draw bricks
   - **d)** Replace lists

4. `BALL_R` is used to…
   - **a)** Know when the circle touches a wall
   - **b)** Store high score
   - **c)** Load PNG sprites
   - **d)** Render HTML

5. Lesson 5.5 adds…
   - **a)** Anvil paddle, angle bounce, lives
   - **b)** Flask forms
   - **c)** Turtle snowflake
   - **d)** pip uninstall

---

<details><summary>Click to reveal answers</summary>

1. **a)** Vector motion for the spark.
2. **b)** Horizontal flip away from the edge.
3. **a)** `dt` keeps speed fair on slow PCs.
4. **a)** Radius for collision with edges.
5. **a)** Paddle control next.
</details>


## What's Next

→ [Lesson 5.5 — Paddle & Lives](../lesson-5-5-bounce-forge-paddle-lives/README.md)

---

*Sparks fly in the forge.*

[← Choose language](README.md)
