# Lesson 4.11: Mouse Pick & Matching

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects · **~35–40 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 38
-->

---

## Title

**Level ★11 — Pair Pick**

---

## Explanation

Course 3 used **keyboard** events in every block. **Glyph Grove** needs **mouse** clicks — gentle first step:

```python
if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
    pos = event.pos  # (x, y) pixels
```

**Hit test** — does the click land inside a tile?

```python
if tile_rect(tile).collidepoint(pos):
    ...
```

Pick tiles from **highest `layer` first** so you grab what your eyes see on top.

---

### Step 1: Free tile rule

A tile you can match must be **free**:

1. **Nothing on top** — no other tile with higher `layer` on the same `row`/`col`.
2. **Open side** — left **or** right neighbor on the **same layer** is empty (no tile there).

Blocked tiles draw **dimmer** so players learn the rule visually.

---

### Step 2: Two-click matching

```python
selected = None

def try_match(first, second, tiles):
    if first is None:
        return second
    if first["kind"] == second["kind"] and is_free(first, tiles) and is_free(second, tiles):
        first["removed"] = True
        second["removed"] = True
        return None
    return second
```

---

### Step 3: Run

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-11-glyph-grove-mouse-matching
python starter\game.py
```

**Expected output (visual):** Click highlights a tile; matching free pairs disappear.

---

## Code Example

**File: [solution/game.py](solution/game.py)** — mouse branch:

```python
if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
    hit = tile_at_point(event.pos, tiles)
    if hit is not None:
        selected = try_match(selected, hit, tiles)
```

---

## Code Execution

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-11-glyph-grove-mouse-matching
python solution\game.py
```

**Expected output (visual):** Play until board clears; move counter increments.

---

## Quick Drills

1. Print `event.pos` on every click — does Y grow downward?
2. Try clicking a covered tile — should it refuse to match?
3. Select two different glyphs — second should replace selection.

---

## Practice Task

**Quest name:** Pair Pick

1. Implement `is_covered`, `has_open_side`, and `is_free` in [starter/game.py](starter/game.py).
2. Wire `MOUSEBUTTONDOWN` matching.
3. **Bonus:** yellow border on `selected` tile.

**Self-mark:** Can you only clear **free** pairs? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Clicks always miss.

**Cause:** `tile_rect` forgets `layer` offset, or you iterate tiles in wrong layer order.

**Fix:** Match `tile_origin` math from lesson 4.10; use `sorted(..., layer reverse=True)` in `tile_at_point`.

---

## Quick Check

1. `collidepoint` needs…
   - **a)** A pygame `Rect` and mouse `(x, y)`
   - **b)** A Flask route name
   - **c)** pip uninstall
   - **d)** A file path string only

2. `MOUSEBUTTONDOWN` with `button == 1` is…
   - **a)** Usually the left mouse button
   - **b)** The Escape key
   - **c)** Middle scroll only
   - **d)** Quit event

3. Covered means…
   - **a)** Higher layer tile same row+col
   - **b)** Tile color is black
   - **c)** Quiz not taken
   - **d)** Score is negative

4. Open side means…
   - **a)** No neighbor on left OR right at same layer
   - **b)** Tile must face north
   - **c)** Window is fullscreen
   - **d)** Two keyboards plugged in

5. Lesson 4.12 adds…
   - **a)** Timer, hint, shuffle, title screen, best time
   - **b)** Removing mouse support
   - **c)** Django migrations
   - **d)** Only print debugging

---

<details><summary>Click to reveal answers</summary>

1. **a)** Rect hit test.
2. **a)** Left click.
3. **a)** Higher layer blocks.
4. **a)** Side openness check.
5. **a)** Full Glyph Grove polish.

</details>

---

## What's Next

→ [Lesson 4.12 — Glyph Grove Complete](../lesson-4-12-glyph-grove-complete/README.md) — win screen, hints, and the **last ★ project**!

---

*Click carefully — edges matter.*

[← Choose language](README.md)