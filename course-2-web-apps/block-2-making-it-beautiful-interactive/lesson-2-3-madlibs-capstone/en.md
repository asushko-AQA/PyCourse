# Lesson 2.3: Mad-Libs Capstone

> **Course:** Web Applications with Python · **Block:** Making It Beautiful & Interactive · **~35–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 11 — Web Story Factory**

---

## Explanation

Your first **web capstone**! Combine templates and POST forms into a Mad-Libs app — like Course 1 `madlibs.py`, but in the browser.

Create **`my_web_madlibs/`** at your **project root** — the folder you open in VS Code, next to `.venv` (and next to `course-2-web-apps/` in Path A).

**Path A:** Open `PyCourse` in VS Code and open the terminal — it already starts in `PyCourse`. Copy the lesson [starter/](starter/) into a new folder called `my_web_madlibs`:

```text
Copy-Item -Recurse course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-3-madlibs-capstone\starter my_web_madlibs
```

**Command Prompt (cmd):** `xcopy /E /I course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-3-madlibs-capstone\starter my_web_madlibs`  
**macOS/Linux:** `cp -r course-2-web-apps/block-2-making-it-beautiful-interactive/lesson-2-3-madlibs-capstone/starter my_web_madlibs`

Prefer the mouse? In the VS Code Explorer, right-click the lesson's `starter` folder → **Copy**, right-click an empty spot under `PyCourse` → **Paste**, then rename the copy to `my_web_madlibs`.

Check: you now have `my_web_madlibs/app.py` and `my_web_madlibs/templates/madlibs.html`.

**Path B:** Inside your workshop folder (next to `.venv`), create `my_web_madlibs/` and put this lesson's `starter/app.py` and `starter/templates/` in it — same idea as `my_adventure/`. See [STUDENT-MAP](../STUDENT-MAP.md).

---

### Step 1: One page, one form

`madlibs.html` has the form and shows the story below when `story` is not empty:

```html
<form method="post">
    <input type="text" name="noun" placeholder="robot">
    <!-- verb, adjective, place -->
    <button type="submit">Create Story</button>
</form>

{% if story %}
<h2>Your Story</h2>
<p>{{ story }}</p>
{% endif %}
```

---

### Step 2: Build the story on POST

```python
@app.route("/", methods=["GET", "POST"])
def madlibs():
    story = ""
    if request.method == "POST":
        noun = request.form.get("noun", "").strip()
        verb = request.form.get("verb", "").strip()
        adjective = request.form.get("adjective", "").strip()
        place = request.form.get("place", "").strip()
        story = (
            f"One sunny day, a {adjective} {noun} decided to {verb} "
            f"all the way to {place}. The crowd cheered. The end!"
        )
    return render_template("madlibs.html", story=story)
```

**TODO in starter:** Read four fields and build the f-string story.

---

### Step 3: Run from my_web_madlibs

**1. Activate your venv.** The VS Code terminal starts in your project root (where `.venv` lives). Activate:

```text
.venv\Scripts\Activate.ps1
```

**Command Prompt (cmd):** `.venv\Scripts\activate.bat` · **macOS/Linux:** `source .venv/bin/activate`

You should see `(.venv)` at the start of the terminal line.

**2. Go into your capstone folder and run** (same commands on Windows, macOS/Linux, and in Path B):

```text
cd my_web_madlibs
python app.py
```

Open `http://127.0.0.1:5000/`.

**Sample words:** robot, dance, sparkly, moon base

---

### Step 4: Make it yours

Change the story template or add a fifth word field. Keep: form → POST → show story on same page.

---

## Code Example

**File: [solution/app.py](solution/app.py)**

```python
@app.route("/", methods=["GET", "POST"])
def madlibs():
    story = ""
    if request.method == "POST":
        noun = request.form.get("noun", "something").strip() or "something"
        verb = request.form.get("verb", "move").strip() or "move"
        adjective = request.form.get("adjective", "silly").strip() or "silly"
        place = request.form.get("place", "somewhere").strip() or "somewhere"
        story = (
            f"One sunny day, a {adjective} {noun} decided to {verb} "
            f"all the way to {place}. The crowd cheered. The end!"
        )
    return render_template("madlibs.html", story=story)
```

Full imports and `app = Flask(__name__)` are at the top of [solution/app.py](solution/app.py). The form lives in [solution/templates/madlibs.html](solution/templates/madlibs.html).

---

## Code Execution

With `(.venv)` active, from your project root:

```text
cd my_web_madlibs
python app.py
```

**Expected output (terminal):**

```text
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

1. Open `http://127.0.0.1:5000/`
2. Type **Adjective** `sparkly`, **Noun** `robot`, **Verb** `dance`, **Place** `moon base` and click **Create Story**

**Expected output (browser, under the form):**

```text
Your Story
One sunny day, a sparkly robot decided to dance all the way to moon base. The crowd cheered. The end!
```

**Expected result:** Your custom Mad-Libs paragraph appears under **Your Story**. Stop the server with **Ctrl+C** when you are done.

---

## Quick Drills

1. **Field map** — match each `name="..."` to its `request.form.get(...)`.
2. **Empty noun** — submit with one blank field. What prints?
3. **New sentence** — rewrite the story with a school or sports theme.

---

## Practice Task

**Quest name:** Your Web Mad-Libs

1. Copy [starter/](starter/) to **`my_web_madlibs/`** at project root.
2. Complete all TODO lines in `app.py` and `madlibs.html`.
3. Write your own two-sentence story template.
4. Play-test with three different word sets.

**Reference solution:** [solution/](solution/)

---

## Debug Corner

**Problem:** Form submits but story area stays empty

**Cause:** The `story` variable was never set inside the `if request.method == "POST":` block.

**Fix:** Build `story = f"..."` before `return render_template("madlibs.html", story=story)`.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. Where should you copy the starter for your capstone project?
   - **a)** `my_web_madlibs/` at the project root
   - **b)** Inside `.venv/Scripts/`
   - **c)** Only in the browser bookmarks bar
   - **d)** Into `course-1-python-basics/`

2. The Mad-Libs form uses `method="post"`. Where do the words go when you submit?
   - **a)** Directly into `pip list`
   - **b)** In the request body — read with `request.form.get(...)`
   - **c)** In the URL as `?noun=robot` only
   - **d)** Into `static/style.css`

3. When should you build the `story` variable?
   - **a)** Only in the browser console
   - **b)** After `deactivate`
   - **c)** Inside the `if request.method == "POST":` block after reading the fields
   - **d)** Before creating `app = Flask(__name__)`

4. What does `{% if story %}` in the template do?
   - **a)** Delete the form after one use
   - **b)** Install Jinja2 with pip
   - **c)** Change GET to POST automatically
   - **d)** Show the story section only when `story` is not empty

5. Each `<input name="noun">` must match what in `app.py`?
   - **a)** The same name in `request.form.get("noun")`
   - **b)** The Flask port number
   - **c)** The `secret_key` string
   - **d)** The `@app.route` decorator name only

---

<details><summary>Click to reveal answers</summary>

1. **a)** Capstone folders live at project root, like other `my_*` projects.
2. **b)** POST sends field data in the body, not the URL.
3. **c)** Build the story only after you have the submitted words.
4. **d)** The template shows the result block when `story` has text.
5. **a)** HTML `name` must match the key in `request.form.get(...)`.

</details>

---

## What's Next

→ [Lesson 2.4: Static Files & CSS](../lesson-2-4-static-files-css/README.md) — link a stylesheet with `url_for`.

---

*Your web story factory is open. Time to add style!*
