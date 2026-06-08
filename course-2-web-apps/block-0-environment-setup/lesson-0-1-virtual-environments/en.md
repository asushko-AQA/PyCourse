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

**Path A — PyCourse repo:**

```text
cd course-2-web-apps\block-0-environment-setup\lesson-0-1-virtual-environments
```

**Path B — your own folder:** Create a new folder on Desktop (for example `web_workshop`). Open it in VS Code — you are ready.

---

### Step 1: Create `.venv`

In the VS Code terminal:

```text
python -m venv .venv
```

This creates a `.venv` folder. It may take a few seconds.

---

### Step 2: Activate the venv

**Windows PowerShell:**

```text
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt (cmd):**

```text
.venv\Scripts\activate.bat
```

**Mac/Linux:**

```text
source .venv/bin/activate
```

When activation works, your prompt often shows `(.venv)` at the start.

---

### Step 3: Install Flask with pip

```text
pip install flask
```

`pip` is Python's package installer. It downloads Flask into your `.venv` only.

---

### Step 4: Run the check script

Open [starter/check_setup.py](starter/check_setup.py), finish the `# TODO` lines, then run:

```text
python starter\check_setup.py
```

**Mac/Linux:** `python starter/check_setup.py`

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

Your prompt returns to normal. Run `check_setup.py` again without the venv — see how the friendly error message guides you back.

---

## Quick Drills

1. Run `pip list` and find `Flask` in the list.
2. Try activation in PowerShell **and** note the cmd command for a different terminal.
3. Rename your project folder — your `.venv` moves with it.

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

**Fix:** Ask a parent or teacher to allow scripts for your user, or use **cmd** with `activate.bat` instead.

---

## What's Next

→ [Lesson 0.2: How the Web Works](../lesson-0-2-how-the-web-works/README.md) — learn what happens when you open a URL.

---

*Your toolbox is ready. Next you will learn how the web actually works!*

[← Choose language](README.md)
