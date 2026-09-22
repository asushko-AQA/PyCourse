# Lesson 1.1: Install Pygame & Game Loop

> **Course:** Game Development with Python · **Block:** Getting Started with Pygame · **~35–40 min**  
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/game.py
minutes: 35
-->

---

## Title

**Level 1 — Window Wizard**

---

## Explanation

Welcome to the **Game Lab**! Turtle drew shapes one command at a time. **Pygame** is different — it runs a **game loop** that repeats many times every second: check events → update → draw → show the frame.

| Piece | What it does |
|-------|--------------|
| `import pygame` | Load the game toolkit (needs `pip install pygame`) |
| `pygame.init()` | Start Pygame's systems |
| `pygame.display.set_mode((w, h))` | Open a window of width `w` and height `h` |
| `pygame.QUIT` | Event when the player clicks the window **X** |
| `pygame.display.flip()` | Show what you drew this frame |
| `clock.tick(60)` | Aim for about 60 frames per second |

**Install once (inside a venv):** You can reuse a Course 2 `.venv` or create a new one at your project root.

```text
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install pygame
```

**Mac/Linux:** `source .venv/bin/activate` then `pip install pygame`.

Check it worked:

```text
python -c "import pygame; print(pygame.version.ver)"
```

---

### Step 1: Activate your venv and install Pygame

Open a VS Code terminal. Activate `.venv`, then run `pip install pygame`. Keep `(.venv)` visible in the prompt while you work.

---

### Step 2: Open starter/game.py

Open [starter/game.py](starter/game.py). Read every `# TODO` — they mark the magic lines of the game loop.

---

### Step 3: cd to this lesson folder

**Path A — PyCourse repo:**

```text
cd course-3-game-dev\block-1-getting-started-pygame\lesson-1-1-install-pygame-game-loop
```

**Path B — your own folder:** Copy `game.py` anywhere. Open VS Code on that folder. See [STUDENT-MAP](../../STUDENT-MAP.md).

**Mac/Linux:** use forward slashes, e.g. `python starter/game.py`.

---

### Step 4: Run the script

```text
python starter\game.py
```

**Expected output (visual):**

- A **Pygame window** opens (check the taskbar — it may sit **behind** VS Code).
- The window is a solid **deep blue**.
- Title bar says **My First Pygame Window** (or your caption).
- Click the **X** — the window closes and the terminal returns to the prompt (no crash).

The terminal may show almost no text — that is normal for Pygame!

---

### Step 5: Trace the game loop

Every frame:

1. `pygame.event.get()` — any clicks, quits, keys?
2. If `QUIT` → `running = False`
3. `screen.fill(...)` — paint the background
4. `pygame.display.flip()` — show the frame
5. `clock.tick(60)` — wait a tiny bit so we are near 60 FPS

When `running` becomes `False`, we leave the `while` loop and call `pygame.quit()`.

---

## Code Example

**File: [starter/game.py](starter/game.py)** (completed shape matches the solution)

```python
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My First Pygame Window")

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 80))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

---

## Code Execution

```text
cd course-3-game-dev\block-1-getting-started-pygame\lesson-1-1-install-pygame-game-loop
python starter\game.py
```

**Expected output (visual):** Deep-blue 640×480 window; closes cleanly on X.

**Expected terminal (typical):** little or no text; prompt returns after quit.

---

## Quick Drills

1. **Bigger portal** — change size to `(800, 600)`. Run. Did the window grow?
2. **New title** — set caption to `"Window Wizard"`. Check the title bar.
3. **No flip** — temporarily comment out `pygame.display.flip()`. What happens? Uncomment it.

---

## Practice Task

**Quest name:** Window Wizard

1. Confirm Pygame imports inside your active venv.
2. Run [starter/game.py](starter/game.py) and close it with the **X** (not only Ctrl+C).
3. Change the fill to any RGB triple you like (each number 0–255).
4. **Bonus:** Print `"Game Lab online!"` once **before** the `while` loop — you should see it in the terminal when the window opens.

**Self-mark:** Window opened? Closed with X? Color changed? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** `ModuleNotFoundError: No module named 'pygame'`

**Cause:** Pygame is not installed in the Python you are using — often the venv is **not activated**, or you installed into a different environment.

**Fix:**

1. Activate `.venv` (prompt shows `(.venv)`).
2. Run `pip install pygame` again.
3. Confirm with `python -c "import pygame; print(pygame.version.ver)"`.
4. Run `python starter\game.py` from the same terminal.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. Where should you install Pygame for this course?
   - **a)** Globally with no venv — always
   - **b)** Inside an activated `.venv` with `pip install pygame`
   - **c)** By copying `pygame.py` into the lesson folder
   - **d)** Only on Mac/Linux — Windows cannot use Pygame

2. What does `pygame.QUIT` mean in the event loop?
   - **a)** The game scored a point
   - **b)** The player clicked the window close (X) button
   - **c)** The clock reached 60 FPS
   - **d)** Python finished installing packages

3. Why call `pygame.display.flip()` each frame?
   - **a)** To install Pygame
   - **b)** To show the frame you just drew on the screen
   - **c)** To close the window
   - **d)** To create a new virtual environment

4. What does `clock.tick(60)` mainly do?
   - **a)** Draw sixty rectangles
   - **b)** Help limit the loop to about 60 frames per second
   - **c)** Set the window title to `"60"`
   - **d)** Delete old events

5. What is the last cleanup call after the game loop ends?
   - **a)** `pip uninstall pygame`
   - **b)** `turtle.done()`
   - **c)** `pygame.quit()`
   - **d)** `screen.fill((0, 0, 0))` only

---

<details><summary>Click to reveal answers</summary>

1. **b)** Keep packages inside `.venv` so projects do not clash.
2. **b)** `QUIT` is the close-window event.
3. **b)** `flip()` pushes your drawn frame to the display.
4. **b)** `tick(60)` paces the loop near 60 FPS.
5. **c)** `pygame.quit()` shuts down Pygame cleanly after the loop.

</details>

---

## What's Next

→ [Lesson 1.2: Game Window & Colors](../lesson-1-2-game-window-colors/README.md) — fill the sky and shift RGB every frame.

---

*Your portal is open. Next up: paint the world!*

[← Choose language](README.md)
