# Lesson 4.1: Functions with def

> **Course:** Python Basics & Command Line Magic · **Block:** Organizing Code · **~30–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 15 — Reusable Workshop Recipes**

---

## Explanation

Welcome to the **Adventure Workshop**! In Block 3 you wrote `if` branches and loops. Now you learn **functions** — reusable recipes you can run again and again without retyping the same code.

**Comments:** Lines starting with `#` are notes for humans — Python skips them. You will see `# TODO` in starter files marking where **you** add code:

```python
# This is a comment — Python ignores it
def draw_banner(text):
    print("===")  # title line
```

A **function** is a named block of steps. You **define** it once with `def`, then **call** it whenever you need those steps:

```python
def draw_banner(text):
    print("===")
    print(text)
    print("===")
```

Calling `draw_banner("Hello")` runs all three `print()` lines inside the function.

**Path A — PyCourse repo:**

```text
cd course-1-python-basics\block-4-organizing-code\lesson-4-1-functions
```

**Path B — your own folder:** Copy [starter/helpers.py](starter/helpers.py) anywhere. Open VS Code on that folder — you are ready.

---

### Step 1: Open helpers.py

Open [starter/helpers.py](starter/helpers.py). You will find two helper recipes and a `main()` function that ties them together.

---

### Step 2: Understand draw_banner

`draw_banner(text)` takes one piece of text and prints it between `===` lines — like a title card for your adventure.

---

### Step 3: Understand ask_yes_no

`ask_yes_no(question)` prints a question, waits for `input()`, and **returns** the string `"yes"` or `"no"`. The caller stores that answer in a variable.

---

### Step 4: Run the script

```text
python starter\helpers.py
```

**Mac/Linux:** Use forward slashes — `python starter/helpers.py`. List files with `ls` instead of `dir`.

**Expected output (you type at the prompt):**

```text
===
Adventure Workshop
===
Ready to build helper functions? (yes/no): yes
You answered: yes
```

---

### Step 5: Call order matters

`main()` calls `draw_banner` first, then `ask_yes_no`. Change the order inside `main()` and see how the output changes.

---

## Code Example

**File: [starter/helpers.py](starter/helpers.py)**

```python
def draw_banner(text):
    print("===")
    print(text)
    print("===")


def ask_yes_no(question):
    answer = input(f"{question} (yes/no): ").lower().strip()
    if answer in ("y", "yes"):
        return "yes"
    return "no"


def main():
    draw_banner("Adventure Workshop")
    answer = ask_yes_no("Ready to build helper functions?")
    print(f"You answered: {answer}")


main()
```

---

## Code Execution

```text
cd course-1-python-basics\block-4-organizing-code\lesson-4-1-functions
python starter\helpers.py
```

Type `yes` or `no` when the terminal waits. Press Enter after each answer.

---

## Quick Drills

1. **Rename the workshop** — change `"Adventure Workshop"` to your own title. Run again.
2. **Extra recipe** — add `def draw_line():` that prints `"----------"` and call it between the banner and the question.
3. **Forgot to call?** — see Debug corner below.

---

## Practice Task

**Quest name:** Build Your Own Helper

1. Add a function `greet(name)` that prints `f"Welcome, {name}!"`.
2. In `main()`, ask for a name with `input()` and pass it to `greet()`.
3. Keep `draw_banner` at the top so your workshop still has a title card.

**Bonus stars:** Make `ask_yes_no` accept `"y"` and `"n"` as shortcuts (the starter already does `"y"` — try adding `"n"` for `"no"`).

**Reference solution:** [solution/helpers.py](solution/helpers.py)

---

## Debug Corner

**Problem:** You wrote `draw_banner("Adventure Workshop")` inside `def main()` but forgot to **call** `main()` at the bottom. The script runs and exits with no output.

**Cause:** Defining a function only **stores** the recipe. Python does not run the steps until you **call** the function by name: `main()`.

**Fix:** Make sure the last line of your file is `main()` (not indented — it lives at the top level). Run again.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. What keyword do you use to **define** a function in Python?
   - **a)** `function`
   - **b)** `def`
   - **c)** `recipe`
   - **d)** `call`

2. You wrote `def draw_banner(text):` but never called it. What happens when you run the file?
   - **a)** Python runs the function automatically
   - **b)** Nothing prints — defining a function only stores the recipe
   - **c)** A SyntaxError appears
   - **d)** VS Code crashes

3. In `helpers.py`, what does `ask_yes_no(question)` **return**?
   - **a)** Nothing — it only prints
   - **b)** The string `"yes"` or `"no"`
   - **c)** A list of answers
   - **d)** The number 1 or 0

4. Why must `main()` appear as the **last line** of the file with **no indent**?
   - **a)** Python always runs the last function name it sees
   - **b)** So you can call `main()` to start the program after all functions are defined
   - **c)** Indented lines are comments
   - **d)** `main()` only works at the top of the file

5. What does `draw_banner("Adventure Workshop")` pass into the function?
   - **a)** A loop counter
   - **b)** One piece of text — the `text` parameter
   - **c)** The whole `main()` function
   - **d)** A dictionary of room names

---

<details><summary>Click to reveal answers</summary>

1. **b)** `def` starts a function definition — your reusable recipe.
2. **b)** Defining stores the recipe; Python runs it only when you **call** it by name.
3. **b)** `ask_yes_no` returns `"yes"` or `"no"` so the caller can store the answer in a variable.
4. **b)** Top-level `main()` kicks off the script after helper functions are ready.
5. **b)** `"Adventure Workshop"` is the value for the `text` parameter inside `draw_banner`.

</details>

---

## What's Next

→ [Lesson 4.2: Lists](../lesson-4-2-lists/README.md) — pack game items into a numbered inventory.

---

*Your workshop has reusable recipes now. Next you will organize items in a list!*

[← Choose language](README.md)
