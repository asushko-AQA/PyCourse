# Lesson 4.5: Jump, Gravity & Spin

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects · **~35–40 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 38
-->

---

## Title

**Level ★5 — Air Spin Cube**

---

## Explanation

An auto-runner feels flat until you can **jump**. Prism Dash uses the same vertical physics as Sky Hopper — but you only jump when **grounded**.

| Piece | Code idea |
|-------|-----------|
| Gravity | `vel_y += GRAVITY * dt` |
| Jump | `KEYDOWN` SPACE + `grounded` → `vel_y = JUMP_V` |
| Land | Snap `player_y` to `GROUND_Y` (or platform top in 4.6) |
| Spin | `angle += ROT_SPEED * dt` while **not** grounded |

Draw the cube on a small `Surface`, rotate with `pygame.transform.rotate`, then `blit` centered — that is the “Geometry” look without image files.

---

### Step 1: Jump gate

```python
if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and grounded:
    vel_y = JUMP_V
    grounded = False
```

---

### Step 2: Gravity + move

```python
vel_y += GRAVITY * dt
player_y += vel_y * dt
```

---

### Step 3: Ground snap

```python
def snap_ground() -> None:
    global player_y, vel_y, grounded
    grounded = False
    if player_y + CUBE_SIZE >= GROUND_Y - 1:
        player_y = GROUND_Y - CUBE_SIZE
        vel_y = 0
        grounded = True
```

---

### Step 4: Spin while airborne

```python
if grounded:
    angle = 0.0
else:
    angle = (angle + ROT_SPEED * dt) % 360
```

---

### Step 5: Run

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-5-prism-dash-jump-rotate
python starter\game.py
```

**Expected output (visual):** Neon cube hops along scrolling ground; spins mid-air; SPACE does nothing while airborne.

---

## Code Example

```python
tile = pygame.Surface((CUBE_SIZE, CUBE_SIZE), pygame.SRCALPHA)
pygame.draw.rect(tile, (255, 110, 210), tile.get_rect(), border_radius=6)
rotated = pygame.transform.rotate(tile, -angle)
surface.blit(rotated, rotated.get_rect(center=(PLAYER_X, center_y)))
```

---

## Code Execution

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-5-prism-dash-jump-rotate
python starter\game.py
```

**Expected output (visual):** Jump + spin demo with HUD showing grounded vs airborne.

---

## Quick Drills

1. **Moon jump** — `GRAVITY = 800`, `JUMP_V = -650`.
2. **No double jump** — confirm SPACE mid-air does nothing.
3. **45° snap** — land with `angle = 0` only (not diagonal).

---

## Practice Task

**Quest name:** Air Spin Cube

1. Finish all TODOs in [starter/game.py](starter/game.py).
2. Cube rotates only while airborne.
3. **Bonus stretch:** brief white flash on jump.

**Self-mark:** One jump per landing? Feet snap to ground without sinking? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Infinite jumping in mid-air.

**Cause:** Missing `and grounded` on SPACE, or `grounded` never set `False`.

**Fix:** Set `grounded = False` right when you jump; only set `True` in snap.

---

## Quick Check

1. Jump should fire when…
   - **a)** SPACE on KEYDOWN and `grounded`
   - **b)** SPACE held every frame in air
   - **c)** Mouse right-click only
   - **d)** Only on game over screen

2. `JUMP_V = -520` means…
   - **a)** Strong upward impulse (negative is up)
   - **b)** Scroll speed
   - **c)** Spike damage
   - **d)** Font size

3. Ground snap sets…
   - **a)** `player_y = GROUND_Y - CUBE_SIZE`
   - **b)** `world_x = 0` always
   - **c)** `pipes.clear()`
   - **d)** Flask debug mode

4. Rotation while airborne uses…
   - **a)** `pygame.transform.rotate`
   - **b)** `pip install` only
   - **c)** `render_template`
   - **d)** Turtle `forward`

5. Prism Dash lesson 4.5 still has…
   - **a)** No deadly spikes yet (those come in 4.6)
   - **b)** Full Tetris grid
   - **c)** Network multiplayer
   - **d)** No scrolling

---

<details><summary>Click to reveal answers</summary>

1. **a)** Ground-only jump.
2. **a)** Same sign convention as Sky Hopper.
3. **a)** Feet align with floor.
4. **a)** Spin the cube surface.
5. **a)** Spikes arrive next lesson.

</details>

---

## What's Next

→ [Lesson 4.6 — Prism Dash Complete](../lesson-4-6-prism-dash-complete/README.md) — spikes, progress bar, attempts, full game loop!

---

*Jump once, spin once, land crisp.*

[← Choose language](README.md)