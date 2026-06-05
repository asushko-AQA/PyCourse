# Lesson 1.4: Reading Error Messages

> **Course:** Python Basics & Command Line Magic · **Block:** Meeting Your Computer's Best Friend · **~30–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 4 — Error Detective Academy**

---

## Explanation

Every hero hits bugs. The difference between a beginner and a detective is simple: **beginners panic; detectives read the clues.**

Errors are not "you failed." They are **messages** telling you what to fix.

Two families of errors in this lesson:

1. **SyntaxError** — Python grammar is broken **inside** your code (missing quote, missing `)`)
2. **can't open file** — the **terminal** cannot find your file (wrong folder or wrong name)

**How to read a traceback:**

1. Scroll to the **bottom** — read the last line first (the error type and message)
2. Find **`File "...", line N`** — that is the line number to fix
3. Open the file in VS Code and go to line N (**Ctrl+G**)

---

### Step 1: Open the case files folder

**Path A — PyCourse repo:**

```text
cd course-1-python-basics\block-1-meeting-your-computer\lesson-1-4-reading-error-messages
```

**Path B — your own copy:** If you downloaded only this lesson folder, `cd` to wherever you saved `lesson-1-4-reading-error-messages` on your computer. The folder must contain `starter/` with the three case files.

```text
dir starter
```

**Expected:** Three files: `bug_missing_quote.py`, `bug_missing_paren.py`, `right_name.py`

---

### Step 2: Case File 1 — missing quote

Open `starter/bug_missing_quote.py` in VS Code.

Run it (it will fail — that is the point!):

```text
python starter\bug_missing_quote.py
```

**Expected error (bottom line):**

```text
SyntaxError: unterminated string literal (detected at line 4)
```

Read `line 4`. Find the missing `"` at the end of the string. Fix it. Save. Run again.

**Expected output after fix:**

```text
Hello, Detective!
Can you spot the missing quote?
```

---

### Step 3: Case File 2 — missing parenthesis

Open `starter/bug_missing_paren.py`.

```text
python starter\bug_missing_paren.py
```

**Expected error:**

```text
SyntaxError: '(' was never closed
```

Find the `print(` that is missing `)`. Fix. Save. Run again.

**Expected output after fix:**

```text
This line is missing something...
Fix it and run again!
```

---

### Step 4: Case File 3 — wrong filename (CLI error)

The file on disk is named **`right_name.py`**. But you will run the **wrong** name on purpose:

```text
python starter\wrong_name.py
```

**Expected error:**

```text
python: can't open file '...\wrong_name.py': [Errno 2] No such file or directory
```

This is **not** a SyntaxError — Python never even read your code. The terminal looked for a file that does not exist.

**Fix:** Use the real filename:

```text
python starter\right_name.py
```

**Expected output:**

```text
You found the right file!
The filename on disk is: right_name.py
```

---

### Step 5: Jump to line N in VS Code

When you see `line 4` in an error:

1. Open the file in VS Code
2. Press **Ctrl+G**
3. Type `4` and press **Enter**
4. Your cursor jumps to the crime scene

---

## Code Example

Three case files live in [starter/](starter/). Each is under 15 lines — only `print()` and comments.

**Case 1 — broken quote (before fix):**

```python
print("Hello, Detective!)
```

**Case 2 — broken parenthesis (before fix):**

```python
print("This line is missing something..."
```

**Case 3 — correct file, wrong command:**

The file `right_name.py` is fine. The bug is typing `wrong_name.py` in the terminal.

Check [solution/](solution/) only after you try fixing each case yourself!

---

## Code Execution

Work through all three cases in order. For each one:

1. Run the broken version
2. Read the error (last line + line number)
3. Fix the code or the command
4. Run again until success

**Final check — all three pass:**

```text
python starter\bug_missing_quote.py
python starter\bug_missing_paren.py
python starter\right_name.py
```

*(Remember: quote and paren files must be fixed by you first!)*

---

## Quick Drills

1. **Spot the bug** — which is wrong? `print("Hello!)` or `print("Hello!")` ?
2. **Find the line** — in `File "bug_missing_quote.py", line 4` — what number do you jump to?
3. **Wrong folder** — `cd ..` out of this lesson, run `python starter\bug_missing_quote.py`, read error, `cd` back and fix.

---

## Practice Task

**Quest name:** Three Case Files

**Your mission:**

1. Fix **all three** starters in [starter/](starter/) without peeking at [solution/](solution/) until done.
2. Write in a notebook: for each case, what **type** of error was it? (SyntaxError or can't open file)
3. Tell a friend the "detective rule": read the **last line** of the error first.

**Bonus stars (optional):**

- Open [exercises/bug_bad_indent.py](exercises/bug_bad_indent.py) — a harder case with **IndentationError** (spaces at the start of a line matter in Python!). Fix the extra spaces before `print`. Check [exercises/bug_bad_indent_solution.py](exercises/bug_bad_indent_solution.py) if stuck.

**Note:** Variable typos (`NameError`) come in Block 2 when you learn variables!

---

## Debug Corner

**Problem:** You see `File "bug_missing_quote.py", line 4` but cannot find the mistake.

**Cause:** You are looking at the wrong line, or the file was not saved after editing.

**Fix:**

1. Press **Ctrl+G**, type the line number from the error.
2. Press **Ctrl+S** to save.
3. Run `python starter\bug_missing_quote.py` again.
4. Compare your line to [solution/bug_missing_quote.py](solution/bug_missing_quote.py) only as a last resort.

---

## What's Next

→ [Lesson 1.5: Mission Control Badge](../lesson-1-5-mission-control-badge/README.md) — earn your Block 1 capstone badge!

---

*Errors are clues. You read the last line. You jump to the line number. Detective badge: earned.*

[← Choose language](README.md)
