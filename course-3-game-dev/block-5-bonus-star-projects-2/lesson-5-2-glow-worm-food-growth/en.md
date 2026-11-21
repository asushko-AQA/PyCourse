# Lesson 5.2: Food, Growth & Collisions

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~32–38 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 35
-->

---

## Title

**Level ★14 — Spark Bite**

---

## Explanation

Your neon trail is alive — time to **hunt spark food** and **grow longer** when you bite it.

In lesson 5.1 you always shortened the tail:

```python
segments = [new_head] + segments[:-1]
```

When the head lands on **food**, you **keep** the old tail — the worm grows one segment:

```python
grow = new_head == food
segments = [new_head] + segments
if not grow:
    segments.pop()
```

**Food spawn:** `spawn_food()` picks a random `(col, row)` that is **not** already in `segments`. A `set(segments)` makes “is this cell taken?” fast.

**Crashes:**

- **Wall** — head outside `0..COLS-1` or `0..ROWS-1` → `alive = False`
- **Self** — `segments[0] in segments[1:]` → biting your own body

**Restart (simple):** When `alive` is false, **SPACE** resets segments, food, score, and flips `alive` back to `True`.

---

### Step 1: Draw spark food

`draw_food` paints a pink glowing dot at `food`’s cell center — smaller than the worm circles.

---

### Step 2: Complete `step_worm`

1. Bail early if `not alive`.
2. Apply `direction` from `pending_dir` and compute `new_head`.
3. Wall hit → `alive = False`, return.
4. Prepend head; **pop tail only if not growing**.
5. Self collision → `alive = False`.
6. On grow: `score += 1`, `food = spawn_food()`.

---

### Step 3: Input rules

- Arrows only when `alive`.
- **SPACE** when dead — reset run (see [solution/game.py](solution/game.py)).

---

### Step 4: Run

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-2-glow-worm-food-growth
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Worm eats pink sparks, score rises, crash shows on HUD; SPACE restarts.

---

## Code Example

**File: [solution/game.py](solution/game.py)** — grow vs slide:

```python
grow = new_head == food
segments = [new_head] + segments
if not grow:
    segments.pop()
if segments[0] in segments[1:]:
    alive = False
    return
if grow:
    score += 1
    food = spawn_food()
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-2-glow-worm-food-growth
python solution\game.py
```

**Expected output (visual):** Longer worm after each spark; game freezes on crash; SPACE starts fresh.

---

## Quick Drills

1. After one bite, print `len(segments)` — did it grow by 1?
2. Force food onto the head cell in code once — does score double safely?
3. Fill the board in your head: what does `spawn_food()` return when every cell is full?

---

## Practice Task

**Quest name:** Spark Bite

1. Wire `step_worm` and arrow handling in [starter/game.py](starter/game.py).
2. Eating **does not** pop the tail; walking **does**.
3. Wall or self hit sets `alive = False`; draw a short “Crashed — SPACE” hint when dead.
4. **SPACE** restart resets worm, food, and score.

**Self-mark:** Score only increases when `grow` is True? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Worm never grows.

**Cause:** Still using `segments[:-1]` every step, even on food.

**Fix:** Only `pop()` when `not grow`.

**Problem:** Instant game over on eating.

**Cause:** Checking self collision **before** popping the tail on a non-grow step, or forgetting that the old head becomes index 1.

**Fix:** Order: prepend → maybe pop → **then** test `segments[0] in segments[1:]`.

**Problem:** Food spawns inside the worm.

**Cause:** `spawn_food` forgot `occupied = set(segments)`.

**Fix:** Skip positions in `occupied`.

---

## Quick Check

1. When the worm eats, you should…
   - **a)** Skip `pop()` so length increases
   - **b)** Always clear the whole list
   - **c)** Set `COLS = 0`
   - **d)** Remove pygame display

2. `spawn_food()` must avoid…
   - **a)** Cells already in `segments`
   - **b)** Drawing circles
   - **c)** Using tuples
   - **d)** The `random` module

3. `alive = False` happens when…
   - **a)** Wall or self collision
   - **b)** Every frame always
   - **c)** Pressing SPACE while playing
   - **d)** Importing lists

4. `(col, row)` order in this project is…
   - **a)** Column first, then row — same as `segments`
   - **b)** Row first in all tuples
   - **c)** Only for Flask URLs
   - **d)** Random each run

5. Next lesson adds…
   - **a)** Start/play/game over states, high score, speed ramp
   - **b)** Django models
   - **c)** Only Turtle
   - **d)** A second pygame window

---

<details><summary>Click to reveal answers</summary>

1. **a)** Keep the tail on grow.
2. **a)** Occupied worm cells.
3. **a)** Crash detection.
4. **a)** `(col, row)` everywhere.
5. **a)** Lesson 5.3 polish.

</details>

---

## What's Next

→ [Lesson 5.3 — Glow Worm Complete](../lesson-5-3-glow-worm-complete/README.md) — title screen, **best score**, and faster ticks as you munch!

---

*Grow the glow — dodge yourself.*

[← Choose language](README.md)