# Lesson 1.4: Delta Time & Smooth Movement

> **Course:** Game Development with Python · **Block:** Getting Started with Pygame · **~30–40 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 35
-->

---

## Title

**Level 4 — Time Slider**

---

## Explanation

In Lesson 1.3 the box moved with `x = x + 3` **every frame**. That secretly ties speed to frame rate:

| Machine | Frames per second | Motion feel with `+ 3` each frame |
|---------|-------------------|-------------------------------------|
| Slow laptop | ~30 FPS | Sluggish voyage |
| Gaming PC | ~120 FPS | Box teleports across the sky |

**Delta time** (`dt`) is “how many **seconds** passed since the last frame?” Move using **pixels per second**:

```python
dt = clock.tick(60) / 1000   # tick returns milliseconds
x = x + speed * dt           # speed e.g. 200 pixels/second
```

`clock.tick(60)` still aims for 60 FPS **and** tells you the real elapsed time. Divide by `1000` to convert milliseconds → seconds.

Keep `x` as a **float** (`50.0`). Draw with `int(x)` so `draw.rect` gets whole pixels.

---

### Step 1: Open starter/game.py

Open [starter/game.py](starter/game.py). Drawing and wrap are ready. TODOs: compute **`dt`**, then move with **`speed * dt`**.

---

### Step 2: Measure dt at the start of the frame

At the top of the `while` loop (before or with events):

```python
dt = clock.tick(60) / 1000
```

Remove any second `clock.tick` at the bottom — one tick per frame is enough.

---

### Step 3: Move with speed * dt

```python
x = x + speed * dt
```

Here `speed = 200` means “about 200 pixels every second,” not “200 pixels every frame.”

---

### Step 4: Run and feel the glide

```text
cd course-3-game-dev\block-1-getting-started-pygame\lesson-1-4-delta-time-smooth-movement
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Teal/mint box glides smoothly left→right and wraps. Closing X still works.

---

### Step 5: Optional experiment

Temporarily use `clock.tick(30)` then `clock.tick(120)`. With `dt`, the **travel speed** should stay roughly the same even if the animation is choppier at 30 FPS.

---

## Code Example

**File: [solution/game.py](solution/game.py)**

```python
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Time Slider")

clock = pygame.time.Clock()
running = True

x = 50.0
y = 220.0
box_w = 50
box_h = 50
speed = 200  # pixels per second

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x = x + speed * dt

    if x > WIDTH:
        x = -box_w

    screen.fill((15, 18, 32))
    pygame.draw.rect(screen, (80, 220, 180), (int(x), int(y), box_w, box_h))
    pygame.display.flip()

pygame.quit()
```

---

## Code Execution

```text
cd course-3-game-dev\block-1-getting-started-pygame\lesson-1-4-delta-time-smooth-movement
python starter\game.py
```

**Expected output (visual):** Smooth horizontal motion at ~200 px/s; wrap on the right edge.

---

## Quick Drills

1. **Slow-mo** — `speed = 60`. Count roughly how long a full crossing takes.
2. **FPS stress** — try `tick(30)` and `tick(120)` with the same `speed`.
3. **Float check** — leave `x` as float; only `int(x)` inside `draw.rect`.

---

## Practice Task

**Quest name:** Time Slider

1. Complete TODOs in [starter/game.py](starter/game.py): `dt` from `clock.tick`, then `x += speed * dt`.
2. Confirm the box still wraps and quits cleanly.
3. **Bonus:** Add vertical drift too: `y += 40 * dt` and wrap on `HEIGHT`.

**Self-mark:** Uses `dt`? Speed feels steady? Wrap works? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Box barely moves, or sits still.

**Cause:** `dt` left as `0`, or you still call `clock.tick` incorrectly, or `speed` is tiny (like `3` — that is pixels/**second**, so very slow!).

**Fix:** Set `dt = clock.tick(60) / 1000` once per frame. Use `speed` around `150–300` for a fun slide. Never multiply by `dt` twice.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. What is delta time (`dt`) in this lesson?
   - **a)** The window width
   - **b)** Seconds elapsed since the previous frame
   - **c)** The RGB red channel
   - **d)** A Turtle command

2. Why is `x += 3` each frame risky?
   - **a)** It uninstalls Pygame
   - **b)** Speed depends on how many frames you get per second
   - **c)** It only works on Mac
   - **d)** It cannot draw rectangles

3. What does `clock.tick(60) / 1000` return (approximately)?
   - **a)** Always exactly `60`
   - **b)** Elapsed time in **seconds** (often near `0.016` at 60 FPS)
   - **c)** A color tuple
   - **d)** The caption string

4. If `speed = 200`, what does `x += speed * dt` mean?
   - **a)** Move 200 pixels every frame no matter what
   - **b)** Move about 200 pixels every **second**
   - **c)** Set FPS to 200
   - **d)** Fill the screen 200 times

5. Why keep `x` as a float and use `int(x)` when drawing?
   - **a)** Pygame forbids floats forever
   - **b)** Small `dt` steps add up smoothly in floats; drawing wants whole pixels
   - **c)** Floats close the window
   - **d)** Only strings can be drawn

---

<details><summary>Click to reveal answers</summary>

1. **b)** `dt` measures real time between frames in seconds.
2. **b)** Per-frame adds make fast machines move farther each second.
3. **b)** Milliseconds from `tick`, divided by 1000 → seconds.
4. **b)** `speed` is pixels per second when multiplied by `dt`.
5. **b)** Float math stays accurate; `draw.rect` prefers integer pixel coords.

</details>

---

## What's Next

→ [Block 1 index](../README.md) — tick the readiness checklist!  
→ **Block 2 (planned):** keyboard controls, sprites, score text, game states.

---

*You slid through time. Block 1 complete — the Game Lab bootcamp is done!*

[← Choose language](README.md)
