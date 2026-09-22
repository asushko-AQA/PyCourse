# Lesson 3.3: Polish

> **Course:** Game Development with Python · **Block:** Physics & Collisions (Final Project) · **~30–40 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 35
-->

---

## Title

**Level 11 — Polish Pro**

---

## Explanation

A shipped game needs **feel**. Three polish layers on top of Lesson 3.2:

| Polish | How |
|--------|-----|
| High score | `high_score` variable — update when a round ends |
| Difficulty ramp | `fall_speed = BASE_FALL + score * 12` |
| Sound | `pygame.mixer.Sound("catch.wav")` inside try/except |

We keep high score **in memory** (resets when you close the window). Saving to a file is a fun stretch later.

```python
if score > high_score:
    high_score = score
```

Sounds are **optional**: if the mixer or files fail, `play_safe` simply does nothing.

---

### Step 1: Open starter/game.py

Open [starter/game.py](starter/game.py). The catch game already runs. TODOs: mixer + Sound load, ramp formula, update `high_score`, play sounds on catch/miss.

---

### Step 2: Init mixer and load sounds

```python
pygame.mixer.init()
try:
    catch_sound = pygame.mixer.Sound(os.path.join(HERE, "catch.wav"))
    miss_sound = pygame.mixer.Sound(os.path.join(HERE, "miss.wav"))
except pygame.error:
    catch_sound = None
    miss_sound = None
```

---

### Step 3: Ramp fall speed

```python
fall_speed = BASE_FALL + score * 12
star.y += int(fall_speed * dt)
```

Higher score → faster stars. Fairer than a fixed speed forever.

---

### Step 4: Update high score on game over

```python
if misses >= MAX_MISSES:
    if score > high_score:
        high_score = score
    state = GAME_OVER
```

Show `high_score` on the title and Game Over screens (already sketched).

---

### Step 5: Play sounds safely

```python
def play_safe(sound):
    if sound is not None:
        sound.play()

# on catch:
play_safe(catch_sound)
# on miss:
play_safe(miss_sound)
```

---

### Step 6: Run

```text
cd course-3-game-dev\block-3-physics-collisions-final-project\lesson-3-3-polish
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual + optional audio):** Title shows High score; play gets harder; beeps on catch/miss if speakers work; best score updates after a round.

---

## Code Example

**File: [solution/game.py](solution/game.py)** — polish highlights:

```python
pygame.mixer.init()
# load catch.wav / miss.wav with try/except → catch_sound, miss_sound

high_score = 0
BASE_FALL = 160

# while PLAYING:
fall_speed = BASE_FALL + score * 12
star.y += int(fall_speed * dt)

if paddle.colliderect(star):
    score += 1
    play_safe(catch_sound)
    reset_star()
elif star.top > HEIGHT:
    misses += 1
    play_safe(miss_sound)
    reset_star()
    if misses >= MAX_MISSES:
        if score > high_score:
            high_score = score
        state = GAME_OVER
```

---

## Code Execution

```text
cd course-3-game-dev\block-3-physics-collisions-final-project\lesson-3-3-polish
python starter\game.py
```

**Expected output (visual):** Polished Catch the Falling Stars with ramp + high score (+ sounds if available).

---

## Quick Drills

1. **Fierce ramp** — `score * 20`.
2. **NEW BEST!** — blit extra text when you beat the high score.
3. **Silent mode** — temporarily set both sounds to `None`; game must still run.

---

## Practice Task

**Quest name:** Polish Pro

1. Complete TODOs in [starter/game.py](starter/game.py): sounds, ramp, high score update.
2. Beat your own high score at least once in a session.
3. **Bonus stretch:** save `high_score` to `highscore.txt` with `open` / `write` (optional — not required).

**Self-mark:** High score persists across rounds (until quit)? Stars get faster? Catch/miss sounds optional but coded safely? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** `pygame.error` about mixer / sound, or game crashes on start.

**Cause:** Mixer not initialized, bad path, or no audio device.

**Fix:** Call `pygame.mixer.init()` once. Wrap Sound load in `try/except pygame.error`. Use `play_safe` so `None` is OK. Confirm `catch.wav` / `miss.wav` sit next to `game.py`.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. Where does this lesson keep high score by default?
   - **a)** In a cloud database only
   - **b)** In a variable for the current session
   - **c)** Inside `coin.png`
   - **d)** In Turtle

2. What does a difficulty ramp do here?
   - **a)** Deletes the paddle
   - **b)** Increases fall speed as score rises
   - **c)** Removes `dt`
   - **d)** Forces fullscreen forever

3. Why wrap Sound loading in try/except?
   - **a)** So missing audio does not crash the game
   - **b)** To install Python twice
   - **c)** To draw Rects
   - **d)** To skip `flip`

4. When should you update `high_score`?
   - **a)** Every frame even on the title
   - **b)** When a round ends and `score` beats the best
   - **c)** Only on QUIT
   - **d)** Never

5. `play_safe(None)` should…
   - **a)** Crash loudly
   - **b)** Do nothing (no sound)
   - **c)** Close Pygame
   - **d)** Reset `dt` to zero

---

<details><summary>Click to reveal answers</summary>

1. **b)** Session variable (in memory).
2. **b)** Faster falls with higher score.
3. **a)** Optional audio stays safe.
4. **b)** Compare after the round ends.
5. **b)** Guard against missing Sound.

</details>

---

## What's Next

→ [Block 3 index](../README.md) — tick the Course 3 graduation checklist!  
→ You finished **Course 3: Game Development with Python**. Show your game!

---

*Polished and proud — Course 3 complete!*

[← Choose language](README.md)
