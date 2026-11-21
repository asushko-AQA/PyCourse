# Lesson 4.10: Tiles & Layout

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects · **~30–35 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 32
-->

---

## Title

**Level ★10 — Garden Tiles**

---

## Explanation

Project **#4** in Block 4 is **Glyph Grove** — a **solitaire matching** puzzle with **our own glyph symbols** (Unicode shapes + colors, not real Mahjong art).

Until now you used the **keyboard** for games. Soon you will add the **mouse**. First, learn how one **tile** is just a Python **dict**:

```python
tile = {
    "id": 0,
    "kind": "★",
    "kind_index": 3,
    "row": 2,
    "col": 4,
    "layer": 1,
    "removed": False,
}
```

- `row` / `col` = place on the garden grid  
- `layer` = stacked height (higher draws on top)  
- `kind` = which glyph must match its pair

---

### Step 1: Fixed layout + shuffled pairs

```python
LAYOUT = [(0, 2, 0), (0, 2, 1), ...]  # (layer, row, col)
kinds = GLYPHS * 2
random.shuffle(kinds)
```

Every position gets exactly one tile; kinds come in **pairs** so the board can always be cleared.

---

### Step 2: Grid → pixels

```python
x = BOARD_X + col * TILE_W + layer * LAYER_DX
y = BOARD_Y + row * TILE_H + layer * LAYER_DY
```

The small `LAYER_DX` shift sells the 3D stack feeling.

---

### Step 3: Draw the glyph

```python
glyph = font_glyph.render(tile["kind"], True, (25, 28, 40))
surface.blit(glyph, (gx, gy))
```

`pygame.font.Font(None, 52)` uses a built-in font — no image files needed.

---

### Step 4: Run

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-10-glyph-grove-tiles-layout
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Layered tiles with colorful glyphs after TODOs are done.

---

## Code Example

**File: [solution/game.py](solution/game.py)** — build + draw loop:

```python
for i, (layer, row, col) in enumerate(LAYOUT):
    tiles.append({"kind": kinds[i], "layer": layer, "row": row, "col": col, ...})
for tile in tiles:
    draw_tile(screen, tile)
```

---

## Code Execution

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-10-glyph-grove-tiles-layout
python solution\game.py
```

**Expected output (visual):** 24 tiles in three layers; glyphs `◆ ● ▲ ★ ✚ ☘` in pairs (shuffled).

---

## Quick Drills

1. Change `GLYPHS[0]` to your favorite symbol — does the color map still match?
2. Print `len(LAYOUT)` — why must it be even?
3. Set `LAYER_DX = 0` — does the stack look flat?

---

## Practice Task

**Quest name:** Garden Tiles

1. Finish all TODOs in [starter/game.py](starter/game.py).
2. Every layout slot shows a glyph centered in its rectangle.
3. **Bonus:** sort `tiles` by `layer` before drawing so low tiles never cover high ones wrongly.

**Self-mark:** Do you see three visible layers? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Screen is empty after `build_tiles`.

**Cause:** `build_tiles` still returns `[]` or `grid is None` pattern carried over.

**Fix:** Zip `LAYOUT` with shuffled `kinds`; append one dict per slot.

---

## Quick Check

1. Each tile stores its spot as…
   - **a)** `row`, `col`, and `layer` keys
   - **b)** A JPG filename only
   - **c)** Flask secret key
   - **d)** Turtle degrees

2. `GLYPHS * 2` before shuffle means…
   - **a)** Every kind appears twice (pairs)
   - **b)** The window is 2× wide
   - **c)** pygame quits early
   - **d)** Keys are disabled

3. `font_glyph.render` returns…
   - **a)** A `Surface` you can `blit`
   - **b)** An HTTP response
   - **c)** A syntax error always
   - **d)** A CSV file

4. Higher `layer` tiles should draw…
   - **a)** After lower layers (on top)
   - **b)** Before the display init
   - **c)** Only on Sundays
   - **d)** Without colors

5. Lesson 4.11 adds…
   - **a)** Mouse picking + free tile rule
   - **b)** Flask forms only
   - **c)** Removing pygame
   - **d)** Turtle snowflakes

---

<details><summary>Click to reveal answers</summary>

1. **a)** Grid coordinates in the dict.
2. **a)** Pair generation.
3. **a)** Text bitmap surface.
4. **a)** Paint order matters.
5. **a)** Mouse matching next.

</details>

---

## What's Next

→ [Lesson 4.11 — Mouse Pick & Matching](../lesson-4-11-glyph-grove-mouse-matching/README.md) — `MOUSEBUTTONDOWN` and the **free tile** rule!

---

*Glyphs you drew — no stolen art.*

[← Choose language](README.md)