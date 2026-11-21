# Lesson 4.6: Prism Dash Complete

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects · **~40–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 42
-->

---

## Title

**Level ★6 — Prism Dash Pro**

---

## Explanation

You have **scroll** (4.4) and **jump + spin** (4.5). Now ship the full loop like Lessons 2.4 and 4.3:

| State | Player sees |
|-------|-------------|
| `start` | Title, best %, SPACE to begin |
| `playing` | Run, jump, progress bar |
| `game_over` | Hit spike — attempts++, SPACE → title |
| `win` | Reached 100% of level string |

**Level data** — one string, one character per tile (`TILE_W` pixels wide):

| Char | Meaning |
|------|---------|
| `_` | Flat ground only |
| `#` | Raised platform you can land on |
| `^` | Floor spike — `colliderect` → restart |

```python
LEVEL = "____##__^^__####__^^__##__^^____####____"
```

**Progress** `int(world_x / len(LEVEL) / TILE_W * 100)` capped at 100.  
**Speed ramp:** `BASE_SCROLL + progress_pct() * 2`.  
**Session best:** update `best_progress` when a run ends.

---

### Step 1: `start_run()` and `die()`

Reset `world_x`, player physics, `state = PLAYING`.  
In `die()`, `attempts += 1`, maybe raise `best_progress`, `state = GAME_OVER`.

---

### Step 2: Draw + collide level

For each tile index `i`, `sx = i * TILE_W - int(world_x)`.  
Build spike `Rect`s slightly inset for fair hits. Triangles are drawn for looks; rects are for logic.

---

### Step 3: Progress bar + HUD

Draw a wide bar at the bottom; fill width = `progress_pct() %`. Show attempts and best %.

---

### Step 4: Win condition

When `world_x >= len(LEVEL) * TILE_W` → `state = WIN` and celebrate.

---

### Step 5: Run

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-6-prism-dash-complete
python starter\game.py
```

**Expected output (visual):** Playable Prism Dash you can show friends.

---

## Code Example

```python
if player_rect().colliderect(spike):
    die()

scroll = BASE_SCROLL + progress_pct() * 2
world_x += scroll * dt
```

---

## Code Execution

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-6-prism-dash-complete
python starter\game.py
```

**Expected output (visual):** Full start → play → spike fail or 100% win → title.

---

## Quick Drills

1. **Easy mode** — remove one `^` from `LEVEL`.
2. **Marathon** — duplicate the middle of `LEVEL` twice.
3. **Checkpoint stretch** — save `world_x` at 50% and respawn there on death.

---

## Practice Task

**Quest name:** Prism Dash Pro

1. Wire every TODO in [starter/game.py](starter/game.py).
2. Beat the level at least once (100% progress).
3. **Bonus stretch:** session best % on title screen updates correctly.

**Self-mark:** Spikes restart run? Platforms landable? Progress bar moves? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Instant death on spawn.

**Cause:** Spike hitbox overlaps spawn; or player spawns inside a block.

**Fix:** Start `world_x = 0` with leading `_` tiles; shrink spike rects with `+ 6` inset.

---

## Quick Check

1. `^` in `LEVEL` means…
   - **a)** Deadly floor spike
   - **b)** Bonus coin
   - **c)** Flask route
   - **d)** Background music

2. Progress % comes from…
   - **a)** `world_x` vs level length in pixels
   - **b)** Random dice roll
   - **c)** Quiz hash only
   - **d)** `pip list`

3. On spike hit you should…
   - **a)** `die()` — attempts++ and game over state
   - **b)** Add 100 to Flask score
   - **c)** Delete the level file
   - **d)** Ignore and fly

4. `#` tiles are…
   - **a)** Platforms with a top you can snap to
   - **b)** Invisible HTML
   - **c)** Sky Hopper pipes only
   - **d)** Turtle pens

5. After this lesson, next ★ slot is…
   - **a)** Lessons 4.7+ (see Block 4 README)
   - **b)** Back to Course 1 Lesson 1.1
   - **c)** Mandatory before Block 1
   - **d)** Only on GitHub Issues

---

<details><summary>Click to reveal answers</summary>

1. **a)** Restart obstacle.
2. **a)** Scroll distance through encoded level.
3. **a)** Fair arcade restart.
4. **a)** Raised blocks.
5. **a)** Tetris-like project planned at 4.7–4.9.

</details>

---

## What's Next

→ [Lesson 4.7 — Grid & Cells](../lesson-4-7-shard-stack-grid-cells/README.md) — ★ project **#3** **Shard Stack** begins!  
→ Or jump to [Block 4 index](../README.md) for the full ★ menu.  
→ Compare Prism Dash scroll + jump to your **Sky Hopper** flap skills!

---

*★ Prism Dash — project two, complete.*

[← Choose language](README.md)