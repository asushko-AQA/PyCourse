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

**TODO in starter:** Add both routes and finish the forms in the templates.

---

### Step 3: Run and compare

**Path A:**

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-2-html-forms
python starter\app.py
```

**Path B:** Copy `starter/` — see [STUDENT-MAP](../STUDENT-MAP.md).

**Mac/Linux:** `python starter/app.py`

1. Open `/greet`, submit a name — watch the URL change to `?name=...`
2. Open `/message`, submit text — URL stays `/message`

**Expected result:** Both pages echo your input on a results area.

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
   - **a)** In the URL, like `?name=Alex`
   - **b)** Only inside the server hard drive, never visible
   - **c)** In the CSS file
   - **d)** In the `.venv` folder name

2. Which Flask code reads GET data from the URL?
   - **a)** `request.args.get("name")`
   - **b)** `request.form.get("name")`
   - **c)** `flash("name")`
   - **d)** `url_for('static', filename='name')`

3. Which Flask code reads POST data from a submitted form?
   - **a)** `request.form.get("text")`
   - **b)** `request.args.get("text")`
   - **c)** `importlib.metadata.version("text")`
   - **d)** `@app.route("<text>")`

4. Why might `/message` use `methods=["GET", "POST"]`?
   - **a)** GET shows the form; POST handles the submitted data on the same URL
   - **b)** Because GET and POST cannot use templates
   - **c)** To install Flask twice
   - **d)** So the URL always shows `?text=...`

5. Why call `.strip()` on form values?
   - **a)** Remove extra spaces at the start or end of what the user typed
   - **b)** Delete the form from HTML
   - **c)** Convert numbers to floats automatically
   - **d)** Hide flash messages

---

<details><summary>Click to reveal answers</summary>

1. **a)** GET form data shows up in the query string.
2. **a)** `request.args` is for URL query parameters.
3. **a)** `request.form` is for POST body fields.
4. **a)** One URL can show the form (GET) and process it (POST).
5. **a)** `.strip()` trims accidental spaces from user input.

</details>

---

## What's Next

→ [Lesson 2.3: Mad-Libs Capstone](../lesson-2-3-madlibs-capstone/README.md) — silly story from form fields.

---

*Forms are how visitors talk to your app. Next up: a story machine!*
