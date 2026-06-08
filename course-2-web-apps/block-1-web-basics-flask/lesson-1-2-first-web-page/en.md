# Lesson 1.2: First Web Page

> **Course:** Web Applications with Python · **Block:** Web Basics with Flask · **~30 min**  
> [Choose language / Выбрать язык](README.md) · [Русский →](ru.md)

---

## Title

**Level 2 — Hello, Web World! Your First Live Page**

---

## Explanation

In [Lesson 0.2](../../block-0-environment-setup/lesson-0-2-how-the-web-works/README.md) you learned the big picture: your **browser** asks for a page, a **server** sends a **response**. Today you **are** the server — Flask listens for requests and your Python code decides what to send back.

**Flask** is a small Python library that turns URLs into Python functions. One function can answer one address — like a doorbell that plays a specific message.

---

### Step 1: Activate venv and open the starter

1. Open VS Code terminal.
2. Activate `.venv` (see [Lesson 1.1](../lesson-1-1-installing-flask/README.md) if you forgot the command).
3. Open [starter/app.py](starter/app.py).

The file already creates `app = Flask(__name__)`. You add the route and the `app.run()` line.

---

### Step 2: What is a route?

A **route** connects a **URL path** (like `/`) to a **Python function**.

- `@app.route("/")` — when someone visits the home address, call this function
- `def home():` — the function that runs
- `return "Hello, Web World!"` — the text sent to the browser

Fill in the TODOs so your file looks like this:

```python
@app.route("/")
def home():
    return "Hello, Web World!"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
```

**`debug=True`** helps while learning — Flask reloads when you save changes. Turn it off before sharing a real site on the internet (we stay local for now).

---

### Step 3: cd to this lesson folder

```text
cd course-2-web-apps\block-1-web-basics-flask\lesson-1-2-first-web-page
```

---

### Step 4: Start the server

```text
python starter\app.py
```

**Expected terminal output (similar):**

```text
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

The terminal looks **busy** — that is normal. The server is waiting for visitors.

**`127.0.0.1`** means "this computer." **`5000`** is the **port** — like a door number on your machine.

---

### Step 5: Open the page in your browser

1. Open Chrome, Edge, or Firefox.
2. In the address bar, type:

```text
http://127.0.0.1:5000
```

3. Press **Enter**.

**Expected browser text:**

```text
Hello, Web World!
```

You just served a web page from Python. Level complete!

---

### Step 6: Stop the server

Click the terminal panel, press **Ctrl+C**.

You should see the server stop and get your prompt back. Always stop the server when you are done — otherwise the port stays busy.

---

### Step 7: Change the message (optional test)

1. Edit the `return` line to say something new, for example `return "Hi from my Flask app!"`
2. Save the file.
3. Run `python starter\app.py` again.
4. Refresh the browser — see your new text?

With `debug=True`, sometimes Flask auto-reloads. If you do not see changes, stop with **Ctrl+C** and start again.

---

## Quick Drills

1. Start the server — terminal shows `Running on http://127.0.0.1:5000`.
2. Browser shows your greeting at `/`.
3. **Ctrl+C** stops the server cleanly.

---

## Try it yourself

### Challenge 1 (required)

Add a second route `/hi` that returns `Hi there!` (copy the `@app.route` pattern). Visit `http://127.0.0.1:5000/hi` in the browser.

### Challenge 2 (bonus)

Change the home message to include your name with an f-string inside the function: `return f"Hello, Web World! — {your_name}"` (set `your_name = "Alex"` above the return).

---

## Debug Corner

**Problem:** Browser says "Unable to connect" or "refused to connect"

**Cause:** The Flask server is not running, or you closed the terminal.

**Fix:** Run `python starter\app.py` again. Keep that terminal open while you browse.

---

**Problem:** `Address already in use` or port 5000 busy

**Cause:** An old server is still running in another terminal.

**Fix:** Find the other terminal and press **Ctrl+C**, or close it. Then start again.

---

**Problem:** Page shows old text after editing

**Cause:** Browser cache or server did not reload.

**Fix:** Hard refresh (**Ctrl+F5**) or stop and restart the server.

---

## What's Next

→ [Lesson 1.3: Dynamic Routes](../lesson-1-3-dynamic-routes/README.md) — greet visitors by name with `/hello/YourName`.

---

*You are officially a web server operator. Next: URLs that change the message!*

[← Choose language](README.md)
