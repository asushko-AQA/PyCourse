# Branch Variations (Bonus) — Lesson 5.3

> [Русский →](branch_variations.ru.md)

You built a **Y-shaped** branch with `draw_branch(length)`. Real snowflakes often have **six** arms. Here is a stretch pattern using a loop and your function.

---

## Idea: six arms in a loop

After your `draw_branch` function works, try this pattern **instead of** the two manual calls:

```python
for arm in range(6):
    draw_branch(80)
    t.left(60)
```

**Expected output (visual):** Six blue spokes like a wheel or snowflake hub.

---

## Challenge 1 — Symmetric sides

Keep the Y shape but add a branch on **both** sides of the main stem:

```python
draw_branch(100)

t.left(60)
draw_branch(70)

t.right(120)
draw_branch(70)
```

Draw on paper first — predict where the turtle ends up.

---

## Challenge 2 — Nested branches (advanced)

Inside `draw_branch`, after `forward(length)`, add tiny side twigs:

```python
def draw_branch(length):
    t.forward(length / 2)
    t.left(45)
    t.forward(length / 4)
    t.backward(length / 4)
    t.right(90)
    t.forward(length / 4)
    t.backward(length / 4)
    t.left(45)
    t.forward(length / 2)
    t.backward(length)
```

This is longer than Course 1 usually goes — treat it as a **bonus quest** for fast finishers.

---

## Your turn

Pick one challenge, save a copy as `snowflake_bonus.py`, and show a parent or friend.

[← Lesson 5.3](../README.md)
