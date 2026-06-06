# Lesson 3.3: for and while loops

> **Course:** Python Basics & Command Line Magic · **Block:** Making Choices · **~45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 13 — Countdown and March**

---

## Explanation

Sometimes one line is not enough — you need a **repeat button**. Python has two loop styles:

| Loop | Analogy | Use when |
|------|---------|----------|
| `while` | Timer counting down | Repeat **until** something becomes False |
| `for` + `range()` | March through checkpoints | Repeat a **fixed number** of times |

**This lesson has two scripts.** Run each separately!

---

## Part A — countdown.py (while loop)

A **`while`** loop checks a condition **before** each repeat:

```python
counter = 5
while counter > 0:
    print(counter)
    counter = counter - 1
print("Blastoff!")
```

**Path A:**

```text
cd course-1-python-basics\block-3-making-choices\lesson-3-3-for-and-while-loops
python starter\countdown.py
```

**Mac/Linux:** Use forward slashes — `python starter/countdown.py`. List files with `ls` instead of `dir`.

**Path B:** Copy `countdown.py` anywhere; `cd` there first.

**Expected output:**

```text
=== COUNTDOWN ===
5
4
3
2
1
Blastoff!
```

---

## Part B — times_table.py (for loop)

A **`for`** loop walks through numbers from `range()`:

```python
number = 3
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
```

**Run:**

```text
python starter\times_table.py
```

**Expected output:**

```text
=== TIMES TABLE ===
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
Table complete!
```

`range(1, 11)` gives 1 through 10 — the **stop** number is **not** included.

---

## Code Example

**while:** [starter/countdown.py](starter/countdown.py)  
**for:** [starter/times_table.py](starter/times_table.py)

---

## Code Execution

Run **both** scripts from the lesson folder (Path A) or from your copy folder (Path B).

---

## Quick Drills

1. In countdown, start at `10` instead of `5`.
2. In times_table, change `number` to `7` — predict line `7 x 4 = ?`.
3. Add `print("Get ready...")` before the while loop.

---

## Practice Task

1. Make countdown print `"Liftoff!"` instead of `"Blastoff!"`.
2. Make times_table print only rows where `i` is even (hint: `if i % 2 == 0:`).
3. Try [exercises/loop_drills.md](exercises/loop_drills.md) for bonus loops.

**Reference solutions:** [solution/countdown.py](solution/countdown.py) · [solution/times_table.py](solution/times_table.py)

---

## Debug Corner

**Problem:** Terminal prints `5` forever (or until you press Ctrl+C).

**Cause:** **Infinite loop** — the `while` condition stays True because you forgot to update `counter` inside the loop.

**Fix:** Make sure every `while` loop has a line that moves toward stopping — here `counter = counter - 1`. Press **Ctrl+C** to stop a runaway loop.

---

## What's Next

→ [Lesson 3.4: Loop Patterns](../lesson-3-4-loop-patterns/README.md) — nested loops and ASCII art!

---

[← Choose language](README.md)
