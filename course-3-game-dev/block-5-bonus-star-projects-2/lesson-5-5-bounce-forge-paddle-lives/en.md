# Lesson 5.5: Paddle & Lives

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~35 min**  
> [Choose language](README.md) · **[Русский →](ru.md)**

<!-- meta
homework: starter/game.py
minutes: 35
-->

---

## Title

**Level ★17 — Anvil Paddle**

---

## Explanation

When the ball falls **down** into the paddle:

```python
hit_frac = (ball_x - paddle.centerx) / (paddle.width / 2)
ball_vx = hit_frac * speed * 0.9
ball_vy = -max(200, speed * 0.85)
```

If `ball_y` passes below the window, subtract a life and reset ball to center.

- `pygame.Rect` paddle; move with A/D or arrows + `dt`
- `hit_frac` from -1 (left edge) to 1 (right edge)
- Steeper `ball_vx` when you hit the paddle edge
- `lives` counter; re-serve ball after a miss

---

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-5-bounce-forge-paddle-lives
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
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-5-bounce-forge-paddle-lives
python solution\game.py
```

**Expected output (visual):** Runnable Bounce Forge milestone for lesson 5.5.

---

## Quick Drills

1. Slow `ball_vx` to half — still bounces?
2. Log `hit_frac` when the paddle strikes.
3. Count bricks left on the HUD.

---

## Practice Task

**Quest name:** Anvil Paddle

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

1. `hit_frac` near +1 means the ball hit…
   - **a)** The right side of the paddle
   - **b)** The top wall only
   - **c)** A brick corner
   - **d)** The food cell

2. Paddle motion should use…
   - **a)** Only `event.KEYDOWN` once per key
   - **b)** `get_pressed()` + `dt` each frame
   - **c)** Turtle.forward
   - **d)** Flask POST

3. `lives` decreases when…
   - **a)** Score hits 100
   - **b)** You press SPACE on title
   - **c)** Ball falls below the paddle
   - **d)** pygame.QUIT fires

4. After a miss you typically…
   - **a)** Re-center the ball and serve upward
   - **b)** Quit pygame instantly
   - **c)** Delete all bricks
   - **d)** Grow snake tail

5. Lesson 5.6 adds…
   - **a)** Brick list, side bounce, score
   - **b)** HTML templates
   - **c)** Virtualenv lesson
   - **d)** Only sound files

---

<details><summary>Click to reveal answers</summary>

1. **a)** Right edge → more rightward vx.
2. **b)** Continuous keyboard polling.
3. **c)** Miss = lose spark life.
4. **a)** Re-serve like classic Breakout.
5. **a)** Ember bricks next.
</details>


## What's Next

→ [Lesson 5.6 — Bricks & Score](../lesson-5-6-bounce-forge-bricks-score/README.md)

---

*Sparks fly in the forge.*

[← Choose language](README.md)
