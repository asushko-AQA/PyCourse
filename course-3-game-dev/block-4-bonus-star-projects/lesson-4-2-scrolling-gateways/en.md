# Lesson 4.2: Scrolling Gateways

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects · **~35–40 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 38
-->

---

## Title

**Level ★2 — Gateway Glider**

---

## Explanation

Time to make Sky Hopper a **real challenge**. Each **gateway** is two green rectangles with a **gap** in the middle — like classic flap games, but **our own art**.

| Piece | Idea |
|-------|------|
| List of pipes | `pipes.append({"x", "gap_y", "scored"})` |
| Scroll | `pipe["x"] -= int(SCROLL * dt)` |
| Score | When `pipe["x"] + PIPE_W < bird.left` and not `scored` → `score += 1` |
| Crash | `bird.colliderect(top)` or `bottom`, or bird leaves screen |

`gap_y` is the **center** of the gap — random so each gateway feels fresh.

---

### Step 1: Implement `spawn_pipe()`

```python
def spawn_pipe() -> None:
    gap_y = random.randint(GAP // 2 + 40, HEIGHT - GAP // 2 - 40)
    pipes.append({"x": WIDTH + PIPE_W, "gap_y": gap_y, "scored": False})
```

Call `spawn_pipe()` once before the loop, and again when the last pipe is far enough left.

---

### Step 2: Scroll and clean up

```python
for pipe in pipes:
    pipe["x"] -= int(SCROLL * dt)
pipes = [p for p in pipes if p["x"] > -PIPE_W]
if not pipes or pipes[-1]["x"] < WIDTH - PIPE_SPACING:
    spawn_pipe()
```

---

### Step 3: Collide and score

Use `pipe_rects(pipe)` for top/bottom `Rect`s. On hit → `crashed = True`.  
On pass → set `scored = True` so you do not double-count.

---

### Step 4: Run

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-2-scrolling-gateways
python starter\game.py
```

**Expected output (visual):** Gateways slide left; score increases; bump shows “Press R”.

---

## Code Example

```python
for pipe in pipes:
    top, bottom = pipe_rects(pipe)
    if bird.colliderect(top) or bird.colliderect(bottom):
        crashed = True
    if not pipe["scored"] and pipe["x"] + PIPE_W < bird.left:
        pipe["scored"] = True
        score += 1
```

---

## Code Execution

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-2-scrolling-gateways
python starter\game.py
```

**Expected output (visual):** Playable gateway run with score and crash reset.

---

## Quick Drills

1. Wider gap — `GAP = 190`.
2. Fewer pipes — increase `PIPE_SPACING`.
3. Draw a star when `scored` flips to True (one frame).

---

## Practice Task

**Quest name:** Gateway Glider

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Score at least **3** in one life.
3. **Bonus stretch:** tint gateways purple every 5 points.

**Self-mark:** Pipes scroll smoothly? Score goes up once per gateway? Crash stops physics? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Score jumps by 10 per gateway.

**Cause:** No `scored` flag — you count every frame while past the pipe.

**Fix:** Set `pipe["scored"] = True` the first time the bird clears the pipe.

---

## Quick Check

1. `gap_y` is…
   - **a)** The vertical center of the safe gap
   - **b)** The bird's PNG filename
   - **c)** Flask secret key
   - **d)** Turtle pen color

2. Scrolling uses…
   - **a)** `pipe["x"] -= int(SCROLL * dt)`
   - **b)** Only `time.sleep`
   - **c)** `pip install flask`
   - **d)** Deleting pygame

3. When should `score` increase?
   - **a)** Every frame always
   - **b)** Once when the bird passes a gateway
   - **c)** On QUIT only
   - **d)** Never in Block 4

4. `colliderect` here checks…
   - **a)** Bird vs pipe rectangles
   - **b)** Email vs password
   - **c)** Two URLs
   - **d)** Markdown headings

5. Lesson 4.3 adds…
   - **a)** Title / game over screens + high score ramp
   - **b)** Django ORM
   - **c)** Removes pygame
   - **d)** Course 1 loops only

---

<details><summary>Click to reveal answers</summary>

1. **a)** Center of the gap.
2. **a)** Move left with dt.
3. **b)** Once per gateway (`scored` flag).
4. **a)** Hit detection.
5. **a)** Full game flow polish.

</details>

---

## What's Next

→ [Lesson 4.3 — Sky Hopper Complete](../lesson-4-3-sky-hopper-complete/README.md) — title screen, game over, high score!

[← Choose language](README.md)