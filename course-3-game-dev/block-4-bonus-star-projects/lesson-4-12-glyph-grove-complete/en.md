# Lesson 4.12: Glyph Grove Complete

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects · **~40–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 42
-->

---

## Title

**Level ★12 — Glyph Grove Pro**

---

## Explanation

You have **tiles** (4.10) and **mouse matching** (4.11). Finish the arcade loop:

| State | Player sees |
|-------|-------------|
| `start` | Title, session best time, click or SPACE to play |
| `playing` | Timer, moves, hint + shuffle buttons |
| `won` | All tiles cleared — celebrate! |
| `stuck` | No legal moves — shuffle or return to title |

**Timer:** `elapsed += dt` each frame while playing.

**Hint:** `find_hint(tiles)` highlights the first free matching pair (key `H` or HUD button).

**Shuffle:** reshuffle `kind` on remaining tiles; if still no moves → `stuck`.

**Session best:** keep the fastest win time in a variable (reset when pygame quits — like other ★ games).

---

### Step 1: Detect end states

```python
def any_moves_left(tiles):
  free = [t for t in tiles if is_free(t, tiles)]
  ...
```

Win when `remaining_count(tiles) == 0`.

---

### Step 2: Title + restart

SPACE from `won` / `stuck` returns to `start` so players can chase a faster time.

---

### Step 3: Run

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-12-glyph-grove-complete
python solution\game.py
```

**Expected output (visual):** Full Glyph Grove with HUD and overlays.

---

## Code Example

**File: [solution/game.py](solution/game.py)** — state machine tail:

```python
if state == PLAYING:
    elapsed += dt
check_end_state()  # sets WON or STUCK
```

---

## Code Execution

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-12-glyph-grove-complete
python solution\game.py
```

**Expected output (visual):** Title → clear the garden → best time updates.

---

## Quick Drills

1. Beat your first time twice — does `best_time` shrink?
2. Force `stuck` by matching until one lonely pair is buried — does shuffle help?
3. Press `H` before any move — do two tiles glow brighter?

---

## Practice Task

**Quest name:** Glyph Grove Pro

1. Merge your 4.11 logic into [starter/game.py](starter/game.py) and add all states.
2. Timer + moves visible while playing.
3. **Bonus:** show “New best!” flash when you beat `best_time`.

**Self-mark:** Can a friend play without you explaining rules? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Timer runs on the title screen.

**Cause:** `elapsed += dt` outside `state == PLAYING` check.

**Fix:** Only accumulate time in the playing branch.

---

## Quick Check

1. `stuck` should happen when…
   - **a)** No free matching pair remains
   - **b)** pygame version is 1.9
   - **c)** Student skips drills
   - **d)** FPS is 60

2. `reshuffle_kinds` should…
   - **a)** Shuffle kinds on non-removed tiles only
   - **b)** Delete the layout list
   - **c)** Install Flask
   - **d)** Clear `best_time` always

3. Session `best_time` is like…
   - **a)** Sky Hopper / Shard Stack high score variables
   - **b)** A MySQL database
   - **c)** Git commit hash
   - **d)** Mandatory homework checker

4. Hint highlights…
   - **a)** One legal free pair if any exists
   - **b)** Every tile always
   - **c)** Only the background
   - **d)** Quiz answers

5. After 4.12 you have finished…
   - **a)** All four ★ bonus games in Course 3
   - **b)** Only Block 1 of Course 1
   - **c)** Course 2 Flask deploy
   - **d)** Nothing — Block 4 is required

---

<details><summary>Click to reveal answers</summary>

1. **a)** No moves detection.
2. **a)** Live tiles only.
3. **a)** Session record pattern.
4. **a)** Helper for stuck players.
5. **a)** Four ★ projects done!

</details>

---

## What's Next

→ [Lesson 5.1 — Grid & Segments](../../block-5-bonus-star-projects-2/lesson-5-1-glow-worm-grid-segments/README.md) — **Block 5 ★ II** begins with **Glow Worm**!  
→ [Block 5 roadmap](../../block-5-bonus-star-projects-2/README.md) — ten more arcade ideas (*Bounce Forge* coming soon).  
→ [Course 3 Student Map](../../STUDENT-MAP.md) — you cleared all four Block 4 ★ games.

---

*★ Four bonus games — you earned the garden.*

[← Choose language](README.md)