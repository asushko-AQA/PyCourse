# Lesson 4.1: Gravity & Flap

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects · **~30–35 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 32
-->

---

## Title

**Level ★1 — Breeze Bird**

---

## Explanation

Welcome to **Block 4: Bonus ★ Star Projects** — optional arcade-style games **after** your main capstone.  
Project #1 is **Sky Hopper**: a flap game with **your own bird shape** (no copyrighted art).

| Force | Code idea |
|-------|-----------|
| Gravity | `vel_y += GRAVITY * dt` every frame |
| Flap | On `KEYDOWN` + SPACE: `vel_y = FLAP_STRENGTH` (negative = up) |
| Position | `bird_y += vel_y * dt` |

Flap is a **one-shot** impulse — use `KEYDOWN`, not `get_pressed`, so one tap = one kick.

---

### Step 1: Open starter/game.py

Bird + clouds already draw. Find the four `TODO` comments for flap and gravity.

---

### Step 2: Flap on SPACE

Inside the event loop:

```python
if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    vel_y = FLAP_STRENGTH
```

---

### Step 3: Apply gravity and move

After the event loop, each frame:

```python
vel_y += GRAVITY * dt
bird_y += vel_y * dt
```

---

### Step 4: Keep the bird on screen (practice bounds)

```python
if bird_y < bird_size:
    bird_y = bird_size
    vel_y = 0
if bird_y > HEIGHT - bird_size:
    bird_y = HEIGHT - bird_size
    vel_y = 0
```

In lesson 4.2, hitting the floor will end a run — for now we **bounce** softly so you can practice.

---

### Step 5: Run

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-1-sky-hopper-gravity-flap
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Bird bobs in a blue sky; SPACE flaps; `vel_y` HUD updates.

---

## Code Example

**File: [solution/game.py](solution/game.py)** — physics core:

```python
GRAVITY = 720
FLAP_STRENGTH = -280

vel_y += GRAVITY * dt
bird_y += vel_y * dt
# clamp top/bottom ...
bird.center = (BIRD_X, int(bird_y))
```

---

## Code Execution

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-1-sky-hopper-gravity-flap
python starter\game.py
```

**Expected output (visual):** Smooth flap arcs; gravity always pulls down between taps.

---

## Quick Drills

1. **Heavy world** — `GRAVITY = 1000`.
2. **Super flap** — `FLAP_STRENGTH = -360`.
3. **Wide bird** — `bird_size = 36`; adjust clamp math.

---

## Practice Task

**Quest name:** Breeze Bird

1. Complete all TODOs in [starter/game.py](starter/game.py).
2. Fly from floor to ceiling without getting stuck.
3. **Bonus stretch:** tint the sky darker as `vel_y` increases (optional).

**Self-mark:** SPACE flaps once per press? Bird falls when you let go? HUD shows changing `vel_y`? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Bird rockets off screen instantly.

**Cause:** Forgot `* dt` on velocity or position, or gravity sign wrong.

**Fix:** Gravity should be **positive** (down). Multiply both velocity and position updates by `dt`.

---

## Quick Check

1. What does `FLAP_STRENGTH = -280` mean?
   - **a)** Always move left
   - **b)** A strong upward kick on SPACE
   - **c)** Deletes pipes
   - **d)** Loads PNG art

2. Why use `KEYDOWN` for flap?
   - **a)** One press = one flap (not holding)
   - **b)** To draw rectangles only
   - **c)** To skip `dt`
   - **d)** Required for Turtle

3. Gravity each frame looks like…
   - **a)** `vel_y += GRAVITY * dt`
   - **b)** `vel_y = 0` forever
   - **c)** `screen.fill()` only
   - **d)** `random.randint` for score

4. In Pygame, increasing `y` moves the bird…
   - **a)** Up
   - **b)** Down
   - **c)** Into another file
   - **d)** Only on Linux

5. Block 4 lessons are…
   - **a)** Required before Block 1
   - **b)** Optional ★ bonus after Block 3
   - **c)** Flask homework only
   - **d)** Written in HTML

---

<details><summary>Click to reveal answers</summary>

1. **b)** Negative vertical velocity = up.
2. **a)** Impulse per tap.
3. **a)** Accumulate downward speed over time.
4. **b)** Y grows downward on screen.
5. **b)** Optional stretch projects.

</details>

---

## What's Next

→ [Lesson 4.2 — Scrolling Gateways](../lesson-4-2-scrolling-gateways/README.md) — add moving pipe gateways and score!

---

*Flap once, fall twice, learn forever.*

[← Choose language](README.md)