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

**Path A:**

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-1-html-templates
python starter\app.py
```

**Path B:** Copy the whole `starter/` folder to your project. Activate venv, run `python app.py`. See [STUDENT-MAP](../STUDENT-MAP.md).

**Mac/Linux:** `python starter/app.py`

Open `http://127.0.0.1:5000/` and click **About** and **Jokes**.

**Expected result:** All three pages share the same nav bar; only the middle content changes.

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

**Cause:** Flask looks for templates inside `templates/` next to `app.py`.

**Fix:** Make sure `starter/templates/home.html` exists and you run `app.py` from the lesson folder (or copy `templates/` with your app).

---

## What's Next

→ [Lesson 2.2: HTML Forms](../lesson-2-2-html-forms/README.md) — send data with GET and POST.

---

*One layout, many pages — your studio is taking shape!*
