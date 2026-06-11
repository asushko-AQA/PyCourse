# Lesson 1.1: Installing Flask

> **Course:** Web Applications with Python · **Block:** Web Basics with Flask · **~30 min**  
> [Choose language / Выбрать язык](README.md) · [Русский →](ru.md)

---

## Title

**Level 1 — Flask Check: Is Your Route Lab Ready?**

---

## Explanation

Welcome to **Route Lab** — Block 1 of Course 2! You already built a **virtual environment** (`.venv`) and installed Flask in [Block 0, Lesson 0.1](../../block-0-environment-setup/lesson-0-1-virtual-environments/README.md). This lesson is a **quick check**, not a repeat of venv setup.

Think of your venv as a **private toolbox** for this web project. Flask lives inside that toolbox. Before every Flask lesson, open the toolbox first — that is called **activating** the venv.

---

### Step 1: Open your project in VS Code

1. Open VS Code.
2. **File → Open Folder** — choose your `PyCourse` folder (or your own project folder with `.venv`).
3. **Terminal → New Terminal** (or **Ctrl + `**).

---

### Step 2: Activate your venv (quick reminder)

**Windows PowerShell** (most common in VS Code):

```text
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt (cmd):**

```text
.venv\Scripts\activate.bat
```

**macOS / Linux:**

```text
source .venv/bin/activate
```

**How you know it worked:** your prompt shows `(.venv)` at the start.

**No `.venv` yet?** Go back to [Lesson 0.1](../../block-0-environment-setup/lesson-0-1-virtual-environments/README.md), create one, run `pip install flask`, then return here.

---

### Step 3: Confirm Flask is installed

With `(.venv)` active, run:

```text
pip list
```

Scroll until you see **Flask** with a version number (for example `3.0.0`).

**Missing Flask?** Install it now:

```text
pip install flask
```

---

### Step 4: Open the check script

Open [starter/check_flask.py](starter/check_flask.py). You will complete three TODOs:

1. `import flask` at the top
2. `print("Flask import OK!")`
3. Print the Flask version using `importlib.metadata.version("flask")`

**Hint for the version line:**

```python
import importlib.metadata

print(f"Flask version: {importlib.metadata.version('flask')}")
```

---

### Step 5: cd to this lesson folder

**Path A — PyCourse repo:**

```text
cd course-2-web-apps\block-1-web-basics-flask\lesson-1-1-installing-flask
```

**Path B — your own copy:** `cd` to wherever you saved `check_flask.py`.

---

### Step 6: Run the check

```text
python starter\check_flask.py
```

**Expected output:**

```text
Flask import OK!
Flask version: 3.x.x
```

(Your version number may differ — that is fine.)

---

## Quick Drills

1. Run `pip list` — circle **Flask** on a sticky note.
2. Run the check script — both lines print without errors.
3. Type `deactivate`, run the script again — see `ModuleNotFoundError`? Reactivate and try again.

---

## Try it yourself

### Challenge 1 (required)

Add one more `print()` line that says `Route Lab ready!` after the version line. Run the script again.

### Challenge 2 (bonus)

Look at `pip show flask` in the terminal. Find the **Location** line — that is where pip stored Flask inside your venv.

---

## Debug Corner

**Problem:** `ModuleNotFoundError: No module named 'flask'`

**Cause:** The venv is not active, or Flask was never installed in this venv.

**Fix:** Run `.\.venv\Scripts\Activate.ps1` (or your OS command), then `pip install flask`, then run the script again.

---

**Problem:** `running scripts is disabled on this system` when activating (PowerShell)

**Cause:** Windows security blocked the activation script.

**Fix:** Ask a parent or teacher to run once: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` — then try activating again.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. This lesson is mainly a check that Flask is ready — not a repeat of what step from Block 0?
   - **a)** Creating and using a virtual environment
   - **b)** Learning Turtle graphics
   - **c)** Writing Mad-Libs in the terminal
   - **d)** Installing Pygame

2. If `pip list` shows Flask while `(.venv)` is active, where is Flask installed?
   - **a)** Inside your project's venv
   - **b)** Only on the Flask company website
   - **c)** Inside your browser cache
   - **d)** In every folder on your Desktop

3. You run `python starter\check_flask.py` and get `ModuleNotFoundError: No module named 'flask'`. What is the most likely fix?
   - **a)** Activate the venv, then `pip install flask`, then run again
   - **b)** Delete `.venv` and never use pip again
   - **c)** Change the port to 8080
   - **d)** Add `@app.route` to the check script

4. What should `check_flask.py` print when everything works?
   - **a)** `Flask import OK!` and a Flask version line
   - **b)** `Hello, Web World!` in the browser only
   - **c)** A list of every website on the internet
   - **d)** Nothing — silence means success

5. Why do Flask lessons start by activating `.venv`?
   - **a)** So Python uses the toolbox where Flask lives
   - **b)** Because Flask only works on Tuesdays
   - **c)** To turn on `debug=True` automatically
   - **d)** Because routes cannot be created without it

---

<details><summary>Click to reveal answers</summary>

1. **a)** Block 0 taught venv + pip; this lesson verifies Flask is there.
2. **a)** Active venv + `pip list` shows packages in that environment.
3. **a)** Usually the venv is off or Flask was never installed there.
4. **a)** The check script confirms import and prints the version.
5. **a)** Flask must be importable from the activated project venv.

</details>

---

## What's Next

→ [Lesson 1.2: First Web Page](../lesson-1-2-first-web-page/README.md) — serve **Hello, Web World!** in your browser.

---

*Flask is in your toolbox. Next stop: a real web page!*

[← Choose language](README.md)
