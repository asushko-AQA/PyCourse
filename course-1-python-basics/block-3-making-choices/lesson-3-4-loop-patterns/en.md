# Lesson 3.4: Loop Patterns

> **Course:** Python Basics & Command Line Magic · **Block:** Making Choices · **~30–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 14 — Star Grid Pattern**

---

## Explanation

**Block 3 finale!** You combine loops to draw patterns in the terminal — like a quest gate made of stars.

**Nested loops:** an **outer** loop picks the row; an **inner** loop prints stars on that row.

```python
for row in range(1, 6):
    for star in range(row):
        print("*", end="")
    print()
```

- `range(1, 6)` → rows 1, 2, 3, 4, 5 (6 is **not** included)
- Inner `range(row)` prints `row` stars on one line
- `print()` with no arguments starts a **new line**
- `end=""` keeps stars on the same line

**`break`** exits a loop early — emergency exit from a repeat:

```python
for row in range(1, 10):
    if row == 4:
        break
    print(row)
# prints 1, 2, 3 — stops at 4 before printing it
```

See [exercises/pattern_variations.md](exercises/pattern_variations.md) Variation 3 for practice.

---

### Step 1: Open ascii_pattern.py

Open [starter/ascii_pattern.py](starter/ascii_pattern.py). Complete the `# TODO` loops.

---

### Step 2: cd and run

**Path A:**

```text
cd course-1-python-basics\block-3-making-choices\lesson-3-4-loop-patterns
python starter\ascii_pattern.py
```

**Mac/Linux:** Use forward slashes — `python starter/ascii_pattern.py`. List files with `ls` instead of `dir`.

**Path B:** Copy `ascii_pattern.py` anywhere; `cd` there first.

**Expected output:**

```text
=== ASCII PATTERN ===
*
**
***
****
*****
Pattern complete!
```

---

## Code Example

See [starter/ascii_pattern.py](starter/ascii_pattern.py) and [solution/ascii_pattern.py](solution/ascii_pattern.py).

---

## Code Execution

```text
cd course-1-python-basics\block-3-making-choices\lesson-3-4-loop-patterns
python starter\ascii_pattern.py
```

---

## Quick Drills

1. Change outer loop to `range(1, 4)` — predict 3 rows, run to check.
2. Replace `"*"` with `"#"` for a hash pyramid.
3. Add a title line `print("Row:", row)` inside the outer loop — read the extra output.

---

## Practice Task

**Quest name:** Pattern Master

1. Draw a **6-row** pyramid (`range(1, 7)`).
2. Try a **square** — inner loop always `range(5)` (see exercises).
3. Tick every box on the [Block 3 readiness checklist](../README.md#block-3-readiness-checklist).

**Bonus:** [exercises/pattern_variations.md](exercises/pattern_variations.md)

**Reference solution:** [solution/ascii_pattern.py](solution/ascii_pattern.py)

---

## Block 3 capstone — Quest Gate (`my_quest/`)

Combine `if`, `while`, and `input()` in one game:

1. Create **`my_quest/`** at project root (next to `my_data/`).
2. Copy [starter/gate_quest.py](starter/gate_quest.py) → **`my_quest/gate_quest.py`**.
3. Run:

```text
cd my_quest
python gate_quest.py
```

Guess the secret number (1–10) in three tries. Uses `random.randint` — a new Python tool for random picks.

**Reference:** [solution/gate_quest.py](solution/gate_quest.py)

Tick the [Block 3 readiness checklist](../README.md#block-3-readiness-checklist) when done.

---

## Debug Corner

**Problem:** Pyramid has one too many or too few rows.

**Cause:** **Off-by-one in `range()`** — `range(1, 5)` gives 4 rows, not 5. The **stop** number is never included.

**Fix:** For 5 rows use `range(1, 6)`. Count: 1, 2, 3, 4, 5 — then 6 stops the loop.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. In a nested star pyramid, the **outer** loop usually picks the…
   - **a)** Row number
   - **b)** Random user input
   - **c)** File name on disk
   - **d)** True/False comparison result

2. How many rows does `for row in range(1, 6):` create?
   - **a)** 5 rows (1, 2, 3, 4, 5)
   - **b)** 6 rows
   - **c)** 4 rows
   - **d)** 10 rows

3. What does `print("*", end="")` do?
   - **a)** Prints a star **on the same line** (no new line yet)
   - **b)** Always starts a new line after each star
   - **c)** Converts `*` to an integer
   - **d)** Stops the loop immediately

4. Why use `range(1, 6)` for a **5-row** pyramid?
   - **a)** The stop number (6) is **not** included — you get 1 through 5
   - **b)** Python always skips the first row
   - **c)** `range(1, 6)` means "repeat 6 times starting at 0"
   - **d)** Slicing requires 6 rows minimum

5. What does `break` do inside a loop?
   - **a)** Exits the loop early
   - **b)** Repeats the loop forever
   - **c)** Converts text to uppercase
   - **d)** Indents the next line

---

<details><summary>Click to reveal answers</summary>

1. **a)** Outer loop = row; inner loop prints stars on that row.
2. **a)** `range(1, 6)` → 1, 2, 3, 4, 5 (6 is excluded).
3. **a)** `end=""` keeps stars on one line; bare `print()` starts a new line.
4. **a)** Off-by-one rule: for 5 rows, stop at 6.
5. **a)** `break` is an emergency exit from the loop.

</details>

---

## What's Next

→ [Lesson 4.1: Functions with def](../../block-4-organizing-code/lesson-4-1-functions/README.md) — reusable workshop recipes in Block 4!

---

*Quest Gate complete! Organize your code in the Adventure Workshop next.*

[← Choose language](README.md)
