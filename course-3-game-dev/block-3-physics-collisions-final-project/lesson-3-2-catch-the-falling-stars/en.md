# Lesson 3.2: Catch the Falling Stars

> **Course:** Game Development with Python · **Block:** Physics & Collisions (Final Project) · **~45–50 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 45
-->

---

## Title

**Level 10 — Star Catcher**

---

## Explanation

This is the **Course 3 capstone** — a game you can demo.

| Piece | Job |
|-------|-----|
| Start screen | Title + SPACE |
| Playing | Paddle LEFT/RIGHT; star falls; catch or miss |
| Game over | Final score + SPACE back to title |

One star at a time keeps the code friendly:

```python
star.y += int(fall_speed * dt)
if paddle.colliderect(star):
    score += 1
    reset_star()
elif star.top > HEIGHT:
    misses += 1
    reset_star()
```

Three misses → `GAME_OVER`. Menus use **KEYDOWN**; paddle uses **get_pressed**.

---

### Step 1: Open starter/game.py

Open [starter/game.py](starter/game.py). Title / play / over drawing and paddle motion are sketched. TODOs: start on `START`, SPACE wiring, fall + catch/miss.

---

### Step 2: Begin on the title screen

```python
state = START
```

---

### Step 3: SPACE starts / returns

```python
if event.type == pygame.KEYDOWN:
    if state == START and event.key in (pygame.K_SPACE, pygame.K_RETURN):
        start_round()
    elif state == GAME_OVER and event.key in (pygame.K_SPACE, pygame.K_RETURN):
        state = START
```

`start_round()` resets score, misses, paddle, and star.

---

### Step 4: Fall, catch, miss

Inside `PLAYING`:

```python
star.y += int(fall_speed * dt)

if paddle.colliderect(star):
    score += 1
    reset_star()
elif star.top > HEIGHT:
    misses += 1
    reset_star()
    if misses >= MAX_MISSES:
        state = GAME_OVER
```

---

### Step 5: Play a full round

```text
cd course-3-game-dev\block-3-physics-collisions-final-project\lesson-3-2-catch-the-falling-stars
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Title → SPACE → stars fall → catch with paddle → after 3 misses Game Over → SPACE → title.

---

## Code Example

**File: [solution/game.py](solution/game.py)** — full listing (capstone length). Key ideas:

```python
def reset_star():
    star.midtop = (random.randint(20, WIDTH - 20), -40)

def start_round():
    global score, misses, state
    score = 0
    misses = 0
    paddle.midbottom = (WIDTH // 2, HEIGHT - 24)
    reset_star()
    state = PLAYING

# In PLAYING:
star.y += int(fall_speed * dt)
if paddle.colliderect(star):
    score += 1
    reset_star()
elif star.top > HEIGHT:
    misses += 1
    reset_star()
    if misses >= MAX_MISSES:
        state = GAME_OVER
```

Open the solution file for the complete runnable program (~120 lines).

---

## Code Execution

```text
cd course-3-game-dev\block-3-physics-collisions-final-project\lesson-3-2-catch-the-falling-stars
python starter\game.py
```

**Expected output (visual):** Complete Catch the Falling Stars loop with restart.

---

## Quick Drills

1. **Easier** — `MAX_MISSES = 5`.
2. **Wider paddle** — `paddle_w = 140` (rebuild the Rect).
3. **Praise** — on Game Over, if `score >= 10`, blit “Star hero!”.

---

## Practice Task

**Quest name:** Star Catcher

1. Finish all TODOs in [starter/game.py](starter/game.py).
2. Play until Game Over, then return to the title and play again.
3. **Bonus:** Slightly increase `fall_speed` after each catch (tiny ramp — more in 3.3).

**Self-mark:** Star falls? Catch adds score? 3 misses → Game Over? SPACE restarts via title? ✓

**Show-and-tell:** Ask a parent or friend to play one round!

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Star never moves, or score never changes when you “catch.”

**Cause:** Forgot `star.y += …`, or collision uses the wrong Rect, or `state` stuck / never `PLAYING`.

**Fix:** Uncomment fall + colliderect TODOs. Confirm `state = START` then SPACE → `start_round()`. Paddle and star must share screen space (star falls from `y = -40`).

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. What makes the star fall smoothly?
   - **a)** `pip install fall`
   - **b)** Adding `fall_speed * dt` to `star.y` each frame
   - **c)** Only `QUIT` events
   - **d)** Deleting the paddle

2. Best definition of a “catch” here?
   - **a)** `paddle.colliderect(star)` while playing
   - **b)** Closing the window
   - **c)** Loading a font
   - **d)** `pygame.init()` twice

3. What should happen when `star.top > HEIGHT`?
   - **a)** Instant win
   - **b)** Count a miss (and maybe game over)
   - **c)** Install Turtle
   - **d)** Freeze forever with no UI

4. Menu SPACE transitions should use…
   - **a)** `KEYDOWN` (one-shot)
   - **b)** Only `get_pressed` without care
   - **c)** Mouse only
   - **d)** `random.randint` only

5. Why call `reset_star()` after catch or miss?
   - **a)** To open a second window
   - **b)** To spawn the next star at the top
   - **c)** To remove `dt`
   - **d)** To uninstall Pygame

---

<details><summary>Click to reveal answers</summary>

1. **b)** Fall speed times delta time.
2. **a)** Paddle overlaps star.
3. **b)** Miss (and check MAX_MISSES).
4. **a)** One-shot KEYDOWN for menus.
5. **b)** Next star appears above the screen.

</details>

---

## What's Next

→ [Lesson 3.3 — Polish](../lesson-3-3-polish/README.md) — sound, high score, difficulty ramp!

---

*You shipped a real mini-game — take a bow!*

[← Choose language](README.md)
