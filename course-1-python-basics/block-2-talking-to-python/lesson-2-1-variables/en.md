# Lesson 2.1: Variables, Strings, Integers

> **Course:** Python Basics & Command Line Magic · **Block:** Talking to Python · **~30–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 6 — Magic Boxes for Your Data**

---

## Explanation

Welcome to the **Data Lab**! In Block 1 you learned to launch scripts and read errors. Now you learn to **store** information in **variables** — labeled magic boxes that hold your data.

**Already did Level 1's `my_intro.py`?** That script printed text directly. Variables let you **save** data once and use it many times — like putting your name on a locker instead of shouting it every time.

You already know the launch sequence from Block 1. No new install steps — just open, edit, save, `cd`, run.

---

### Step 1: What is a variable?

A **variable** is a labeled box with a name. You put a value inside with `=`:

```python
name = "Alex"
```

- `name` is the label on the box
- `=` means "put this value inside"
- `"Alex"` is the value (text in quotes)

---

### Step 2: Two kinds of boxes

**Strings** — text in quotes:

```python
favorite_game = "Minecraft"
```

**Integers** — whole numbers **without** quotes:

```python
age = 11
```

If you put quotes around a number (`"11"`), Python treats it as text, not math. You will fix that in Lesson 2.3.

---

### Step 3: Open the character sheet

Open [starter/character_sheet.py](starter/character_sheet.py). Three variables are ready — fill in the **TODO `print()` lines** to show your character sheet.

---

### Step 4: cd to this lesson folder

**Path A — PyCourse repo:**

```text
cd course-1-python-basics\block-2-talking-to-python\lesson-2-1-variables
```

**Path B — your own folder:** Open VS Code on any project folder. If `character_sheet.py` is there, you are already in the right place.

---

### Step 5: Run the script

```text
python starter\character_sheet.py
```

**Expected output:**

```text
=== CHARACTER SHEET ===
Name: Alex
Age: 11
Favorite game: Minecraft
Edit the variables above, then run again!
```

---

### Step 6: Reuse a variable

You can use the same variable in many `print()` lines:

```python
print("Name:", name)
print(name, "is ready for adventure!")
```

Change the value in the box once — every `print()` that uses `name` updates automatically.

---

## Code Example

**File: [starter/character_sheet.py](starter/character_sheet.py)**

```python
name = "Alex"
age = 11
favorite_game = "Minecraft"

print("=== CHARACTER SHEET ===")
print("Name:", name)
print("Age:", age)
print("Favorite game:", favorite_game)
```

**No `input()` yet** — you type values directly in the code. Interactive questions come in Lesson 2.2.

---

## Code Execution

```text
cd course-1-python-basics\block-2-talking-to-python\lesson-2-1-variables
python starter\character_sheet.py
```

**Expected output:**

```text
=== CHARACTER SHEET ===
Name: Alex
Age: 11
Favorite game: Minecraft
Edit the variables above, then run again!
```

---

## Quick Drills

1. **Change age** — set `age = 12` (or your age). Run. Did the output match your prediction?
2. **Fourth box** — add `school = "Creator Academy"` and `print("School:", school)`.
3. **Name typo** — change `name` to `nmae` in one `print()`. Run. Read `NameError`. Fix it.

---

## Practice Task

**Quest name:** Your Character Sheet

1. Edit all three variables to **your** real data (or fun fictional data).
2. Add a fourth variable — `school`, `pet`, or `favorite_food`.
3. Add one `print()` that combines two variables with a comma:

```python
print(name, "loves", favorite_game)
```

**Bonus stars:** Add a title line with `===` banners like the example. Try `print("Age next year:", age + 1)` — Python can add 1 to a number!

**Reference solution:** [solution/character_sheet.py](solution/character_sheet.py)

---

## Debug Corner

**Problem:** `NameError: name 'nmae' is not defined`

**Cause:** Python looks for a box labeled `nmae`, but you only created `name`. Variable names must match **exactly** — spelling and capitalization.

**Fix:** Find the typo. Change `nmae` back to `name`. Run again.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. What does the `=` sign do in `name = "Alex"`?
   - **a)** Compares two values
   - **b)** Puts a value inside a labeled variable
   - **c)** Prints text to the screen
   - **d)** Deletes a variable

2. Which line stores a **whole number** correctly?
   - **a)** `age = "11"`
   - **b)** `age = 11`
   - **c)** `age = True`
   - **d)** `11 = age`

3. If you put quotes around a number like `"11"`, Python treats it as…
   - **a)** An integer for math
   - **b)** Text (a string), not a number for math
   - **c)** A True/False value
   - **d)** An error that always stops the program

4. You get `NameError: name 'nmae' is not defined`. What is the most likely cause?
   - **a)** A typo in the variable name (spelling must match exactly)
   - **b)** You forgot to use `input()`
   - **c)** You used `==` instead of `=`
   - **d)** The number was too big

5. You change `name = "Alex"` to `name = "Sam"`. What happens to every `print()` that uses `name`?
   - **a)** They automatically show the new value
   - **b)** They still show "Alex" until you restart the computer
   - **c)** Python deletes the other variables
   - **d)** You must rename every `print()` line by hand

---

<details><summary>Click to reveal answers</summary>

1. **b)** `=` stores a value in a variable (labeled box).
2. **b)** Integers are whole numbers **without** quotes.
3. **b)** Quotes make it text; Lesson 2.3 covers fixing that with `int()`.
4. **a)** Variable names must match exactly; `nmae` ≠ `name`.
5. **a)** Change the value once; every line using that variable updates.

</details>

---

## What's Next

→ [Lesson 2.2: f-strings and input()](../lesson-2-2-f-strings-and-input/README.md) — ask the visitor questions through the mic.

---

*Your data lives in magic boxes now. Next you will ask the user to fill them in!*

[← Choose language](README.md)
