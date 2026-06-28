# Pattern Variations — Stretch Challenges

**Lesson:** 3.4 · **Block:** Making Choices

---

## Variation 1: Square grid

Print a 5×5 grid of stars (5 rows, 5 stars each):

```text
*****
*****
*****
*****
*****
```

**Hint:** Outer loop `range(5)`, inner loop also `range(5)`.

---

## Variation 2: Number pyramid

Print row numbers instead of stars:

```text
1
22
333
4444
55555
```

**Hint:** `print(row, end="")` in the inner loop.

---

## Variation 3: break early

Use `break` to stop the outer loop after row 3 — only 3 rows print.

**Hint:** `if row == 3: break` inside the outer loop (after printing the row).
