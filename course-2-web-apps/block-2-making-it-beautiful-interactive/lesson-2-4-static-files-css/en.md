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

### Step 2: Learn a CSS rule

A **selector** names the part of the page you style, such as `body` or `nav a`. The look goes inside braces, one declaration per line: `{ property: value; }`.

```css
nav a {
    color: #4a90d9;
}
```

`nav a` means every link inside the menu. `#4a90d9` is the blue the solution uses for those links.

Treat `body` as the centered container. The starter already sets the font. Add the rest inside that same `body` block:

- `background: #f4f7fb;` — light gray-blue page
- `color: #222;` — dark text
- `max-width: 640px;` — keep the page a readable column
- `margin: 0 auto;` — `auto` centers the column. The solution writes `margin: 2rem auto`, which centers the same way and also adds space above and below
- `padding: 1rem;` and `line-height: 1.5;` — space inside the edges, and lines that are easier to read

The solution uses these selectors and colors, so you can finish every TODO from this list:

| Selector | What to write |
|----------|----------------|
| `body` | background `#f4f7fb`, text `#222`, `max-width: 640px`, `margin: 2rem auto`, `padding: 1rem`, `line-height: 1.5` |
| `nav` | `border-bottom: 2px solid #4a90d9` (blue line under the menu) |
| `nav a` | `color: #4a90d9`, `font-weight: bold`, `text-decoration: none`, `margin-right: 1rem` |
| `nav a:hover` | `text-decoration: underline` when the pointer is on the link |
| `h1` | `color: #2c5282` |
| `button` | background `#4a90d9`, text `white`, `border: none`, `padding: 0.5rem 1rem`, `border-radius: 4px`, `cursor: pointer` |
| `input[type="text"]` | `border: 1px solid #ccc`, `padding: 0.4rem`, `border-radius: 4px`, `width: 100%`, `max-width: 280px` |

`@media` can change rules on a narrow screen. The solution uses `@media (max-width: 480px)` to set `body` to `margin: 1rem` and `padding: 0.5rem`.

---

### Step 3: Style the page

Finish the TODOs in [starter/static/style.css](starter/static/style.css) with the rules from Step 2:

- Background color and `max-width` on `body`
- Nav link colors
- `@media` rule for small screens

---

### Step 4: Add the About route

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

### Step 5: Run the app

**Path A:**

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-4-static-files-css
python starter\app.py
```

**Path B:** Copy `starter/` — see [STUDENT-MAP](../STUDENT-MAP.md).

**Mac/Linux:** `python starter/app.py`

Visit `/` and `/about`. Gray-blue background and styled nav mean CSS loaded.

---

## Code Example

**File: [solution/templates/base.html](solution/templates/base.html)** (CSS link)

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

**File: [solution/app.py](solution/app.py)**

```python
@app.route("/")
def home():
    return render_template(
        "home.html",
        page_title="Home",
        headline="Welcome to My Styled Studio",
    )
```

Styles live in [solution/static/style.css](solution/static/style.css).

---

## Code Execution

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-4-static-files-css
python starter\app.py
```

**Mac/Linux:** `python starter/app.py`

Visit `http://127.0.0.1:5000/` and `/about`.

**Expected result:** Gray-blue background, styled navigation, and readable typography (not plain HTML).

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
