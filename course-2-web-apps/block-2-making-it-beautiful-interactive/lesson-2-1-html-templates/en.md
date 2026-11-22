# Lesson 2.1: HTML Templates

> **Course:** Web Applications with Python · **Block:** Making It Beautiful & Interactive · **~30 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Studio Pages — Shared Layout**

---

## Explanation

In Block 1 you returned HTML as one big string. **Templates** are separate HTML files in a `templates/` folder. Flask fills them in with **Jinja2**.

Think of `base.html` as a picture frame: navigation links and an empty spot (`{% block content %}`) where each page paints its own content.

**New term:** `render_template("home.html", page_title="Home")` — Flask finds the file, runs Jinja2, and sends finished HTML to the browser.

---

### Step 1: Study base.html

[starter/templates/base.html](starter/templates/base.html) has shared navigation. Child pages **extend** it:

```html
{% extends "base.html" %}
{% block content %}
<h1>{{ headline }}</h1>
{% endblock %}
```

---

### Step 2: Home route

```python
@app.route("/")
def home():
    return render_template(
        "home.html",
        page_title="Home",
        headline="Welcome to My Studio",
    )
```

Variables you pass in Python become `{{ headline }}` in HTML.

---

### Step 3: Add About and Jokes routes

**TODO in starter:** Add `/about` and `/jokes` routes with their own templates. Pass joke text as variables — same idea as Block 1 Lesson 1.4, but with template files instead of one long string.

---

### Step 4: Run the app

**1. Activate your venv.** In VS Code, open the folder that has your `.venv` (**Path A:** the `PyCourse` folder; **Path B:** your own workshop folder, for example `web_workshop`). Open the terminal (**Terminal → New Terminal**) — it already starts in that folder. Activate:

```text
.venv\Scripts\Activate.ps1
```

**Command Prompt (cmd):** `.venv\Scripts\activate.bat` · **macOS/Linux:** `source .venv/bin/activate`

You should see `(.venv)` at the start of the terminal line.

**2. Go to the starter folder and run.**

**Path A:**

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-1-html-templates\starter
python app.py
```

**macOS/Linux:** `cd course-2-web-apps/block-2-making-it-beautiful-interactive/lesson-2-1-html-templates/starter`, then `python app.py`

**Path B:** Copy this lesson's whole `starter/` folder (with `templates/` inside) into your workshop folder, next to `.venv`, and rename it `lesson-2-1`. Then `cd lesson-2-1` and `python app.py`. See [STUDENT-MAP](../STUDENT-MAP.md).

Open `http://127.0.0.1:5000/` and click **About** and **Jokes**.

**Expected result:** All three pages share the same nav bar; only the middle content changes.

---

## Code Example

**File: [solution/app.py](solution/app.py)**

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "home.html",
        page_title="Home",
        headline="Welcome to My Studio",
    )


@app.route("/about")
def about():
    return render_template(
        "about.html",
        page_title="About",
        bio="I am learning Flask and building pages with templates!",
    )


if __name__ == "__main__":
    app.run(port=5000, debug=True)
```

Child templates live in `solution/templates/` — each extends [solution/templates/base.html](solution/templates/base.html).

---

## Code Execution

With `(.venv)` active, from the folder you opened in VS Code:

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-1-html-templates\starter
python app.py
```

**macOS/Linux:** `cd course-2-web-apps/block-2-making-it-beautiful-interactive/lesson-2-1-html-templates/starter`, then `python app.py` · **Path B:** `cd lesson-2-1`, then `python app.py`

**Expected output (terminal):**

```text
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Open `http://127.0.0.1:5000/`, then **About** and **Jokes**.

**Expected output (browser, home page):**

```text
Home | About | Jokes
Welcome to My Studio
Use the links above to visit About and Jokes.
```

**Expected result:** Shared navigation on every page; only the middle section changes. Stop the server with **Ctrl+C** when you are done.

---

## Quick Drills

1. **Block spot** — find `{% block content %}` in `base.html`. What goes there?
2. **New variable** — pass `bio="..."` to `about.html` and show it in a `<p>`.
3. **Fourth page** — add `/contact` with a new child template (bonus: link it in nav).

---

## Practice Task

**Quest name:** Finish Studio Pages

1. Complete all TODO lines in `app.py` and child templates.
2. Visit `/`, `/about`, and `/jokes`.
3. **Bonus:** Write your own joke in the Jokes template.

**Reference solution:** [solution/](solution/)

---

## Debug Corner

**Problem:** `TemplateNotFound: home.html`

**Cause:** Flask looks for templates in a folder called `templates/` that sits **right next to `app.py`** — not in the folder your terminal happens to be in.

**Fix:** Check that the file is at `templates/home.html` beside `app.py` (if you copied `app.py`, copy its `templates/` folder too). Check the spelling: the folder is `templates` with an **s**, and the file name must match `render_template("home.html", ...)` exactly.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. Why move HTML into a `templates/` folder instead of one giant string in `app.py`?
   - **a)** Browsers cannot show strings anymore
   - **b)** pip installs templates automatically
   - **c)** Easier to read, edit, and reuse layout across pages
   - **d)** Flask refuses to return strings after Block 1

2. What does `render_template("home.html", headline="Welcome")` do?
   - **a)** Downloads home.html from the internet
   - **b)** Copies CSS into the terminal
   - **c)** Activates the virtual environment
   - **d)** Fills the template with variables and sends HTML to the browser

3. In Jinja2, what does `{{ headline }}` mean?
   - **a)** Show the value of the `headline` variable from Python
   - **b)** Start a Python function
   - **c)** Comment out HTML
   - **d)** Link to `static/style.css`

4. What is `{% block content %}` in `base.html` for?
   - **a)** The port number (5000)
   - **b)** A placeholder where each child page puts its unique content
   - **c)** A list of pip packages
   - **d)** The Flask secret key

5. A child template starts with `{% extends "base.html" %}`. What does that mean?
   - **a)** Run the app without `app.run()`
   - **b)** Send forms with GET only
   - **c)** Reuse the shared frame (nav, layout) from `base.html`
   - **d)** Delete `base.html` after saving

---

<details><summary>Click to reveal answers</summary>

1. **c)** Templates separate page layout from Python logic.
2. **d)** `render_template` merges data into HTML files.
3. **a)** Double braces print a variable's value.
4. **b)** Child templates fill in the `content` block.
5. **c)** `extends` inherits the parent layout.

</details>

---

## What's Next

→ [Lesson 2.2: HTML Forms](../lesson-2-2-html-forms/README.md) — send data with GET and POST.

---

*One layout, many pages — your studio is taking shape!*
