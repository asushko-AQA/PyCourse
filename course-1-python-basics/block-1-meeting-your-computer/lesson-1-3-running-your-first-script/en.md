# Lesson 1.3: Running Your First Script

> **Course:** Python Basics & Command Line Magic · **Block:** Meeting Your Computer's Best Friend · **~30–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 3 — Master the Launch Sequence**

---

## Explanation

You met the `print()` spell in Level 1. You learned to walk folders in Level 2. Now you master the **launch sequence** — the exact steps to run a script **every time**, without guessing.

**What Level 1 already gave you:** create `hello.py`, one `cd`, run once.

**What is new in Level 3:** save correctly, always launch from the **right folder**, and fix `can't open file` errors like a pro.

**Already did Level 1's `my_intro.py`?** Great — this quest focuses on the **launch workflow** (save, folder, run), not new `print()` tricks.

The launch sequence:

1. **Create** your `.py` file in VS Code
2. **Save** it (watch the extension — `.py` not `.py.txt`)
3. **cd** to the folder where the file lives
4. **python file.py** — blast off!

---

### Step 1: Understand `.py` files

A file ending in `.py` is a Python script. Windows sometimes hides extensions — your file might secretly be `hello.py.txt`.

**Check in VS Code:** look at the tab title. It should say `hello.py`, not `hello.py.txt`.

**Check in Explorer:** **View → Show → File name extensions** (Windows).

---

### Step 2: Save vs Save As

- **Save (Ctrl+S)** — updates the file you already have open.
- **Save As** — creates a **new** file with a new name. Use this for `launch.py` in the practice quest.

**Rule:** After every edit, Save. Unsaved files cannot run!

---

### Step 3: Same folder, two views

Your file lives in a folder. You can see that folder in two places:

1. **VS Code Explorer** (left sidebar) — click folders to browse
2. **Terminal** — the path in the prompt is the same folder (when aligned)

If Explorer shows `hello.py` but the terminal prompt is a different path, `python hello.py` will fail. Align them!

---

### Step 4: Open this lesson's script

Open [starter/hello.py](starter/hello.py). This is the same spell from Level 1 — a reference, not a new concept.

---

### Step 5: cd to this lesson folder

**Path A — PyCourse repo** (if you cloned the full course):

```text
cd course-1-python-basics\block-1-meeting-your-computer\lesson-1-3-running-your-first-script
```

**Path B — your own folder:** Open VS Code on any folder where you keep scripts. Skip the long `cd` path — you are already in the right place when the terminal prompt matches your project folder.

The goal: you can reach `starter\hello.py` from where you stand in the terminal.

---

### Step 6: Confirm with dir

From the lesson folder:

```text
dir starter
```

**Expected:**

```text
hello.py
```

Both `hello.py` and your new `launch.py` (practice quest) live in **`starter/`** — the same folder.

---

### Step 7: Run from the terminal

```text
python starter\hello.py
```

**Mac/Linux:** Use forward slashes — `python starter/hello.py`. List files with `ls` instead of `dir`.

**Expected output:**

```text
Hello, World!
I am learning Python!
My code is alive!
```

---

### Step 8: Run button vs terminal

**Terminal way:** `python starter\hello.py` — heroes use this. You always know which folder you are in.

**VS Code Run button:** click the play icon (top-right) when a `.py` file is open. The Python extension runs it. Still check the terminal panel — it shows output and errors.

Both work. Learn the terminal way first — it builds maze skills from Level 2.

---

## Code Example

**File: [starter/hello.py](starter/hello.py)**

```python
# hello.py
# Your first Python spell — this file tells the computer what to say.

# print() sends a message to the screen (like opening a magic scroll).
print("Hello, World!")

# You can send more than one message. Each print() is a new line.
print("I am learning Python!")
print("My code is alive!")
```

You already know `print()`. This lesson is about **launching** it reliably.

---

## Code Execution

### 1. Go to this lesson folder

```text
cd course-1-python-basics\block-1-meeting-your-computer\lesson-1-3-running-your-first-script
```

### 2. Run hello.py

```text
python starter\hello.py
```

**Expected output:**

```text
Hello, World!
I am learning Python!
My code is alive!
```

### 3. Bonus check — Python version from same folder

```text
python --version
```

**Expected:**

```text
Python 3.12.x
```

---

## Quick Drills

1. **Wrong folder on purpose** — `cd ..` twice, then run `python starter\hello.py`. Read the error. Fix with `cd` back to the lesson folder.
2. **dir check** — `dir starter` — confirm `hello.py` is listed.
3. **Correct launch** — run again from the right folder until you see three lines.

More scenarios: [exercises/wrong_folder_scenarios.md](exercises/wrong_folder_scenarios.md)

---

## Practice Task

**Quest name:** Double Launch

**Your mission (do this on your own):**

1. In VS Code, open the **`starter/`** folder inside this lesson.
2. Create a new file **`starter/launch.py`** (same folder as `hello.py`).
3. Add **two** `print()` lines:
   - Line 1: A greeting — e.g. `print("Greetings, Creator! Ready for launch.")`
   - Line 2: Your favorite hobby — e.g. `print("My favorite hobby is drawing dragons.")`
4. **Save** — confirm the file is `launch.py`, not `launch.py.txt`
5. In terminal, `cd` to this **lesson folder** (parent of `starter/`, not inside `starter/` unless you use Path B below).
6. Run both scripts in sequence:

```text
python starter\hello.py
python starter\launch.py
```

**Path B — run from inside `starter/`:**

```text
cd starter
python hello.py
python launch.py
```

7. You should see output from **both** scripts (five lines total).

**Bonus stars (optional):**

- Rename `starter/launch.py` to `launch.py.txt` on purpose. Try to run it. Fix until `python starter\launch.py` works.
- Right-click your folder in VS Code → **Copy path** — compare with the terminal prompt.

**Reference solution:** [solution/launch.py](solution/launch.py)

---

## Debug Corner

**Problem:** `python: can't open file '...\launch.py': [Errno 2] No such file or directory`

**Cause:** One of three things:

1. Terminal is in the **wrong folder**
2. Filename is **misspelled** (`launch.py` vs `lauch.py`)
3. File was saved as **`launch.py.txt`** (hidden extension)

**Fix:**

1. `dir` — is your file listed? Note the exact name.
2. If missing, `cd` to where you saved the file.
3. In Explorer, enable file extensions and rename to `.py` only.
4. Run again with the exact name from `dir`.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. What is the correct launch sequence from this lesson?
   - **a)** Run first, then save, then `cd`
   - **b)** Create `.py` file → Save → `cd` to folder → `python file.py`
   - **c)** `cd` → delete file → `print`
   - **d)** Save As → never `cd` → run from anywhere

2. Your VS Code tab says `launch.py.txt` instead of `launch.py`. What is wrong?
   - **a)** You need to install Flask
   - **b)** The real extension may be hidden — the file is not a true `.py` script
   - **c)** You must use `python3` instead of `python`
   - **d)** VS Code is broken

3. You see `can't open file ... No such file or directory`. What is a likely cause?
   - **a)** A missing quote in `print()`
   - **b)** Terminal is in the wrong folder or the filename is misspelled
   - **c)** Python is not installed
   - **d)** You need more RAM

4. Why should the Explorer folder and terminal prompt match before running `python hello.py`?
   - **a)** Python only runs on certain days
   - **b)** Python looks for the file relative to your current terminal folder
   - **c)** VS Code will crash if they differ
   - **d)** It only matters for Mac users

5. What does `dir starter` help you do before running a script?
   - **a)** Delete the `starter` folder
   - **b)** Confirm `hello.py` (or your script) is listed in that folder
   - **c)** Install the Python extension
   - **d)** Clear the screen

---

<details><summary>Click to reveal answers</summary>

1. **b)** The launch sequence is create, save, navigate to the right folder, then run.
2. **b)** Windows can hide extensions — `launch.py.txt` is not a real Python script name.
3. **b)** This error usually means wrong folder, typo, or a hidden `.txt` extension.
4. **b)** `python hello.py` looks for the file in the folder shown in your terminal prompt.
5. **b)** Listing `starter` confirms the script exists before you run it.

</details>

---

## What's Next

→ [Lesson 1.4: Reading Error Messages](../lesson-1-4-reading-error-messages/README.md) — become an error detective.

---

*You know the spell. Now you know the launch pad. Every great Creator runs from the right folder — every time.*

[← Choose language](README.md)
