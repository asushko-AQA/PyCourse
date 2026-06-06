# Lesson 5.3: Functions and Turtle

> **Course:** Python Basics & Command Line Magic · **Block:** Creative Python with Turtle · **~30–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 21 — Snowflake Builder**

---

## Explanation

You learned **functions** in Block 4 — reusable recipes with parameters. Now you combine functions with turtle to draw a **snowflake branch**: one main arm and one side arm, built from the same `draw_branch(length)` recipe.

```python
def draw_branch(length):
    t.forward(length)
    t.backward(length)
```

Everything **indented under** `def` belongs to the function. Call it twice with turns between:

```python
draw_branch(100)
t.left(60)
draw_branch(70)
```

The function draws a line forward, then back — so the turtle returns to the joint and can turn for the next branch.

---

### Step 1: Open snowflake.py

Open [starter/snowflake.py](starter/snowflake.py). Complete the TODO section after `draw_branch`.

---

### Step 2: Run

**Path A:**

```text
cd course-1-python-basics\block-5-creative-turtle\lesson-5-3-functions-and-turtle
python starter\snowflake.py
```

**Path B:** Copy `snowflake.py` to your folder. See [STUDENT-MAP](../../STUDENT-MAP.md).

**Expected output (visual):**

- Light blue **Y-shaped** branch on a white canvas (main stem up, one side branch at 60°).
- Turtle window stays open until you close it or press **Ctrl+C** in the terminal.

---

## Code Example

**File: [starter/snowflake.py](starter/snowflake.py)**

```python
import turtle

t = turtle.Turtle()
t.speed(3)
t.color("deepskyblue")
t.width(3)


def draw_branch(length):
    t.forward(length)
    t.backward(length)


t.left(90)

draw_branch(100)

t.left(60)
draw_branch(70)

turtle.done()
```

---

## Code Execution

```text
cd course-1-python-basics\block-5-creative-turtle\lesson-5-3-functions-and-turtle
python starter\snowflake.py
```

**Expected output (visual):** Blue Y-shaped snowflake branch; window stays open.

---

## Quick Drills

1. **Longer stem** — change the first call to `draw_branch(150)`.
2. **Thicker lines** — try `t.width(5)`.
3. **Bonus patterns** — open [exercises/branch_variations.md](exercises/branch_variations.md) for a six-arm snowflake idea.

---

## Practice Task

**Quest name:** Snowflake Builder

1. Make sure `draw_branch` is indented correctly and called **twice** with a `left()` turn between.
2. Run and confirm the Y shape looks right.
3. **Bonus:** Add a second side branch on the other side with `t.right(120)` and a third `draw_branch(70)` call.

**Reference solution:** [solution/snowflake.py](solution/snowflake.py)

---

## Block 5 capstone — Turtle Gallery (`my_gallery/`)

Show your best Turtle art in one script:

1. Create **`my_gallery/`** at project root.
2. Copy [starter/gallery.py](starter/gallery.py) → **`my_gallery/gallery.py`**.
3. Run — you should see a **colorful star** and a **snowflake** in the same window.

```text
cd my_gallery
python gallery.py
```

**Reference:** [solution/gallery.py](solution/gallery.py)

Complete the [Course 1 graduation checklist](../../STUDENT-MAP.md#course-1-graduation-checklist) — run all five capstone folders!

---

## Debug Corner

**Problem:** The turtle draws lines in the wrong place — branches stick out from random spots, not from one center.

**Cause:** Code inside `def draw_branch` is **not indented**. Python thinks `forward` and `backward` run at the top level, not inside the function.

**Wrong:**

```python
def draw_branch(length):
t.forward(length)
t.backward(length)
```

**Error:** `IndentationError: expected an indented block after function definition`

**Fix:** Indent every line inside the function with **four spaces**:

```python
def draw_branch(length):
    t.forward(length)
    t.backward(length)
```

Save and run again.

---

## What's Next

→ [Course 2: Web Applications with Python](../../../../course-2-web-apps/README.md) — you finished Course 1! Next: Flask and web pages.

---

*Course 1 complete — you draw with code, loop, color, and functions. Web apps await!*

[← Choose language](README.md)
