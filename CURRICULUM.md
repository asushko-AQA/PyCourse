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

### Block 4 *(optional bonus ★)*: Star Projects

After Block 3. Not required for graduation. Each ★ arcade-style game uses 2–3 lessons; numbering **4.1–4.3** (Sky Hopper), **4.4–4.6** (Prism Dash), **4.7–4.9** (Shard Stack), **4.10–4.12** (Glyph Grove).

| Lesson | Topic | Mini-project / outcome |
|--------|-------|------------------------|
| **4.1** | Gravity & flap | **Sky Hopper** — procedural bird, `vel_y`, SPACE flap |
| **4.2** | Scrolling gateways | Pipe pairs, `colliderect`, score per gateway |
| **4.3** | Sky Hopper complete | Title / play / game over, session high score, speed ramp |
| **4.4** | Auto-scroll runner | **Prism Dash** — `world_x` scroll, cube fixed at `PLAYER_X` |
| **4.5** | Jump, gravity & spin | Grounded jump, snap landing, `transform.rotate` cube |
| **4.6** | Prism Dash complete | Level string obstacles, progress %, attempts, best %, speed ramp |
| **4.7** | Grid & cells | **Shard Stack** — 2D `grid`, draw well, piece offsets |
| **4.8** | Falling shards | `can_move`, `lock_piece`, timer drop, arrow controls |
| **4.9** | Shard Stack complete | Rotate, clear lines, score/level, next preview, high score |
| **4.10** | Tile grid & glyphs | **Glyph Grove** — tile dicts, layered layout, procedural font symbols |
| **4.11** | Mouse & free tiles | `MOUSEBUTTONDOWN`, `collidepoint`, free-tile rule, pair removal |
| **4.12** | Glyph Grove complete | Hint, shuffle, timer/moves, win/stuck, session best time |

### Block 5 *(optional bonus ★ II)*: Star Projects II

After Block 4 ★. Ten more arcade ideas on the roadmap; lessons ship one ★ game per PR.

| Lesson | Topic | Mini-project / outcome |
|--------|-------|------------------------|
| **5.1** | Grid & segments | **Glow Worm** — `(col, row)` list, direction tuple, timed steps |
| **5.2** | Food & growth | Random food, grow tail, wall/self crash |
| **5.3** | Glow Worm complete | Title / play / game over, score, speed ramp, session best |
| **5.4** | Ball & walls | **Bounce Forge** — velocity vector, wall bounce, forge spark art |
| **5.5** | Paddle & lives | Anvil paddle, angle from `hit_frac`, lives counter |
| **5.6** | Bricks & score | `Rect` brick list, collision side, remove brick, score |
| **5.7** | Bounce Forge complete | Levels, speed-up, win/lose, session best, optional 2-player Pong |
| **5.8** | Patrol ship & blasters | **Orbit Guard** — bottom ship, bolt list, cooldown, cleanup |
| **5.9** | Invader formation | Grid march sideways, step down at margins |
| **5.10** | Shields, lives & score | Bullet ↔ invader, enemy fire, destructible shields |
| **5.11** | Orbit Guard complete | Waves, speed-up, UFO bonus, states, session best |
| **5.12** | Crystal grid & clicks | **Mine Whisper** — 2D cell dicts, draw board, mouse → `(col, row)` |
| **5.13** | Mines & neighbor counts | Random mines after first safe click, `neighbors`, reveal numbers |
| **5.14** | Flood reveal & flags | Recursive/ stack flood-fill for zeros, right-click flags |
| **5.15** | Mine Whisper complete | Difficulty presets, mine counter, timer, win/lose, session best time |
| **5.16** | Rune lattice & spawn | **Merge Magic** — 4×4 int grid, `RUNE_COLORS`, spawn 2/4 in empty cell |
| **5.17** | Slide & merge | `merge_row` compress/merge; four directions; spawn on change only |
| **5.18** | Merge Magic complete | Score, win 2048 + continue, game over, undo, session best |
| **5.19** | Symbol deck & grid | **Twin Cards** — pairs list, `random.shuffle`, draw backs vs shapes |
| **5.20** | Flip & match | Mouse picks, `idle/first/waiting`, `wait_timer`, matched stay open |
| **5.21** | Twin Cards complete | Moves + timer, 3 grid sizes, win stars, restart, session best moves |
| **5.22** | Grid & hot-seat turns | **Tic-Tac-Bot** — 9-cell list, draw X/O shapes, mouse place, two-player |
| **5.23** | Win lines & scoreboard | `WIN_LINES`, highlight winner, draws, score table, round restart |
| **5.24** | Tic-Tac-Bot complete | Easy/Medium/Hard bot, move delay, who starts, session W/L/D, minimax Hard |
| **5.25** | Player & jump | **Leap Lands** — `Rect` player, arrows + `dt`, gravity, grounded jump |
| **5.26** | Text map & tiles | `#`/`=` solids, `S` spawn, build rects, axis-separated collision |
| **5.27** | Coins, spikes & lives | `C` coins, `^` hazards, lives, respawn, HUD |
| **5.28** | Patrollers & camera | `E` patrol enemies, stomp, horizontal `camera_x` scroll |
| **5.29** | Leap Lands complete | 3 map levels, `F` flag, game states, timer + coins, session best |

*Coming soon in Block 5:* Night Swarm, Lane Rush — see [block-5 README](course-3-game-dev/block-5-bonus-star-projects-2/README.md).

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
