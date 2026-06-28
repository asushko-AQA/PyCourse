# Lesson 4.3: Dictionaries

> **Course:** Python Basics & Command Line Magic · **Block:** Organizing Code · **~30–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 17 — Character Stat Sheet**

---

## Explanation

Lists use **number slots** (0, 1, 2…). A **dictionary** uses **name tags** — each value has a **key** you choose:

```python
character = {
    "name": "Alex",
    "level": 5,
    "hp": 42,
}
```

Think of it as a character sheet with labeled boxes: `"name"`, `"level"`, `"hp"`.

Read a value with square brackets:

```python
print(character["hp"])
```

**Path A — PyCourse repo:**

```text
cd course-1-python-basics\block-4-organizing-code\lesson-4-3-dictionaries
```

**Path B — your own folder:** Copy [starter/character_stats.py](starter/character_stats.py) anywhere. Run from that folder.

---

### Step 1: Open character_stats.py

Open [starter/character_stats.py](starter/character_stats.py). Three stats are already filled in.

---

### Step 2: Print known keys

The script uses `character["name"]`, `character["level"]`, and `character["hp"]`. Change the values and run again.

---

### Step 3: Safe lookup with .get()

What if `"magic"` is not on the sheet yet? Brackets crash with `KeyError`. **`.get()`** returns a default instead:

```python
magic = character.get("magic", 0)
print(f"Magic: {magic}")
```

If `"magic"` is missing, you get `0` — no crash.

---

### Step 4: Run the script

```text
python starter\character_stats.py
```

**Mac/Linux:** Use forward slashes — `python starter/character_stats.py`. List files with `ls` instead of `dir`.

**Expected output:**

```text
=== CHARACTER STATS ===
Name: Alex
Level: 5
HP: 42
Magic: 0
Special skill: none
Edit the dict keys above, then run again!
```

---

## Code Example

**File: [starter/character_stats.py](starter/character_stats.py)**

```python
character = {
    "name": "Alex",
    "level": 5,
    "hp": 42,
}

print("=== CHARACTER STATS ===")
print(f"Name: {character['name']}")
print(f"Level: {character['level']}")
print(f"HP: {character['hp']}")

magic = character.get("magic", 0)
print(f"Magic: {magic}")

skill = character.get("skill", "none")
print(f"Special skill: {skill}")
```

---

## Code Execution

```text
cd course-1-python-basics\block-4-organizing-code\lesson-4-3-dictionaries
python starter\character_stats.py
```

No keyboard input — output appears immediately.

---

## Quick Drills

1. **Add MP** — put `"mp": 10` in the dict and print `f"MP: {character['mp']}"`.
2. **Typo trap** — change `"hp"` to `"hpp"` in one print line. Run. Read `KeyError`. Fix it.
3. **Default power** — add `"power": 7` and print it with `.get("power", 1)`.

---

## Practice Task

**Quest name:** Your Hero Sheet

1. Change all three stats to your hero (real or fictional).
2. Add two new keys — `"class"` and `"gold"`.
3. Use `.get()` for `"pet"` with default `"none"` even if you never add a `"pet"` key.

**Bonus quest:** See [exercises/phonebook_lookup.md](exercises/phonebook_lookup.md) for a mini phonebook challenge.

**Reference solution:** [solution/character_stats.py](solution/character_stats.py)

---

## Debug Corner

**Problem:** `KeyError: 'magc'` when you write `character["magc"]`.

**Cause:** Dictionary keys must match **exactly** — spelling matters. You asked for `"magc"` but only `"magic"` exists (or the key was never added).

**Fix:** Check the key name inside `{ }`. Use `.get("magic", 0)` when a key might be missing.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. How is a dictionary different from a list?
   - **a)** A dictionary uses **name tags (keys)** instead of only number slots
   - **b)** A dictionary cannot store text
   - **c)** A dictionary has no values
   - **d)** A dictionary always has exactly three items

2. How do you read the hero's HP from `character = {"hp": 42}`?
   - **a)** `character(42)`
   - **b)** `character["hp"]`
   - **c)** `character.hp`
   - **d)** `hp[character]`

3. What does `character.get("magic", 0)` do if `"magic"` is **not** in the dict?
   - **a)** Crashes with KeyError
   - **b)** Returns `0` without crashing
   - **c)** Deletes the dictionary
   - **d)** Adds `"magic"` automatically

4. You write `character["magc"]` but the key is `"magic"`. What error appears?
   - **a)** SyntaxError
   - **b)** KeyError
   - **c)** IndexError
   - **d)** No error — Python guesses the key

5. When should you prefer `.get()` over square brackets `[]`?
   - **a)** When the key might be missing and you want a safe default
   - **b)** When you never want to read values
   - **c)** Only for lists, not dicts
   - **d)** When you want Python to ignore typos

---

<details><summary>Click to reveal answers</summary>

1. **a)** Dicts pair **keys** (labels like `"hp"`) with values — lists use numbered indexes.
2. **b)** Square brackets with the exact key name: `character["hp"]`.
3. **b)** `.get()` returns the default (`0`) when the key is missing — no crash.
4. **b)** Keys must match **exactly**; a typo triggers `KeyError`.
5. **a)** Use `.get(key, default)` when a key might not exist yet on the stat sheet.

</details>

---

## What's Next

→ [Lesson 4.4: Text Adventure Capstone](../lesson-4-4-text-adventure-capstone/README.md) — combine functions, lists, and dicts in one game.

---

*Your stat sheet has labeled boxes now. Next you will build a room-based adventure!*

[← Choose language](README.md)
