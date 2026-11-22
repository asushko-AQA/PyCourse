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

### Step 2: How a CSS rule is written

CSS is a list of rules. Every rule has the same shape — a **selector**, then curly braces, then `property: value;` lines:

```css
selector {
    property: value;
}
```

The selector names the HTML you want to change. `body` is the whole page. `nav` is the menu. `nav a` is a link inside that menu. `nav a:hover` is that link when the mouse is on it. `h1` is the big heading. `button` and `input[type="text"]` are the button and the text box (you style those in the bonus).

Here is the page rule, with this lesson's colors. `#f4f7fb` is the soft gray-blue background, and `#222` is dark text. `max-width` plus `margin: 2rem auto` keeps the words in a centered column:

```css
body {
    background: #f4f7fb;
    color: #222;
    max-width: 640px;
    margin: 2rem auto;
}
```

Give each other selector its own `{ }` block, and end every property with `;`:

- `nav` — `border-bottom: 2px solid #4a90d9;` (blue line under the menu)
- `nav a` — `color: #4a90d9;` (same blue) and `font-weight: bold;`
- `h1` — `color: #2c5282;` (a deeper blue)

`@media (max-width: 480px)` is a rule that applies only on a narrow screen, like a phone. Inside it, set `body` to `margin: 1rem;` and `padding: 0.5rem;` so the text still fits.

**Bonus colors:** `button` uses `background: #4a90d9;` and `color: white;`. `input[type="text"]` uses `border: 1px solid #ccc;`.

---

### Step 3: Style the page

Finish the `# TODO` in [starter/static/style.css](starter/static/style.css) with the rules from Step 2. The starter stays your file to fill in — peek at [solution/static/style.css](solution/static/style.css) only after you try.

- Background color and `max-width` on `body`
- Nav link colors (`nav` and `nav a`)
- An `@media` rule for small screens

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

**1. Activate your venv.** The VS Code terminal starts in your project root (where `.venv` lives). Activate:

```text
.venv\Scripts\Activate.ps1
```

**Command Prompt (cmd):** `.venv\Scripts\activate.bat` · **macOS/Linux:** `source .venv/bin/activate`

You should see `(.venv)` at the start of the terminal line.

**2. Go into this lesson folder and run:**

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-4-static-files-css
python starter\app.py
```

**macOS/Linux:**

```text
cd course-2-web-apps/block-2-making-it-beautiful-interactive/lesson-2-4-static-files-css
python starter/app.py
```

**Path B:** Copy `starter/` into your workshop folder (next to `.venv`) and run `python app.py` from that copy. See [STUDENT-MAP](../STUDENT-MAP.md).

Visit `/` and `/about`. A gray-blue background (`#f4f7fb`) and a blue nav mean CSS loaded.

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

With `(.venv)` active, from your project root:

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-4-static-files-css
python starter\app.py
```

**macOS/Linux:**

```text
cd course-2-web-apps/block-2-making-it-beautiful-interactive/lesson-2-4-static-files-css
python starter/app.py
```

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
   - **a)** Activate the virtual environment
   - **b)** Control colors, fonts, and layout — how the page looks
   - **c)** Store Python routes
   - **d)** Replace HTML entirely

2. Where should `style.css` live in a Flask project?
   - **a)** In the `.venv` folder
   - **b)** On a USB drive only
   - **c)** In the `static/` folder next to `app.py`
   - **d)** Inside `templates/base.html` only as plain text

3. Why use `{{ url_for('static', filename='style.css') }}` in a template?
   - **a)** To read POST form data
   - **b)** To set `app.secret_key`
   - **c)** To define a dynamic route `<name>`
   - **d)** Flask builds the correct link to the CSS file

4. HTML tells the browser what to show. CSS tells it what?
   - **a)** How it should look
   - **b)** Which pip packages to install
   - **c)** Which port to open
   - **d)** How to run `python app.py`

5. What does a `@media (max-width: 480px)` rule help with?
   - **a)** Delete flash messages
   - **b)** Adjust styles on narrow screens (responsive layout)
   - **c)** Block all CSS from loading
   - **d)** Convert GET forms to POST

---

<details><summary>Click to reveal answers</summary>

1. **b)** CSS styles the page — colors, spacing, fonts.
2. **c)** Flask serves files from `static/` automatically.
3. **d)** `url_for` generates the right `/static/style.css` path.
4. **a)** HTML = structure; CSS = appearance.
5. **b)** Media queries tweak layout for small screens.

</details>

---

## What's Next

→ [Lesson 2.5: Flash Messages & Validation](../lesson-2-5-flash-and-validation/README.md) — friendly errors and form calculator capstone.

---

*Your pages have style. One more lesson to finish Block 2!*
