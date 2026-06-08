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

**Path A:**

```text
cd Documents\PyCourse
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

```text
cd Documents\PyCourse\my_web_madlibs
python app.py
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

## What's Next

→ [Lesson 2.4: Static Files & CSS](../lesson-2-4-static-files-css/README.md) — link a stylesheet with `url_for`.

---

*Your web story factory is open. Time to add style!*
