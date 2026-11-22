# Lesson 2.2: HTML Forms (GET/POST)

> **Course:** Web Applications with Python · **Block:** Making It Beautiful & Interactive · **~30 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Form Lab — GET vs POST**

---

## Explanation

A **form** is how the browser sends data to your server.

| Method | Where data goes | Flask reads it with |
|--------|-----------------|---------------------|
| GET | Visible in the URL (`?name=Alex`) | `request.args.get("name")` |
| POST | Hidden in the request body | `request.form.get("text")` |

This lesson has two mini-forms:

- **`/greet`** — GET only; name appears in the URL
- **`/message`** — GET shows the form, POST echoes what you typed

---

### Step 1: GET greeting

```python
@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "").strip()
    message = ""
    if name:
        message = f"Hello, {name}! Nice to meet you."
    return render_template("greet.html", message=message, name=name)
```

Add the form in `greet.html`:

```html
<form method="get" action="/greet">
    <input type="text" name="name" placeholder="Your name">
    <button type="submit">Say hi</button>
</form>
```

---

### Step 2: POST message echo

```python
@app.route("/message", methods=["GET", "POST"])
def message():
    text = ""
    reply = ""
    if request.method == "POST":
        text = request.form.get("text", "").strip()
        if text:
            reply = f"You said: {text}"
    return render_template("message.html", message=reply, text=text)
```

Add the form in `message.html` — no `action` needed, because the form posts back to the same URL:

```html
<form method="post">
    <input type="text" name="text" placeholder="Your message">
    <button type="submit">Send</button>
</form>
```

**TODO in starter:** Add both routes and finish the forms in the templates.

---

### Step 3: Run and compare

**1. Activate your venv.** In VS Code, open the folder that has your `.venv` (**Path A:** `PyCourse`; **Path B:** your workshop folder). The terminal starts there. Activate:

```text
.venv\Scripts\Activate.ps1
```

**Command Prompt (cmd):** `.venv\Scripts\activate.bat` · **macOS/Linux:** `source .venv/bin/activate`

You should see `(.venv)` at the start of the terminal line.

**2. Go to the starter folder and run.**

**Path A:**

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-2-html-forms\starter
python app.py
```

**macOS/Linux:** `cd course-2-web-apps/block-2-making-it-beautiful-interactive/lesson-2-2-html-forms/starter`, then `python app.py`

**Path B:** Copy this lesson's `starter/` folder into your workshop folder, next to `.venv`, and rename it `lesson-2-2`. Then `cd lesson-2-2` and `python app.py`. See [STUDENT-MAP](../STUDENT-MAP.md).

1. Open `/greet`, submit a name — watch the URL change to `?name=...`
2. Open `/message`, submit text — URL stays `/message`

**Expected result:** Both pages echo your input on a results area.

---

## Code Example

**File: [solution/app.py](solution/app.py)**

```python
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "").strip()
    message = ""
    if name:
        message = f"Hello, {name}! Nice to meet you."
    return render_template("greet.html", message=message, name=name)


@app.route("/message", methods=["GET", "POST"])
def message():
    text = ""
    reply = ""
    if request.method == "POST":
        text = request.form.get("text", "").strip()
        if text:
            reply = f"You said: {text}"
    return render_template("message.html", message=reply, text=text)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
```

Form HTML is in `solution/templates/` — see [solution/templates/greet.html](solution/templates/greet.html).

---

## Code Execution

With `(.venv)` active, from the folder you opened in VS Code:

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-2-html-forms\starter
python app.py
```

**macOS/Linux:** `cd course-2-web-apps/block-2-making-it-beautiful-interactive/lesson-2-2-html-forms/starter`, then `python app.py` · **Path B:** `cd lesson-2-2`, then `python app.py`

**Expected output (terminal):**

```text
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

1. Open `http://127.0.0.1:5000/greet`, enter `Sam` — URL becomes `/greet?name=Sam`
2. Open `http://127.0.0.1:5000/message`, type `Hi there` and send — URL stays `/message`

**Expected output (browser, under each form):**

```text
Hello, Sam! Nice to meet you.
```

```text
You said: Hi there
```

**Expected result:** Both pages show your input in the results area. Stop the server with **Ctrl+C** when you are done.

---

## Quick Drills

1. **URL detective** — submit GET with name `Sam`. Copy the full URL.
2. **Empty POST** — submit `/message` with an empty box. What happens?
3. **Strip** — why do we call `.strip()` on form values?

---

## Practice Task

**Quest name:** Polite Greeter

1. Finish TODO routes and form HTML in [starter/](starter/).
2. Customize the greeting and echo messages.
3. **Bonus:** Add a `color` field to the POST form and echo it too.

**Reference solution:** [solution/](solution/)

---

## Debug Corner

**Problem:** `Method Not Allowed` when submitting a form

**Cause:** The route does not allow that HTTP method.

**Fix:** Use `methods=["GET"]` for GET forms and `methods=["GET", "POST"]` when the same URL handles both.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. With a **GET** form on `/greet`, where does the name often appear after submit?
   - **a)** Only inside the server hard drive, never visible
   - **b)** In the CSS file
   - **c)** In the `.venv` folder name
   - **d)** In the URL, like `?name=Alex`

2. Which Flask code reads GET data from the URL?
   - **a)** `request.args.get("name")`
   - **b)** `request.form.get("name")`
   - **c)** `flash("name")`
   - **d)** `url_for('static', filename='name')`

3. Which Flask code reads POST data from a submitted form?
   - **a)** `@app.route("<text>")`
   - **b)** `request.form.get("text")`
   - **c)** `request.args.get("text")`
   - **d)** `importlib.metadata.version("text")`

4. Why might `/message` use `methods=["GET", "POST"]`?
   - **a)** To install Flask twice
   - **b)** So the URL always shows `?text=...`
   - **c)** GET shows the form; POST handles the submitted data on the same URL
   - **d)** Because GET and POST cannot use templates

5. Why call `.strip()` on form values?
   - **a)** Delete the form from HTML
   - **b)** Convert numbers to floats automatically
   - **c)** Hide flash messages
   - **d)** Remove extra spaces at the start or end of what the user typed

---

<details><summary>Click to reveal answers</summary>

1. **d)** GET form data shows up in the query string.
2. **a)** `request.args` is for URL query parameters.
3. **b)** `request.form` is for POST body fields.
4. **c)** One URL can show the form (GET) and process it (POST).
5. **d)** `.strip()` trims accidental spaces from user input.

</details>

---

## What's Next

→ [Lesson 2.3: Mad-Libs Capstone](../lesson-2-3-madlibs-capstone/README.md) — silly story from form fields.

---

*Forms are how visitors talk to your app. Next up: a story machine!*
