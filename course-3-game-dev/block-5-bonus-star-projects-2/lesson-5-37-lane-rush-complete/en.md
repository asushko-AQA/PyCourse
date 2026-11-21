# Lesson 5.37: Lane Rush Complete

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~38 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 38
-->

---

## Title

**Level ★49 — Lane Rush Pro**

---

## Explanation

**Lane Rush** closes **Block 5 ★ II** — all **ten** bonus arcade games. Shapes only, top-down dodge with fuel, pickups, and a victory lap for dedicated learners.

This lesson focuses on: **speed ramp over time, fuel drain, coin/fuel pickups, near-miss bonus, start/game over/graduate, session best distance, celebration linking back to the course map.**

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-37-lane-rush-complete
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

---

### Step 2: Compare the solution

Study [solution/game.py](solution/game.py) for MENU / PLAY / GAME_OVER / GRADUATE.

---

## Code Example

**File: [solution/game.py](solution/game.py)**:

```python
state = "MENU"
```

---

## Code Execution

```text
python solution\game.py
```

**Expected output (visual):** Full Lane Rush — reach **1200 m** to see the Block 5 graduation screen.

---

## Quick Drills

1. Where is session best saved? (`~/.lane_rush_best.json`)
2. What happens when `fuel` hits 0?
3. When do you earn a near-miss bonus?

---

## Practice Task

**Quest name:** Lane Rush Pro

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: play one run; beat your session best or read the GRADUATE screen.
3. **Bonus stretch:** change `NEAR_MISS` threshold and feel the risk.

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Game ends instantly

**Cause:** `fuel` drain without pickups, or collision on frame one.

**Fix:** Start with full fuel; spawn traffic only after `state == "PLAY"`.

---

## Quick Check

1. Session best stores…
   - **a)** Longest distance in meters
   - **b)** Git commit hash
   - **c)** Flask secret key
   - **d)** Turtle pen colour
2. Speed ramp…
   - **a)** Increases scroll and traffic speed with `elapsed`
   - **b)** Stops pygame
   - **c)** Removes lanes
   - **d)** Disables input forever
3. Near-miss bonus needs…
   - **a)** Close gap without `colliderect`
   - **b)** Merge to 2048
   - **c)** Flood-fill zero
   - **d)** Win tic-tac-toe
4. GRADUATE screen celebrates…
   - **a)** Finishing all Block 5 ★ games
   - **b)** Only Block 1 install
   - **c)** Course 2 deploy
   - **d)** pip uninstall pygame
5. What's next for the course map…
   - **a)** [STUDENT-MAP graduation checklist](../../STUDENT-MAP.md)
   - **b)** Django tutorial
   - **c)** Lane Rush coming soon
   - **d)** Delete repo

---

<details><summary>Click to reveal answers</summary>

1. **a)** Longest distance in meters
2. **a)** Increases scroll and traffic speed with `elapsed`
3. **a)** Close gap without `colliderect`
4. **a)** Finishing all Block 5 ★ games
5. **a)** [STUDENT-MAP graduation checklist](../../STUDENT-MAP.md)

</details>

## What's Next

→ [Course 3 STUDENT-MAP](../../STUDENT-MAP.md) — tick your **★ II Bonus** graduation items!

---

*You shipped every Block 5 ★ game — incredible!*

[Choose language](README.md)