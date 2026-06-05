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
└── .cursor/skills/           # Project skills for lesson authoring
```

### Lesson folder convention

Each lesson lives in its own directory:

```
course-1-python-basics/
  block-1-meeting-your-computer/
    lesson-1-1-installing-python/
      README.md          # Student-facing lesson (required)
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
| `review-lesson` | Checking a lesson for completeness and age fit |

Skills live in `.cursor/skills/<name>/SKILL.md`.

## Development Order

Build **Course 1** completely before Course 2. Course 2 requires functions, lists, and dicts. Course 3 requires loops, conditionals, and functions.

Suggested first milestone: **Course 1, Block 1, Lesson 1.1** (Installing Python & VS Code).

## Key References

- [Python official tutorial](https://docs.python.org/3/tutorial/) — agent reference only, not student reading
- [Flask quickstart](https://flask.palletsprojects.com/en/latest/quickstart/)
- [Pygame docs — getting started](https://www.pygame.org/docs/tut/PygameIntro.html)
- [KidsCanCode Pygame lessons](https://kidscancode.org/lessons/) — project inspiration
