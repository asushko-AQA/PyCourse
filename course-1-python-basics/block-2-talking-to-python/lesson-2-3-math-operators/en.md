# Lesson 2.3: Math Operators

> **Course:** Python Basics & Command Line Magic · **Block:** Talking to Python · **~30–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 8 — Calculator Spells**

---

## Explanation

Time for **calculator spells**! Python can add, subtract, multiply, and divide numbers — but remember: `input()` gives you **text**. Wrap it with `int()` to turn typed digits into real numbers.

| Operator | Meaning | Example |
|----------|---------|---------|
| `+` | Add | `5 + 3` → `8` |
| `-` | Subtract | `5 - 3` → `2` |
| `*` | Multiply | `5 * 3` → `15` |
| `/` | Divide | `10 / 4` → `2.5` |

**Note:** `/` always produces a decimal when needed. We skip `//` and `%` for now — those come later.

---

### Step 1: Convert input with int()

```python
num1 = int(input("Enter the first number: "))
```

You type `7`, press Enter, and `num1` holds the **number** 7, not the text `"7"`.

---

### Step 2: Open calculator.py

Open [starter/calculator.py](starter/calculator.py). The `Sum:` line is already written as an example. Your TODOs:

1. **TODO 1–2:** Replace the placeholders `0` and `1` with `int(input(...))`, like Step 1. Prompts: `"Enter the first number: "` and `"Enter the second number: "`.
2. **TODO 3–5:** Copy the pattern of the `Sum:` line to print `Difference:` (`-`), `Product:` (`*`), and `Quotient:` (`/`).

Save the file (**Ctrl+S**).

---

### Step 3: Run

**Path A:**

```text
cd course-1-python-basics\block-2-talking-to-python\lesson-2-3-math-operators
python starter\calculator.py
```

**Mac/Linux:** Use forward slashes — `python starter/calculator.py`. List files with `ls` instead of `dir`.

**Type:** `10` then `3`

**Expected output:**

```text
=== CALCULATOR SPELLS ===
Sum: 13
Difference: 7
Product: 30
Quotient: 3.3333333333333335
Calculator complete!
```

The script did not ask you for numbers and printed `Sum: 1`? TODO 1–2 are not done yet — go back to Step 2.

---

## Code Example

**File: [solution/calculator.py](solution/calculator.py)**

```python
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("=== CALCULATOR SPELLS ===")
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)

print("Calculator complete!")
```

---

## Code Execution

```text
cd course-1-python-basics\block-2-talking-to-python\lesson-2-3-math-operators
python solution\calculator.py
```

**Mac/Linux:** `python solution/calculator.py`

**Type:** `10` then `3`

**Expected output:**

```text
=== CALCULATOR SPELLS ===
Sum: 13
Difference: 7
Product: 30
Quotient: 3.3333333333333335
Calculator complete!
```

---

## Quick Drills

1. **Predict** — before running, guess all four results for `8` and `2`.
2. **Mental math sheet** — complete [exercises/mental_math.md](exercises/mental_math.md).
3. **Bad input** — type `hello` instead of a number. Read `ValueError`. Run again with real numbers.

---

## Practice Task

**Quest name:** Calculator Spells

1. Complete all five TODOs in [starter/calculator.py](starter/calculator.py) (Step 2).
2. Run with your birth month and birth day as the two numbers.
3. **Bonus — Quick calc:** Make a shorter version that only prints **sum** and **product** (two operations instead of four).

**Reference solution:** [solution/calculator.py](solution/calculator.py)

---

## Debug Corner

**Problem:** `ValueError: invalid literal for int() with base 10: 'hello'`

**Cause:** `int()` expected digits but got text. `input()` always returns a string — if it is not a valid whole number, conversion fails.

**Fix:** Type only numbers like `5` or `12`. No letters or decimals for now.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. What is `10 / 4` in Python?
   - **a)** `2.5`
   - **b)** `3`
   - **c)** `2` with no decimal
   - **d)** `2`

2. What is `5 * 3`?
   - **a)** `8`
   - **b)** `15`
   - **c)** `53`
   - **d)** `2`

3. Why wrap `input()` with `int()` before adding numbers?
   - **a)** Because `input()` only works with letters
   - **b)** Because Python cannot add any numbers
   - **c)** Because `input()` gives text, and `int()` turns digits into a real number
   - **d)** Because `int()` makes strings uppercase

4. You type `hello` when the program expects a number. What error appears?
   - **a)** `NameError`
   - **b)** `IndexError`
   - **c)** `SyntaxError`
   - **d)** `ValueError`

5. For inputs `10` and `3`, what is the **difference** (`num1 - num2`)?
   - **a)** `7`
   - **b)** `30`
   - **c)** `3.333…`
   - **d)** `13`

---

<details><summary>Click to reveal answers</summary>

1. **a)** `/` can produce a decimal (`2.5`).
2. **b)** `*` means multiply: `5 * 3 = 15`.
3. **c)** `input()` returns a string; `int()` converts valid whole-number text.
4. **d)** `int()` cannot convert non-digit text like `hello`.
5. **a)** `10 - 3 = 7` (matches the lesson's calculator example).

</details>

---

## What's Next

→ [Lesson 2.4: Strings in Action](../lesson-2-4-strings-in-action/README.md) — transform text with `.upper()` and slicing.

---

*Numbers obey your spells now. Next: the Story Factory!*

[← Choose language](README.md)
