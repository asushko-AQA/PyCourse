# Lesson 3.1: Collision Detection

> **Course:** Game Development with Python · **Block:** Physics & Collisions (Final Project) · **~30–35 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 30
-->

---

## Title

**Level 9 — Coin Collector**

---

## Explanation

Games feel alive when things **touch**. In Pygame, every blit target has a **Rect**. Two Rects overlap when:

```python
if player.colliderect(coin):
    # they touch!
```

| Idea | Meaning |
|------|---------|
| `colliderect` | True if the rectangles overlap (AABB box test) |
| After a hit | Move the coin away — or you score every frame while overlapping |
| Same tools | Arrows = `get_pressed`, motion = `speed * dt`, HUD = `font.render` |

Today you build a tiny **coin collector**: touch the coin → `score += 1` → coin teleports.

---

### Step 1: Open starter/game.py

Open [starter/game.py](starter/game.py). Player motion, coin image, and score HUD are ready. Your job is the **collision** TODO.

---

### Step 2: Test the overlap

```python
if player.colliderect(coin):
    score += 1
```

Run once and notice: if you **stand still on the coin**, score explodes. Fix that next.

---

### Step 3: Relocate the coin after a hit

```python
if player.colliderect(coin):
    score += 1
    coin.center = (
        random.randint(40, WIDTH - 40),
        random.randint(40, HEIGHT - 120),
    )
```

Now each touch is one clean collect.

---

### Step 4: Run

```text
cd course-3-game-dev\block-3-physics-collisions-final-project\lesson-3-1-collision-detection
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Blue box moves; golden coin; `Coins: N` climbs one per touch; coin jumps after each collect.

---

## Code Example

**File: [solution/game.py](solution/game.py)**

```python
import pygame
import os
import random

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Collector")

clock = pygame.time.Clock()
running = True

HERE = os.path.dirname(os.path.abspath(__file__))

player = pygame.Rect(0, 0, 48, 48)
player.center = (WIDTH // 2, HEIGHT - 60)
speed = 280

coin_img = pygame.image.load(os.path.join(HERE, "coin.png")).convert_alpha()
coin = coin_img.get_rect()
coin.center = (random.randint(40, WIDTH - 40), random.randint(40, HEIGHT - 120))

score = 0
font = pygame.font.Font(None, 36)

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= int(speed * dt)
    if keys[pygame.K_RIGHT]:
        player.x += int(speed * dt)
    if keys[pygame.K_UP]:
        player.y -= int(speed * dt)
    if keys[pygame.K_DOWN]:
        player.y += int(speed * dt)

    player.clamp_ip(screen.get_rect())

    if player.colliderect(coin):
        score += 1
        coin.center = (
            random.randint(40, WIDTH - 40),
            random.randint(40, HEIGHT - 120),
        )

    screen.fill((18, 22, 40))
    pygame.draw.rect(screen, (80, 200, 255), player)
    screen.blit(coin_img, coin)
    score_surf = font.render(f"Coins: {score}", True, (255, 255, 255))
    screen.blit(score_surf, (16, 12))
    hint = font.render("Touch the coin!", True, (180, 190, 210))
    screen.blit(hint, (16, 48))

    pygame.display.flip()

pygame.quit()
```

---

## Code Execution

```text
cd course-3-game-dev\block-3-physics-collisions-final-project\lesson-3-1-collision-detection
python starter\game.py
```

**Expected output (visual):** Collect coins; score rises by 1 per touch; coin relocates.

---

## Quick Drills

1. **Debug print** — `print("got one!", score)` inside the hit branch (remove later).
2. **Faster player** — try `speed = 400`.
3. **Coin near edges** — tighten the `randint` ranges so the coin never hides under the HUD.

---

## Practice Task

**Quest name:** Coin Collector

1. Complete the TODO in [starter/game.py](starter/game.py): `colliderect` → add score → move coin.
2. Collect at least **5** coins in one run.
3. **Bonus:** Play a tiny terminal `print("bling!")` on each collect (sound comes in 3.3).

**Self-mark:** Coin moves after touch? Score +1 once per collect (not every frame)? Window still closes with X? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Score jumps by hundreds while you stand on the coin.

**Cause:** Overlap stays True every frame; you never move the coin (or move it on top of the player again).

**Fix:** After scoring, set a **new** `coin.center` far enough away. Optionally require the coin to leave before the next collect.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. What does `player.colliderect(coin)` return when they overlap?
   - **a)** A PNG file
   - **b)** `True`
   - **c)** Always `False`
   - **d)** The font size

2. Why move the coin after a successful collect?
   - **a)** To install Pygame again
   - **b)** So you do not score every frame while still overlapping
   - **c)** To delete `dt`
   - **d)** Because Rects cannot sit still

3. Continuous arrow movement should use…
   - **a)** Only `QUIT`
   - **b)** `get_pressed()` (held keys)
   - **c)** `mixer.Sound` only
   - **d)** A second window

4. Where does `coin.png` usually live in this lesson?
   - **a)** Next to `game.py` in `starter/` / `solution/`
   - **b)** Inside `pygame.init`
   - **c)** On a website only
   - **d)** In Course 1 Turtle

5. What is AABB-style collision here?
   - **a)** Exact pixel art matching
   - **b)** Axis-aligned rectangle overlap (`colliderect`)
   - **c)** 3D physics
   - **d)** Closing the window

---

<details><summary>Click to reveal answers</summary>

1. **b)** Overlap → True.
2. **b)** Relocate so one touch = one point.
3. **b)** Held arrows → get_pressed.
4. **a)** Asset beside the script (path via `HERE`).
5. **b)** Simple box vs box test.

</details>

---

## What's Next

→ [Lesson 3.2 — Catch the Falling Stars](../lesson-3-2-catch-the-falling-stars/README.md) — full mini-game capstone!

---

*Touched a coin? You’re ready for falling stars!*

[← Choose language](README.md)
