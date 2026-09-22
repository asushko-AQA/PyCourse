# Lesson 2.1: Keyboard Events

> **Course:** Game Development with Python · **Block:** Player Controls & Animations · **~30–35 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 30
-->

---

## Title

**Level 5 — Key Captain**

---

## Explanation

Until now the box moved **by itself**. Real games wait for **you**.

Pygame offers two keyboard styles:

| Style | When to use | API |
|-------|-------------|-----|
| One-shot press | Menu confirm, jump once | `event.type == KEYDOWN` |
| **Held** keys | Walk / fly while holding | `pygame.key.get_pressed()` |

For a captain who keeps flying while the arrow is down, use **`get_pressed()`**:

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    x = x - speed * dt
```

`keys[...]` is `True` every frame the key is held. Combine with **`speed * dt`** so motion stays smooth (Lesson 1.4).

---

### Step 1: Open starter/game.py

Open [starter/game.py](starter/game.py). Window, `dt`, draw, and quit are ready. TODO: read keys and move `x` / `y`.

---

### Step 2: Read held keys each frame

After the event loop:

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    x = x - speed * dt
if keys[pygame.K_RIGHT]:
    x = x + speed * dt
if keys[pygame.K_UP]:
    y = y - speed * dt
if keys[pygame.K_DOWN]:
    y = y + speed * dt
```

Remember: **up** decreases `y` (origin is top-left!).

---

### Step 3: Keep the box on screen (clamp)

```python
x = max(0, min(x, WIDTH - box_w))
y = max(0, min(y, HEIGHT - box_h))
```

---

### Step 4: Run

```text
cd course-3-game-dev\block-2-player-controls-animations\lesson-2-1-keyboard-events
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Gold square in the center; arrow keys steer it; it stops at the edges. Quit with X.

---

### Step 5: Diagonal tip

Holding LEFT+UP at once moves diagonally — both `if`s run. No extra code needed!

---

## Code Example

**File: [solution/game.py](solution/game.py)**

```python
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Key Captain")

clock = pygame.time.Clock()
running = True

x = 295.0
y = 215.0
box_w = 50
box_h = 50
speed = 250

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x = x - speed * dt
    if keys[pygame.K_RIGHT]:
        x = x + speed * dt
    if keys[pygame.K_UP]:
        y = y - speed * dt
    if keys[pygame.K_DOWN]:
        y = y + speed * dt

    x = max(0, min(x, WIDTH - box_w))
    y = max(0, min(y, HEIGHT - box_h))

    screen.fill((20, 24, 40))
    pygame.draw.rect(screen, (255, 200, 50), (int(x), int(y), box_w, box_h))
    pygame.display.flip()

pygame.quit()
```

---

## Code Execution

```text
cd course-3-game-dev\block-2-player-controls-animations\lesson-2-1-keyboard-events
python starter\game.py
```

**Expected output (visual):** Controllable gold square; edges clamp; X closes the window.

---

## Quick Drills

1. **Turbo** — `speed = 400`. Still steerable?
2. **WASD twin** — also check `K_a` / `K_d` / `K_w` / `K_s`.
3. **Slow crawl** — `speed = 80` and feel the difference.

---

## Practice Task

**Quest name:** Key Captain

1. Complete TODOs in [starter/game.py](starter/game.py): `get_pressed` + four arrow directions.
2. Clamp so the square cannot leave the window.
3. **Bonus:** Change color while any arrow is held (e.g. brighter gold).

**Self-mark:** Arrows move the box? Hold keeps moving? Edges stop you? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** The box only twitches once when you tap an arrow — it does not keep moving.

**Cause:** You handled `KEYDOWN` in the event loop (one event per press) instead of **`get_pressed()`** every frame.

**Fix:** After events, call `keys = pygame.key.get_pressed()` and use `if keys[pygame.K_LEFT]:` each frame.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. Which call is best for **continuous** movement while a key is held?
   - **a)** Only `pygame.QUIT`
   - **b)** `pygame.key.get_pressed()`
   - **c)** `pip install keys`
   - **d)** `screen.fill(keys)`

2. What does `keys[pygame.K_UP]` mean when True?
   - **a)** The window closed
   - **b)** The up arrow is currently held down
   - **c)** Score increased
   - **d)** Pygame failed to install

3. Why multiply by `dt` when moving?
   - **a)** To close the window
   - **b)** So speed is pixels **per second**, smooth on any FPS
   - **c)** To load images
   - **d)** To change the caption

4. Increasing `y` moves the player…
   - **a)** Up
   - **b)** Down
   - **c)** Into the venv
   - **d)** Off the keyboard

5. What does clamp with `max` / `min` do here?
   - **a)** Installs fonts
   - **b)** Keeps `x`/`y` inside the window bounds
   - **c)** Creates a new surface
   - **d)** Deletes the game loop

---

<details><summary>Click to reveal answers</summary>

1. **b)** `get_pressed()` reports held keys every frame.
2. **b)** That flag is True while the up arrow is down.
3. **b)** `speed * dt` is frame-rate independent motion.
4. **b)** In Pygame, larger `y` is lower on the screen.
5. **b)** Clamp stops the box from leaving the playfield.

</details>

---

## What's Next

→ [Lesson 2.2: Images & Sprites](../lesson-2-2-images-sprites/README.md) — swap the square for a real sprite image.

---

*You have the stick. Next: give the captain a face!*

[← Choose language](README.md)
