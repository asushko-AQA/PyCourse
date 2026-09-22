# Lesson 1.3: Shapes & Coordinates

> **Course:** Game Development with Python · **Block:** Getting Started with Pygame · **~30–35 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 30
-->

---

## Title

**Level 3 — Box Voyager**

---

## Explanation

Time to put a **hero on the map**. In Pygame, the map is a grid of pixels. Important surprise vs math class:

| Idea | In Pygame |
|------|-----------|
| Origin `(0, 0)` | **Top-left** corner of the window |
| Increasing `x` | Move **right** |
| Increasing `y` | Move **down** (not up!) |

A rectangle needs a top-left corner `(x, y)` plus width and height:

```python
pygame.draw.rect(screen, (255, 200, 50), (x, y, box_w, box_h))
```

Move the hero by changing variables each frame:

```python
x = x + speed
```

When `x` goes past the right edge, wrap it back so the voyage never ends.

---

### Step 1: Open starter/game.py

Open [starter/game.py](starter/game.py). Window, fill, and quit are ready. TODOs: **move** and **draw**.

---

### Step 2: Update x each frame

After the event loop, before drawing:

```python
x = x + speed
```

---

### Step 3: Draw the rectangle

After `screen.fill(...)`:

```python
pygame.draw.rect(screen, (255, 200, 50), (x, y, box_w, box_h))
```

Color is gold-ish; change it if you want a neon hero.

---

### Step 4: Wrap (solution includes this)

```python
if x > WIDTH:
    x = -box_w
```

Starting at `-box_w` lets the box slide in from the left edge.

---

### Step 5: Run

```text
cd course-3-game-dev\block-1-getting-started-pygame\lesson-1-3-shapes-coordinates
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Dark background; gold box slides right; with wrap, it reappears on the left. Quit with X.

---

## Code Example

**File: [solution/game.py](solution/game.py)**

```python
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Box Voyager")

clock = pygame.time.Clock()
running = True

x = 100
y = 200
box_w = 50
box_h = 50
speed = 3

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x = x + speed
    if x > WIDTH:
        x = -box_w

    screen.fill((20, 24, 40))
    pygame.draw.rect(screen, (255, 200, 50), (x, y, box_w, box_h))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

---

## Code Execution

```text
cd course-3-game-dev\block-1-getting-started-pygame\lesson-1-3-shapes-coordinates
python starter\game.py
```

**Expected output (visual):** Moving filled rectangle on a dark fill; wraps when past the right edge (after you add wrap or use the solution).

---

## Quick Drills

1. **Turbo** — set `speed = 10`. Still readable?
2. **Vertical voyage** — move `y` instead of `x`; wrap with `HEIGHT`.
3. **Tiny scout** — `box_w = 20`, `box_h = 20`.

---

## Practice Task

**Quest name:** Box Voyager

1. Complete TODOs in [starter/game.py](starter/game.py): update `x`, draw the rect.
2. Add wrap so the box returns from the left (see Code Example).
3. **Bonus:** Bounce instead of wrap — when `x` hits an edge, flip `speed` to `-speed`.

**Self-mark:** Box visible? Moves? Wraps or bounces? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** You call `draw.rect` but never see the box — only the background.

**Cause:** Drawing **before** `fill` (fill paints over the box), or `x`/`y` are way off-screen, or you forgot `flip()`.

**Fix:** Order each frame: events → update `x`/`y` → `fill` → `draw.rect` → `flip` → `tick`. Confirm `x` starts near `100` and `y` near `200`.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. Where is `(0, 0)` in a Pygame window?
   - **a)** Bottom-left (like math class)
   - **b)** Top-left
   - **c)** Center of the screen
   - **d)** Bottom-right

2. What does increasing `y` do?
   - **a)** Move the shape up
   - **b)** Move the shape down
   - **c)** Change the window title
   - **d)** Install Pygame

3. Which call draws a filled rectangle?
   - **a)** `pygame.draw.rect(screen, color, (x, y, w, h))`
   - **b)** `screen.fill(rect)`
   - **c)** `turtle.forward(w)`
   - **d)** `pip install rect`

4. Why update `x` every frame?
   - **a)** To close the window
   - **b)** So the box's position changes over time (motion)
   - **c)** To change RGB permanently
   - **d)** To create a venv

5. A good order for one frame is:
   - **a)** flip → fill → draw → update
   - **b)** events → update position → fill → draw → flip → tick
   - **c)** quit → init → pip
   - **d)** draw only once before the loop

---

<details><summary>Click to reveal answers</summary>

1. **b)** Pygame's origin is the top-left pixel.
2. **b)** Larger `y` means lower on the screen.
3. **a)** `draw.rect` takes surface, color, and the `(x, y, w, h)` rectangle.
4. **b)** Changing `x` each frame creates movement.
5. **b)** Update, then paint, then show, then pace the frame.

</details>

---

## What's Next

→ [Lesson 1.4: Delta Time & Smooth Movement](../lesson-1-4-delta-time-smooth-movement/README.md) — same voyage, but smooth on fast and slow computers.

---

*The box sails. Next: teach it to respect real time!*

[← Choose language](README.md)
