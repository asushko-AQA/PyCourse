# Lesson 1.5: Mission Control Badge (Block 1 Capstone)

> **Course:** Python Basics & Command Line Magic · **Block:** Meeting Your Computer's Best Friend · **~45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 5 — Earn Your Mission Control Badge**

---

## Explanation

You installed Python. You walked the folder maze. You mastered the launch sequence. You fixed bugs like a detective.

Now you combine **everything** in one final mission and earn your **Mission Control Badge**.

This is Block 1's capstone — no new concepts, only **proof** you can:

1. Create a folder
2. Write a multi-line script
3. Navigate with `cd` and `dir`
4. Run `python badge.py`
5. Break your code on purpose, read the error, and fix it

Before you start, tick the [Block 1 readiness checklist](../../README.md#block-1-readiness-checklist).

---

### Step 1: Create your mission folder

**Recommended:** Use VS Code Explorer — right-click your **project root** (e.g. `PyCourse`), choose **New Folder**, name it **`my_mission`**.

**Or in terminal** — first go to your project root, then create the folder:

```text
cd Documents\PyCourse
```

*(Adjust if your project lives elsewhere — match the path in VS Code's title bar.)*

```text
mkdir my_mission
```

**Expected:** A new empty folder `my_mission` **next to** `course-1-python-basics`, not inside a lesson folder.

---

### Step 2: Open the badge skeleton

Open [starter/badge.py](starter/badge.py). It has `# TODO` comments — your job is to replace them with real `print()` lines.

Copy or recreate `badge.py` **inside** your `my_mission` folder.

---

### Step 3: Write your badge script

Fill in **5 to 8** `print()` lines. Ideas:

- Line 1: Title banner — `print("=== MISSION CONTROL BADGE ===")`
- Line 2: Your name
- Line 3: One skill you learned in Block 1
- Line 4: Your favorite terminal command
- Line 5: Victory message — `print("Block 1 complete!")`
- Lines 6–8 (optional): Joke, fun fact, or ASCII art with `print()`

See [solution/badge.py](solution/badge.py) for inspiration **after** you try your own version.

---

### Step 4: Save and confirm

Press **Ctrl+S**. Confirm the file is `badge.py` inside `my_mission` — not `.py.txt`.

---

### Step 5: Navigate to my_mission

From your **project root**:

```text
cd my_mission
```

If you created `my_mission` on Desktop instead:

```text
cd Desktop\my_mission
```

*(Always match where you actually created the folder.)*

```text
dir
```

**Expected:** `badge.py` is listed.

---

### Step 6: Launch your badge

```text
python badge.py
```

**Mac/Linux:** Use forward slashes in paths. List files with `ls` instead of `dir`.

**Expected:** 5–8 lines of your custom output appear. **Mission Control Badge earned!**

---

### Step 7: Break and fix (detective drill)

1. Open `badge.py` and delete one closing `"` from a `print()` line on purpose.
2. Save. Run `python badge.py` again.
3. Read the **SyntaxError** — find the line number.
4. Fix the quote. Save. Run again until clean output returns.

You just proved you can debug your **own** code!

---

## Code Example

**File: [starter/badge.py](starter/badge.py)** (skeleton — you complete it)

```python
# badge.py
# Mission Control Badge — fill in your TODO lines below!

# TODO: Print a title banner (line 1)

# TODO: Print your name (line 2)

# TODO: Print one skill you learned in Block 1 (line 3)

# TODO: Print one command you can use in the terminal (line 4)

# TODO: Print a victory message (line 5)
```

**Reference: [solution/badge.py](solution/badge.py)**

```python
print("=== MISSION CONTROL BADGE ===")
print("Name: Alex the Creator")
print("Skill unlocked: Navigate folders with cd and dir")
print("Favorite command: python badge.py")
print("Block 1 complete — ready for variables!")
print("Why do programmers prefer dark mode? Because light attracts bugs!")
```

---

## Code Execution

Full sequence from a clean start:

```text
mkdir my_mission
cd my_mission
```

Create and save `badge.py` with your lines, then:

```text
dir
python badge.py
```

**Expected:** Your personal badge output — at least 5 lines.

```text
python --version
```

**Expected:**

```text
Python 3.12.x
```

---

## Quick Drills

Before the main quest, tick every box on the [Block 1 readiness checklist](../../README.md#block-1-readiness-checklist).

If any box is empty, revisit that lesson before continuing.

---

## Practice Task

**Quest name:** Mission Control Badge

**Your mission (complete all steps):**

1. Create folder `my_mission/`
2. Write `badge.py` with 5–8 `print()` lines (your own words!)
3. `cd my_mission` and `dir` — confirm `badge.py` is there
4. `python badge.py` — success output
5. Introduce one bug on purpose (missing quote or `)`), read error, fix, re-run
6. Show output to a friend, parent, or teacher

**Bonus stars (optional):**

- Take a screenshot of your terminal output.
- Add one more joke line to `badge.py`.
- Complete the full [Block 1 checklist](../../README.md#block-1-readiness-checklist) — you are ready for Block 2!

---

## Debug Corner

**Problem:** "It worked once, now it does not."

**Cause:** Usually one of two things:

1. You edited the file but forgot **Save** (Ctrl+S)
2. You created `my_mission` but the terminal is still in the **old** folder

**Fix:**

1. Save the file — watch the dot disappear from the VS Code tab.
2. `cd` to `my_mission` again. `dir` — is `badge.py` there?
3. Run `python badge.py` again.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. Where should you create the `my_mission` folder for this capstone?
   - **a)** Inside a lesson's `starter` folder
   - **b)** Next to `course-1-python-basics` at your project root — not inside a lesson
   - **c)** Only inside `badge.py`
   - **d)** Nowhere — use the terminal only

2. How many `print()` lines should your finished `badge.py` have?
   - **a)** Exactly 1
   - **b)** 5 to 8 lines of your own output
   - **c)** 50 minimum
   - **d)** Zero — only `# TODO` comments

3. What terminal command creates a new folder called `my_mission`?
   - **a)** `mkdir my_mission`
   - **b)** `python my_mission`
   - **c)** `dir my_mission`
   - **d)** `cd my_mission`

4. After `cd my_mission`, what command runs your badge script?
   - **a)** `python badge.py`
   - **b)** `badge.py`
   - **c)** `run badge`
   - **d)** `cd badge.py`

5. In Step 7 you break `badge.py` on purpose. What error type do you practice fixing?
   - **a)** NameError
   - **b)** SyntaxError (for example a missing `"` in `print()`)
   - **c)** Database connection error
   - **d)** A PATH installation error

---

<details><summary>Click to reveal answers</summary>

1. **b)** `my_mission` belongs at project root, beside the course folders.
2. **b)** The capstone asks for 5–8 personal `print()` lines in your badge.
3. **a)** `mkdir` makes a new folder; then you `cd` into it.
4. **a)** From inside `my_mission`, run `python badge.py` to launch your badge.
5. **b)** Deleting a closing quote causes a SyntaxError — you read it and fix it.

</details>

---

## What's Next

→ [Lesson 2.1: Variables, Strings, Integers](../../block-2-talking-to-python/lesson-2-1-variables/README.md) — Block 2 begins!

→ [Block 1 index](../../README.md) — review all five lessons and your checklist.

---

*Mission Control Badge: earned. You install, navigate, launch, and debug. Block 1 complete — welcome to the guild, Creator!*

[← Choose language](README.md)
