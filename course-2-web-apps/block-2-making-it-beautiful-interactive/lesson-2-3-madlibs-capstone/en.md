# Lesson 2.3: Mad-Libs Capstone

> **Course:** Web Applications with Python · **Block:** Making It Beautiful & Interactive · **~35–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 11 — Web Story Factory**

---

## Explanation

Your first **web capstone**! Combine templates and POST forms into a Mad-Libs app — like Course 1 `madlibs.py`, but in the browser.

Create **`my_web_madlibs/`** at your **project root** (next to `course-2-web-apps/`).

**Path A:** the VS Code terminal is already in `PyCourse`. If `(.venv)` is not showing, activate the toolbox from Lesson 0.1 first (it lives in this folder):

**Windows:** `.venv\Scripts\Activate.ps1`  
**macOS:** `source .venv/bin/activate`

Then create the capstone folder (no `cd Documents\PyCourse` — you are already there):

```text
mkdir my_web_madlibs
```

Copy [starter/](starter/) into `my_web_madlibs/` (`app.py` + `templates/`).

**Path B:** Create `my_web_madlibs` on Desktop — same idea as `my_adventure/`. See [STUDENT-MAP](../STUDENT-MAP.md).

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

With `(.venv)` still active (activate at the `PyCourse` root first if the prompt does not show it):

**Windows:**

```text
cd my_web_madlibs
python app.py
```

**macOS:**

```text
cd my_web_madlibs
python3 app.py
```

Or test the lesson starter first:

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-3-madlibs-capstone
python starter\app.py
```

**Mac/Linux:** `python starter/app.py`

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

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-3-madlibs-capstone
python starter\app.py
```

**Mac/Linux:** `python starter/app.py`

1. Open `http://127.0.0.1:5000/`
2. Fill in sample words (robot, dance, sparkly, moon base) and click **Create Story**

**Expected result:** Your custom Mad-Libs paragraph appears under **Your Story**.

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
   - **a)** Only in the browser bookmarks bar
   - **b)** Inside `.venv/Scripts/`
   - **c)** `my_web_madlibs/` at the project root
   - **d)** Into `course-1-python-basics/`

2. The Mad-Libs form uses `method="post"`. Where do the words go when you submit?
   - **a)** Directly into `pip list`
   - **b)** In the URL as `?noun=robot` only
   - **c)** Into `static/style.css`
   - **d)** In the request body — read with `request.form.get(...)`

3. When should you build the `story` variable?
   - **a)** Inside the `if request.method == "POST":` block after reading the fields
   - **b)** Before creating `app = Flask(__name__)`
   - **c)** Only in the browser console
   - **d)** After `deactivate`

4. What does `{% if story %}` in the template do?
   - **a)** Delete the form after one use
   - **b)** Show the story section only when `story` is not empty
   - **c)** Install Jinja2 with pip
   - **d)** Change GET to POST automatically

5. Each `<input name="noun">` must match what in `app.py`?
   - **a)** The `secret_key` string
   - **b)** The Flask port number
   - **c)** The same name in `request.form.get("noun")`
   - **d)** The `@app.route` decorator name only

---

<details><summary>Click to reveal answers</summary>

1. **c)** Capstone folders live at project root, like other `my_*` projects.
2. **d)** POST sends field data in the body, not the URL.
3. **a)** Build the story only after you have the submitted words.
4. **b)** The template shows the result block when `story` has text.
5. **c)** HTML `name` must match the key in `request.form.get(...)`.

</details>

---

## What's Next

→ [Lesson 2.4: Static Files & CSS](../lesson-2-4-static-files-css/README.md) — link a stylesheet with `url_for`.

---

*Your web story factory is open. Time to add style!*
