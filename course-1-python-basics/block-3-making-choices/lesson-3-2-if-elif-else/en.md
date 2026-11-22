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

Open [starter/choose_path.py](starter/choose_path.py). The `input()` line is ready. The three branches are missing — they are marked `# TODO 1`, `# TODO 2`, and `# TODO 3`.

---

### Step 2: cd to this lesson folder

**Path A — PyCourse repo:**

```text
cd course-1-python-basics\block-3-making-choices\lesson-3-2-if-elif-else
```

**Path B:** Copy `choose_path.py` anywhere. `cd` to that folder before running.

---

### Step 3: Run the starter as it is

```text
python starter\choose_path.py
```

**Mac/Linux:** Use forward slashes — `python starter/choose_path.py`. List files with `ls` instead of `dir`.

**Type:** `left`

No branches yet, so only the reminder line prints:

```text
=== CHOOSE YOUR PATH ===
You stand at a fork in the quest trail.
Go left or right? (left/right): left
(No branches yet — write your if / elif / else above this line!)
Thanks for choosing!
```

---

### Step 4: Write the three branches

Under the TODO comments, write `if`, `elif`, and `else` — the same shape as the example in the Explanation, with the messages from the TODOs:

- `if choice == "left":` → crystal message
- `elif choice == "right":` → robot guide message
- `else:` → snack message

Each of these lines ends with a colon `:`, and each `print()` inside a branch starts with 4 spaces. Then **delete** the reminder line `print("(No branches yet ...")`.

---

### Step 5: Run and choose

Run the same command as in Step 3.

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

The finished story — the reference [solution/choose_path.py](solution/choose_path.py):

```python
# choose_path.py — reference solution

print("=== CHOOSE YOUR PATH ===")
print("You stand at a fork in the quest trail.")

choice = input("Go left or right? (left/right): ")

if choice == "left":
    print("You find a glowing crystal! +10 quest points.")
elif choice == "right":
    print("You meet a friendly robot guide. It waves hello.")
else:
    print("You sit down for a snack. Adventure can wait!")

print("Thanks for choosing!")
```

**Watch out:** `==` compares text **exactly**, letter by letter — `"Left" == "left"` is `False`. Quick Drill 3 lets you see this and fix it.

---

## Code Execution

```text
cd course-1-python-basics\block-3-making-choices\lesson-3-2-if-elif-else
python starter\choose_path.py
```

Try `left`, `right`, and `snack` as inputs. With `right` you should see:

```text
=== CHOOSE YOUR PATH ===
You stand at a fork in the quest trail.
Go left or right? (left/right): right
You meet a friendly robot guide. It waves hello.
Thanks for choosing!
```

With `snack` you should see `You sit down for a snack. Adventure can wait!` before `Thanks for choosing!`.

---

## Quick Drills

1. **Predict** — before running, write what prints for `left` and for `pizza`.
2. **Third path** — add `elif choice == "straight":` with a new message between `right` and `else`.
3. **Case test** — type `Left` (capital L). Which branch runs? You get the snack line, because `"Left"` and `"left"` are different text for Python. **Fix it:** add `.lower()` (from Lesson 2.4) to the end of the input line — `choice = input("Go left or right? (left/right): ").lower()`. Run again and type `Left` — now you find the crystal!

---

## Practice Task

**Quest name:** Expand the Trail

1. Finish TODOs 1–3 in `starter/choose_path.py` — your output must match Step 5 for `left` and Code Execution for `right`.
2. Add a welcome line before `input()`.
3. Add a third branch with `elif` (e.g. `"straight"` → bridge scene).
4. Change the crystal message to use an f-string with the word `"crystal"`.

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
   - **a)** Nothing extra
   - **b)** A colon `:`
   - **c)** A semicolon `;`
   - **d)** An equals sign `=`

3. When does the `else` branch run?
   - **a)** Only when the user types `left`
   - **b)** Never — it is optional decoration
   - **c)** When no `if` or `elif` condition matched
   - **d)** Always, before any `if`

4. What does `elif` mean?
   - **a)** "End loop if" — stop a while loop
   - **b)** "Equal if" — assign a variable
   - **c)** "Every line if" — run all branches
   - **d)** "Else if" — try the next check if the first one was False

5. Code inside an `if` branch must be…
   - **a)** Indented (4 spaces) under the `if` line
   - **b)** Written on the same line as `if`
   - **c)** In ALL CAPS
   - **d)** Wrapped in quotes

---

<details><summary>Click to reveal answers</summary>

1. **a)** Only the first matching branch runs.
2. **b)** Every `if`, `elif`, and `else` line needs a colon.
3. **c)** `else` is the catch-all when nothing above matched.
4. **d)** `elif` checks another condition if the previous ones failed.
5. **a)** Indented code belongs to the branch (4 spaces in examples).

</details>

---

## What's Next

→ [Lesson 3.3: for and while loops](../lesson-3-3-for-and-while-loops/README.md) — repeat actions with countdowns and tables!

---

[← Choose language](README.md)
