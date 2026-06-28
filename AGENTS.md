# PyCourse — Agent Instructions

Python course for young creators (age 11+). Three courses: **Python Basics**, **Web Apps (Flask)**, **Game Dev (Pygame)**.

## Project Overview

| Item | Value |
|------|-------|
| Audience | Ages 11+, no prior coding required |
| Python | 3.12+ (stdlib + pip packages only where noted) |
| Editor | VS Code with Python extension |
| OS | Windows-first instructions; note macOS/Linux equivalents |
| Pedagogy | Project-based, short lessons (~30 min), visible results every lesson |

Full expanded curriculum: [CURRICULUM.md](CURRICULUM.md)

## Platform Architecture

PyCourse is evolving from a markdown-only course repo into a gamified, multi-channel
learning platform (web app + Telegram bot, shared FastAPI backend, SQLite, stars/streaks,
external homework execution). The **canonical architecture source of truth** is
[documents/plans/platform-architecture.md](documents/plans/platform-architecture.md).

Binding decisions (do not re-litigate in individual plans):

1. **Stack** — FastAPI backend (`backend/`, shared core) + Next.js frontend (`frontend/`);
   web app and Telegram bot (`bot/`) both consume the backend over HTTP; the bot is a
   separate process.
2. **Lesson storage** — markdown in git is canonical; SQLite stores only metadata + user
   data (a sync job indexes markdown → DB).
3. **Gamification** — stars + streaks are primary; legacy XP/levels is retired.
4. **Homework checking** — student `.py` runs on an external executor (Piston/Judge0),
   never inside the backend process.

The atomic build plans (00–17) live in `tmp/`; completed plans move to `tmp/completed/`.

## Repository Structure

Three-level hierarchy for all course content: **course → block → lesson**. Planning and tooling sit beside the courses at the repo root.

```
PyCourse/                          # Open this folder in VS Code
├── AGENTS.md                      # Agent briefing (this file)
├── CURRICULUM.md                  # Master curriculum — scope, order, outcomes
├── README.md                      # Human-facing project intro
├── .gitignore                     # Ignores .venv, __pycache__, .env, etc.
│
├── course-1-python-basics/        # Course 1 — Block 0 warm-up + 5 blocks, 23 lessons (complete)
├── course-2-web-apps/             # Course 2 — 3 blocks, 11 lessons (complete)
├── course-3-game-dev/             # Course 3 — placeholder README only (planned)
│
├── shared/                        # Cross-course assets (templates, images, CSS) — sparse
├── documents/                     # Planning notes — NOT student-facing
├── tools/                         # Maintainer scripts (e.g. quiz bulk-apply)
└── .cursor/skills/                # Agent skills for authoring and QA
```

Student capstone projects are **not** in the repo — learners create them at **project root** next to the course folders (see [Student project folders](#student-project-folders-at-project-root)).

### Course folders (`course-N-{slug}/`)

Each course is a self-contained tree with a course index and bilingual student maps.

| File | Purpose |
|------|---------|
| `README.md` | Course overview, block table, prerequisites, exit skills |
| `STUDENT-MAP.md` / `STUDENT-MAP.ru.md` | Whole-course folder map for students and teachers |

| Course | Folder | Blocks | Status |
|--------|--------|--------|--------|
| Python Basics | `course-1-python-basics/` | 5 (blocks 1–5) | Content complete |
| Web Apps (Flask) | `course-2-web-apps/` | 3 (blocks 0–2) | Content complete |
| Game Dev (Pygame) | `course-3-game-dev/` | — | Planned |

### Block folders (`block-{B}-{slug}/`)

Blocks group lessons by theme. Each block has an index and optional per-block student maps.

| File | Purpose |
|------|---------|
| `README.md` | Block overview, lesson list, prerequisites, capstone notes |
| `STUDENT-MAP.md` / `STUDENT-MAP.ru.md` | Block-level paths, scripts, and `cd` hints (optional but common) |

**Slug rules:** lowercase, hyphenated, descriptive — e.g. `block-2-talking-to-python`, `block-0-environment-setup`.

### Lesson folders (`lesson-{B}-{L}-{slug}/`)

One folder per lesson. Slug has no lesson number in the name (numbers live in the folder prefix).

| Path | Required? | Purpose |
|------|-----------|---------|
| `README.md` | Yes | Language chooser — links to `en.md` and `ru.md` |
| `en.md` | Yes | Full lesson in English |
| `ru.md` | Yes | Full lesson in Russian (same section order as `en.md`) |
| `starter/` | Usually | Runnable skeleton with `# TODO`; must not contain full solutions |
| `solution/` | Usually | Reference code matching starter filenames |
| `exercises/` | Optional | Extra challenges — `.md` prompts and/or `.py` drill scripts |

**Lesson `en.md` / `ru.md` section order** — the canonical format is **lesson schema v2**;
the full contract (sections, metadata comment, quiz hash, parity rules) lives in
[documents/plans/lesson-schema-v2.md](documents/plans/lesson-schema-v2.md). Use matching
localized headings in `ru.md`.

1. Title and intro (optional `<!-- meta ... -->` comment for `homework`/`checker`/`minutes`)
2. `## Title` (bold level name)
3. `## Explanation` + numbered `### Step N` tutorial steps
4. `## Code Example` — full runnable snippet + file ref **(required in v2)**
5. `## Code Execution` — exact run command + **Expected output** **(required in v2)**
6. Quick Drills / Быстрые упражнения
7. **Practice Task** / Задание для практики (canonical heading; legacy `Try it yourself` is normalized)
8. Debug Corner / Уголок отладки
9. **Quick Check** / **Проверь себя** — 3–5 multiple-choice questions, collapsible answers
10. What's Next / Что дальше (legacy **Дальше** normalized) — link to **next lesson's `README.md`**

Link "What's next" to the **README** chooser, not directly to `en.md` or `ru.md`. New
lessons must use the canonical headings; the parser only normalizes legacy variants for
already-published lessons (migration tracked in
[documents/issues/lesson-schema-v2-gap-list.md](documents/issues/lesson-schema-v2-gap-list.md)).

### Flask lesson layout (Course 2)

Beyond `starter/` and `solution/`, web lessons often include:

```
lesson-2-1-html-templates/
  starter/
    app.py
    templates/           # Jinja2 HTML — base.html, child pages
  solution/
    app.py
    templates/
lesson-2-4-static-files-css/
  starter/
    app.py
    templates/
    static/
      style.css          # CSS linked via url_for('static', ...)
```

Run from the folder containing `app.py` (usually `starter/` or the student's copied project). Course 2 assumes an activated `.venv` with Flask installed.

### Student project folders (at project root)

Capstones and finale apps live **beside** `course-1-python-basics/`, not inside lesson folders.

| Folder | Course | Created in | Main script |
|--------|--------|------------|-------------|
| `my_mission/` | 1 | Block 1 capstone (1.5) | `badge.py` |
| `my_data/` | 1 | Block 2 capstone (2.5) | `creator_pack.py` |
| `my_quest/` | 1 | Block 3 capstone (3.4) | `gate_quest.py` |
| `my_adventure/` | 1 | Block 4 capstone (4.4) | `game.py` |
| `my_gallery/` | 1 | Block 5 capstone (5.3) | `gallery.py` |
| `my_web_madlibs/` | 2 | Block 2 capstone (2.3) | Flask Mad-Libs app |
| `my_web_calc/` | 2 | Block 2 finale (2.5) | Flask calculator with validation |

### `documents/` — planning (not student-facing)

Use [documents/](documents/) to collect notes before they become curriculum or lessons. See [documents/README.md](documents/README.md).

| Subfolder | Use for |
|-----------|---------|
| `documents/ideas/` | Raw ideas, verification improvements, feedback |
| `documents/plans/` | Milestones, lesson drafts, block outlines |
| `documents/issues/` | Bugs, gaps, typos, open questions |

Copy `_template.md` from the relevant subfolder when adding a note. After **verify-lesson-in-block**, file suggestions to `ideas/` and gaps to `issues/`. Approved outcomes go into `CURRICULUM.md` or lesson READMEs — not left only in `documents/`.

### `tools/` — maintainer utilities

| Path | Purpose |
|------|---------|
| `tools/quizzes/*.json` | Quick Check quiz text keyed by lesson folder slug |
| `tools/apply_lesson_quizzes.py` | Inserts quiz sections into `en.md` / `ru.md` (skips lessons that already have them) |

### `.cursor/skills/` — agent authoring

| Skill | File | Use when |
|-------|------|----------|
| `youth-python-pedagogy` | `SKILL.md` | Tone, pacing, age-appropriate examples |
| `write-lesson` | `SKILL.md` | New lesson directory and README template |
| `verify-lesson-in-block` | `SKILL.md` + `block-checklist.md` | After every lesson create/update |
| `review-lesson` | `SKILL.md` | Manual QA checklist |

### `shared/`

Reserved for cross-course reusable assets (shared HTML snippets, images, CSS). Prefer lesson-local `starter/` / `static/` unless an asset is used in multiple courses.

### Do not commit

Per `.gitignore` and git workflow: `.venv/`, `venv/`, `__pycache__/`, `*.pyc`, student `.env` files, and local IDE noise. Student capstone folders (`my_mission/`, `my_data/`, etc.) are created on the learner's machine — they are not part of the repo template.

## Commands

```bash
# Verify Python
python --version

# Run a lesson script (from lesson directory)
python starter/hello.py

# Course 2 — Flask (from project folder, after venv + pip install flask)
python app.py

# Course 3 — Pygame (after pip install pygame)
python starter/game.py

# Backend lesson metadata sync (from backend/)
python -m app.sync.index_lessons
python -m app.sync.index_lessons --check
```

No build step for lesson scripts. For the web frontend, run end-to-end regression tests:

```bash
pip install -r tools/mcp/tests/requirements.txt
playwright install chromium
pytest tools/mcp/tests/
```

## When Building Lessons

1. Read [CURRICULUM.md](CURRICULUM.md) for scope and prerequisites.
2. Apply skill **youth-python-pedagogy** for tone, pacing, and age-appropriate examples.
3. Apply skill **write-lesson** for file structure and README template.
4. One concept per lesson; end with a runnable mini-result.
5. Keep programs **15–50 lines** (Course 1), **30–80 lines** (Courses 2–3).
6. After every new or substantially updated lesson, apply **verify-lesson-in-block**: delegate to a readonly subagent, then file improvements in [documents/ideas/](documents/ideas/) and gaps in [documents/issues/](documents/issues/).

## Content Rules

### Voice & tone

- Friendly mentor, not textbook. Use "you" and active voice.
- Analogies: variables = labeled boxes, functions = reusable recipes, loops = repeat button.
- Celebrate errors as detective work — never shame mistakes.
- Avoid jargon without a plain-English definition first.

### Code style (student examples)

```python
# ✅ Good — clear names, small functions, one idea per block
def greet(name: str) -> None:
    print(f"Hello, {name}!")

# ❌ Avoid — clever one-liners, magic numbers without context
```

- Use `snake_case` for variables and functions.
- Prefer f-strings over `%` or `.format()`.
- Add brief comments only where logic is non-obvious.
- No type hints in Course 1; optional in Course 2+.

### Platform notes

- Windows: `dir`, `cd`, `python`, backslashes in paths explained but prefer forward slashes in code.
- Include VS Code steps: open folder, integrated terminal, Run button.
- When installing packages, always use a virtual environment from Course 2 onward.

## Course Boundaries

| Do | Don't |
|----|-------|
| Stdlib + Flask + Pygame only | Django, FastAPI, numpy, pandas |
| Simple HTML/CSS in templates | JavaScript frameworks, databases (Course 2) |
| Local `python app.py` / `flask run` | Cloud deploy, Docker, Heroku (future stretch goal) |
| Mini-games and calculators | Network multiplayer, file I/O of untrusted paths |

## Git Workflow

- Branch per lesson or block: `course-1/lesson-1-1-installing-python`
- Commit message style: `course-1: add lesson 1.1 installing Python and VS Code`
- Do not commit `.venv/`, `__pycache__/`, or student `.env` files.
- **Custom command:** send **`--ok`** in chat when you want the agent to commit current work (see `.cursor/rules/commit-on-ok.mdc`).

## Skills (project-local)

| Skill | Use when |
|-------|----------|
| `youth-python-pedagogy` | Writing or reviewing any student-facing content |
| `write-lesson` | Creating a new lesson directory and README |
| `verify-lesson-in-block` | **After every lesson create/update** — subagent verification + file to `documents/` |
| `review-lesson` | Lesson QA checklist (used by verification subagent; manual review) |

Skills live in `.cursor/skills/<name>/SKILL.md`.

### Lesson create → verify workflow

```
write-lesson  →  verify-lesson-in-block (Task subagent, readonly)
                      ↓
              documents/ideas/   (suggestions, improvements)
              documents/issues/  (gaps, critical findings)
```

Fix critical gaps in the lesson when practical, then re-run verification.

## Development Order

Build **Course 1** block by block. Course 2 requires Block 1 complete (especially functions, lists, dicts from later blocks). Course 3 requires loops, conditionals, and functions.

**Course 1, Block 0** (two warm-up lessons — pre-install, concept-only):

| Lesson | Topic |
|--------|-------|
| 0.1 | What Is a Programming Language? (programs as ordered instructions) |
| 0.2 | How Code Comes Alive (code → interpreter → result) |

Block index: [block-0-getting-started/README.md](course-1-python-basics/block-0-getting-started/README.md)

**Course 1, Block 1** (five lessons + capstone):

| Lesson | Topic |
|--------|-------|
| 1.1 | Installing Python & VS Code |
| 1.2 | Terminal / CLI + `treasure.py` |
| 1.3 | Launch workflow + `starter/launch.py` |
| 1.4 | Error messages (SyntaxError + CLI) |
| 1.5 | **Capstone:** `my_mission/badge.py` |

Block index: [block-1-meeting-your-computer/README.md](course-1-python-basics/block-1-meeting-your-computer/README.md)  
Student folder map: [STUDENT-MAP.md](course-1-python-basics/block-1-meeting-your-computer/STUDENT-MAP.md)

**Course 1, Block 2** (five lessons + capstone):

| Lesson | Topic |
|--------|-------|
| 2.1 | Variables, strings, integers — `character_sheet.py` |
| 2.2 | f-strings and `input()` — `greeting.py` |
| 2.3 | Math operators + `int()` — `calculator.py` |
| 2.4 | String methods — `madlibs.py` |
| 2.5 | **Capstone:** `my_data/creator_pack.py` |

Block index: [block-2-talking-to-python/README.md](course-1-python-basics/block-2-talking-to-python/README.md)  
Student folder map: [STUDENT-MAP.md](course-1-python-basics/block-2-talking-to-python/STUDENT-MAP.md)

**Development order (Block 2):** 2.1 → 2.2 → 2.3 → 2.4 → 2.5 → Block 3.

**Course 1, Block 3** (four lessons — no capstone folder):

| Lesson | Topic |
|--------|-------|
| 3.1 | Booleans and comparisons — `true_false_quiz.py` |
| 3.2 | `if`, `elif`, `else` — `choose_path.py` |
| 3.3 | `for` and `while` loops — `countdown.py`, `times_table.py` |
| 3.4 | Loop patterns — `ascii_pattern.py` |
| 3.4 capstone | **`my_quest/gate_quest.py`** — guess game (Lesson 3.4) |

Block index: [block-3-making-choices/README.md](course-1-python-basics/block-3-making-choices/README.md)  
Student folder map: [STUDENT-MAP.md](course-1-python-basics/block-3-making-choices/STUDENT-MAP.md)

**Course 1, Block 4** (four lessons + capstone):

| Lesson | Topic |
|--------|-------|
| 4.1 | Functions — `helpers.py` |
| 4.2 | Lists — `inventory.py` |
| 4.3 | Dictionaries — `character_stats.py` |
| 4.4 | **Capstone:** `my_adventure/game.py` |

Block index: [block-4-organizing-code/README.md](course-1-python-basics/block-4-organizing-code/README.md)  
Student folder map: [STUDENT-MAP.md](course-1-python-basics/block-4-organizing-code/STUDENT-MAP.md)

**Course 1, Block 5** (three lessons — Turtle bridge):

| Lesson | Topic |
|--------|-------|
| 5.1 | Turtle basics — `shapes.py` |
| 5.2 | Loops and color — `star.py` |
| 5.3 | Functions + Turtle — `snowflake.py` |
| 5.3 capstone | **`my_gallery/gallery.py`** — star + snowflake show |

Block index: [block-5-creative-turtle/README.md](course-1-python-basics/block-5-creative-turtle/README.md)  
Student folder map: [STUDENT-MAP.md](course-1-python-basics/block-5-creative-turtle/STUDENT-MAP.md)

**Development order (Course 1):** Block 0 (warm-up) → 1 → 2 → 3 → 4 → 5 → [Course 2](../course-2-web-apps/README.md).

**Course 2, Block 0** (two lessons — environment):

| Lesson | Topic |
|--------|-------|
| 0.1 | Virtual environments & pip |
| 0.2 | How the web works |

Block index: [block-0-environment-setup/README.md](course-2-web-apps/block-0-environment-setup/README.md)

**Course 2, Block 1** (four lessons — Flask routes):

| Lesson | Topic |
|--------|-------|
| 1.1 | Installing Flask (venv verify) |
| 1.2 | First web page |
| 1.3 | Dynamic routes |
| 1.4 | Multiple routes + URL calculator |

Block index: [block-1-web-basics-flask/README.md](course-2-web-apps/block-1-web-basics-flask/README.md)

**Course 2, Block 2** (five lessons — templates, forms, capstones):

| Lesson | Topic |
|--------|-------|
| 2.1 | HTML templates |
| 2.2 | HTML forms (GET/POST) |
| 2.3 | **Capstone:** `my_web_madlibs/` |
| 2.4 | Static files & CSS |
| 2.5 | Flash & validation + `my_web_calc/` |

Block index: [block-2-making-it-beautiful-interactive/README.md](course-2-web-apps/block-2-making-it-beautiful-interactive/README.md)

**Development order (Course 2):** Block 0 → 1 → 2 → [Course 3](../course-3-game-dev/README.md).

Suggested milestone when starting fresh: **Lesson 0.1** (Course 1 warm-up) or **Lesson 0.1** (Course 2).

## Key References

- [Python official tutorial](https://docs.python.org/3/tutorial/) — agent reference only, not student reading
- [Flask quickstart](https://flask.palletsprojects.com/en/latest/quickstart/)
- [Pygame docs — getting started](https://www.pygame.org/docs/tut/PygameIntro.html)
- [KidsCanCode Pygame lessons](https://kidscancode.org/lessons/) — project inspiration
