# Block 4: Bonus ★ Star Projects / Бонус: проекты со звёздочкой

> **Course:** Game Development with Python  
> **Block:** Bonus ★ Star Projects *(optional — after Block 3)*  
> **Status:** Sky Hopper (4.1–4.3) + Prism Dash (4.4–4.6) + Shard Stack (4.7–4.9) + Glyph Grove (4.10–4.12) · **Block 4 complete**  
> **Optional:** Finish Block 3 first; these lessons are extra credit, not required for Course 3 graduation.

**Folder map / Карта папок:** [STUDENT-MAP.md](../STUDENT-MAP.md) · [STUDENT-MAP.ru.md](../STUDENT-MAP.ru.md)

**Theme:** Famous arcade ideas — rebuilt with **your own names and art** (procedural shapes, simple sprites you draw). No copyrighted assets.

---

## Lesson numbering (for contributors)

Block 4 uses **lesson IDs 4.x**. Each ★ mini-game gets **2–3 consecutive lessons** (3 for the first project).

| Lessons | ★ Project | Game style | Status |
|---------|-----------|------------|--------|
| **4.1 – 4.3** | **Sky Hopper** | flap + scrolling gateways (Flappy-like) | **Shipped** |
| **4.4 – 4.6** | **Prism Dash** | auto-scroll + jump + level string obstacles | **Shipped** |
| **4.7 – 4.9** | **Shard Stack** | 2D grid, falling shards, line clear | **Shipped** |
| **4.10 – 4.12** | **Glyph Grove** | mouse match, free-tile rule, hint/shuffle | **Shipped** |

**Folder pattern:** `lesson-4-{n}-{slug}/` inside `block-4-bonus-star-projects/`.  
When adding a new ★ game, use the next free **4.x** slot (see table above); do not restart at 4.1.

---

## Lessons / Уроки — Sky Hopper (project #1)

| # | English | Русский | Level |
|---|---------|---------|-------|
| 4.1 | [Gravity & Flap](lesson-4-1-sky-hopper-gravity-flap/README.md) | Гравитация и взмах | Level ★1 — Breeze Bird |
| 4.2 | [Scrolling Gateways](lesson-4-2-scrolling-gateways/README.md) | Прокручивающиеся врата | Level ★2 — Gateway Glider |
| 4.3 | [Sky Hopper Complete](lesson-4-3-sky-hopper-complete/README.md) | Sky Hopper целиком | Level ★3 — Sky Hopper Pro |

**Previous / Предыдущее:** [Block 3 — Physics & Collisions](../block-3-physics-collisions-final-project/README.md) (required foundation)

## Lessons / Уроки — Prism Dash (project #2)

| # | English | Русский | Level |
|---|---------|---------|-------|
| 4.4 | [Auto Scroll & Runner](lesson-4-4-prism-dash-auto-scroll/README.md) | Автопрокрутка и бег | Level ★4 — Neon Cruiser |
| 4.5 | [Jump, Gravity & Spin](lesson-4-5-prism-dash-jump-rotate/README.md) | Прыжок и вращение | Level ★5 — Air Spin Cube |
| 4.6 | [Prism Dash Complete](lesson-4-6-prism-dash-complete/README.md) | Prism Dash целиком | Level ★6 — Prism Dash Pro |

## Lessons / Уроки — Shard Stack (project #3)

| # | English | Русский | Level |
|---|---------|---------|-------|
| 4.7 | [Grid & Cells](lesson-4-7-shard-stack-grid-cells/README.md) | Сетка и клетки | Level ★7 — Crystal Well |
| 4.8 | [Falling Pieces & Controls](lesson-4-8-shard-stack-falling-pieces/README.md) | Падающие осколки | Level ★8 — Drift Shard |
| 4.9 | [Shard Stack Complete](lesson-4-9-shard-stack-complete/README.md) | Shard Stack целиком | Level ★9 — Shard Stack Pro |

## Lessons / Уроки — Glyph Grove (project #4)

| # | English | Русский | Level |
|---|---------|---------|-------|
| 4.10 | [Tiles & Layout](lesson-4-10-glyph-grove-tiles-layout/README.md) | Плитки и раскладка | Level ★10 — Garden Tiles |
| 4.11 | [Mouse Pick & Matching](lesson-4-11-glyph-grove-mouse-matching/README.md) | Мышь и совпадения | Level ★11 — Pair Pick |
| 4.12 | [Glyph Grove Complete](lesson-4-12-glyph-grove-complete/README.md) | Glyph Grove целиком | Level ★12 — Glyph Grove Pro |

**You finished Block 4 ★ / Блок 4 ★ пройден:** all four bonus arcade games shipped!

---

## Block 4 readiness checklist (Glyph Grove)

- [ ] Tile dicts with `kind`, `row`, `col`, `layer` draw with font glyphs
- [ ] `MOUSEBUTTONDOWN` + `rect.collidepoint` selects tiles
- [ ] Free rule: not covered, open left or right
- [ ] Matching pair sets `removed`; win when board empty
- [ ] Hint, shuffle, timer, moves, start/win/stuck, session best time

---

## Block 4 readiness checklist (Shard Stack)

- [ ] `grid[row][col]` draws a 10×20 well
- [ ] `can_move` stops at walls and locked cells
- [ ] Timer + arrows move the active shard
- [ ] `rotate_cells` with simple wall nudge works
- [ ] Full lines clear; score, level, session high score feel fair

---

## Block 4 readiness checklist (Prism Dash)

- [ ] `world_x` scrolls; cube stays at `PLAYER_X`
- [ ] Jump only when `grounded`; cube spins mid-air
- [ ] `LEVEL` string builds platforms (`#`) and spikes (`^`)
- [ ] Spike hit restarts run; progress % and attempts HUD work
- [ ] Session **best %** on title; gentle **speed ramp** feels fair

---

## Block 4 readiness checklist (Sky Hopper)

- [ ] Gravity pulls the bird down every frame with `dt`
- [ ] SPACE gives an upward flap impulse
- [ ] Pipes scroll left; passing a gateway adds to score
- [ ] Start → play → game over → title restart works
- [ ] Session **high score** and gentle **speed ramp** feel fair

---

## For parents and teachers

These lessons are **optional stretch goals** after the Course 3 capstone. Same homework style as Block 3: **self-mark + Quick Check quiz**. Expect ~30–40 min per lesson (~2 hours per ★ mini-game).

**Display:** Graphical desktop required (Pygame window).

**Common stuck points:** forgetting to multiply movement by `dt`; scoring every frame instead of once per pipe (`scored` flag); mixing up `KEYDOWN` (flap once) vs `get_pressed` (hold).

---

*★ means bonus — shine after you finish the main quest!*