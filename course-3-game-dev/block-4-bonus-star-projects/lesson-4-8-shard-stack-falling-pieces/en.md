# Lesson 4.8: Falling Pieces & Controls

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects · **~35–40 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 36
-->

---

## Title

**Level ★8 — Drift Shard**

---

## Explanation

Lesson 4.7 drew a static well. Now the **shard moves**.

| Piece | Idea |
|-------|------|
| Anchor | `piece_row`, `piece_col` — top-left reference cell |
| Shape | `PIECE_OFFSETS` list of `(dr, dc)` |
| Gravity timer | `fall_timer += dt`; every `FALL_INTERVAL`, try down |
| Controls | `KEYDOWN` arrows — one nudge per press |

```python
def can_move(dr, dc):
    for pr, pc in PIECE_OFFSETS:
        r = piece_row + pr + dr
        c = piece_col + pc + dc
        if c < 0 or c >= COLS or r >= ROWS:
            return False
        if r >= 0 and grid[r][c]:
            return False
    return True
```

If down is blocked → **`lock_piece()`** copies colors into `grid` and respawns at the top.

---

### Step 1: `try_move`

```python
if can_move(dr, dc):
    piece_row += dr
    piece_col += dc
    return True
return False
```

---

### Step 2: Timer drop

```python
fall_timer += dt
if fall_timer >= FALL_INTERVAL:
    fall_timer = 0.0
    if not try_move(1, 0):
        lock_piece()
```

---

### Step 3: Soft drop key

On `KEYDOWN` `K_DOWN`, call `try_move(1, 0)` or `lock_piece()` immediately — same as one gravity tick.

---

### Step 4: Run

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-8-shard-stack-falling-pieces
python starter\game.py
```

**Expected output (visual):** Purple T falls, slides left/right, locks when it lands.

---

## Code Example

**File: [solution/game.py](solution/game.py)**:

```python
if not try_move(1, 0):
    lock_piece()
```

---

## Code Execution

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-8-shard-stack-falling-pieces
python solution\game.py
```

**Expected output (visual):** Continuous fall + keyboard steering; stacks build on the floor.

---

## Quick Drills

1. Hold DOWN vs tap — why use `KEYDOWN` not `get_pressed` for soft drop here?
2. Block off column 0 — can you still move right?
3. Log `can_move(1, 0)` when shard hovers above a stack.

---

## Practice Task

**Quest name:** Drift Shard

1. Wire all TODOs in [starter/game.py](starter/game.py).
2. Piece never leaves the well sideways.
3. **Bonus stretch:** flash locked cells white for 0.1s on lock.

**Self-mark:** Timer drop works without holding keys? Locks at bottom? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Shard falls through the floor.

**Cause:** `r >= ROWS` check missing, or `lock_piece` never runs.

**Fix:** `r >= ROWS` should return **blocked** in `can_move`; call `lock_piece()` when down fails.

---

## Quick Check

1. `FALL_INTERVAL` controls…
   - **a)** Seconds between automatic down steps
   - **b)** Flask port number
   - **c)** Sprite file size
   - **d)** Quiz XP

2. `can_move(0, -1)` tests…
   - **a)** Left move for every offset cell
   - **b)** Email validation
   - **c)** Only the anchor cell
   - **d)** `pip install`

3. When down is blocked you should…
   - **a)** Call `lock_piece()` then respawn
   - **b)** Delete `grid`
   - **c)** Quit pygame instantly
   - **d)** Ignore and clip through

4. Locked cells live in…
   - **a)** The 2D `grid` list
   - **b)** A `.png` file only
   - **c)** Jinja template
   - **d)** Turtle window

5. Lesson 4.9 adds…
   - **a)** Rotation, line clear, score, game states
   - **b)** Only Flask static files
   - **c)** Removing the grid
   - **d)** Mahjong matching

---

<details><summary>Click to reveal answers</summary>

1. **a)** Auto-drop cadence.
2. **a)** All shard cells must fit.
3. **a)** Lock then new piece.
4. **a)** Grid memory.
5. **a)** Full Shard Stack rules.

</details>

---

## What's Next

→ [Lesson 4.9 — Shard Stack Complete](../lesson-4-9-shard-stack-complete/README.md) — rotate, clear lines, score, title screen!

---

*Fall steady, move wisely.*

[← Choose language](README.md)