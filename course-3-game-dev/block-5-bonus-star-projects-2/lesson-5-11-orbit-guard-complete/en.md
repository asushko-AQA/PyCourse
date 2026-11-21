# Lesson 5.11: Orbit Guard Complete

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~40 min**  
> [Choose language](README.md) · **[Русский →](ru.md)**

<!-- meta
homework: starter/game.py
minutes: 40
-->

---

## Title

**Level ★23 — Orbit Guard Pro**

---

## Explanation

- States: `START`, `PLAYING`, `WAVE_CLEAR`, `GAME_OVER`, `VICTORY` (like Glow Worm 5.3).
- Four waves with more invaders; `march_speed` rises when fewer remain.
- Bonus **UFO** crosses the top — shoot it for +350 and session `high_score`.
- SPACE on title starts; SPACE after wave advances; track best score in memory.

---

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-11-orbit-guard-complete
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Orbit window; finish TODOs to match the lesson goal.

---

### Step 2: Compare the solution

Study [solution/game.py](solution/game.py) for patrol ship, formation march, shields, or full waves — depending on this lesson.

---

## Code Example

**File: [solution/game.py](solution/game.py)** — key pattern from this lesson:

```python
high_score = max(high_score, score)
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-11-orbit-guard-complete
python solution\game.py
```

**Expected output (visual):** Runnable Orbit Guard milestone for lesson 5.11.

---

## Quick Drills

1. Print `len(player_bolts)` after each shot.
2. Log `formation_x` when the grid steps down.
3. Skim [solution/game.py](solution/game.py) for orbit colors.

---

## Practice Task

**Quest name:** Orbit Guard Pro

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: does the orbit window behave like the lesson goal?
3. **Bonus stretch:** add an extra star twinkle on the background (see solution).

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Bolts never disappear.

**Cause:** Forgot to filter `player_bolts` after moving.

**Fix:** Reassign the list with a comprehension checking `PLAY_TOP < y < HEIGHT`.

**Problem:** Formation teleports off-screen.

**Cause:** Not flipping `march_dir` at margins.

**Fix:** When `formation_x` passes margin, multiply `march_dir` by -1 and add `step_down`.


---

## Quick Check

1. `WAVE_CLEAR` means…
   - **a)** All invaders destroyed this wave
   - **b)** Flask error
   - **c)** Ship deleted
   - **d)** No pygame

2. `high_score` updates when…
   - **a)** Current score exceeds it
   - **b)** Every frame always
   - **c)** Only on START
   - **d)** Never

3. UFO bonus gives roughly…
   - **a)** +350 points
   - **b)** Extra life always
   - **c)** Free pip install
   - **d)** No effect

4. More waves generally mean…
   - **a)** Faster march / tougher grid
   - **b)** Slower pygame
   - **c)** No shields
   - **d)** Less code

5. Next ★ roadmap project is…
   - **a)** Mine Whisper (coming soon)
   - **b)** Course 1 turtle only
   - **c)** Block 0 essays
   - **d)** Removing lists


---

<details><summary>Click to reveal answers</summary>

1. **a)** Pause before the next wave.
2. **a)** Session best like other ★ games.
3. **a)** Shoot the crossing UFO.
4. **a)** Difficulty ramp across waves.
5. **a)** See block README item 4.

</details>


## What's Next

→ [Block 5 — Mine Whisper (coming soon)](../README.md) — Orbit secure! Next ★ project on the roadmap is **Mine Whisper**.

---

*Defend the orbit with code.*

[← Choose language](README.md)
