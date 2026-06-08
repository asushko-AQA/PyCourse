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

## What's Next

→ [Lesson 2.5: Flash Messages & Validation](../lesson-2-5-flash-and-validation/README.md) — friendly errors and form calculator capstone.

---

*Your pages have style. One more lesson to finish Block 2!*
