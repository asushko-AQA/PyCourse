# Lesson 4.9: Shard Stack Complete

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects · **~40–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 42
-->

---

## Title

**Level ★9 — Shard Stack Pro**

---

## Explanation

You have a **grid** (4.7) and **falling controls** (4.8). Finish the arcade loop:

| State | Player sees |
|-------|-------------|
| `start` | Title, session best, SPACE to play |
| `playing` | Fall, rotate, score HUD, next preview |
| `game_over` | Grid full — show score, SPACE → title |

**Rotate 90° clockwise** on offsets:

```python
def rotate_cells(cells):
    return [(c, -r) for r, c in cells]
```

If rotation hits a wall, nudge `piece_col` by ±1 (simple wall kick).

**Clear lines** — any row where **every** cell is filled is removed; rows above slide down.

```python
def clear_lines():
    kept = [row for row in grid if not all(row)]
    cleared = ROWS - len(kept)
    while len(kept) < ROWS:
        kept.insert(0, [0] * COLS)
    grid[:] = kept
    return cleared
```

**Score:** `cleared * 100 * level`. **Level:** rises every 10 total lines; `fall_interval()` gets shorter.

**Next shard:** pick `next_name` at spawn; draw a mini preview panel.

---

### Step 1: `lock_piece` pipeline

1. Paint piece colors into `grid`
2. `cleared = clear_lines()`
3. Update `score`, `level`
4. `spawn_piece()` or `GAME_OVER` if blocked at top

---

### Step 2: `try_rotate`

Build `rotated = rotate_cells(piece_cells)`; test `can_move`; optionally shift column.

---

### Step 3: Session `high_score`

On `game_over`, if `score > high_score`, save it; show on title screen.

---

### Step 4: Run

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-9-shard-stack-complete
python starter\game.py
```

**Expected output (visual):** Playable stacker with rotation, line flashes, speed-up.

---

## Code Example

**File: [solution/game.py](solution/game.py)** — line clear:

```python
cleared = clear_lines()
if cleared:
    score += cleared * 100 * level
```

---

## Code Execution

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-9-shard-stack-complete
python solution\game.py
```

**Expected output (visual):** Full game loop; next piece panel; game over when spawn blocked.

---

## Quick Drills

1. Clear two lines at once — score jump should feel big.
2. Add shape `"L"` to `SHAPES` + color.
3. Prove four rotations return to the same offsets (math in notebook).

---

## Practice Task

**Quest name:** Shard Stack Pro

1. Finish every TODO in [starter/game.py](starter/game.py).
2. Clear at least **one** line in a real play test.
3. **Bonus stretch:** gentle sound on line clear (optional `pygame.mixer`).

**Self-mark:** UP rotates without clipping? Lines vanish? Title shows best? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Lines clear but colors wrong.

**Cause:** Using `int` flags in grid then forgetting to store RGB tuples when locking.

**Fix:** Store the same color tuple you draw for the active piece.

---

## Quick Check

1. `rotate_cells` maps `(r, c)` to…
   - **a)** `(c, -r)` for 90° clockwise
   - **b)** `(r, c)` always
   - **c)** Flask route
   - **d)** Random.randint

2. A full row means…
   - **a)** `all(row)` is true for every cell non-empty
   - **b)** Row index is 19 only
   - **c)** Score is zero
   - **d)** No pygame display

3. Game over when…
   - **a)** New shard cannot `can_move` at spawn
   - **b)** Window width is 640
   - **c)** Student skips quiz
   - **d)** Turtle closes

4. `fall_interval()` should…
   - **a)** Shrink as `level` rises
   - **b)** Grow forever
   - **c)** Stay zero
   - **d)** Disable keyboard

5. Next ★ slot after 4.9 is…
   - **a)** Lessons 4.10–4.12 (Block 4 README)
   - **b)** Course 1 Lesson 0.1
   - **c)** Mandatory Block 5
   - **d)** Deprecated content

---

<details><summary>Click to reveal answers</summary>

1. **a)** Standard offset rotation.
2. **a)** Every cell filled.
3. **a)** Spawn collision.
4. **a)** Speed ramp fairness.
5. **a)** Planned ★ project #4.

</details>

---

## What's Next

→ [Lesson 4.10 — Tiles & Layout](../lesson-4-10-glyph-grove-tiles-layout/README.md) — ★ project **#4** **Glyph Grove** begins!  
→ [Block 4 index](../README.md) — you finished ★ project **#3**!  
→ Compare grid logic to your **Prism Dash** side-scroller!

---

*★ Shard Stack — project three, complete.*

[← Choose language](README.md)