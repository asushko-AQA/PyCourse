# Block 4: Bonus ★ Star Projects / Бонус: проекты со звёздочкой

> **Course:** Game Development with Python  
> **Block:** Bonus ★ Star Projects *(optional — after Block 3)*  
> **Status:** Sky Hopper (4.1–4.3) available · more ★ games planned  
> **Optional:** Finish Block 3 first; these lessons are extra credit, not required for Course 3 graduation.

**Folder map / Карта папок:** [STUDENT-MAP.md](../STUDENT-MAP.md) · [STUDENT-MAP.ru.md](../STUDENT-MAP.ru.md)

**Theme:** Famous arcade ideas — rebuilt with **your own names and art** (procedural shapes, simple sprites you draw). No copyrighted assets.

---

## Lesson numbering (for contributors)

Block 4 uses **lesson IDs 4.x**. Each ★ mini-game gets **2–3 consecutive lessons** (3 for the first project).

| Lessons | ★ Project | Game style | Status |
|---------|-----------|------------|--------|
| **4.1 – 4.3** | **Sky Hopper** | flap + scrolling gateways (Flappy-like) | **This PR** |
| 4.4 – 4.6 | *(planned)* | Geometry Dash-like runner | Future PR |
| 4.7 – 4.9 | *(planned)* | Tetris-like stack puzzle | Future PR |
| 4.10 – 4.12 | *(planned)* | Mahjong solitaire-like match | Future PR |

**Folder pattern:** `lesson-4-{n}-{slug}/` inside `block-4-bonus-star-projects/`.  
When adding project #2, start at **4.4**, not 4.1 again.

---

## Lessons / Уроки — Sky Hopper (project #1)

| # | English | Русский | Level |
|---|---------|---------|-------|
| 4.1 | [Gravity & Flap](lesson-4-1-sky-hopper-gravity-flap/README.md) | Гравитация и взмах | Level ★1 — Breeze Bird |
| 4.2 | [Scrolling Gateways](lesson-4-2-scrolling-gateways/README.md) | Прокручивающиеся врата | Level ★2 — Gateway Glider |
| 4.3 | [Sky Hopper Complete](lesson-4-3-sky-hopper-complete/README.md) | Sky Hopper целиком | Level ★3 — Sky Hopper Pro |

**Previous / Предыдущее:** [Block 3 — Physics & Collisions](../block-3-physics-collisions-final-project/README.md) (required foundation)

**Next / Дальше:** *(future)* ★ Project #2 at lessons 4.4–4.6.

---

## Block 4 readiness checklist (Sky Hopper)

- [ ] Gravity pulls the bird down every frame with `dt`
- [ ] SPACE gives an upward flap impulse
- [ ] Pipes scroll left; passing a gateway adds to score
- [ ] Start → play → game over → title restart works
- [ ] Session **high score** and gentle **speed ramp** feel fair

---

## For parents and teachers

These lessons are **optional stretch goals** after the Course 3 capstone. Same homework style as Block 3: **self-mark + Quick Check quiz**. Expect ~30–40 min per lesson (~2 hours for Sky Hopper).

**Display:** Graphical desktop required (Pygame window).

**Common stuck points:** forgetting to multiply movement by `dt`; scoring every frame instead of once per pipe (`scored` flag); mixing up `KEYDOWN` (flap once) vs `get_pressed` (hold).

---

*★ means bonus — shine after you finish the main quest!*