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

Open [starter/calculator.py](starter/calculator.py). Two inputs and four print lines await.

---

### Step 3: Run

**Path A:**

```text
cd course-1-python-basics\block-2-talking-to-python\lesson-2-3-math-operators
python starter\calculator.py
```

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

## Code Example

```python
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)
```

---

## Quick Drills

1. **Predict** — before running, guess all four results for `8` and `2`.
2. **Mental math sheet** — complete [exercises/mental_math.md](exercises/mental_math.md).
3. **Bad input** — type `hello` instead of a number. Read `ValueError`. Run again with real numbers.

---

## Practice Task

**Quest name:** Calculator Spells

1. Complete all four print lines in [starter/calculator.py](starter/calculator.py).
2. Run with your birth month and birth day as the two numbers.
3. **Bonus — Quick calc:** Make a shorter version that only prints **sum** and **product** (two operations instead of four).

**Reference solution:** [solution/calculator.py](solution/calculator.py)

---

## Debug Corner

**Problem:** `ValueError: invalid literal for int() with base 10: 'hello'`

**Cause:** `int()` expected digits but got text. `input()` always returns a string — if it is not a valid whole number, conversion fails.

**Fix:** Type only numbers like `5` or `12`. No letters or decimals for now.

---

## What's Next

→ [Lesson 2.4: Strings in Action](../lesson-2-4-strings-in-action/README.md) — transform text with `.upper()` and slicing.

---

*Numbers obey your spells now. Next: the Story Factory!*

[← Choose language](README.md)
