# Lesson 0.1: Virtual Environments & pip

> **Course:** Web Applications with Python · **Block:** Environment Setup · **~30–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 0 — Your Isolated Web Toolbox**

---

## Explanation

Welcome to the **Web Workshop**! Before you build pages in the browser, you need a clean workspace for installing tools like Flask.

A **virtual environment** (`.venv`) is like a labeled toolbox just for this project. Packages you install with `pip` stay inside it instead of mixing with every other Python project on your computer.

**One toolbox for all of Course 2.** Create `.venv` in the folder you open in VS Code. In the PyCourse repo that folder is the **project root** (`PyCourse`). Lesson 1.1 and the capstones `my_web_madlibs/` and `my_web_calc/` activate **that same** `.venv`. Do not create a second `.venv` inside a lesson folder.

**Path A — PyCourse repo:** **File → Open Folder** → `PyCourse`. **Terminal → New Terminal** already starts there. If the prompt ends with `PyCourse`, you are in the right place. Do **not** `cd` into this lesson before `python -m venv .venv`.

**Path B — your own folder:** Create a folder (for example `web_workshop`), open **that** folder in VS Code, and copy [starter/check_setup.py](starter/check_setup.py) into it. Every command below runs in the folder you opened. Your `.venv` lives next to that copy.

Check Python once: `python --version` should show `Python 3.12` or newer. On macOS, use `python3 --version` if `python` is not found, and use `python3` in place of `python` for the rest of this lesson.

---

### Step 1: Create `.venv`

In the VS Code terminal (the `PyCourse` root for Path A, your own folder for Path B):

```text
python -m venv .venv
```

This creates a `.venv` folder **here**. It may take a few seconds.

---

### Step 2: Activate the venv

**Windows PowerShell** (the usual VS Code terminal):

```text
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt (cmd):**

```text
.venv\Scripts\activate.bat
```

**macOS / Linux:**

```text
source .venv/bin/activate
```

When activation works, your prompt often shows `(.venv)` at the start. You can change folders after this — the toolbox stays open.

---

### Step 3: Install Flask with pip

```text
pip install flask
```

`pip` is Python's package installer. It downloads Flask into your `.venv` only.

---

### Step 4: Two new tools, then run the check script

Open [starter/check_setup.py](starter/check_setup.py). The skeleton already has `try` / `except`. You fill in the `# TODO` prints.

**`try` / `except`** is a safety net. Python runs the `try` block. If `import flask` fails, it raises `ImportError` and jumps to `except` instead of crashing. You print setup steps there.

**`importlib.metadata.version("flask")`** looks up the installed Flask version and gives you a text string like `3.1.3`. Put it inside an f-string: `print(f"Flask version: {importlib.metadata.version('flask')}")`.

Finish the `# TODO` lines inside `main()`. The shape is already in the file:

```python
import importlib.metadata


def main():
    try:
        import flask
        # TODO: print "venv ready"
        # TODO: print the version with importlib.metadata.version("flask")
    except ImportError:
        print("Flask is not installed yet.")
        # TODO: print "Steps:" and three numbered lines
        # (activate .venv, pip install flask, run this script again)
```

**Path A — Windows** (from `PyCourse`, after `(.venv)` shows):

```text
cd course-2-web-apps\block-0-environment-setup\lesson-0-1-virtual-environments
python starter\check_setup.py
```

**Path A — macOS:**

```text
cd course-2-web-apps/block-0-environment-setup/lesson-0-1-virtual-environments
python starter/check_setup.py
```

**Path B:** you copied `check_setup.py` next to `.venv`, so run `python check_setup.py`.

**Expected output (when venv is active and Flask is installed):**

```text
venv ready
Flask version: 3.x.x
```

---

### Step 5: Deactivate (optional practice)

```text
deactivate
```

Your prompt returns to normal. Run the same `python starter\check_setup.py` command again (macOS: `python3 starter/check_setup.py`) — the friendly error message guides you back. Activate again before the next lesson.

---

## Code Example

**File: [solution/check_setup.py](solution/check_setup.py)** (after finishing the TODOs)

```python
import importlib.metadata


def main():
    try:
        import flask

        print("venv ready")
        print(f"Flask version: {importlib.metadata.version('flask')}")
    except ImportError:
        print("Flask is not installed yet.")
        print("Steps:")
        print("  1. Activate your .venv (see lesson steps)")
        print("  2. Run: pip install flask")
        print("  3. Run this script again")


main()
```

---

## Code Execution

Run this from the folder you opened (`PyCourse` for Path A). Create and activate `.venv` **there**, then walk into the lesson to run the script.

**Windows PowerShell:**

```text
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install flask
cd course-2-web-apps\block-0-environment-setup\lesson-0-1-virtual-environments
python starter\check_setup.py
```

**macOS / Linux:**

```text
python3 -m venv .venv
source .venv/bin/activate
pip install flask
cd course-2-web-apps/block-0-environment-setup/lesson-0-1-virtual-environments
python3 starter/check_setup.py
```

**Expected output (venv active, Flask installed):**

```text
venv ready
Flask version: 3.x.x
```

---

## Quick Drills

1. Run `pip list` and find `Flask` in the list.
2. Type `deactivate`, run `pip list` again. Flask should be missing from this second list. Activate once more.
3. While `(.venv)` shows, run `where python` (Windows) or `which python` (macOS). The path should contain `.venv`. If you rename or move the project folder, delete `.venv` and repeat Steps 1–3. A moved toolbox keeps old folder paths inside and stops working.

---

## Practice Task

**Quest name:** Workshop Label

1. After `venv ready` prints, add one more line to the script: `print("My web workshop is open!")`
2. Run again and show the output to a parent or teacher.

**Reference solution:** [solution/check_setup.py](solution/check_setup.py)

---

## Debug Corner

**Problem:** `Activate.ps1` cannot be loaded because running scripts is disabled.

**Cause:** Windows security settings block some PowerShell scripts.

**Fix:** Ask a parent or teacher, then run this **once** in PowerShell and activate again:

```text
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Or skip PowerShell and use **cmd** with `.venv\Scripts\activate.bat`.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. What is a virtual environment (`.venv`) like in this lesson?
   - **a)** A backup copy of all your Python files
   - **b)** A special browser for testing websites
   - **c)** A folder that keeps packages for just this project
   - **d)** A command that deletes old packages

2. When your venv is active, what do you often see at the start of the terminal prompt?
   - **a)** `[Flask]`
   - **b)** `C:\Windows\`
   - **c)** `>>> `
   - **d)** `(.venv)`

3. What does `pip install flask` do in an **activated** venv?
   - **a)** Installs Flask only inside that venv
   - **b)** Deletes Flask from your computer
   - **c)** Opens Flask in the browser automatically
   - **d)** Copies Flask into every Python project on your PC

4. Why should you activate the venv before running `python starter\check_setup.py`?
   - **a)** Because `.py` files only run after activation
   - **b)** So Python can find Flask that you installed in the venv
   - **c)** To make the script run twice as fast
   - **d)** Because VS Code refuses to open the terminal otherwise

5. What does `deactivate` do?
   - **a)** Uninstalls Flask from the internet
   - **b)** Deletes the `.venv` folder forever
   - **c)** Turns off the venv and returns you to normal terminal Python
   - **d)** Closes VS Code

---

<details><summary>Click to reveal answers</summary>

1. **c)** A venv is a project toolbox — packages stay separate from other projects.
2. **d)** `(.venv)` in the prompt means the virtual environment is active.
3. **a)** `pip install` inside an active venv installs only there.
4. **b)** Without activation, Python may not see packages you installed in `.venv`.
5. **c)** `deactivate` exits the venv — you are back to system Python.

</details>

---

## What's Next

→ [Lesson 0.2: How the Web Works](../lesson-0-2-how-the-web-works/README.md) — learn what happens when you open a URL.

---

*Your toolbox is ready. Next you will learn how the web actually works!*

[← Choose language](README.md)
