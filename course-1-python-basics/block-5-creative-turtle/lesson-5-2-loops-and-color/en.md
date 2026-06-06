# Lesson 5.2: Loops and Color

> **Course:** Python Basics & Command Line Magic · **Block:** Creative Python with Turtle · **~30–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 20 — Star Painter**

---

## Explanation

Time to add **color** to the Turtle Studio! In Lesson 5.1 you looped to draw shapes. Now you loop to draw a **five-point star**, changing the pen color on every point.

| Command | What it does |
|---------|--------------|
| `t.pencolor("red")` | Set the line color (use color **names** in quotes) |
| `t.speed(0)` | Fastest drawing (good for patterns) |
| `t.right(144)` | Turn right 144° — the magic angle for a star point |

**Why 144?** A five-point star needs turns of 144° (not 72°). Trust the number for now — change it in Quick Drills to see what breaks!

Store colors in a **list** and pick one per loop:

```python
colors = ["red", "orange", "yellow", "green", "blue"]
t.pencolor(colors[point])
```

---

### Step 1: Open star.py

Open [starter/star.py](starter/star.py). Five loop steps draw five star points in five colors.

---

### Step 2: Run

**Path A:**

```text
cd course-1-python-basics\block-5-creative-turtle\lesson-5-2-loops-and-color
python starter\star.py
```

**Path B:** Copy `star.py` to your folder, `cd` there, run `python star.py`. See [STUDENT-MAP](../../STUDENT-MAP.md).

**Expected output (visual):**

- Turtle window opens (check taskbar if hidden **behind** VS Code).
- A **five-point star** appears in the center.
- Each of the five segments is a **different color** (red → orange → yellow → green → blue).
- Window stays open until you close it.

---

## Code Example

**File: [starter/star.py](starter/star.py)**

```python
import turtle

t = turtle.Turtle()
t.speed(0)

colors = ["red", "orange", "yellow", "green", "blue"]

for point in range(5):
    t.pencolor(colors[point])
    t.forward(100)
    t.right(144)

turtle.done()
```

---

## Code Execution

```text
cd course-1-python-basics\block-5-creative-turtle\lesson-5-2-loops-and-color
python starter\star.py
```

**Expected output (visual):** Colorful five-point star; window stays open.

---

## Quick Drills

1. **Sixth color** — append `"purple"` to the list. Does the star still have five points? (Yes — the loop still runs 5 times.)
2. **Rainbow repeat** — change the loop to `range(10)` and use `colors[point % 5]` for the index.
3. **Size** — change `forward(100)` to `forward(150)` for a bigger star.

---

## Practice Task

**Quest name:** Star Painter

1. Complete the TODO loop in [starter/star.py](starter/star.py).
2. Run and admire your colorful star.
3. **Bonus:** Pick your own five favorite color names and update the list.

**Reference solution:** [solution/star.py](solution/star.py)

---

## Debug Corner

**Problem:** `turtle.TurtleGraphicsError: bad color string: purpel`

**Cause:** `pencolor()` needs a **valid color name** Python recognizes. `"purpel"` is a typo — Python does not know that word.

**Fix:** Spell color names carefully. Common names: `"red"`, `"blue"`, `"green"`, `"orange"`, `"purple"`, `"black"`, `"white"`. Fix the typo and run again.

**Also check:** If nothing appears, the window may be **behind** VS Code — click the Python icon on the taskbar.

---

## What's Next

→ [Lesson 5.3: Functions and Turtle](../lesson-5-3-functions-and-turtle/README.md) — build a snowflake branch with a reusable function.

---

*Your star shines! One more Turtle Studio lesson before web apps.*

[← Choose language](README.md)
