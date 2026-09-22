# Lesson 2.2: Images & Sprites

> **Course:** Game Development with Python · **Block:** Player Controls & Animations · **~30–40 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 35
-->

---

## Title

**Level 6 — Sprite Summoner**

---

## Explanation

A **sprite** is a picture you draw on the game window — your hero, a coin, a star. In Pygame:

1. **Load** the image into a `Surface`
2. Track where it sits with a **`Rect`**
3. **Blit** (stamp) it onto the screen each frame

```python
player = pygame.image.load("player.png").convert_alpha()
player_rect = player.get_rect()
screen.blit(player, player_rect)
```

`.convert_alpha()` makes drawing faster and keeps PNG transparency.

**Path tip:** If you run from another folder, `"player.png"` may not be found. The starter uses `os.path` next to the script so load always works.

---

### Step 1: Confirm player.png is present

In [starter/](starter/) you should see `game.py` **and** `player.png`. Open [starter/game.py](starter/game.py).

---

### Step 2: Load the image once (before the loop)

```python
HERE = os.path.dirname(os.path.abspath(__file__))
player = pygame.image.load(os.path.join(HERE, "player.png")).convert_alpha()
player_rect = player.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT // 2)
```

Load **once** outside the loop — loading every frame is slow and wasteful.

---

### Step 3: Blit instead of draw.rect

After `screen.fill(...)`:

```python
screen.blit(player, player_rect)
```

Remove the temporary `draw.rect` stand-in.

---

### Step 4: Move the rect with keys (already sketched)

The starter already nudges `player_rect.x` / `.y` with arrows and `clamp_ip`. Keep that — only swap **how** you paint the hero.

---

### Step 5: Run

```text
cd course-3-game-dev\block-2-player-controls-animations\lesson-2-2-images-sprites
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Teal ship sprite instead of a plain square; arrows move it; stays on screen.

---

## Code Example

**File: [solution/game.py](solution/game.py)**

```python
import pygame
import os

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Summoner")

clock = pygame.time.Clock()
running = True

HERE = os.path.dirname(os.path.abspath(__file__))
player = pygame.image.load(os.path.join(HERE, "player.png")).convert_alpha()
player_rect = player.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT // 2)

speed = 250

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= int(speed * dt)
    if keys[pygame.K_RIGHT]:
        player_rect.x += int(speed * dt)
    if keys[pygame.K_UP]:
        player_rect.y -= int(speed * dt)
    if keys[pygame.K_DOWN]:
        player_rect.y += int(speed * dt)

    player_rect.clamp_ip(screen.get_rect())

    screen.fill((15, 18, 32))
    screen.blit(player, player_rect)
    pygame.display.flip()

pygame.quit()
```

---

## Code Execution

```text
cd course-3-game-dev\block-2-player-controls-animations\lesson-2-2-images-sprites
python starter\game.py
```

**Expected output (visual):** Sprite ship moves with arrows; no plain gold square once blit is wired.

---

## Quick Drills

1. **Bigger ship** — `pygame.transform.scale(player, (72, 72))` after load (rebuild `player_rect`).
2. **Mirror** — when moving left, blit a flipped copy.
3. **Decor** — blit a second tiny rect/surface in a corner as a “star”.

---

## Practice Task

**Quest name:** Sprite Summoner

1. Complete TODOs in [starter/game.py](starter/game.py): load `player.png`, blit it, remove the stand-in rect.
2. Confirm arrows still move the rect and `clamp_ip` works.
3. **Bonus:** Replace `player.png` with your own 48×48 (or scaled) art — keep the filename or update the path.

**Self-mark:** PNG visible? Transparent edges OK? Keys still work? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** `FileNotFoundError: No such file or directory: 'player.png'`

**Cause:** Python looks for the file relative to the **current working directory** (where you ran `python`), not always next to `game.py`.

**Fix:** Use the starter’s `HERE = os.path.dirname(...)` pattern, **or** `cd` into the folder that contains both `game.py` and `player.png` before running.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. What does `screen.blit(player, player_rect)` do?
   - **a)** Deletes the image file
   - **b)** Stamps the image onto the screen at the rect’s position
   - **c)** Installs Pygame
   - **d)** Closes the window

2. Why call `.convert_alpha()` after loading a PNG?
   - **a)** To make drawing faster and keep transparency
   - **b)** To uninstall Turtle
   - **c)** To create a venv
   - **d)** To flip the screen

3. Where should you load the image?
   - **a)** Every frame inside the loop
   - **b)** Once before the game loop
   - **c)** After `pygame.quit()`
   - **d)** Only in the README

4. What does `player.get_rect()` give you?
   - **a)** A Rect matching the image size (for position)
   - **b)** The RGB of one pixel
   - **c)** A new font
   - **d)** The delta time

5. `player_rect.clamp_ip(screen.get_rect())` …
   - **a)** Plays a sound
   - **b)** Keeps the sprite rect inside the window
   - **c)** Loads another PNG
   - **d)** Changes FPS to 1

---

<details><summary>Click to reveal answers</summary>

1. **b)** Blit copies the surface onto the display surface.
2. **a)** Convert prepares the surface for fast blits with alpha.
3. **b)** Load once; blit many times.
4. **a)** A Rect you can move and clamp.
5. **b)** Clamp keeps the hero on screen.

</details>

---

## What's Next

→ [Lesson 2.3: Score & Text Rendering](../lesson-2-3-score-text-rendering/README.md) — put a live score on the HUD with `font.render`.

---

*The ship appears. Next: write the score in lights!*

[← Choose language](README.md)
