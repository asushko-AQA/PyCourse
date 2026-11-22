# Lesson 2.5: Creator Data Pack (Block 2 Capstone)

> **Course:** Python Basics & Command Line Magic · **Block:** Talking to Python · **~45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 10 — Pack Your Creator Data**

---

## Explanation

Block 2 finale! You will pack **variables**, **input**, **f-strings**, **math**, and **string transforms** into one script — just like Block 1's Mission Control Badge combined launch skills.

Create **`my_data/`** at your **project root** (next to `my_mission/`, not inside this lesson folder). Copy the skeleton into that folder and make it yours.

Before you start, tick the [Block 2 readiness checklist](../README.md#block-2-readiness-checklist).

---

### Step 1: Create my_data folder

**VS Code:** Right-click project root (e.g. `PyCourse`) → **New Folder** → `my_data`

**Or terminal:**

```text
cd Documents\PyCourse
mkdir my_data
```

**Path B:** Create `my_data` on Desktop or inside your own project — same idea as `my_mission`.

---

### Step 2: Copy the skeleton

Open [starter/creator_pack.py](starter/creator_pack.py). Copy or recreate it as **`my_data/creator_pack.py`**.

---

### Step 3: Fill in your pack

Your script should:

1. Print a title banner
2. Ask for name and favorite game (`input()`)
3. Ask for age and convert with `int()`
4. Calculate `days = age * 365` (approximate days on Earth)
5. Create `shout = name.upper()` and print it
6. End with `Block 2 complete!`

---

### Step 4: Run from my_data

```text
cd my_data
python creator_pack.py
```

**Sample output:**

```text
=== CREATOR DATA PACK ===
What is your name? Alex
What is your favorite game? Minecraft
How old are you? 11
Name: Alex
Favorite game: Minecraft
Days on Earth (about): 4015
Shout: ALEX RULES!
Block 2 complete!
```

---

### Step 5: Break and fix

Remove one closing quote in a string. Run — read `SyntaxError`. Fix it. See [exercises/debug_quotes.md](exercises/debug_quotes.md).

---

## Code Example

**File: [solution/creator_pack.py](solution/creator_pack.py)**

```python
print("=== CREATOR DATA PACK ===")

name = input("What is your name? ")
favorite_game = input("What is your favorite game? ")
age = int(input("How old are you? "))

days_on_earth = age * 365

print(f"Name: {name}")
print(f"Favorite game: {favorite_game}")
print(f"Days on Earth (about): {days_on_earth}")
print(f"Shout: {name.upper()} RULES!")
print("Block 2 complete!")
```

---

## Code Execution

```text
cd my_data
python creator_pack.py
```

**Type:** Alex, Minecraft, 11 (or your own answers)

**Expected output:**

```text
=== CREATOR DATA PACK ===
What is your name? Alex
What is your favorite game? Minecraft
How old are you? 11
Name: Alex
Favorite game: Minecraft
Days on Earth (about): 4015
Shout: ALEX RULES!
Block 2 complete!
```

---

## Quick Drills

1. **Checklist** — tick all five items on the Block 2 checklist.
2. **Math without int** — `age = input(...)` then `age * 365` repeats the digits (`1111…`), it does not crash. `age + 1` raises `TypeError: can only concatenate str (not "int") to str`. Then use `int()`.
3. **Shout** — change `RULES!` to your own phrase.

---

## Practice Task

**Quest name:** Creator Data Pack

1. Create `my_data/` at project root.
2. Write 8–12 lines in `creator_pack.py` using all Block 2 skills.
3. Run successfully from `my_data/`.
4. Break one quote, fix it, run again.

**Bonus:** Add one more `input()` — favorite hobby or school — and print it with an f-string.

**Reference solution:** [solution/creator_pack.py](solution/creator_pack.py)

---

## Debug Corner

**Problem:** `days_on_earth` prints a huge string like `111111…` instead of a number — or `TypeError: can only concatenate str (not "int") to str` if you write `age + 1`.

**Cause:** `age = input(...)` is text. `'11' * 365` repeats those characters 365 times (no error). `'11' + 1` cannot add text and a number.

**Fix:** `age = int(input("How old are you? "))` — convert before math.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. Where should you create the `my_data/` folder for this capstone?
   - **a)** In the Python installation folder
   - **b)** Inside the lesson-2-5 folder only
   - **c)** At your **project root** (next to `my_mission/`, not inside the lesson folder)
   - **d)** Nowhere — run only from `starter/`

2. Your script should calculate `days = age * 365`. What must happen to `age` first?
   - **a)** Delete it before multiplying
   - **b)** Leave it as text from `input()`
   - **c)** Wrap it in quotes
   - **d)** Convert it with `int()` after `input()`

3. What does `shout = name.upper()` do?
   - **a)** Stores the name in ALL CAPS
   - **b)** Stores the name in all lowercase
   - **c)** Slices the first three letters
   - **d)** Compares the name to "ALEX"

4. `TypeError: can only concatenate str (not "int") to str` often means…
   - **a)** You forgot a colon after `if`
   - **b)** You wrote `age + 1` while `age` was still text from `input()`
   - **c)** You misspelled a variable name
   - **d)** You used `.upper()` on a number

5. Which Block 2 skills does the Creator Data Pack combine?
   - **a)** Only comparisons and `if` statements
   - **b)** Only Turtle graphics
   - **c)** Variables, `input()`, f-strings, math, and string transforms
   - **d)** Flask routes and HTML templates

---

<details><summary>Click to reveal answers</summary>

1. **c)** Create `my_data/` at project root, like Block 1's `my_mission/`.
2. **d)** Use `int(input(...))` so `age` is a number before `* 365`.
3. **a)** `.upper()` makes the name shout in ALL CAPS.
4. **b)** Text and a number cannot be added with `+`. Convert with `int()` first. (`age * 365` repeats the text instead of raising this error.)
5. **c)** The capstone packs all Block 2 data skills into one script.

</details>

---

## What's Next

→ [Lesson 3.1: Booleans and Comparisons](../../block-3-making-choices/lesson-3-1-booleans/README.md) — predict true and false in the terminal.

---

*Block 2 complete! Your Creator Data Pack is packed. Time to make choices in Block 3!*

[← Choose language](README.md)
