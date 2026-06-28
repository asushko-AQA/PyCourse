# Lesson 3.2: if, elif, else

> **Course:** Python Basics & Command Line Magic · **Block:** Making Choices · **~30–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 12 — Fork in the Quest Path**

---

## Explanation

In Lesson 3.1 you **printed** True or False. Now you **act** on those results with **`if`** — a fork in the quest path.

| Keyword | When it runs |
|---------|--------------|
| `if` | First check — if True, run this block |
| `elif` | Else-if — try the next check |
| `else` | Catch-all when nothing above matched |

**Rules that trip up everyone:**

1. Put a **colon** `:` at the end of every `if`, `elif`, and `else` line
2. **Indent** the code inside each branch (4 spaces)

```python
if choice == "left":
    print("Crystal found!")
elif choice == "right":
    print("Robot guide!")
else:
    print("Snack break!")
```

Only **one** branch runs — the first match wins.

---

### Step 1: Open choose_path.py

Open [starter/choose_path.py](starter/choose_path.py). Fill in the `# TODO` branches.

---

### Step 2: cd to this lesson folder

**Path A — PyCourse repo:**

```text
cd course-1-python-basics\block-3-making-choices\lesson-3-2-if-elif-else
```

**Path B:** Copy `choose_path.py` anywhere. `cd` to that folder before running.

---

### Step 3: Run and choose

```text
python starter\choose_path.py
```

**Mac/Linux:** Use forward slashes — `python starter/choose_path.py`. List files with `ls` instead of `dir`.

**Type:** `left`

**Expected output:**

```text
=== CHOOSE YOUR PATH ===
You stand at a fork in the quest trail.
Go left or right? (left/right): left
You find a glowing crystal! +10 quest points.
Thanks for choosing!
```

**Type:** `right` — robot guide line. **Type:** anything else — snack break line.

---

## Code Example

```python
choice = input("Go left or right? (left/right): ").lower().strip()

if choice == "left":
    print("You find a glowing crystal! +10 quest points.")
elif choice == "right":
    print("You meet a friendly robot guide. It waves hello.")
else:
    print("You sit down for a snack. Adventure can wait!")
```

**Tip:** `.lower()` turns `"Left"` into `"left"` so your branches still match.

---

## Code Execution

```text
cd course-1-python-basics\block-3-making-choices\lesson-3-2-if-elif-else
python starter\choose_path.py
```

Try `left`, `right`, and `snack` as inputs.

---

## Quick Drills

1. **Predict** — before running, write what prints for `left` and for `pizza`.
2. **Third path** — add `elif choice == "straight":` with a new message between `right` and `else`.
3. **Case test** — type `Left` (capital L). Does it match? Why not?

---

## Practice Task

**Quest name:** Expand the Trail

1. Add a welcome line before `input()`.
2. Add a third branch with `elif` (e.g. `"straight"` → bridge scene).
3. Change the crystal message to use an f-string with the word `"crystal"`.

**Reference solution:** [solution/choose_path.py](solution/choose_path.py)

---

## Debug Corner

**Problem:** `SyntaxError: invalid syntax` on the line with `if`.

**Cause:** You forgot the **colon** at the end: `if choice == "left"` needs `:` → `if choice == "left":`

**Fix:** Add `:` after every `if`, `elif`, and `else`. Save and run again.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. How many `if` / `elif` / `else` branches run when the program executes?
   - **a)** Only **one** — the first match wins
   - **b)** All of them, every time
   - **c)** Exactly two
   - **d)** None — they only print True/False

2. What must appear at the end of `if choice == "left"`?
   - **a)** A colon `:`
   - **b)** A semicolon `;`
   - **c)** An equals sign `=`
   - **d)** Nothing extra

3. When does the `else` branch run?
   - **a)** When no `if` or `elif` condition matched
   - **b)** Always, before any `if`
   - **c)** Only when the user types `left`
   - **d)** Never — it is optional decoration

4. What does `elif` mean?
   - **a)** "Else if" — try the next check if the first one was False
   - **b)** "End loop if" — stop a while loop
   - **c)** "Equal if" — assign a variable
   - **d)** "Every line if" — run all branches

5. Code inside an `if` branch must be…
   - **a)** Indented (4 spaces) under the `if` line
   - **b)** Written on the same line as `if`
   - **c)** In ALL CAPS
   - **d)** Wrapped in quotes

---

<details><summary>Click to reveal answers</summary>

1. **a)** Only the first matching branch runs.
2. **a)** Every `if`, `elif`, and `else` line needs a colon.
3. **a)** `else` is the catch-all when nothing above matched.
4. **a)** `elif` checks another condition if the previous ones failed.
5. **a)** Indented code belongs to the branch (4 spaces in examples).

</details>

---

## What's Next

→ [Lesson 3.3: for and while loops](../lesson-3-3-for-and-while-loops/README.md) — repeat actions with countdowns and tables!

---

[← Choose language](README.md)
