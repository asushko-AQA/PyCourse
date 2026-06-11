# Lesson 2.4: Static Files & CSS

> **Course:** Web Applications with Python · **Block:** Making It Beautiful & Interactive · **~30 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Styled Studio — CSS & Static Files**

---

## Explanation

HTML tells the browser *what* to show. **CSS** tells it *how* it looks.

Flask serves CSS from a **`static/`** folder next to `app.py`. Link it with **`url_for`**:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

**Responsive** layouts adapt to narrow screens using `@media (max-width: 480px)`.

---

### Step 1: Link the stylesheet

In [starter/templates/base.html](starter/templates/base.html), add the `<link>` tag in `<head>`.

---

### Step 2: Style the page

Finish TODOs in [starter/static/style.css](starter/static/style.css):

- Background color and `max-width` on `body`
- Nav link colors
- `@media` rule for small screens

---

### Step 3: Add the About route

```python
@app.route("/about")
def about():
    return render_template(
        "about.html",
        page_title="About",
        tagline="CSS makes plain HTML look like a real website.",
    )
```

Home and About both extend `base.html` and share the same CSS.

---

### Step 4: Run the app

**Path A:**

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-4-static-files-css
python starter\app.py
```

**Path B:** Copy `starter/` — see [STUDENT-MAP](../STUDENT-MAP.md).

**Mac/Linux:** `python starter/app.py`

Visit `/` and `/about`. Gray-blue background and styled nav mean CSS loaded.

---

## Quick Drills

1. **Color swap** — change `background` in `body`. Refresh.
2. **Inspect** — browser DevTools → Network → confirm `style.css` status 200.
3. **Narrow test** — shrink the window. Does padding change at 480px?

---

## Practice Task

**Quest name:** Brand Your Studio

1. Complete TODOs in `base.html`, `style.css`, and `app.py`.
2. Pick your own color theme.
3. **Bonus:** Style the `<button>` and `<input>` like the solution does.

**Reference solution:** [solution/](solution/)

---

## Debug Corner

**Problem:** Page looks like plain HTML — no colors

**Cause:** CSS not linked or `static/style.css` missing.

**Fix:** Check `url_for('static', filename='style.css')` in `base.html` and that `static/style.css` exists.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. What is the main job of **CSS** in this lesson?
   - **a)** Control colors, fonts, and layout — how the page looks
   - **b)** Store Python routes
   - **c)** Replace HTML entirely
   - **d)** Activate the virtual environment

2. Where should `style.css` live in a Flask project?
   - **a)** In the `static/` folder next to `app.py`
   - **b)** Inside `templates/base.html` only as plain text
   - **c)** In the `.venv` folder
   - **d)** On a USB drive only

3. Why use `{{ url_for('static', filename='style.css') }}` in a template?
   - **a)** Flask builds the correct link to the CSS file
   - **b)** To read POST form data
   - **c)** To set `app.secret_key`
   - **d)** To define a dynamic route `<name>`

4. HTML tells the browser what to show. CSS tells it what?
   - **a)** How it should look
   - **b)** Which pip packages to install
   - **c)** Which port to open
   - **d)** How to run `python app.py`

5. What does a `@media (max-width: 480px)` rule help with?
   - **a)** Adjust styles on narrow screens (responsive layout)
   - **b)** Block all CSS from loading
   - **c)** Convert GET forms to POST
   - **d)** Delete flash messages

---

<details><summary>Click to reveal answers</summary>

1. **a)** CSS styles the page — colors, spacing, fonts.
2. **a)** Flask serves files from `static/` automatically.
3. **a)** `url_for` generates the right `/static/style.css` path.
4. **a)** HTML = structure; CSS = appearance.
5. **a)** Media queries tweak layout for small screens.

</details>

---

## What's Next

→ [Lesson 2.5: Flash Messages & Validation](../lesson-2-5-flash-and-validation/README.md) — friendly errors and form calculator capstone.

---

*Your pages have style. One more lesson to finish Block 2!*
