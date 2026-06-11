# Lesson 1.3: Dynamic Routes

> **Course:** Web Applications with Python · **Block:** Web Basics with Flask · **~30 min**  
> [Choose language / Выбрать язык](README.md) · [Русский →](ru.md)

---

## Title

**Level 3 — Personal Greetings with `/hello/<name>`**

---

## Explanation

Lesson 1.2 always returned the same text. Real sites change based on the URL — like `/profile/Alex` showing Alex's page.

A **dynamic route** has a **variable part** in the path. Flask captures that part and passes it to your function as an argument — like handing a name tag to a greeter at the door.

---

### Step 1: Open the starter app

1. Activate `.venv`.
2. Open [starter/app.py](starter/app.py).

The home route is already done. You add one new route with a `<name>` placeholder.

---

### Step 2: Add `/hello/<name>`

Complete the TODO:

```python
@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"
```

**What each piece means:**

| Piece | Meaning |
|-------|---------|
| `/hello/<name>` | Path with a variable slot called `name` |
| `def hello(name):` | Flask fills `name` from the URL |
| `f"Hello, {name}!"` | f-string — plug the URL value into the text |

---

### Step 3: Run the server

```text
cd course-2-web-apps\block-1-web-basics-flask\lesson-1-3-dynamic-routes
python starter\app.py
```

---

### Step 4: Test in the browser

Try these addresses (change `Alex` to your name):

| URL | Expected page |
|-----|----------------|
| `http://127.0.0.1:5000/` | Welcome message with a hint |
| `http://127.0.0.1:5000/hello/Alex` | `Hello, Alex!` |
| `http://127.0.0.1:5000/hello/Web` | `Hello, Web!` |

Edit only the **last part** of the URL in the address bar and press **Enter** — no code change needed!

---

### Step 5: Stop when finished

**Ctrl+C** in the terminal.

---

## Quick Drills

1. Visit three different names in `/hello/...` — each shows a different greeting.
2. Spell your name with caps — does Flask keep the caps you typed?
3. Visit `/hello/` with nothing after — read the 404 error (Flask could not match a route).

---

## Try it yourself

### Challenge 1 (required)

Add `/goodbye/<name>` that returns `Goodbye, {name}! See you later!`

### Challenge 2 (bonus)

Add `/hello/<name>/<age>` with **two** variables. Return: `Hello, Alex! You are 12 years old.` (Use two parameters: `def hello(name, age):` — note: `age` comes from the URL as text; that is OK for display.)

---

## Debug Corner

**Problem:** `TypeError` or strange error about function arguments

**Cause:** The variable name in `<name>` does not match the function parameter, or you have a typo in the decorator.

**Fix:** Use `@app.route("/hello/<name>")` with `def hello(name):` — the names must match exactly.

---

**Problem:** `404 Not Found` for `/hello/Alex`

**Cause:** Server not running, wrong port, or route not saved.

**Fix:** Confirm `python starter\app.py` is running, check spelling (`/hello/` not `/hellos/`), save the file and restart if needed.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. What makes `/hello/<name>` a **dynamic** route?
   - **a)** Part of the URL changes and Flask passes it into your function
   - **b)** The page reloads automatically every second
   - **c)** It only works on mobile phones
   - **d)** It requires a CSS file

2. In `@app.route("/hello/<name>")` and `def hello(name):`, what must match?
   - **a)** The variable name in the path and the function parameter
   - **b)** The port number and the file name
   - **c)** The browser brand and the OS version
   - **d)** The HTML tag and the pip version

3. You visit `/hello/Alex`. What should the `name` argument be?
   - **a)** `Alex`
   - **b)** `/hello`
   - **c)** `name`
   - **d)** `5000`

4. You visit `/hello/` with nothing after the slash. What often happens?
   - **a)** Flask cannot match the route — often a 404 error
   - **b)** The server installs Flask again
   - **c)** The browser deletes the URL
   - **d)** Python opens a new `.venv`

5. Why use an f-string like `f"Hello, {name}!"`?
   - **a)** To plug the URL value into the text you send back
   - **b)** To store files in the `static/` folder
   - **c)** To activate the virtual environment
   - **d)** To hide the URL from the user forever

---

<details><summary>Click to reveal answers</summary>

1. **a)** `<name>` captures the changing part of the URL.
2. **a)** The path variable and parameter must share the same name.
3. **a)** Flask passes the URL segment as `name='Alex'`.
4. **a)** An empty name usually does not match the route pattern.
5. **a)** f-strings insert the dynamic value into your greeting.

</details>

---

## What's Next

→ [Lesson 1.4: Multiple Routes & URL Calculator](../lesson-1-4-multiple-routes/README.md) — build a mini-site with Home, About, Jokes, and `/add/3/5`.

---

*URLs can carry data into Python. Next: a whole mini-site plus a calculator!*

[← Choose language](README.md)
