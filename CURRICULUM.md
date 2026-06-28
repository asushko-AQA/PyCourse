# Master Curriculum: Python for Young Creators (Age 11+)

Expanded plan based on project-based learning research, age-appropriate pacing (30–45 min sessions), and progression from CLI → Turtle bridge → Flask → Pygame.

**Program length (estimate):** ~8–10 months at 1–2 lessons/week.

---

## Design Principles

| Principle | Implementation |
|-----------|----------------|
| Visible results fast | Every lesson ends with something that runs or draws |
| Projects over theory | Concepts taught through mini-projects, not lectures |
| Debugging is a skill | Dedicated lesson; errors framed as clues |
| Gradual complexity | 15–25 lines (early) → 30–50 lines (Course 1 end) → 60–100 lines (Course 3) |
| Interests as hooks | Games, web pages, drawings, stories, calculators |

---

## Course 1: Python Basics & Command Line Magic

**Goal:** Write Python scripts, use the terminal, understand variables through functions and collections.

**Prerequisites:** None.

### Block 0: Getting Started (warm-up, no install)

A pre-syntax, no-install warm-up that builds the mental model before any tooling. Read-and-think only; pen-and-paper practice.

| Lesson | Topic | Mini-project / outcome |
|--------|-------|------------------------|
| 0.1 | What Is a Programming Language? | Understand programs as ordered, exact instructions; write a plain-English "program" |
| 0.2 | How Code Comes Alive | Mental model: code → interpreter → result; trace `print` output by hand |

### Block 1: Meeting Your Computer's Best Friend

| Lesson | Topic | Mini-project / outcome |
|--------|-------|------------------------|
| 1.1 | Installing Python & VS Code | `python --version` works; VS Code opens a `.py` file |
| 1.2 | Using the Terminal/CLI | Navigate folders with `cd`, list files with `dir`/`ls`; run `treasure.py` |
| 1.3 | Running Your First Script | Reliable create → save → `cd` → `python file.py` workflow |
| 1.4 | Reading Error Messages | Fix 3 intentional bugs; learn SyntaxError vs CLI file errors |
| 1.5 | Block 1 Capstone: Mission Control Badge | Create `my_mission/badge.py`; navigate, run, fix one bug |

### Block 2: Talking to Python (Variables & Data)

| Lesson | Topic | Mini-project / outcome |
|--------|-------|------------------------|
| 2.1 | Variables, Strings, Integers | `character_sheet.py` — store name, age, favorite game in variables |
| 2.2 | f-strings and `input()` | Interactive greeting program |
| 2.3 | Math Operators | Simple calculator in the terminal |
| 2.4 | Strings in Action | Mad-libs style word game (`.upper()`, `.lower()`, slicing basics) |
| 2.5 | Block 2 Capstone: Creator Data Pack | Create `my_data/creator_pack.py`; variables, input, f-strings, math, strings |

### Block 3: Making Choices & Repeating Actions

| Lesson | Topic | Mini-project / outcome |
|--------|-------|------------------------|
| 3.1 | Booleans and Comparisons | Predict true/false quiz in the terminal |
| 3.2 | `if`, `elif`, `else` | Choose-your-path story (2–3 branches) |
| 3.3 | `for` and `while` loops | Countdown timer; multiplication table |
| **3.4** *(new)* | **Loop Patterns** | Draw ASCII art patterns; `range()` and `break` |

### Block 4: Organizing Code

| Lesson | Topic | Mini-project / outcome |
|--------|-------|------------------------|
| 4.1 | Functions with `def` | Reusable `draw_banner()` and `ask_yes_no()` helpers |
| 4.2 | Lists | High-score list, inventory of game items |
| 4.3 | Dictionaries | Personal phonebook / character stats sheet |
| **4.4** *(new)* | **Capstone: Text Adventure** | Room-based game using functions, lists, dicts |

### Block 5 *(new)*: Creative Python with Turtle

Bridge between basics and game/web courses. Uses stdlib `turtle` — no pip install.

| Lesson | Topic | Mini-project / outcome |
|--------|-------|------------------------|
| 5.1 | Turtle Basics | Draw a square and triangle |
| 5.2 | Loops & Color | Spiral or star pattern |
| 5.3 | Functions + Turtle | Snowflake or geometric art function |

**Course 1 exit skills:** variables, I/O, conditionals, loops, functions, lists, dicts, CLI, basic debugging, Turtle graphics.

---

## Course 2: Web Applications with Python

**Goal:** Build interactive web pages locally with Flask and HTML templates.

**Prerequisites:** Course 1 (especially functions, dicts, string formatting).

### Block 0 *(new)*: Environment Setup

| Lesson | Topic | Mini-project / outcome |
|--------|-------|------------------------|
| 0.1 | Virtual Environments & pip | Create `.venv`, install Flask, understand why |
| 0.2 | How the Web Works | Browser, server, URL, request/response (concept lesson + diagram) |

### Block 1: Web Basics with Flask

| Lesson | Topic | Mini-project / outcome |
|--------|-------|------------------------|
| 1.1 | Installing Flask | `pip install flask` inside venv |
| 1.2 | First Web Page | "Hello, Web World!" at `localhost:5000` |
| 1.3 | Dynamic Routes | `/hello/YourName` personalized greeting |
| **1.4** *(new)* | **Multiple Routes** | Mini-site: Home, About, Jokes + URL calculator (`/add/<a>/<b>`) |

### Block 2: Making It Beautiful & Interactive

| Lesson | Topic | Mini-project / outcome |
|--------|-------|------------------------|
| 2.1 | HTML Templates (`render_template`) | Jinja2 base layout + child pages |
| 2.2 | HTML Forms (GET/POST) | Form that echoes user input on a results page |
| 2.3 | Mad-Libs Web App | Capstone: `my_web_madlibs/` form-driven story |
| **2.4** *(new)* | **Static Files & CSS** | Link stylesheet; simple responsive styling |
| **2.5** *(new)* | **Flash Messages & Validation** | Flash errors + POST calculator in `my_web_calc/` |

**Course 2 exit skills:** Flask routes, templates, forms, GET/POST, static files, venv, local dev server.

**Stretch goals (optional later):** sessions/cookies, SQLite with Flask-SQLAlchemy, deploy to PythonAnywhere.

---

## Course 3: Game Development with Python

**Goal:** Build a complete 2D mini-game with Pygame.

**Prerequisites:** Course 1 (loops, conditionals, functions, lists). Turtle (Block 5) recommended.

### Block 1: Getting Started with Pygame

| Lesson | Topic | Mini-project / outcome |
|--------|-------|------------------------|
| 1.1 | Install Pygame & game loop | Window opens, closes cleanly |
| 1.2 | Game Window & Colors | Fill background; change colors each frame |
| 1.3 | Shapes & Coordinates | Move a rectangle with x/y variables |
| **1.4** *(new)* | **Delta Time & Smooth Movement** | Frame-rate independent motion |

### Block 2: Player Controls & Animations

| Lesson | Topic | Mini-project / outcome |
|--------|-------|------------------------|
| 2.1 | Keyboard Events | Arrow keys move a player square |
| 2.2 | Images & Sprites | Replace square with a sprite image |
| 2.3 | Score & Text Rendering | Score counter with `font.render()` |
| **2.4** *(new)* | **Game States** | Start screen → playing → game over |

### Block 3: Physics & Collisions (Final Project)

| Lesson | Topic | Mini-project / outcome |
|--------|-------|------------------------|
| 3.1 | Collision Detection | `rect.colliderect()` — collect a coin |
| 3.2 | **Catch the Falling Stars** | Full capstone: spawn, fall, catch, score, restart |
| **3.3** *(new)* | **Polish** | Sound effects, high score, difficulty ramp |

**Course 3 exit skills:** game loop, events, sprites, collision, game states, scoring.

**Alternative entry path:** Pygame Zero (`pgzero`) for simpler first game — document in `shared/notes/pygame-zero-alternative.md` if needed.

---

## Cross-Course Project Progression

```
CLI hello.py → interactive terminal apps → Turtle art → Flask web page → Pygame mini-game
```

| Stage | Example project | Lines of code (typical) |
|-------|-----------------|-------------------------|
| Week 1–4 | Greeting, calculator, story | 15–30 |
| Week 5–8 | Text adventure, Turtle snowflake | 30–50 |
| Week 9–12 | Flask mad-libs site | 40–80 |
| Week 13–16 | Catch the Falling Stars | 80–150 |

---

## Lesson README Template (every lesson)

Each lesson folder uses a **bilingual chooser** plus split language files:

| File | Purpose |
|------|---------|
| `README.md` | Language chooser — What you'll build/learn, Before you start, Quick drills |
| `en.md` / `ru.md` | Full lesson (Title, Explanation, Code Example, Code Execution, Quick drills, Practice, Debug corner, What's next) |
| `starter/` / `solution/` | Runnable Python (same filenames) |
| `exercises/` | Optional EN + RU micro-challenges |

Link **What's next** to the following lesson's `README.md`, not directly to `en.md`.

---

## External Resources (inspiration, not copy)

| Resource | Use for |
|----------|---------|
| [KidsCanCode Pygame](https://kidscancode.org/lessons/) | Game lesson structure |
| [LaunchCode Flask intro](https://education.launchcode.org/lchs/chapters/flask-intro/) | Form/template patterns |
| [Python Turtle (CAS)](https://www.computingatschool.org.uk/resources/2024/november/turtle-python-snow-flakes/) | Turtle Block 5 |
| *Python for Kids* (Briggs) | Chapter pacing reference |
| [Real Python — Flask tutorial](https://realpython.com/tutorials/flask/) | Instructor reference |

---

## Future Courses (backlog)

- **Course 4:** Data & APIs — CSV files, JSON, simple public API consumption
- **Course 5:** Creative AI — rule-based chatbot, then optional LLM API (parental gate)
- **Course 6:** Hardware — Micro:bit or Raspberry Pi GPIO intro
