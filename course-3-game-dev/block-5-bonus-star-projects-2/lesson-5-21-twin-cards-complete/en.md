# Lesson 5.21: Twin Cards Complete

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~35 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 35
-->

---

## Title

**Level ★33 — Twin Cards Pro**

---

## Explanation

**Twin Cards** is a calm memory game: flip two cards at a time and find matching **cosmic symbols** drawn with Pygame shapes — no downloaded art.

Each card is a small **dict** in a list:

| Key | Meaning |
|-----|---------|
| `col`, `row` | Grid position |
| `symbol` | Pair id (0 … n−1) |
| `face_up` | Showing the symbol? |
| `matched` | Pair already solved? |

This lesson focuses on: **Moves + timer, 4×3 / 4×4 / 6×4, win stars, restart, session best, flip anim.**

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-21-twin-cards-complete
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Purple card grid; finish TODOs for this lesson's goal.

---

### Step 2: Compare the solution

Study [solution/game.py](solution/game.py) for the full pattern.

---

## Code Example

**File: [solution/game.py](solution/game.py)**:

```python
deck = list(range(pair_count)) * 2
random.shuffle(deck)
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-21-twin-cards-complete
python solution\game.py
```

**Expected output (visual):** Runnable Twin Cards milestone for lesson 5.21.

---

## Quick Drills

1. Print `len(deck)` — is it always `cols * rows`?
2. Count each `symbol` value — does every id appear **exactly twice**?
3. Change one color in `SYMBOL_COLORS` and rerun.

---

## Practice Task

**Quest name:** Twin Cards Pro

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: does the window match this lesson's goal?
3. **Bonus stretch:** add a HUD line with grid size.

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Every card shows the same symbol

**Cause:** `build_deck` forgot to duplicate ids before shuffling.

**Fix:** Use `list(range(pair_count)) * 2`, then `random.shuffle(deck)`.

---

## Quick Check

1. A full deck for 4×3 has…
   - **a)** 12 cards (6 pairs)
   - **b)** 6 cards only
   - **c)** 8 pairs
   - **d)** No shuffle allowed

2. `random.shuffle`…
   - **a)** Rearranges the list in place
   - **b)** Returns a new Flask app
   - **c)** Deletes pygame
   - **d)** Only works on strings

3. `face_up=False` means…
   - **a)** Draw the card back
   - **b)** Delete the row
   - **c)** Start Turtle
   - **d)** HTTP POST

4. Each `symbol` id should appear…
   - **a)** Exactly twice in the deck
   - **b)** Once only
   - **c)** Zero times
   - **d)** Four times always

5. Next lesson adds…
   - **a)** Click-to-flip memory flow
   - **b)** Only pip install
   - **c)** Course 2 Flask
   - **d)** Deleting lists

---

<details><summary>Click to reveal answers</summary>

1. **a)** 12 cards (6 pairs).

2. **a)** Rearranges the list in place.

3. **a)** Draw the card back.

4. **a)** Exactly twice in the deck.

5. **a)** Click-to-flip memory flow (lesson arc).

</details>

## What's Next

→ [Block 5 — Tic-Tac-Bot (coming soon)](../README.md)

---

*Brains + stars!*

[Choose language](README.md)
