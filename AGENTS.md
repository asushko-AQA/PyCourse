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

## Repository Structure

```
PyCourse/
├── AGENTS.md                 # This file — agent briefing
├── CURRICULUM.md             # Master plan (expanded)
├── README.md                 # Human-facing project intro
├── course-1-python-basics/   # Course 1 content
├── course-2-web-apps/        # Course 2 content
├── course-3-game-dev/        # Course 3 content
├── shared/                   # Reusable assets (templates, images, CSS)
├── documents/                # Ideas, plans, issues (not student-facing)
└── .cursor/skills/           # Project skills for lesson authoring
```

### documents/ folder

Use [documents/](documents/) to collect planning notes before they become curriculum or lessons:

| Subfolder | Use for |
|-----------|---------|
| `documents/ideas/` | Raw ideas, project hooks, feedback |
| `documents/plans/` | Milestones, lesson drafts, block outlines |
| `documents/issues/` | Bugs, gaps, typos, open questions |

Copy `_template.md` from the relevant subfolder when adding a new note. Approved outcomes go into `CURRICULUM.md` or lesson READMEs — not left only in `documents/`.

### Lesson folder convention

Each lesson lives in its own directory:

```
course-1-python-basics/
  block-1-meeting-your-computer/
    lesson-1-1-installing-python/
      README.md          # Language chooser (required)
      en.md              # Lesson in English (required)
      ru.md              # Lesson in Russian (required)
      starter/           # Optional starter code
      solution/          # Optional reference solution
      exercises/         # Optional extra challenges
```

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
```

No build step. No test suite yet — validate by running lesson scripts manually.

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

**Development order (Block 2):** 2.1 → 2.2 → 2.3 → 2.4 → 2.5 → Block 3 placeholder.

Suggested milestone when starting fresh: **Lesson 1.1**.

## Key References

- [Python official tutorial](https://docs.python.org/3/tutorial/) — agent reference only, not student reading
- [Flask quickstart](https://flask.palletsprojects.com/en/latest/quickstart/)
- [Pygame docs — getting started](https://www.pygame.org/docs/tut/PygameIntro.html)
- [KidsCanCode Pygame lessons](https://kidscancode.org/lessons/) — project inspiration
