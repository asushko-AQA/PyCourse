# Lesson 5.1: Grid & Segments

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~30–35 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 33
-->

---

## Title

**Level ★13 — Neon Trail**

---

## Explanation

Block 5’s first ★ game is **Glow Worm** — a friendly **grid trail** made of **neon circles** (our own look; not a clone of any classic tile set).

You already know **lists** from Course 1. Here the worm’s body is one list:

```python
segments = [(8, 8), (7, 8), (6, 8)]  # head first — each item is (col, row)
```

- **`col`** counts sideways (0 = left edge of the board).
- **`row`** counts downward (0 = top).
- **`direction`** is a **tuple** `(dc, dr)` — how many cells to move per step.
  - Right = `(1, 0)`, left = `(-1, 0)`, up = `(0, -1)`, down = `(0, 1)`.

**Why a timer?** Arrow keys should **pick a direction**, but the worm should **slide one cell** only every `MOVE_INTERVAL` seconds — not 60 jumps per second.

**No U-turn:** If you’re moving right, pressing left immediately would crash into your neck. Queue `pending_dir` and refuse the opposite direction with `is_opposite`.

---

### Step 1: Board constants

```python
COLS = 20
ROWS = 16
CELL = 26
BOARD_X = 36
BOARD_Y = 48
MOVE_INTERVAL = 0.2
```

`draw_cell_grid` loops all cells and paints dark squares inside a rounded frame.

---

### Step 2: Glowing segments

`draw_glow_segment` draws **two circles** — a big soft outer ring and a bright inner disk. The **head** uses mint green; the **body** uses sky blue.

```python
for i, (col, row) in enumerate(segments):
    draw_glow_segment(screen, col, row, is_head=(i == 0))
```

---

### Step 3: One grid step

In `step_worm`:

1. Copy `pending_dir` into `direction`.
2. Read head `(hc, hr) = segments[0]`.
3. `new_head = (hc + dc, hr + dr)`.
4. **Lesson 5.1 only:** if `new_head` is outside the board, **return** (no move yet — game over comes in 5.2).
5. Slide: `segments = [new_head] + segments[:-1]` — new head, drop old tail.

---

### Step 4: Input + timer in the loop

```python
move_timer += dt
if move_timer >= MOVE_INTERVAL:
    move_timer = 0.0
    step_worm()
```

Arrow keys update `pending_dir` when the new direction is **not** opposite to `direction`.

---

### Step 5: Run

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-1-glow-worm-grid-segments
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Dark grid; mint head and blue tail creep right when you finish the TODOs. HUD may show direction + head cell.

---

## Code Example

**File: [solution/game.py](solution/game.py)** — head slide + timer tick:

```python
def step_worm() -> None:
    global segments, direction
    direction = pending_dir
    hc, hr = segments[0]
    dc, dr = direction
    new_head = (hc + dc, hr + dr)
    if new_head[0] < 0 or new_head[0] >= COLS or new_head[1] < 0 or new_head[1] >= ROWS:
        return
    segments = [new_head] + segments[:-1]
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-1-glow-worm-grid-segments
python solution\game.py
```

**Expected output (visual):** Worm glides on the grid; arrows change course; walls block the step in 5.1.

---

## Quick Drills

1. Change starting `segments` to length 5 — still one head?
2. Set `pending_dir` without calling `step_worm` — head frozen until timer fires?
3. Draw a tiny white dot at the center of each cell for debugging coordinates.

---

## Practice Task

**Quest name:** Neon Trail

1. Finish TODOs in [starter/game.py](starter/game.py): init `segments`, arrows, `move_timer`, and `step_worm`.
2. Worm moves **on the timer**, not every frame.
3. **U-turn blocked** while moving horizontally or vertically.
4. **Bonus stretch:** tiny “eyes” on the head like the solution.

**Self-mark:** Does `segments[0]` always lead, and does the tail follow one cell behind? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Worm zips at lightning speed or stutters.

**Cause:** Calling `step_worm()` every frame instead of when `move_timer >= MOVE_INTERVAL`.

**Fix:** Accumulate `dt` in `move_timer`; reset timer after one step.

**Problem:** Pressing opposite arrow instantly kills the run (later lessons).

**Cause:** Updating `direction` directly without `is_opposite` check.

**Fix:** Only change `pending_dir` when `not is_opposite(new_dir, direction)`.

---

## Quick Check

1. `segments[0]` is…
   - **a)** The worm’s head cell `(col, row)`
   - **b)** The food position only
   - **c)** A Flask route name
   - **d)** Turtle pen color

2. `(1, 0)` as `direction` means…
   - **a)** Move one column right per step
   - **b)** Move one row down
   - **c)** Draw a circle radius 1
   - **d)** Import pygame twice

3. `MOVE_INTERVAL` controls…
   - **a)** Seconds between grid steps
   - **b)** Window width in pixels
   - **c)** Number of food items
   - **d)** High score storage

4. Why `pending_dir`?
   - **a)** Queue a turn between timer ticks; block 180° flips
   - **b)** Store PNG filenames
   - **c)** Replace `pygame.QUIT`
   - **d)** Only for macOS paths

5. Next lesson adds…
   - **a)** Food spawn, growth, wall/self crash
   - **b)** HTML templates
   - **c)** Turtle snowflake gallery
   - **d)** pip uninstall flask

---

<details><summary>Click to reveal answers</summary>

1. **a)** Head is index 0.
2. **a)** `dc=1`, `dr=0` → right.
3. **a)** Timer-based grid motion.
4. **a)** Safe queued turns.
5. **a)** Lesson 5.2 eating and collisions.

</details>

---

## What's Next

→ [Lesson 5.2 — Food, Growth & Collisions](../lesson-5-2-glow-worm-food-growth/README.md) — spark food and **grow without popping the tail**!

---

*One list, many neon links.*

[← Choose language](README.md)