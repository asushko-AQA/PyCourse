# Lesson 1.4: Multiple Routes & URL Calculator

> **Course:** Web Applications with Python · **Block:** Web Basics with Flask · **~30–45 min**  
> [Choose language / Выбрать язык](README.md) · [Русский →](ru.md)

---

## Title

**Level 4 — Mini-Site: Home, About, Jokes + URL Calculator**

---

## Explanation

One Flask app can serve **many pages** — each `@app.route` is another door. You already used string variables (`<name>`). Now you will use **integer** variables (`<int:a>`) so Flask converts URL pieces into numbers you can add.

This lesson is your **Block 1 capstone**: a tiny site with links plus a calculator that reads numbers from the URL. In Block 2 you will build a fancier form-based calculator — same idea, better UI.

---

### Step 1: Explore the starter home page

Open [starter/app.py](starter/app.py). The `/` route already returns HTML with links:

- **About** → `/about`
- **Jokes** → `/jokes`
- **Calculator examples** → `/add/3/5`

**HTML** (HyperText Markup Language) tags you will see:

| Tag | Purpose |
|-----|---------|
| `<h1>...</h1>` | Big heading |
| `<p>...</p>` | Paragraph |
| `<a href='/about'>About</a>` | Clickable link |

---

### Step 2: Add the About route

```python
@app.route("/about")
def about():
    return "<h1>About Me</h1><p>I am learning Flask and building web pages with Python!</p>"
```

Change the paragraph to mention **your** name or hobby.

---

### Step 3: Add the Jokes route

```python
@app.route("/jokes")
def jokes():
    return (
        "<h1>Jokes</h1>"
        "<p>Why do programmers prefer dark mode?</p>"
        "<p>Because light attracts bugs!</p>"
    )
```

Swap in your own joke if you like — keep it friendly!

---

### Step 4: Add the URL calculator

```python
@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    total = a + b
    return f"<h1>Calculator</h1><p>{a} + {b} = {total}</p>"
```

**`<int:a>`** tells Flask: "this piece must be a whole number, and call it `a`."

So `/add/3/5` gives `a=3`, `b=5`, and `total=8`.

---

### Step 5: Run and click through the site

```text
cd course-2-web-apps\block-1-web-basics-flask\lesson-1-4-multiple-routes
python starter\app.py
```

Open `http://127.0.0.1:5000` and:

1. Click **About** — see your about page.
2. Click **Jokes** — see the joke.
3. Click a calculator link — see the sum.
4. Manually try `http://127.0.0.1:5000/add/10/7` — should show `10 + 7 = 17`.

Stop with **Ctrl+C** when done.

---

## Quick Drills

1. Home page has working links to all three sections.
2. `/add/0/0` shows `0 + 0 = 0`.
3. Count routes: `/`, `/about`, `/jokes`, `/add/<int:a>/<int:b>` — four routes, one app.

---

## Try it yourself

### Challenge 1 (required)

Add a `/multiply/<int:a>/<int:b>` route that shows `a * b =` the product.

### Challenge 2 (bonus)

On the home page, add another link: `<a href='/add/100/25'>/add/100/25</a>`. Refresh and test it.

**Level up:** Add a link back to home on the About page: `<a href='/'>Home</a>`.

---

## Debug Corner

**Problem:** Link shows `404 Not Found`

**Cause:** The route function is missing, misspelled, or the server was not restarted after saving.

**Fix:** Check `@app.route("/about")` spelling matches the `href` exactly. Save, restart `python starter\app.py`.

---

**Problem:** `/add/three/five` fails or shows an error

**Cause:** `<int:a>` only accepts whole numbers, not words.

**Fix:** Use digits in the URL: `/add/3/5`. That is why we call it a **URL calculator** — numbers live in the address bar.

---

**Problem:** Page shows raw HTML tags as plain text

**Cause:** Rare with Flask return strings — usually a typo in quotes or returning a tuple by accident.

**Fix:** Return one string: `return "<h1>Title</h1><p>Text</p>"` — check all quotes match.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. How can one Flask `app` serve Home, About, and Jokes?
   - **a)** Several `@app.route` decorators — one function per path
   - **b)** Only one route is allowed per file
   - **c)** You must run a separate `python` command for each page
   - **d)** Each page needs its own `.venv`

2. In `<a href='/about'>About</a>`, what does `href` tell the browser?
   - **a)** Which path to request when the link is clicked
   - **b)** Which CSS color to use
   - **c)** Which pip package to install
   - **d)** The secret key for flash messages

3. What does `<int:a>` in `/add/<int:a>/<int:b>` tell Flask?
   - **a)** Capture a whole number from the URL and call it `a`
   - **b)** Accept any word, including `three`
   - **c)** Import the math module automatically
   - **d)** Send the form with POST

4. Why does `/add/three/five` fail with `<int:a>`?
   - **a)** `three` and `five` are words, not integers
   - **b)** Addition only works on the home page
   - **c)** The browser cannot click links
   - **d)** Flask does not allow more than one route

5. This lesson's URL calculator puts numbers where?
   - **a)** In the address bar as part of the URL
   - **b)** Inside a hidden `static/` folder only
   - **c)** In the terminal prompt after `(.venv)`
   - **d)** In a `{% block content %}` in Jinja2

---

<details><summary>Click to reveal answers</summary>

1. **a)** Each path gets its own route function in the same `app`.
2. **a)** `href` is the link destination path.
3. **a)** `<int:a>` converts the URL piece to an integer named `a`.
4. **a)** Integer converters reject non-numeric text.
5. **a)** `/add/3/5` passes numbers through the URL itself.

</details>

---

## What's Next

→ [Lesson 2.1: HTML Templates](../../block-2-making-it-beautiful-interactive/lesson-2-1-html-templates/README.md) — move HTML into template files with `render_template`.

---

*Block 1 complete! You served multiple pages and a calculator from Python. Block 2 makes it beautiful.*

[← Choose language](README.md)
