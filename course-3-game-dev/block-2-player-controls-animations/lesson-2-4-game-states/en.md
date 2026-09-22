# Lesson 2.4: Game States

> **Course:** Game Development with Python · **Block:** Player Controls & Animations · **~35–40 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 35
-->

---

## Title

**Level 8 — Stage Director**

---

## Explanation

A real game is not one endless loop of “always playing.” It has **scenes**:

| State | What the player sees | Typical input |
|-------|----------------------|---------------|
| `start` | Title + “Press SPACE” | SPACE → begin |
| `playing` | Move, score, timer | Arrows (held) |
| `game_over` | Final score + restart hint | SPACE → title |

One variable steers the show:

```python
state = "start"  # or START / PLAYING / GAME_OVER constants
```

Each frame: handle events → update **only if playing** → draw the screen that matches `state`.

**Menus love `KEYDOWN`.** Continuous motion still uses `get_pressed()`. Do not mix them up!

This lesson uses a short **15-second** timer so you can reach Game Over quickly while testing.

---

### Step 1: Open starter/game.py

Open [starter/game.py](starter/game.py). Drawing for all three screens is sketched. TODOs: start in `START`, wire SPACE, switch to `GAME_OVER` when time is up.

---

### Step 2: Begin on the title screen

```python
state = START
```

(Not `PLAYING` — that was only a temporary default in the starter.)

---

### Step 3: SPACE changes state

Inside the event loop, on `KEYDOWN`:

```python
if state == START and event.key in (pygame.K_SPACE, pygame.K_RETURN):
    state = PLAYING
    score = 0.0
    play_time = 0.0
    x, y = 295.0, 215.0
elif state == GAME_OVER and event.key in (pygame.K_SPACE, pygame.K_RETURN):
    state = START
```

Resetting score / time / position makes every round fair.

---

### Step 4: Time out → game over

In the `PLAYING` branch:

```python
if play_time >= TIME_LIMIT:
    state = GAME_OVER
```

---

### Step 5: Run the full loop

```text
cd course-3-game-dev\block-2-player-controls-animations\lesson-2-4-game-states
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Title → SPACE → play with score + countdown → after ~15s Game Over → SPACE → title again.

---

## Code Example

**File: [solution/game.py](solution/game.py)**

```python
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stage Director")

clock = pygame.time.Clock()
running = True

font_big = pygame.font.Font(None, 64)
font_small = pygame.font.Font(None, 32)

START = "start"
PLAYING = "playing"
GAME_OVER = "game_over"

state = START

x = 295.0
y = 215.0
box_w = 50
box_h = 50
speed = 250
score = 0.0
play_time = 0.0
TIME_LIMIT = 15.0

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if state == START and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                state = PLAYING
                score = 0.0
                play_time = 0.0
                x, y = 295.0, 215.0
            elif state == GAME_OVER and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                state = START

    screen.fill((12, 14, 28))

    if state == START:
        title = font_big.render("Key Captain", True, (255, 220, 80))
        hint = font_small.render("Press SPACE to start", True, (200, 200, 220))
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30)))

    elif state == PLAYING:
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

        play_time = play_time + dt
        score = play_time * 10

        if play_time >= TIME_LIMIT:
            state = GAME_OVER

        pygame.draw.rect(screen, (255, 200, 50), (int(x), int(y), box_w, box_h))
        score_surf = font_small.render(f"Score: {int(score)}", True, (255, 255, 255))
        screen.blit(score_surf, (16, 12))
        time_left = max(0, TIME_LIMIT - play_time)
        timer_surf = font_small.render(f"Time: {time_left:.1f}", True, (180, 220, 255))
        screen.blit(timer_surf, (16, 48))

    elif state == GAME_OVER:
        over = font_big.render("Game Over", True, (255, 100, 100))
        final = font_small.render(f"Final score: {int(score)}", True, (255, 255, 255))
        hint = font_small.render("Press SPACE for title", True, (200, 200, 220))
        screen.blit(over, over.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50)))
        screen.blit(final, final.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10)))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50)))

    pygame.display.flip()

pygame.quit()
```

---

## Code Execution

```text
cd course-3-game-dev\block-2-player-controls-animations\lesson-2-4-game-states
python starter\game.py
```

**Expected output (visual):** Full state machine — title, play, game over, return to title.

---

## Quick Drills

1. **Longer round** — `TIME_LIMIT = 30`.
2. **Flavor text** — if `score < 20` on Game Over, blit “Keep practicing!”.
3. **ESC quit** — on Start, `K_ESCAPE` sets `running = False`.

---

## Practice Task

**Quest name:** Stage Director

1. Complete TODOs in [starter/game.py](starter/game.py): `state = START`, SPACE transitions, timeout → `GAME_OVER`.
2. Play one full loop: title → play → over → title.
3. **Bonus:** From Game Over, SPACE goes straight to `PLAYING` (skip title) — or keep title; your call, document it in a comment.

**Self-mark:** All three screens? SPACE works both ways? Timer ends the round? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Pressing SPACE during play pauses or flickers menus, or you skip straight past the title.

**Cause:** You used `get_pressed()[K_SPACE]` for menus (True for many frames) or forgot to reset `state` / left starter stuck on `PLAYING`.

**Fix:** Menu confirms → **`KEYDOWN` only**. Continuous move → `get_pressed`. Set initial `state = START`. Reset score/time when entering `PLAYING`.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. Why keep a `state` variable?
   - **a)** To install fonts
   - **b)** So one program can show different screens / behaviors
   - **c)** To delete `dt`
   - **d)** To replace Python

2. Best input style for “Press SPACE to start”?
   - **a)** `get_pressed` every frame without care
   - **b)** `KEYDOWN` event (one-shot)
   - **c)** Only mouse required
   - **d)** `pip install space`

3. Why reset `score` and `play_time` when entering PLAYING?
   - **a)** So each round starts fresh
   - **b)** Because Pygame forbids old variables
   - **c)** To close the window
   - **d)** To load PNGs

4. What should happen when `play_time >= TIME_LIMIT`?
   - **a)** Install Turtle
   - **b)** Switch `state` to game over
   - **c)** Delete the font
   - **d)** Freeze forever with no UI

5. Arrow movement during PLAYING should use…
   - **a)** Only `QUIT`
   - **b)** `get_pressed()` for held keys
   - **c)** `render` without blit
   - **d)** A second `pygame.init()`

---

<details><summary>Click to reveal answers</summary>

1. **b)** States let you stage title, play, and game over cleanly.
2. **b)** One-shot KEYDOWN avoids repeating the transition every frame.
3. **a)** Fair, repeatable rounds.
4. **b)** Time up → game over screen.
5. **b)** Held arrows still use get_pressed.

</details>

---

## What's Next

→ [Block 2 index](../README.md) — tick the Block 2 readiness checklist!  
→ **Block 3 (planned):** collisions, **Catch the Falling Stars**, polish.

---

*Curtain call for Block 2 — you directed the whole show!*

[← Choose language](README.md)
