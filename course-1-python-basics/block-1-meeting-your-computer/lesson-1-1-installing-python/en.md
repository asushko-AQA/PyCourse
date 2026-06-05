# Lesson 1.1: Installing Python & VS Code

> **Course:** Python Basics & Command Line Magic · **Block:** Meeting Your Computer's Best Friend · **~30 min**  
> [Choose language / Выбрать язык](README.md) · [Русский →](ru.md)

---

## Title

**Level 1 — Unlock Your Coding Powers: Install Python & VS Code**

---

## Explanation

Welcome, Creator! You are about to install two power tools on your computer:

1. **Python** — a magical translator. You write instructions in a language humans understand. Python turns them into actions for your computer.
2. **VS Code** — your **Mission Control**. This is where you write code, save files, and open the **Command Portal** (the terminal).

Think of it like a video game:

- **Python** = the game engine that makes things happen.
- **Add to PATH** = putting the game on your desktop so you can launch it from anywhere. **Do not skip this!**
- **VS Code** = your custom base where you craft spells (programs).
- **Terminal** = the portal where you type commands and run your code.

---

### Step 1: Download Python

1. Open your web browser.
2. Go to **https://www.python.org/downloads/**
3. Click the big yellow button: **Download Python 3.12** (or the newest version you see).
4. Wait for the file to download. It might be called something like `python-3.12.x-amd64.exe`.

You just picked up your magic translator. Nice work!

---

### Step 2: Install Python — and check "Add to PATH"!

This step is a **boss fight**. One checkbox wins the whole level.

1. Double-click the downloaded file to start the installer.
2. **IMPORTANT:** On the first screen, look at the bottom.
3. Check the box: **"Add python.exe to PATH"** (or **"Add Python to PATH"**).
4. Click **"Install Now"**.
5. Wait until you see **"Setup was successful"**.
6. Click **Close**.

**Why PATH matters:** PATH is like a treasure map for your computer. When PATH knows where Python lives, you can type `python` in the terminal from any folder. If you forget this checkbox, your computer will say "I cannot find Python!" — and that is no fun.

**Already installed but forgot PATH?** Run the installer again, choose **Modify**, and enable **Add Python to environment variables**.

---

### Step 3: Check that Python works

1. Press **Windows key**, type **cmd**, and open **Command Prompt**  
   *(or in VS Code later: **Terminal → New Terminal**)*.
2. Type this and press **Enter**:

```text
python --version
```

3. You should see something like:

```text
Python 3.12.x
```

If you see a version number — **Level Complete!** Python is ready.

---

### Step 4: Install VS Code

1. Go to **https://code.visualstudio.com/**
2. Click **Download for Windows**.
3. Run the installer. Default options are fine.
4. Click through until installation finishes.
5. Open **Visual Studio Code**.

---

### Step 5: Add the Python extension (your power-up)

1. In VS Code, click the **Extensions** icon on the left (four squares).
2. Search for **Python**.
3. Install **Python** by **Microsoft** (the one with millions of downloads).
4. This extension helps VS Code understand your Python code. It is like giving Mission Control a smart assistant.

---

### Step 6: Open your project folder in VS Code

1. Click **File → Open Folder**.
2. Choose your course folder (for example: `Documents\PyCourse`).
3. Click **Select Folder**.

You are now inside your coding base!

---

### Step 7: Open the terminal in VS Code

The terminal is your **Command Portal**. Heroes use it to run programs.

1. In VS Code, click **Terminal → New Terminal** (or press **Ctrl + `** — the key above Tab).
2. A panel opens at the bottom. That is the terminal.
3. You will see a blinking cursor. That means the portal is open and waiting for your command.

**Tip:** You can also click the **+** in the terminal panel to open another terminal tab.

---

## Code Example

Create your first spell file. In VS Code:

1. Go to **File → New Text File**.
2. Save it as **`hello.py`** inside your project folder.
3. Type the code below.

A **`.py` file** is a Python script — a scroll of instructions for your computer.

**File: `hello.py`**

```python
# hello.py
# Your first Python spell — this file tells the computer what to say.

# print() sends a message to the screen (like opening a magic scroll).
print("Hello, World!")

# You can send more than one message. Each print() is a new line.
print("I am learning Python!")
print("My code is alive!")
```

**What each line does:**

| Line | What it means |
|------|----------------|
| Lines starting with `#` | Notes for humans. Python ignores them. |
| `print("...")` | Show text on the screen. |
| Quotes `"..."` | A text **string** — a chain of characters, like a name tag. |

You can also open the ready-made file in this lesson folder: [starter/hello.py](starter/hello.py).

---

## Code Execution

Time to cast your spell! Use the **terminal** (Command Portal).

### 1. Go to the folder where `hello.py` lives

If your file is in `Documents\PyCourse`, type:

```text
cd Documents\PyCourse
```

*(Change the path if your folder is somewhere else. `cd` means **c**hange **d**irectory — walk to a new folder.)*

### 2. Run your script

```text
python hello.py
```

Press **Enter**.

### Expected output

```text
Hello, World!
I am learning Python!
My code is alive!
```

If you see those three lines — **you did it!** You ran real Python code.

### Bonus check (any time)

```text
python --version
```

---

### Run from VS Code (easier way)

1. Open `hello.py` in the editor.
2. Open the terminal (**Terminal → New Terminal**).
3. Make sure you are in the right folder (use `cd` if needed).
4. Type `python hello.py` and press **Enter**.

**Or:** click the **Run** button (play icon) at the top-right when the Python extension is installed.

---

## Quick Drills

1. **Version check** — open terminal, run `python --version`, write the number down.
2. **Portal open** — in VS Code, **Terminal → New Terminal** — see the blinking cursor?
3. **First run** — from this lesson folder, run `python starter\hello.py` after install.

---

## Practice Task

**Quest name:** The Creator's Introduction

**Your mission (do this on your own):**

1. Create a new file called **`my_intro.py`** (or edit `hello.py`).
2. Use **`print()`** to show **four lines**:
   - Line 1: `Hello, World!`
   - Line 2: Your name — for example: `My name is Sam.`
   - Line 3: Your age — for example: `I am 11 years old.`
   - Line 4: One thing you want to build with code — for example: `I will build a cool game!`
3. Save the file.
4. Open the terminal and run:

```text
python my_intro.py
```

5. Take a screenshot or tell a friend what appeared on the screen.

**Bonus stars (optional):**

- Run `python --version` and write down the number in a notebook. That is your Python level.
- Add one more `print()` line with a joke or a fun fact about yourself.

**Stuck?** Read the error message like a detective clue. Common fixes:

- **`python is not recognized`** → Install again and check **Add to PATH**.
- **`No such file`** → Use `cd` to go to the folder where your `.py` file is saved.
- **Forgot quotes** → Text inside `print()` must be inside `"..."`.

---

## Debug Corner

**Problem:** The terminal says `'python' is not recognized as an internal or external command`.

**Cause:** Windows cannot find Python. Usually the **Add to PATH** box was not checked.

**Fix:** Run the Python installer again → **Modify** → enable **Add Python to environment variables** → finish → close and reopen the terminal → try `python --version` again.

---

## What's Next

→ [Lesson 1.2: Using the Terminal/CLI](../lesson-1-2-using-the-terminal/README.md) — learn to walk through folders like a maze master.

---

*You installed the engine. You opened Mission Control. You ran your first spell. Welcome to the guild, Creator!*

[← Choose language](README.md)
