# Lesson 5.35: Scrolling Road & Lanes

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~34 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 34
-->

---

## Title

**Level ★47 — Neon Stripes**

---

## Explanation

**Lane Rush** — Block 5 ★ project **#10** — is a **top-down dodge racer**: your neon car stays near the bottom while the **road scrolls** and lane stripes repeat forever (shapes only).

This lesson focuses on: **repeating lane stripes with `scroll_offset`, switching lanes, smooth left-right lerp with `dt`.**

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-35-lane-rush-road-scroll
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Dark road window; finish TODOs for scrolling stripes and lane lerp.

---

### Step 2: Compare the solution

Study [solution/game.py](solution/game.py) for the full pattern.

---

## Code Example

**File: [solution/game.py](solution/game.py)**:

```python
scroll_offset = (scroll_offset + SCROLL_SPEED * dt) % STRIPE_H
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-35-lane-rush-road-scroll
python solution\game.py
```

**Mac/Linux:** `python solution/game.py`

**Expected output (visual):** Yellow stripes scroll down; car eases between lane centers.

---

## Quick Drills

1. Print `scroll_offset` each second — why use `% STRIPE_H`?
2. Change `LANE_LERP` — snappier or floatier?
3. How many pixels wide is one lane if `ROAD_WIDTH = 360` and `NUM_LANES = 4`?

---

## Practice Task

**Quest name:** Neon Stripes

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: stripes scroll and the car lerps between lanes?
3. **Bonus stretch:** tint lane divider lines a new colour.

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Stripes jitter or jump backwards

**Cause:** Forgetting modulo wrap on `scroll_offset`.

**Fix:** After adding `SCROLL_SPEED * dt`, assign `% STRIPE_H`.

---

## Quick Check

1. Modulo on `scroll_offset` keeps stripes…
   - **a)** Seamlessly repeating
   - **b)** Frozen forever
   - **c)** In Flask only
   - **d)** Without pygame
2. Lane center for lane `2` uses…
   - **a)** `ROAD_LEFT + lane * LANE_W + LANE_W / 2`
   - **b)** Only `HEIGHT`
   - **c)** Turtle degrees
   - **d)** `pip install`
3. Lerp with `dt` makes lane changes…
   - **a)** Smooth at any FPS
   - **b)** Instant teleport only
   - **c)** Delete fuel
   - **d)** Disable keys
4. LEFT/RIGHT should…
   - **a)** Change `player_lane` inside 0..NUM_LANES-1
   - **b)** Quit pygame
   - **c)** Start Flask server
   - **d)** Merge runes
5. Next lesson adds…
   - **a)** Traffic spawns and crashes
   - **b)** Course 1 install
   - **c)** HTML forms
   - **d)** Minesweeper flood

---

<details><summary>Click to reveal answers</summary>

1. **a)** Seamlessly repeating
2. **a)** `ROAD_LEFT + lane * LANE_W + LANE_W / 2`
3. **a)** Smooth at any FPS
4. **a)** Change `player_lane` inside 0..NUM_LANES-1
5. **a)** Traffic spawns and crashes

</details>

## What's Next

→ [Lesson 5.36 — Traffic Spawns](../lesson-5-36-lane-rush-traffic-spawn/README.md)

---

*Stay in your lane — or switch fast!*

[Choose language](README.md)