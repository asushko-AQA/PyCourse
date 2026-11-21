# Course 3: Game Development with Python

> **Status:** Draft — Blocks 1–4; Block 5 ★ II (Glow Worm … Twin Cards 5.1–5.21 shipped)  
> **Audience:** Ages 11+ · **Python:** 3.12+ · **Pygame**  
> **Pace:** ~4–6 weeks at 1–2 lessons/week (~30–40 min each) when all blocks ship  
> **Prerequisites:** [Course 1](../course-1-python-basics/README.md) (loops, conditionals, functions, lists). Turtle (Block 5) recommended. Course 2 is helpful for venv/`pip` habits but not required.

Build a complete 2D mini-game with **Pygame** — windows, colors, shapes, keyboard, sprites, collisions, and a playable capstone.

**Master curriculum:** [CURRICULUM.md](../CURRICULUM.md)  
**Folder map (all blocks):** [STUDENT-MAP.md](STUDENT-MAP.md) · [STUDENT-MAP.ru.md](STUDENT-MAP.ru.md)

---

## Blocks / Блоки

| Block | Theme | Lessons | Status | Index |
|-------|-------|---------|--------|-------|
| 1 | Getting Started with Pygame | 1.1 – 1.4 | **Draft** | [block-1-getting-started-pygame](block-1-getting-started-pygame/README.md) |
| 2 | Player Controls & Animations | 2.1 – 2.4 | **Draft** | [block-2-player-controls-animations](block-2-player-controls-animations/README.md) |
| 3 | Physics & Collisions (Final Project) | 3.1 – 3.3 | **Draft** | [block-3-physics-collisions-final-project](block-3-physics-collisions-final-project/README.md) |
| 4 ★ | Bonus Star Projects *(optional)* | 4.1 – 4.12 | **Draft** | [block-4-bonus-star-projects](block-4-bonus-star-projects/README.md) |
| 5 ★ | Bonus Star Projects II *(optional)* | 5.1 – 5.37 *(roadmap)* | **Glow Worm … Twin Cards 5.1–5.21** | [block-5-bonus-star-projects-2](block-5-bonus-star-projects-2/README.md) |

**Suggested path:** Block 1 → 2 → 3 (11 lessons). **Block 4 ★** is extra credit after the capstone (Sky Hopper 4.1–4.3, Prism Dash 4.4–4.6, Shard Stack 4.7–4.9, Glyph Grove 4.10–4.12). **Block 5 ★ II** adds more arcade games (Glow Worm, Bounce Forge, Orbit Guard, Mine Whisper, Merge Magic, Twin Cards). **44 lessons** when Blocks 4–5 bonus content shipped so far is included.

---

## Exit skills (full course)

When you finish Block 3 (required path), you can:

- Install Pygame in a virtual environment and run a classic game loop
- Fill windows with color, draw shapes, and move them with coordinates
- Use **delta time** for smooth, frame-rate independent motion
- Handle keyboard events, load sprites, render score text, and switch game states
- Detect collisions and ship a polished mini-game (**Catch the Falling Stars**)

**Block 4 ★ (optional):** **Sky Hopper**, **Prism Dash**, **Shard Stack**, **Glyph Grove** — bonus arcade games with procedural shapes and font glyphs only.

**Block 5 ★ II (optional):** **Glow Worm**, **Bounce Forge**, **Orbit Guard**, **Mine Whisper**, **Merge Magic**, and **Twin Cards**; three more ★ games on the roadmap (*coming soon*).

**Block 1 exit skills (now):** game loop, window + quit, RGB fill, `draw.rect`, x/y motion, `clock.tick` + `dt`.

---

## Homework style

Pygame windows are hard to autograde headlessly. For Course 3:

- **Self-mark** the Practice Task (did your window do the thing?)
- Complete the **Quick Check** quiz
- No `checker_ref` required for Block 1

---

## For contributors

Content draft lives under the rollout plan (plan 16). Copy this tree into the repo `course-3-game-dev/` when ready for Helper QA. Do not commit from agent scratch folders.

---

*Built with PyCourse — Python for young creators (age 11+).*
