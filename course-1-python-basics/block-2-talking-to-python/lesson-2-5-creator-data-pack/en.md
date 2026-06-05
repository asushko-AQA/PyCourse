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

Before you start, tick the [Block 2 readiness checklist](../../README.md#block-2-readiness-checklist).

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

See [solution/creator_pack.py](solution/creator_pack.py) after you try your own version.

---

## Quick Drills

1. **Checklist** — tick all five items on the Block 2 checklist.
2. **Math without int** — what if you wrote `age = input(...)` and then `age * 365`? Try it briefly — see the error or weird result. Then use `int()`.
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

**Problem:** `TypeError: can't multiply sequence by non-int of type 'str'` (or unexpected huge number when using `+`)

**Cause:** You used `age = input(...)` without `int()`, then tried `age * 365`. Python treated age as text, not a number.

**Fix:** `age = int(input("How old are you? "))` — convert before math.

---

## What's Next

→ [Lesson 3.1: Booleans and Comparisons](../../block-3-making-choices/lesson-3-1-booleans/README.md) — predict true and false in the terminal.

---

*Block 2 complete! Your Creator Data Pack is packed. Time to make choices in Block 3!*

[← Choose language](README.md)
