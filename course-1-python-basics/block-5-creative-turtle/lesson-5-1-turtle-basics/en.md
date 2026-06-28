# Lesson 5.1: Turtle Basics

> **Course:** Python Basics & Command Line Magic · **Block:** Creative Python with Turtle · **~30–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 19 — Shape Sketcher**

---

## Explanation

Welcome to the **Turtle Studio**! Python includes a drawing robot called **turtle**. You give it commands — move forward, turn left — and it leaves a trail on the screen like a pen on paper.

| Command | What it does |
|---------|--------------|
| `import turtle` | Load the drawing toolkit (stdlib — no pip!) |
| `t = turtle.Turtle()` | Create one turtle named `t` |
| `t.forward(100)` | Move 100 pixels forward, drawing a line |
| `t.left(90)` | Turn left 90 degrees |
| `turtle.done()` | Keep the window open until you close it |

You already know **loops** from Block 3. Instead of typing the same four lines four times for a square, you loop:

```python
for side in range(4):
    t.forward(100)
    t.left(90)
```

A triangle needs **three** sides and **120°** turns (because 360 ÷ 3 = 120).

---

### Step 1: Open shapes.py

Open [starter/shapes.py](starter/shapes.py). You will draw a square, move aside, then draw a triangle.

---

### Step 2: cd to this lesson folder

**Path A — PyCourse repo:**

```text
cd course-1-python-basics\block-5-creative-turtle\lesson-5-1-turtle-basics
```

**Path B — your own folder:** Copy `shapes.py` anywhere. Open VS Code on that folder. See [STUDENT-MAP](../../STUDENT-MAP.md).

**Mac/Linux:** `python starter/shapes.py` (forward slashes).

---

### Step 3: Run the script

```text
python starter\shapes.py
```

**Expected output (visual):**

- A separate **Turtle window** opens (check the taskbar if you do not see it — it may be **behind** VS Code).
- A **black square** appears on the left.
- A **black triangle** appears to the right of the square.
- The window stays open until you click its close button.

The terminal may show no text — that is normal for turtle programs!

---

## Code Example

**File: [starter/shapes.py](starter/shapes.py)**

```python
import turtle

t = turtle.Turtle()
t.speed(3)

for side in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.forward(150)
t.pendown()

for side in range(3):
    t.forward(100)
    t.left(120)

turtle.done()
```

- `penup()` / `pendown()` lift the pen so the turtle moves without drawing between shapes.

---

## Code Execution

```text
cd course-1-python-basics\block-5-creative-turtle\lesson-5-1-turtle-basics
python starter\shapes.py
```

**Expected output (visual):** Square + triangle on a white canvas; window stays open.

---

## Quick Drills

1. **Smaller shapes** — change every `100` to `50`. Run. Did both shapes shrink?
2. **Speed** — try `t.speed(1)` (slow) and `t.speed(0)` (fastest).
3. **Wrong turn** — use `left(90)` for the triangle once. What shape appears instead?

---

## Practice Task

**Quest name:** Shape Sketcher

1. Complete any TODO lines in [starter/shapes.py](starter/shapes.py).
2. Run and confirm you see a square and a triangle.
3. **Bonus:** Add a third shape — a small hexagon (six sides, `left(60)` each time) after the triangle.

**Reference solution:** [solution/shapes.py](solution/shapes.py)

---

## Debug Corner

**Problem:** The turtle window flashes open and closes instantly — you barely see anything.

**Cause:** `turtle.done()` is missing (or commented out). Without it, Python exits and closes the window immediately.

**Fix:** Add this as the **last line** of your script:

```python
turtle.done()
```

Save, run again, and close the window when you are finished.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. How do you load the turtle drawing toolkit?
   - **a)** `pip install turtle`
   - **b)** `import turtle` (stdlib — no pip needed)
   - **c)** `from web import turtle`
   - **d)** `python turtle.py` in the terminal first

2. The turtle window closes instantly after drawing. What is the most likely fix?
   - **a)** Delete `import turtle`
   - **b)** Add `turtle.done()` as the **last line** of the script
   - **c)** Use `print()` instead of `forward()`
   - **d)** Run the file twice

3. How many sides and what turn angle does the lesson use for a **square**?
   - **a)** 3 sides, `left(120)`
   - **b)** 4 sides, `left(90)`
   - **c)** 5 sides, `right(144)`
   - **d)** 6 sides, `left(60)`

4. Why does the triangle loop use `left(120)`?
   - **a)** Because 360 ÷ 3 = 120 degrees per corner
   - **b)** Because turtles only turn 120°
   - **c)** Because `120` is the default speed
   - **d)** Because squares need 120°

5. What do `t.penup()` and `t.pendown()` do together between shapes?
   - **a)** Change the turtle's color
   - **b)** Move without drawing a line between the square and triangle
   - **c)** Close the turtle window
   - **d)** Delete the previous shape

---

<details><summary>Click to reveal answers</summary>

1. **b)** `turtle` is in Python's standard library — just `import turtle`.
2. **b)** `turtle.done()` keeps the window open until you close it.
3. **b)** A square needs 4 repeats of forward + `left(90)`.
4. **a)** Three equal turns of 120° add up to 360° for a closed triangle.
5. **b)** Pen up lifts the pen so the turtle can reposition without a connecting line.

</details>

---

## What's Next

→ [Lesson 5.2: Loops and Color](../lesson-5-2-loops-and-color/README.md) — paint a colorful star with a loop.

---

*You can sketch with code now. Next up: color and patterns!*

[← Choose language](README.md)
