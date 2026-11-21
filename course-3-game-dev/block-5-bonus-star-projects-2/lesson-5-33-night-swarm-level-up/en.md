# Lesson 5.33: XP & Level-Up Choices

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~36 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 36
-->

---

## Title

**Level ★45 — Bright Choice**

---

## Explanation

**Night Swarm** — Block 5 ★ project **#9** — is a calm **top-down lantern keeper** game: you repel soft **shadow creatures** with **light orbs** (shapes only, no violence graphics).

This lesson focuses on: **collect gems → XP, level-up pause, 3 random upgrades from a dict (keys 1–3).**

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-33-night-swarm-level-up
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Twilight arena window; finish TODOs for this lesson's goal.

---

### Step 2: Compare the solution

Study [solution/game.py](solution/game.py) for the full pattern.

---

## Code Example

**File: [solution/game.py](solution/game.py)**:

```python
level_choices = pick_level_up_choices(UPGRADE_POOL, 3, rng)
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-33-night-swarm-level-up
python solution\game.py
```

**Mac/Linux:** `python solution/game.py`

**Expected output (visual):** Runnable Night Swarm milestone for lesson 5.33.

---

## Quick Drills

1. Print your move vector before `normalize()` — when is length > 1?
2. Change `PLAYER_SPEED` and feel the difference with the same `dt`.
3. Name one upgrade key from `UPGRADE_POOL` and what it boosts.

---

## Practice Task

**Quest name:** Upgrade Spark

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: does the window match this lesson's goal?
3. **Bonus stretch:** tint the arena grid a new colour.

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Diagonal movement feels faster than cardinal directions

**Cause:** Adding `(1,1)` without normalizing makes length √2.

**Fix:** Call `move.normalize()` whenever `move.length_squared() > 0`.

---

## Quick Check

1. Upgrade stats live well in…
   - **a)** A dict keyed by upgrade id
   - **b)** A single bool
   - **c)** requirements.txt
   - **d)** Git branches only
2. Level-up screen should…
   - **a)** Pause combat until player picks
   - **b)** Quit pygame instantly
   - **c)** Skip drawing
   - **d)** Ignore keyboard
3. Three random choices means…
   - **a)** Shuffle keys then take 3
   - **b)** Always the same 3
   - **c)** Zero upgrades
   - **d)** Infinite damage
4. Collecting a gem should…
   - **a)** Add to xp counter
   - **b)** Delete player
   - **c)** Close window
   - **d)** Run Flask
5. Next lesson adds…
   - **a)** survive timer and full game states
   - **b)** Only print()
   - **c)** Course 2 CSS
   - **d)** Turtle snowflake

---

<details><summary>Click to reveal answers</summary>

1. **a)** A dict keyed by upgrade id
2. **a)** Pause combat until player picks
3. **a)** Shuffle keys then take 3
4. **a)** Add to xp counter
5. **a)** survive timer and full game states

</details>

## What's Next

→ [Lesson 5.34 — Night Swarm Complete](../lesson-5-34-night-swarm-complete/README.md)

---

*Keep the lantern bright!*

[Choose language](README.md)
