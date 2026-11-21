# Lesson 4.7: Grid & Cells

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects · **~30–35 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 32
-->

---

## Title

**Level ★7 — Crystal Well**

---

## Explanation

Project **#3** in Block 4 is **Shard Stack** — our own stack puzzle with **colored square shards** (no copyrighted tiles or names).

Course 1 taught **1D lists** (`inventory = ["sword", "potion"]`). A game board is a **2D list**: a list of rows, each row a list of columns.

```python
grid = [
    [0, 0, 0],
    [0, 0, 0],
    [1, 1, 0],
]
```

- Read: `grid[row][col]`
- `0` = empty cell; any other value = locked shard color or flag

Think of `row` as **how far down** on the screen (row 0 is the top).

---

### Step 1: Build the well

```python
COLS = 10
ROWS = 20
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
```

The inner `for _ in range(COLS)` makes **one row**. The outer loop repeats that **ROWS** times.

---

### Step 2: Cell → pixels

Each cell is a `CELL`×`CELL` square:

```python
x = BOARD_X + col * CELL
y = BOARD_Y + row * CELL
pygame.draw.rect(surface, color, (x, y, CELL - 1, CELL - 1), border_radius=4)
```

---

### Step 3: Shard as offsets

Instead of four separate variables, store a **piece** as offsets from an anchor:

```python
T = [(0, 1), (1, 0), (1, 1), (1, 2)]
anchor_row, anchor_col = 2, 4
for dr, dc in T:
    draw_cell(surface, anchor_row + dr, anchor_col + dc, PURPLE)
```

---

### Step 4: Run

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-7-shard-stack-grid-cells
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Empty well grid; when solved, demo locked cells + purple T.

---

## Code Example

**File: [solution/game.py](solution/game.py)** — grid creation + draw loop:

```python
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
for row in range(ROWS):
    for col in range(COLS):
        ...
```

---

## Code Execution

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-7-shard-stack-grid-cells
python solution\game.py
```

**Expected output (visual):** Framed 10×20 well, sample locked row, floating T shard.

---

## Quick Drills

1. Set `grid[19][5] = 1` — only bottom center lights up.
2. Draw grid lines in light gray for empty cells.
3. Print `len(grid)` and `len(grid[0])` on the HUD.

---

## Practice Task

**Quest name:** Crystal Well

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Well shows **empty** vs **locked** cells clearly.
3. **Bonus stretch:** click (optional) not required — tint alternate rows.

**Self-mark:** Is `grid[row][col]` used everywhere instead of flat math? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** `TypeError: 'NoneType' object is not subscriptable`.

**Cause:** Forgot to assign the 2D list (`grid = None`).

**Fix:** Run the list comprehension once at startup.

---

## Quick Check

1. `grid[3][7]` means…
   - **a)** Row 3, column 7
   - **b)** Flask template row
   - **c)** Turtle pen width
   - **d)** A PNG file path

2. A 2D list in this lesson is…
   - **a)** List of rows, each row a list of columns
   - **b)** Only dictionaries
   - **c)** HTML table tag
   - **d)** One giant string

3. `CELL` is…
   - **a)** Pixel width/height of one board square
   - **b)** An import from Flask
   - **c)** Volume knob
   - **d)** Quiz hash salt

4. Piece offsets are stored as…
   - **a)** `(row, col)` tuples relative to anchor
   - **b)** JPEG coordinates
   - **c)** Only `print()` statements
   - **d)** `def main():`

5. Next lesson adds…
   - **a)** Falling timer + arrow movement
   - **b)** Flask forms
   - **c)** Turtle snowflake only
   - **d)** pip uninstall pygame

---

<details><summary>Click to reveal answers</summary>

1. **a)** Row then column.
2. **a)** Rows contain column lists.
3. **a)** Grid spacing in pixels.
4. **a)** Offset list pattern.
5. **a)** Lesson 4.8 motion.

</details>

---

## What's Next

→ [Lesson 4.8 — Falling Pieces & Controls](../lesson-4-8-shard-stack-falling-pieces/README.md) — timer drop + `can_move`!

---

*Rows of lists — stacks of fun.*

[← Choose language](README.md)