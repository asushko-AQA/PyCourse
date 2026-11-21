# Block 5: Bonus ★ Star Projects II / Бонус: проекты со звёздочкой II

> **Course:** Game Development with Python  
> **Block:** Bonus ★ Star Projects II *(optional — after Block 4)*  
> **Status:** Glow Worm (5.1–5.3) · **Bounce Forge–Lane Rush: coming soon**  
> **Optional:** Finish Block 3 (required path) and Block 4 ★ if you like; these lessons are extra credit.

**Folder map / Карта папок:** [STUDENT-MAP.md](../STUDENT-MAP.md) · [STUDENT-MAP.ru.md](../STUDENT-MAP.ru.md)

**Theme:** More arcade ideas — **original names and glowing shape art** (no copyrighted sprites).

---

## Full roadmap (contributors)

Block 5 uses **lesson IDs 5.x**. Each ★ mini-game gets **2–5 consecutive lessons**.

| Lessons | ★ Project | Game style | Status |
|---------|-----------|------------|--------|
| **5.1 – 5.3** | **Glow Worm** | grid snake, segments list, grow + speed | **Shipped** |
| 5.4 – 5.7 | **Bounce Forge** | Pong / Breakout-like | *Coming soon* |
| 5.8 – 5.11 | **Orbit Guard** | Space Invaders-like | *Coming soon* |
| 5.12 – 5.15 | **Mine Whisper** | Minesweeper-like | *Coming soon* |
| 5.16 – 5.18 | **Merge Magic** | 2048-like | *Coming soon* |
| 5.19 – 5.21 | **Twin Cards** | memory / pairs | *Coming soon* |
| 5.22 – 5.24 | **Tic-Tac-Bot** | tic-tac-toe + simple AI | *Coming soon* |
| 5.25 – 5.29 | **Leap Lands** | mini platformer, text map level | *Coming soon* |
| 5.30 – 5.34 | **Night Swarm** | top-down survivor-like | *Coming soon* |
| 5.35 – 5.37 | **Lane Rush** | top-down dodge racer | *Coming soon* |

**Folder pattern:** `lesson-5-{n}-{slug}/` inside `block-5-bonus-star-projects-2/`.  
Add one ★ game per PR using the next free **5.x** slots.

---

## Lessons / Уроки — Glow Worm (project #1)

| # | English | Русский | Level |
|---|---------|---------|-------|
| 5.1 | [Grid & Segments](lesson-5-1-glow-worm-grid-segments/README.md) | Сетка и сегменты | Level ★13 — Neon Trail |
| 5.2 | [Food, Growth & Collisions](lesson-5-2-glow-worm-food-growth/README.md) | Еда, рост и столкновения | Level ★14 — Spark Bite |
| 5.3 | [Glow Worm Complete](lesson-5-3-glow-worm-complete/README.md) | Glow Worm целиком | Level ★15 — Glow Worm Pro |

**Previous / Предыдущее:** [Block 4 ★](../block-4-bonus-star-projects/README.md) — [Glyph Grove 4.12](../block-4-bonus-star-projects/lesson-4-12-glyph-grove-complete/README.md) *(recommended)*

---

## Block 5 readiness checklist (Glow Worm)

- [ ] `segments` is a list of `(col, row)` cells; `direction` is a `(dc, dr)` tuple
- [ ] Arrow keys queue direction; no instant 180° U-turn into the body
- [ ] Timer step moves the worm one cell per tick
- [ ] Food spawns on empty cells; eating grows the worm and bumps score
- [ ] Wall or self hit ends the run
- [ ] Start → play → game over → restart; session **best score**; speed ramps with score

---

## For parents and teachers

These lessons are **optional stretch goals** after Block 4 ★. Same homework style: **self-mark + Quick Check quiz**. Expect ~30–40 min per lesson (~2 hours per ★ mini-game).

**Display:** Graphical desktop required (Pygame window).

**Common stuck points:** mixing up `(col, row)` order; moving every frame instead of on a timer; popping the tail when the worm should grow after food.

---

*★ II means more bonus shine — take your time!*