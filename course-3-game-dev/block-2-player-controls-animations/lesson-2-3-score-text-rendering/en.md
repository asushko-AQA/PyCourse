# Lesson 2.3: Score & Text Rendering

> **Course:** Game Development with Python · **Block:** Player Controls & Animations · **~30–35 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 30
-->

---

## Title

**Level 7 — Score Scribbler**

---

## Explanation

Games need a **HUD** (heads-up display) — score, lives, timer. In Pygame, text is just another **Surface**:

```python
font = pygame.font.Font(None, 36)  # None = default font
score_surf = font.render(f"Score: {int(score)}", True, (255, 255, 255))
screen.blit(score_surf, (16, 12))
```

| Piece | Meaning |
|-------|---------|
| `Font(None, 36)` | Default font, height about 36 px |
| `render(text, True, color)` | Build a Surface; `True` = smooth edges |
| `blit(..., (x, y))` | Stamp text at top-left of that Surface |

Rebuild the text Surface when the number changes (each frame is fine for one line of HUD).

This lesson’s practice: **hold RIGHT** to earn points (`score += rate * dt`) so you see the counter climb.

---

### Step 1: Open starter/game.py

Open [starter/game.py](starter/game.py). Movement and optional sprite load are ready. TODOs: create **Font**, **render** + **blit** the score.

---

### Step 2: Create a Font once

Before the loop:

```python
font = pygame.font.Font(None, 36)
```

---

### Step 3: Render and blit each frame

After drawing the player, before `flip`:

```python
score_surf = font.render(f"Score: {int(score)}", True, (255, 255, 255))
screen.blit(score_surf, (16, 12))
```

Use `int(score)` so you do not show ugly floats like `12.38471`.

---

### Step 4: Earn points (already in starter)

Holding RIGHT adds `score_rate * dt`. You only need to **show** the number.

---

### Step 5: Run

```text
cd course-3-game-dev\block-2-player-controls-animations\lesson-2-3-score-text-rendering
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Player moves; top-left white `Score: N` climbs while you hold RIGHT.

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
pygame.display.set_caption("Score Scribbler")

clock = pygame.time.Clock()
running = True

HERE = os.path.dirname(os.path.abspath(__file__))
player_rect = pygame.Rect(0, 0, 48, 48)
player_rect.center = (WIDTH // 2, HEIGHT // 2)
player_img = None
sprite_path = os.path.join(HERE, "player.png")
if os.path.isfile(sprite_path):
    player_img = pygame.image.load(sprite_path).convert_alpha()
    player_rect = player_img.get_rect(center=player_rect.center)

speed = 250
score = 0.0
score_rate = 10

font = pygame.font.Font(None, 36)

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
        score = score + score_rate * dt
    if keys[pygame.K_UP]:
        player_rect.y -= int(speed * dt)
    if keys[pygame.K_DOWN]:
        player_rect.y += int(speed * dt)

    player_rect.clamp_ip(screen.get_rect())

    screen.fill((18, 22, 38))
    if player_img is not None:
        screen.blit(player_img, player_rect)
    else:
        pygame.draw.rect(screen, (255, 200, 50), player_rect)

    score_surf = font.render(f"Score: {int(score)}", True, (255, 255, 255))
    screen.blit(score_surf, (16, 12))
    pygame.display.flip()

pygame.quit()
```

---

## Code Execution

```text
cd course-3-game-dev\block-2-player-controls-animations\lesson-2-3-score-text-rendering
python starter\game.py
```

**Expected output (visual):** HUD score updates while holding RIGHT; X quits.

---

## Quick Drills

1. **Neon HUD** — render with `(80, 255, 120)`.
2. **Second line** — blit `f"Rate: {score_rate}"` at `(16, 48)`.
3. **Reset** — on `KEYDOWN` for `K_r`, set `score = 0`.

---

## Practice Task

**Quest name:** Score Scribbler

1. Complete TODOs in [starter/game.py](starter/game.py): create `font`, render + blit `Score: …`.
2. Confirm the number rises when holding RIGHT.
3. **Bonus:** Show score centered at the top (`score_surf.get_rect(midtop=(WIDTH // 2, 12))`).

**Self-mark:** Text visible? Updates live? Still can move? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** You call `font.render(...)` but never see text — only the player.

**Cause:** You forgot to **`blit`** the returned Surface, or you blit **before** `fill` (fill paints over it), or the color matches the background.

**Fix:** After `fill` and player draw: `screen.blit(score_surf, (16, 12))`, then `flip`. Use a bright color like white.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. What does `font.render(...)` return?
   - **a)** An integer score
   - **b)** A Surface you can blit
   - **c)** A new display window
   - **d)** A keyboard event

2. Why use `Font(None, 36)`?
   - **a)** To delete all fonts
   - **b)** Default system font at about size 36
   - **c)** To install Pygame
   - **d)** To set FPS

3. Why show `int(score)` in the string?
   - **a)** Floats cannot be added
   - **b)** Clean whole-number HUD instead of long decimals
   - **c)** Pygame forbids f-strings
   - **d)** It closes the window

4. When should you create the Font object?
   - **a)** Once before the loop (typical)
   - **b)** Only after `quit`
   - **c)** Inside `pip`
   - **d)** Never — text draws itself

5. Text still invisible after render — first check:
   - **a)** Did you `blit` the surface after `fill`?
   - **b)** Did you uninstall Python?
   - **c)** Did you delete `dt`?
   - **d)** Did you rename the course?

---

<details><summary>Click to reveal answers</summary>

1. **b)** `render` builds a Surface with the glyphs painted on it.
2. **b)** `None` picks the default font; `36` is the size.
3. **b)** Keep score as float for math; display a neat integer.
4. **a)** Create once; render/blit as needed each frame.
5. **a)** Render alone does not draw — blit does.

</details>

---

## What's Next

→ [Lesson 2.4: Game States](../lesson-2-4-game-states/README.md) — title screen, playing, and game over.

---

*The score sings. Next: direct the whole stage!*

[← Choose language](README.md)
