# Lesson 2.4: Strings in Action

> **Course:** Python Basics & Command Line Magic · **Block:** Talking to Python · **~30–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 9 — Story Factory**

---

## Explanation

Welcome to the **Story Factory**! Strings are not just boxes — they are clay you can shape. Three transformer tools:

| Tool | What it does | Example |
|------|--------------|---------|
| `.upper()` | ALL CAPS | `"hi".upper()` → `HI` |
| `.lower()` | all lowercase | `"HI".lower()` → `hi` |
| `[0:3]` | slice first 3 letters | `"Alex"[0:3]` → `Ale` |

This lesson uses a **brand new script** — `madlibs.py`. It is not an extension of `greeting.py` from Lesson 2.2.

---

### Step 1: Collect words with input()

Ask for a hero, a silly creature, a place, and a superpower — four magic boxes for your battle story.

---

### Step 2: Transform in the story

```python
short_creature = creature[0:3]

print(f"{hero} battled a {creature.lower()} in {place}.")
print(f"The creature's first three letters: {short_creature}")
print(f"{hero} used {power.upper()} to win!")
```

- `.lower()` on the creature name keeps it silly but readable.
- `.upper()` on the superpower makes the final move feel dramatic.
- `[0:3]` slices the first three letters of the creature for a quick preview.

---

### Step 3: Run madlibs.py

**Path A:**

```text
cd course-1-python-basics\block-2-talking-to-python\lesson-2-4-strings-in-action
python starter\madlibs.py
```

**Path B:** Copy `madlibs.py` to any folder you control, `cd` there, then run `python madlibs.py`. See [STUDENT-MAP](../../STUDENT-MAP.md).

**Mac/Linux:** `python starter/madlibs.py` (forward slashes).

**Sample input:** Sam, dragon, castle, laser

**Expected output (story varies with your words):**

```text
=== STORY FACTORY ===
Sam battled a dragon in castle.
The creature's first three letters: dra
Sam used LASER to win!
The end.
```

---

## Code Example

See [starter/madlibs.py](starter/madlibs.py) — four inputs, `.upper()`, `.lower()`, and one slice.

---

## Quick Drills

1. **Upper predict** — what does `"minecraft".upper()` produce? Check in Python.
2. **Slice** — complete [exercises/slice_challenge.md](exercises/slice_challenge.md).
3. **Re-run** — play madlibs three times with different themes (space, school, sports).

---

## Practice Task

**Quest name:** Your Story Template

1. Complete all TODO lines in [starter/madlibs.py](starter/madlibs.py).
2. Run with your own silly words.
3. **Bonus:** Write a **new** 3-sentence story template in a copy of the file — keep `.upper()` on one word and a slice on another.

**Reference solution:** [solution/madlibs.py](solution/madlibs.py)

---

## Debug Corner

**Problem:** `IndexError: string index out of range` on `creature[5]` (single index, not slice)

**Cause:** You asked for a letter position that does not exist. A 3-letter word only has indices 0, 1, 2.

**Fix:** Use slicing `[0:3]` — it safely stops at the end. Or check the string length before using a high index.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. What does `"minecraft".upper()` produce?
   - **a)** `minecraft`
   - **b)** `MINECRAFT`
   - **c)** `Minecraft`
   - **d)** An error

2. What does `"Alex"[0:3]` produce?
   - **a)** `Alex`
   - **b)** `Ale`
   - **c)** `lex`
   - **d)** `A`

3. In this lesson, `madlibs.py` is…
   - **a)** A brand-new script (not an extension of `greeting.py`)
   - **b)** A copy of `character_sheet.py`
   - **c)** A file that only uses integers
   - **d)** A web browser app

4. Why might `creature[5]` cause `IndexError` on a short creature name?
   - **a)** You asked for a letter position that does not exist
   - **b)** You forgot the `f` in an f-string
   - **c)** You used `==` instead of `=`
   - **d)** You forgot a colon after `if`

5. In the sample story, `power.upper()` makes the superpower…
   - **a)** ALL CAPS for a dramatic final move
   - **b)** all lowercase
   - **c)** Only the first three letters
   - **d)** Disappear from the story

---

<details><summary>Click to reveal answers</summary>

1. **b)** `.upper()` makes ALL CAPS.
2. **b)** `[0:3]` slices the first three letters: `Ale`.
3. **a)** The lesson uses a new `madlibs.py` script.
4. **a)** A 3-letter word only has indices 0, 1, 2; use `[0:3]` for safe slicing.
5. **a)** `.upper()` on the superpower makes it feel epic (e.g. `LASER`).

</details>

---

## What's Next

→ [Lesson 2.5: Creator Data Pack](../lesson-2-5-creator-data-pack/README.md) — pack all Block 2 skills into one capstone.

---

*Your Story Factory is open. One more quest to complete Block 2!*

[← Choose language](README.md)
