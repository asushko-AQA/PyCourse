# Lesson 2.5: Flash Messages & Validation

> **Course:** Web Applications with Python · **Block:** Making It Beautiful & Interactive · **~35–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 12 — Form Calculator with Friendly Errors**

---

## Explanation

Block 2 finale! Build a **form calculator** — partner to Block 1's URL calculator (`/add/3/5`). Users type numbers in a form instead of the address bar.

When fields are empty, show a **flash message** — a short note that appears once on the next page load.

Create **`my_web_calc/`** at your **project root** (next to `my_web_madlibs/`).

**Path A:**

```text
cd Documents\PyCourse
mkdir my_web_calc
```

Copy [starter/](starter/) into `my_web_calc/`.

**Path B:** Same folder idea on Desktop — see [STUDENT-MAP](../STUDENT-MAP.md).

---

### Step 1: Set secret_key

```python
app.secret_key = "learning-flash-key"
```

Flash needs a secret for local sessions. Any random string works for practice.

---

### Step 2: Validate and calculate

```python
@app.route("/", methods=["GET", "POST"])
def calc():
    total = None
    if request.method == "POST":
        raw_a = request.form.get("a", "").strip()
        raw_b = request.form.get("b", "").strip()
        if not raw_a or not raw_b:
            flash("Please enter both numbers.")
        else:
            try:
                num_a = int(raw_a)
                num_b = int(raw_b)
                total = num_a + num_b
            except ValueError:
                flash("Use whole numbers only (like 3 or 10).")
    return render_template("calc.html", total=total)
```

**TODO in starter:** Complete the POST block in `app.py`.

---

### Step 3: Show flash in calc.html

```html
{% for message in get_flashed_messages() %}
<p class="error"><strong>{{ message }}</strong></p>
{% endfor %}
```

Result appears on the same page when `total` is set:

```html
{% if total is not none %}
<h2>Result</h2>
<p><strong>{{ total }}</strong></p>
{% endif %}
```

---

### Step 4: Run from my_web_calc

```text
cd Documents\PyCourse\my_web_calc
python app.py
```

Or test the lesson starter:

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-5-flash-and-validation
python starter\app.py
```

**Mac/Linux:** `python starter/app.py`

1. Enter `7` and `5` → result `12`
2. Leave a field empty → flash error, no crash

---

## Quick Drills

1. **Flash once** — trigger an error, then submit valid numbers. Does the old error stay?
2. **Compare** — Block 1 URL calculator vs this form calculator.
3. **Bad input** — type `abc` + `2`. What flash message appears?

---

## Practice Task

**Quest name:** Your Web Calculator

1. Copy [starter/](starter/) to **`my_web_calc/`** at project root.
2. Complete all TODO lines.
3. Customize flash message text.
4. **Bonus:** Add subtraction with a dropdown.

**Reference solution:** [solution/](solution/)

---

## Debug Corner

**Problem:** `RuntimeError: The session is unavailable because no secret key was set`

**Cause:** `flash()` called without `app.secret_key`.

**Fix:** Add `app.secret_key = "any-random-string"` after creating the Flask app.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. Why does `flash()` need `app.secret_key`?
   - **a)** Flash uses sessions locally; the secret key makes that work
   - **b)** To change the CSS background color
   - **c)** To replace `request.form`
   - **d)** Because addition only works with a secret

2. When should you call `flash("Please enter both numbers.")`?
   - **a)** When a required field is empty after POST
   - **b)** Every time the server starts
   - **c)** Before activating `.venv`
   - **d)** Only when the user visits with GET

3. User types `abc` in a number field. What should happen?
   - **a)** Show a friendly flash error — not a scary crash
   - **b)** Silently ignore the form forever
   - **c)** Delete `calc.html`
   - **d)** Redirect to Course 3 automatically

4. How is this form calculator different from Block 1's `/add/3/5`?
   - **a)** Users type numbers in a form instead of putting them in the URL
   - **b)** It does not use Python
   - **c)** It cannot show errors
   - **d)** It only works without templates

5. Where do you loop to **display** flash messages in the template?
   - **a)** `{% for message in get_flashed_messages() %}`
   - **b)** `{% extends "flash.html" %}` only
   - **c)** `request.args.get("message")`
   - **d)** Inside `static/style.css`

---

<details><summary>Click to reveal answers</summary>

1. **a)** Sessions need a secret key to store flash messages safely.
2. **a)** Flash user-friendly errors when validation fails.
3. **a)** Catch bad input with `try/except` or checks, then `flash()`.
4. **a)** Forms hide numbers from the URL and feel more like real apps.
5. **a)** `get_flashed_messages()` returns messages to show once.

</details>

---

## What's Next

→ [Block 2 readiness checklist](../README.md#block-2-readiness-checklist)  
→ [Course 2 graduation checklist](../../../STUDENT-MAP.md#course-2-graduation-checklist)  
→ [Course 3: Game Development](../../../../course-3-game-dev/README.md) — Pygame is next!

---

*You finished Block 2 — templates, forms, CSS, and validation. Real web apps, built by you!*
