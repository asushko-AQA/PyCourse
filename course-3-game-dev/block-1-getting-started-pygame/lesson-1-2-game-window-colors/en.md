# Lesson 1.2: Game Window & Colors

> **Course:** Game Development with Python · **Block:** Getting Started with Pygame · **~30–35 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 30
-->

---

## Title

**Level 2 — Color Caster**

---

## Explanation

Yesterday you opened a portal. Today you **paint** it. In Pygame, a color is three numbers — **R**ed, **G**reen, **B**lue — each from **0** (off) to **255** (full blast).

| RGB | Looks like |
|-----|------------|
| `(255, 0, 0)` | Pure red |
| `(0, 255, 0)` | Pure green |
| `(0, 0, 255)` | Pure blue |
| `(255, 255, 255)` | White |
| `(0, 0, 0)` | Black |
| `(30, 30, 80)` | Deep blue (Lesson 1.1) |

Call `screen.fill((r, g, b))` **every frame**, then change `r`, `g`, or `b` a little. The sky slowly shifts — magic with math!

Keep channels in range:

```python
r = (r + 1) % 256
```

`% 256` wraps 256 back to 0 so you never leave the legal 0–255 band.

---

### Step 1: Open starter/game.py

Open [starter/game.py](starter/game.py). The window and quit loop are ready. Your quest: **fill** + **nudge color**.

---

### Step 2: Fill the screen each frame

Inside the `while` loop, after events:

```python
screen.fill((r, g, b))
```

Without this, you only see a blank/black surface.

---

### Step 3: Change a channel each frame

Right after `fill`:

```python
r = (r + 1) % 256
```

Try `+ 1` first (slow). Later try `+ 3` or nudge `g` / `b` instead.

---

### Step 4: Run it

**Path A:**

```text
cd course-3-game-dev\block-1-getting-started-pygame\lesson-1-2-game-window-colors
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Window opens; background color slowly shifts as red cycles. Close with X.

---

## Code Example

**File: [solution/game.py](solution/game.py)** (target after TODOs)

```python
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Caster")

clock = pygame.time.Clock()
running = True

r = 40
g = 80
b = 160

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((r, g, b))
    r = (r + 1) % 256

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

---

## Code Execution

```text
cd course-3-game-dev\block-1-getting-started-pygame\lesson-1-2-game-window-colors
python starter\game.py
```

**Expected output (visual):** Full-window fill that gradually shifts hue/brightness as `r` cycles 0→255.

---

## Quick Drills

1. **Green pulse** — leave `r` alone; do `g = (g + 2) % 256` instead.
2. **Fast caster** — use `r = (r + 8) % 256`. Too wild? Dial it back.
3. **Sunset** — start at `(255, 100, 40)` and slowly decrease `r` (careful with wrap!).

---

## Practice Task

**Quest name:** Color Caster

1. Complete the `# TODO` lines in [starter/game.py](starter/game.py): `fill` + color nudge.
2. Run until you clearly see the color changing, then quit with X.
3. **Bonus:** Cycle two channels (e.g. `r` up and `b` down) for a richer sky.

**Self-mark:** Fill every frame? Color changes? Quits cleanly? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Window stays black / never changes color.

**Cause:** You forgot `screen.fill((r, g, b))`, or you never update `r`/`g`/`b`, or you update color **before** fill with values that stay at zero.

**Fix:** Fill **with the current** `(r, g, b)`, **then** nudge a channel, **then** `flip()`. Order matters for what you see this frame.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. What does `(0, 255, 0)` mean in Pygame?
   - **a)** Pure red
   - **b)** Pure green
   - **c)** Pure blue
   - **d)** Transparent

2. Why call `screen.fill` every frame?
   - **a)** To install Pygame
   - **b)** To paint the background color for this frame
   - **c)** To close the window
   - **d)** To create a new event

3. What does `r = (r + 1) % 256` do?
   - **a)** Deletes the window
   - **b)** Increases red by 1 and wraps back to 0 after 255
   - **c)** Sets FPS permanently to 256
   - **d)** Draws a rectangle

4. Valid range for each RGB channel is:
   - **a)** 0–100 only
   - **b)** 0–255
   - **c)** −1–1
   - **d)** Any string like `"blue"`

5. Where should color updates usually happen?
   - **a)** Only once before `pygame.init()`
   - **b)** Inside the game loop each frame
   - **c)** Inside `pip install`
   - **d)** Only after `pygame.quit()`

---

<details><summary>Click to reveal answers</summary>

1. **b)** Green is the middle channel at full strength.
2. **b)** Fill paints the background for the current frame.
3. **b)** `% 256` keeps the channel in 0–255 while cycling.
4. **b)** Each of R, G, B is an integer 0–255.
5. **b)** Changing color each frame is what makes the sky animate.

</details>

---

## What's Next

→ [Lesson 1.3: Shapes & Coordinates](../lesson-1-3-shapes-coordinates/README.md) — draw a box and sail it across the screen.

---

*You cast color. Next: give the world a moving hero square!*

[← Choose language](README.md)
