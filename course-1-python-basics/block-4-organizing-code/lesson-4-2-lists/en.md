# Lesson 4.2: Lists

> **Course:** Python Basics & Command Line Magic · **Block:** Organizing Code · **~30–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 16 — Adventure Inventory Pack**

---

## Explanation

Every adventurer needs a **backpack**. In Python, a **list** is an ordered collection — like slots in a bag where each item has a position number called an **index**.

```python
inventory = ["torch", "rope"]
```

- Index `0` is `"torch"` (first item)
- Index `1` is `"rope"` (second item)

Use `.append()` to add a new item to the end:

```python
inventory.append("key")
```

**Path A — PyCourse repo:**

```text
cd course-1-python-basics\block-4-organizing-code\lesson-4-2-lists
```

**Path B — your own folder:** Copy [starter/inventory.py](starter/inventory.py) anywhere. Run from that folder.

---

### Step 1: Open inventory.py

Open [starter/inventory.py](starter/inventory.py). Two items are already in the backpack.

---

### Step 2: Add an item

Uncomment or complete the `.append("key")` line. The list grows by one slot.

---

### Step 3: Print a numbered list

Use a `for` loop with `range(len(inventory))` to visit each index:

```python
for i in range(len(inventory)):
    print(f"{i + 1}. {inventory[i]}")
```

We add 1 to `i` so players see `1. torch` instead of `0. torch`.

---

### Step 4: Run the script

```text
python starter\inventory.py
```

**Mac/Linux:** Use forward slashes — `python starter/inventory.py`. List files with `ls` instead of `dir`.

**Expected output:**

```text
=== INVENTORY ===
1. torch
2. rope
3. key
You are carrying 3 items.
```

---

## Code Example

**File: [starter/inventory.py](starter/inventory.py)**

```python
inventory = ["torch", "rope"]
inventory.append("key")

print("=== INVENTORY ===")

for i in range(len(inventory)):
    print(f"{i + 1}. {inventory[i]}")

print(f"You are carrying {len(inventory)} items.")
```

---

## Code Execution

```text
cd course-1-python-basics\block-4-organizing-code\lesson-4-2-lists
python starter\inventory.py
```

No keyboard input — output appears immediately.

---

## Quick Drills

1. **Pack more gear** — `.append("map")` and `.append("potion")`. How many items now?
2. **First slot** — add `print("First item:", inventory[0])` before the loop.
3. **Empty list** — start with `inventory = []` and append three items yourself.

---

## Practice Task

**Quest name:** Full Adventure Pack

1. Start with at least four items that fit your adventure theme.
2. Print a title banner with `=== INVENTORY ===`.
3. After the numbered list, print the **last** item using a negative index: `inventory[-1]`.

**Bonus quest:** See [exercises/high_score.md](exercises/high_score.md) for a high-score list stretch challenge.

**Reference solution:** [solution/inventory.py](solution/inventory.py)

---

## Debug Corner

**Problem:** `IndexError: list index out of range` when you print `inventory[3]` but the list only has three items (indexes 0, 1, 2).

**Cause:** List indexes start at **0**. A list with 3 items has indexes `0`, `1`, and `2` — not `3`.

**Fix:** Use `inventory[-1]` for the last item, or `len(inventory) - 1` for the last index. Count slots before you pick a number.

---

## What's Next

→ [Lesson 4.3: Dictionaries](../lesson-4-3-dictionaries/README.md) — store character stats with labeled keys.

---

*Your backpack is organized. Next you will label stat boxes with dictionaries!*

[← Choose language](README.md)
