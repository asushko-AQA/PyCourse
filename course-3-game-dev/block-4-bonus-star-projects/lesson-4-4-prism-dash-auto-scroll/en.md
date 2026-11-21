# Lesson 4.4: Auto Scroll & Runner

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects · **~30–35 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 32
-->

---

## Title

**Level ★4 — Neon Cruiser**

---

## Explanation

Project **#2** in Block 4 is **Prism Dash** — our own auto-runner with **procedural neon shapes** (no copyrighted art).

In a runner the hero often stays near the left while the **level moves**:

| Piece | Idea |
|-------|------|
| Hero X | Fixed `PLAYER_X` (cube does not drift right) |
| World scroll | `world_x += SCROLL * dt` each frame |
| Draw tile | `screen_x = tile_world_x - int(world_x)` |

Think of `world_x` as “how many pixels the level has marched past you.”

---

### Step 1: Grow `world_x`

After `dt = clock.tick(60) / 1000`:

```python
world_x += SCROLL * dt
```

---

### Step 2: Scroll decor blocks

For each `"#"` in the pattern string:

```python
sx = i * TILE_W - int(world_x)
if -TILE_W < sx < WIDTH + TILE_W:
    block = pygame.Rect(sx, GROUND_Y - 56, TILE_W, 56)
    pygame.draw.rect(surface, (70, 120, 255), block, border_radius=4)
```

---

### Step 3: Run

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-4-prism-dash-auto-scroll
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Cube stays put; blue blocks glide left; `world_x` HUD rises.

---

## Code Example

**File: [solution/game.py](solution/game.py)** — scroll core:

```python
world_x += SCROLL * dt
sx = i * TILE_W - int(world_x)
```

---

## Code Execution

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-4-prism-dash-auto-scroll
python starter\game.py
```

**Expected output (visual):** Smooth endless skyline scroll.

---

## Quick Drills

1. **Sprint mode** — `SCROLL = 350`.
2. **Tall towers** — draw blocks `GROUND_Y - 90` tall.
3. **HUD** — print `int(world_x)` on screen (already in starter).

---

## Practice Task

**Quest name:** Neon Cruiser

1. Complete scroll TODOs in [starter/game.py](starter/game.py).
2. Decor blocks slide smoothly with no popping.
3. **Bonus stretch:** parallax stripes move at half speed (`world_x * 0.5`).

**Self-mark:** Cube X never changes? Blocks exit left and new ones enter right? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Blocks jitter or teleport.

**Cause:** Forgetting `int(world_x)` or mixing modulo wrong on both `i` and `world_x`.

**Fix:** Use plain `i * TILE_W - int(world_x)` like Lesson 4.2 pipe scroll.

---

## Quick Check

1. In an auto-runner, the cube usually…
   - **a)** Stays near a fixed X while the world scrolls
   - **b)** Drifts right off screen automatically
   - **c)** Only moves with the mouse
   - **d)** Replaces Flask templates

2. `world_x` tracks…
   - **a)** How far the level has scrolled
   - **b)** Pygame version number
   - **c)** Quiz score only
   - **d)** Turtle pen color

3. A tile at index `i` draws at screen X…
   - **a)** `i * TILE_W - int(world_x)`
   - **b)** `i + world_x` only
   - **c)** Always `0`
   - **d)** `random.randint` each frame

4. Multiply scroll by `dt` because…
   - **a)** Speed should be time-based, not frame-based
   - **b)** It disables pygame
   - **c)** Lessons require HTML
   - **d)** Spikes need Flask

5. Prism Dash art is…
   - **a)** Shapes drawn in code (no copyrighted assets)
   - **b)** Copied PNGs from a famous mobile game
   - **c)** Blender movie files
   - **d)** Markdown tables only

---

<details><summary>Click to reveal answers</summary>

1. **a)** Classic runner camera trick.
2. **a)** Distance counter for the level.
3. **a)** World position minus scroll.
4. **a)** Same `dt` lesson as Block 1.4.
5. **a)** Original procedural look.

</details>

---

## What's Next

→ [Lesson 4.5 — Jump, Gravity & Spin](../lesson-4-5-prism-dash-jump-rotate/README.md) — add jump, ground snap, and cube spin!

---

*Run in place, scroll the world.*

[← Choose language](README.md)