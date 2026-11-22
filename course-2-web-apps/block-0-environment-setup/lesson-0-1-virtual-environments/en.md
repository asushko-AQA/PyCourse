# Lesson 0.1: Virtual Environments & pip

> **Course:** Web Applications with Python · **Block:** Environment Setup · **~30–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 0 — Your Isolated Web Toolbox**

---

## Explanation

Welcome to the **Web Workshop**! In Course 1 you ran Python scripts on your computer. In Course 2 you will build **web apps** — programs that talk to a browser. First you need a clean, separate set of tools for web projects.

A **virtual environment** (venv) is a folder (usually called `.venv`) that keeps packages for **just one project**. Picture labeled toolboxes: one for games, another for the web. Without a venv, `pip install` mixes packages into your global Python, and versions can clash.

**`pip`** is Python's package installer. In an **activated** venv, `pip install flask` puts Flask **only** into this project's toolbox.

**Comments:** lines starting with `#` are notes for humans — Python skips them. In `check_setup.py` you will see `# TODO` — places where **you** write the code.

### Where does `.venv` live?

You make **one** `.venv` for the whole course. It lives in the folder you open in VS Code:

**Path A — PyCourse repo:** the `PyCourse` folder itself — the one that contains `course-1-python-basics` and `course-2-web-apps`. Your venv will be `PyCourse\.venv`.

**Path B — your own folder:** create a new folder on your Desktop, for example `web_workshop`. Your venv will be `web_workshop\.venv`. Copy [starter/check_setup.py](starter/check_setup.py) into `web_workshop` now — you will run it in Step 6.

```text
PyCourse/                      web_workshop/
├── .venv/        ← Path A     ├── .venv/        ← Path B
├── course-1-python-basics/    └── check_setup.py
└── course-2-web-apps/
```

Never create `.venv` inside a lesson folder. Every Course 2 lesson starts the same way: open this folder in VS Code → activate `.venv` → **then** `cd` into the lesson folder.

**A venv cannot move.** If you rename or move the folder that holds `.venv`, the venv breaks. Delete the old `.venv` folder and repeat Steps 2–4 to make a fresh one.

---

### Step 1: Open your folder in VS Code

1. **File → Open Folder** — choose `PyCourse` (Path A) or `web_workshop` (Path B).
2. **Terminal → New Terminal**. The terminal starts in that folder.

Check Python:

```text
python --version
```

You should see `Python 3.12` or newer.

**Mac/Linux:** if `python` is not found, use `python3` for the commands in Steps 1–2. Once the venv is active, plain `python` works.

---

### Step 2: Create `.venv`

In the same terminal (still in the folder you opened):

```text
python -m venv .venv
```

This creates a `.venv` folder — your isolated toolbox. It may take a few seconds. Keep the name `.venv` — later lessons expect it.

**Expected result:** a `.venv` folder appears in the VS Code file list. You do not need to look inside.

---

### Step 3: Activate the venv

Activating tells the terminal to use the Python inside `.venv`, not the global one.

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

**Expected result:** your prompt shows `(.venv)` at the start — the toolbox is open.

**Red error in PowerShell about running scripts?** See the [Debug Corner](#debug-corner) — or use **cmd** with `activate.bat` instead.

---

### Step 4: Install Flask with pip

When `(.venv)` shows in the prompt:

```text
pip install flask
```

**Expected output (the last line, details may differ):**

```text
Successfully installed ... flask-3.x.x ...
```

Check the package list:

```text
pip list
```

Find the line with `Flask`.

---

### Step 5: Finish check_setup.py

Open `check_setup.py` — Path A: [starter/check_setup.py](starter/check_setup.py); Path B: the copy in your `web_workshop` folder. You need two new tools.

**Tool 1 — `try` / `except`: a safety net.** Python tries the code under `try:`. If an error happens there, Python jumps to `except` instead of crashing. Try this tiny demo:

```python
try:
    import unicorn_magic
    print("unicorn_magic found!")
except ImportError:
    print("No unicorn_magic here — but no crash either!")
```

**Output:**

```text
No unicorn_magic here — but no crash either!
```

There is no package called `unicorn_magic`, so `import` fails and the `except ImportError:` block runs. (Python names this error `ModuleNotFoundError` — it is a kind of `ImportError`, so `except ImportError:` catches it.)

**Tool 2 — ask for a version number.** `importlib` comes built into Python. This line prints which Flask version pip installed:

```python
import importlib.metadata

print(f"Flask version: {importlib.metadata.version('flask')}")
```

**Your job — the three `# TODO` lines in `main()`:**

1. Under `try:`, write `import flask`.
2. Still under `try:`, print `"venv ready"` and the Flask version line.
3. Under `except ImportError:`, print friendly steps: activate `.venv`, run `pip install flask`, run the script again.

**Stuck?** Copy the shape of the `unicorn_magic` demo and swap in `flask`.

---

### Step 6: Run the check script

With `(.venv)` active, from the folder you opened in Step 1:

**Path A — PyCourse repo:**

```text
python course-2-web-apps\block-0-environment-setup\lesson-0-1-virtual-environments\starter\check_setup.py
```

**Path B — your own folder:**

```text
python check_setup.py
```

**Mac/Linux:** use forward slashes: `python course-2-web-apps/block-0-environment-setup/lesson-0-1-virtual-environments/starter/check_setup.py`

**Expected output:**

```text
venv ready
Flask version: 3.x.x
```

(Your version number may differ — that is fine.) See the setup steps instead? Re-read Steps 3 and 4: Flask is probably not installed in the **active** venv.

---

### Step 7: Deactivate and compare

```text
deactivate
```

`(.venv)` disappears from the prompt. Run the same command from Step 6 again (Mac/Linux: `python3` instead of `python`). Now the safety net catches the error:

```text
Flask is not installed yet.
Steps:
  1. Activate your .venv (see lesson steps)
  2. Run: pip install flask
  3. Run this script again
```

(If you still see `venv ready`, Flask is also installed outside your venv — that is OK.)

Activate again (Step 3) before you continue.

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

**Path A** — in the `PyCourse` folder (Windows PowerShell):

```text
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install flask
python course-2-web-apps\block-0-environment-setup\lesson-0-1-virtual-environments\starter\check_setup.py
```

**Path B** — in your `web_workshop` folder: the same first three commands, then `python check_setup.py`.

**cmd:** `.venv\Scripts\activate.bat` · **Mac/Linux:** `python3 -m venv .venv`, then `source .venv/bin/activate` and forward slashes in paths.

**Expected output (venv active, Flask installed):**

```text
venv ready
Flask version: 3.x.x
```

---

## Quick Drills

1. **Find Flask** — with the venv active, run `pip list` and find `Flask`. Run `deactivate`, then `pip list` again: Flask should be missing from the global list. (If `pip` is not found outside the venv, that proves the same thing!) Activate again.
2. **Wrong toolbox** — deactivate, run `check_setup.py` and read the setup steps. Activate again, run it again — back to `venv ready`.
3. **Two terminals, two commands** — write the PowerShell **and** the cmd activation commands on a sticky note. Every Course 2 lesson starts with one of them.

---

## Practice Task

**Quest name:** Workshop Label

1. Finish all TODOs in `check_setup.py` so its output matches the reference solution.
2. After the `Flask version` line, add one more line: `print("My web workshop is open!")`
3. Run the script twice: with the venv active and after `deactivate`. Compare the output, then show it to a parent or teacher.

**Expected output (venv active):**

```text
venv ready
Flask version: 3.x.x
My web workshop is open!
```

**Bonus stars:** in the `except` block, add a fourth tip: `print("  4. Make sure (.venv) shows in your terminal prompt")`

**Reference solution:** [solution/check_setup.py](solution/check_setup.py)

---

## Debug Corner

**Problem:** `check_setup.py` prints `Flask is not installed yet.` even after `pip install flask`. (A script without `try`/`except` would crash with `ModuleNotFoundError: No module named 'flask'`.)

**Cause:** The venv is **not active**. Flask went into a different Python, or the script ran with the global Python.

**Fix:** Activate again (Step 3), check that `(.venv)` shows, run `pip install flask` once more, then run the script again.

---

**Problem:** PowerShell says `Activate.ps1 cannot be loaded because running scripts is disabled on this system`.

**Cause:** Windows security settings block local PowerShell scripts.

**Fix:** Ask a parent or teacher first — this changes a Windows setting for your user account. Then run this **once** and activate again:

```text
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

No permission? Use **cmd** with `.venv\Scripts\activate.bat` instead.

---

**Problem:** Activation fails: PowerShell says `The term '.venv\Scripts\Activate.ps1' is not recognized`, or Mac/Linux says `.venv/bin/activate: No such file or directory`.

**Cause:** The terminal is not in the folder that holds `.venv` — for example, you already `cd`-ed into a lesson folder.

**Fix:** Close the terminal and open a new one (**Terminal → New Terminal**) — it starts in the folder you opened in VS Code. Activate there first, then `cd`.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. What is a virtual environment (`.venv`) like in this lesson?
   - **a)** A folder that keeps packages for just this project
   - **b)** A special browser for testing websites
   - **c)** A backup copy of all your Python files
   - **d)** A command that deletes old packages

2. When your venv is active, what do you often see at the start of the terminal prompt?
   - **a)** `[Flask]`
   - **b)** `(.venv)`
   - **c)** `>>> `
   - **d)** `C:\Windows\`

3. What does `pip install flask` do in an **activated** venv?
   - **a)** Opens Flask in the browser automatically
   - **b)** Copies Flask into every Python project on your PC
   - **c)** Installs Flask only inside that venv
   - **d)** Deletes Flask from your computer

4. Why should you activate the venv before running `check_setup.py`?
   - **a)** Because `.py` files only run after activation
   - **b)** To make the script run twice as fast
   - **c)** Because VS Code refuses to open the terminal otherwise
   - **d)** So Python can find Flask that you installed in the venv

5. What does `deactivate` do?
   - **a)** Turns off the venv and returns you to normal terminal Python
   - **b)** Deletes the `.venv` folder forever
   - **c)** Uninstalls Flask from the internet
   - **d)** Closes VS Code

---

<details><summary>Click to reveal answers</summary>

1. **a)** A venv is a project toolbox — packages stay separate from other projects.
2. **b)** `(.venv)` in the prompt means the virtual environment is active.
3. **c)** `pip install` inside an active venv installs only there.
4. **d)** Without activation, Python may not see packages you installed in `.venv`.
5. **a)** `deactivate` exits the venv — you are back to system Python.

</details>

---

## What's Next

→ [Lesson 0.2: How the Web Works](../lesson-0-2-how-the-web-works/README.md) — learn what happens when you open a URL.

---

*Your toolbox is ready. Next you will learn how the web actually works!*

[← Choose language](README.md)
