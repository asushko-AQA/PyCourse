# Lesson 4.3: Sky Hopper Complete

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects · **~40–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 42
-->

---

## Title

**Level ★3 — Sky Hopper Pro**

---

## Explanation

You built **physics** (4.1) and **gateways** (4.2). Now wire **game states** like Lesson 2.4:

| State | Player sees |
|-------|-------------|
| `start` | Title, best score, SPACE to begin |
| `playing` | Flap, scroll, score |
| `game_over` | Final score, best, SPACE → title |

On crash, update **`high_score`** (session memory — same idea as Lesson 3.3).  
**Difficulty ramp:** `scroll_speed = BASE_SCROLL + score * 8` so later gateways feel faster.

---

### Step 1: `start_round()` and `crash()`

Reset `score`, bird position, `pipes`, and `scroll_speed`. Set `state = PLAYING`.  
In `crash()`, compare `score` to `high_score`, then `state = GAME_OVER`.

---

### Step 2: Event wiring

```python
if state == START and event.key in (pygame.K_SPACE, pygame.K_RETURN):
    start_round()
elif state == PLAYING and event.key == pygame.K_SPACE:
    vel_y = FLAP_STRENGTH
elif state == GAME_OVER and event.key in (pygame.K_SPACE, pygame.K_RETURN):
    state = START
```

---

### Step 3: Playing loop

Copy your working pipe logic from 4.2, but call `crash()` instead of `crashed = True`.  
Only simulate physics when `state == PLAYING`.

---

### Step 4: Run

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-3-sky-hopper-complete
python starter\game.py
```

**Expected output (visual):** Full Sky Hopper loop you can show friends.

---

## Code Example

```python
scroll_speed = BASE_SCROLL + score * 8
for pipe in pipes:
    pipe["x"] -= int(scroll_speed * dt)

if score > high_score:
    high_score = score  # inside crash() when round ends
```

---

## Code Execution

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-3-sky-hopper-complete
python starter\game.py
```

**Expected output (visual):** Title → run → game over → title; best score tracks across rounds.

---

## Quick Drills

1. Add a silly subtitle on the title screen.
2. Cap `scroll_speed` at 300.
3. Flash background red for 0.2s on crash (timer variable).

---

## Practice Task

**Quest name:** Sky Hopper Pro

1. Complete all TODOs in [starter/game.py](starter/game.py).
2. Beat your **high score** twice in one sitting.
3. **Bonus stretch:** save `high_score` to `sky_hopper_best.txt` (optional).

**Self-mark:** Three states work? Best updates on game over? Speed HUD rises with score? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Game starts in PLAYING or never leaves title.

**Cause:** `state` not updated in `KEYDOWN`, or physics runs on every state.

**Fix:** Guard the physics block with `elif state == PLAYING:` only.

---

## Quick Check

1. When do we update `high_score`?
   - **a)** Every frame on title
   - **b)** When a round ends and score beats best
   - **c)** On import pygame
   - **d)** Never in bonus block

2. Difficulty ramp here means…
   - **a)** Gateways scroll faster as score grows
   - **b)** Window shrinks to zero
   - **c)** Removing `dt`
   - **d)** Switching to Flask

3. After game over, SPACE should…
   - **a)** Return to title (`START`)
   - **b)** Quit Python instantly
   - **c)** Delete pipes list permanently from disk
   - **d)** Open a browser

4. Sky Hopper art is…
   - **a)** Procedural shapes we drew in code
   - **b)** Copied commercial sprites
   - **c)** Only SVG from the internet
   - **d)** Mandatory 3D model

5. Next ★ project in Block 4 will use lessons…
   - **a)** 4.4 – 4.6
   - **b)** 5.1 – 5.3
   - **c)** 1.1 – 1.3
   - **d)** 99.1 – 99.9

---

<details><summary>Click to reveal answers</summary>

1. **b)** End of round comparison.
2. **a)** Faster scroll with score.
3. **a)** Back to title to replay.
4. **a)** Our own drawn shapes.
5. **a)** Next numbered slot per block README.

</details>

---

## What's Next

→ [Block 4 index](../README.md) — you finished ★ project **#1**!  
→ Future lessons **4.4–4.6** will start the next bonus game.  
→ Show **Sky Hopper** to someone who played your Catch the Falling Stars capstone!

---

*★ Sky Hopper — project one, complete.*

[← Choose language](README.md)