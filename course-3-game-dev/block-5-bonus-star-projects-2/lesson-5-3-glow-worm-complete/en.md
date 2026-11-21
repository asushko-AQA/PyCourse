# Lesson 5.3: Glow Worm Complete

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~35–40 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 38
-->

---

## Title

**Level ★15 — Glow Worm Pro**

---

## Explanation

You already move, eat, and crash. Now turn the prototype into a **tiny arcade loop** players recognize:

| Phase | `state` value | Player action |
|-------|---------------|---------------|
| Title | `START` | **SPACE** → `start_game()` |
| Run | `PLAYING` | Arrows steer; timer steps worm |
| End | `GAME_OVER` | **SPACE** → new run; show score |

**Session `high_score`:** When `crash()` runs, if `score > high_score`, save the new best. It lasts until you close the window — perfect for “one more try” energy.

**Speed ramp:** Instead of a fixed `MOVE_INTERVAL`, compute `move_interval` from score:

```python
def move_interval_for_score() -> float:
    speedup = min(12, score // 3)
    return max(MIN_INTERVAL, BASE_INTERVAL - speedup * 0.012)
```

Each few sparks shave a few milliseconds off the wait — capped at `MIN_INTERVAL` so humans can still react.

**Polish:** Pulse the food and head glow with `pygame.time.get_ticks()`; draw semi-transparent overlays for start and game over (see [solution/game.py](solution/game.py)).

**Win edge case:** If `spawn_food()` returns `(-1, -1)` because the board is full, jump to `GAME_OVER` — you beat the grid!

---

### Step 1: `start_game()`

Reset `segments`, directions, `food`, `score`, `move_timer`, `move_interval = BASE_INTERVAL`, and set `state = PLAYING`.

---

### Step 2: `crash()`

If `score > high_score`, update `high_score`. Set `state = GAME_OVER`.

---

### Step 3: Event routing

```python
if state in (START, GAME_OVER) and event.key == pygame.K_SPACE:
    start_game()
elif state == PLAYING:
    # arrow keys → pending_dir
```

Only accumulate `move_timer` and call `step_worm()` when `state == PLAYING`.

---

### Step 4: Run

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-3-glow-worm-complete
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Title overlay → play → game over with score and best; worm speeds up as score climbs.

---

## Code Example

**File: [solution/game.py](solution/game.py)** — states + ramp:

```python
if grow:
    score += 1
    move_interval = move_interval_for_score()
    food = spawn_food()
```

```python
def crash() -> None:
    global state, high_score
    if score > high_score:
        high_score = score
    state = GAME_OVER
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-3-glow-worm-complete
python solution\game.py
```

**Expected output (visual):** Full Glow Worm: HUD shows score and best; faster motion at high scores; SPACE loops cleanly.

---

## Quick Drills

1. Print `move_interval` every 5 points — is it monotonically smaller?
2. Beat `high_score`, crash on purpose — does the title show the new number?
3. Add “Glow Worm” subtitle text on the start overlay.

---

## Practice Task

**Quest name:** Glow Worm Pro

1. Finish TODOs in [starter/game.py](starter/game.py): `move_interval_for_score`, `start_game`, `crash`, draw overlays, gated timer step.
2. **START** and **GAME_OVER** accept **SPACE**; **PLAYING** uses arrows only.
3. HUD shows **score** and **high_score** while playing.
4. **Bonus stretch:** pulsing glow on food and head like the solution.

**Self-mark:** Can you play three runs in a row without restarting Python? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Worm keeps moving on the title screen.

**Cause:** `step_worm()` runs regardless of `state`.

**Fix:** Wrap timer logic in `if state == PLAYING:`.

**Problem:** High score resets every crash.

**Cause:** Putting `high_score = 0` inside `start_game()`.

**Fix:** Only reset **run** variables in `start_game()`; leave `high_score` alone.

**Problem:** Speed never changes.

**Cause:** Still using constant `MOVE_INTERVAL` from 5.1.

**Fix:** After each eat, set `move_interval = move_interval_for_score()`.

---

## Quick Check

1. `state == START` means…
   - **a)** Waiting for SPACE to call `start_game()`
   - **b)** Flask debug mode
   - **c)** Turtle is drawing
   - **d)** Food list is empty only

2. `high_score` should update in…
   - **a)** `crash()` when current score is bigger
   - **b)** Every frame in the draw loop
   - **c)** `spawn_food()` only
   - **d)** `pygame.quit()` always

3. `move_interval_for_score()` makes the worm…
   - **a)** Faster (shorter wait) as score rises, down to a floor
   - **b)** Slower forever
   - **c)** Invisible
   - **d)** Use only keyboard events, no timer

4. Grow logic from 5.2 still means…
   - **a)** `pop()` tail only when not eating
   - **b)** Always shrink
   - **c)** Ignore food tuple
   - **d)** Delete pygame.Surface

5. After this ★ project, Block 5 continues with…
   - **a)** **Bounce Forge** — Lesson 5.4 next
   - **b)** Flask calculator capstone
   - **c)** Course 1 installing Python
   - **d)** Removing all lists

---

<details><summary>Click to reveal answers</summary>

1. **a)** Title / attract mode.
2. **a)** Best score on crash.
3. **a)** Speed ramp with `MIN_INTERVAL` cap.
4. **a)** Same grow rule as 5.2.
5. **a)** See [Block 5 README](../README.md).

</details>

---

## What's Next

Congratulations — **Glow Worm** is a full ★ mini-game!

→ [Lesson 5.4 — Ball & Wall Bounces](../lesson-5-4-bounce-forge-ball-walls/README.md) — start **Bounce Forge** (spark ball + walls)!  
→ [Block 5 roadmap](../README.md) — **Orbit Guard** and more ★ games *coming soon*.

---

*Neon trails, real arcade feels.*

[← Choose language](README.md)