# Block 3: Physics & Collisions (Final Project)

> **Course:** Game Development with Python  
> **Block:** Physics & Collisions (Final Project)  
> **Lessons:** 3.1 – 3.3 · **~2–2.5 hours total** · **Status: Draft**

**Folder map / Карта папок:** [STUDENT-MAP.md](../STUDENT-MAP.md) · [STUDENT-MAP.ru.md](../STUDENT-MAP.ru.md)

**Theme:** Final Mission — collide, catch falling stars, then polish the show.

---

## Lessons / Уроки

| # | English | Русский | Level |
|---|---------|---------|-------|
| 3.1 | [Collision Detection](lesson-3-1-collision-detection/README.md) | Обнаружение столкновений | Level 9 — Coin Collector |
| 3.2 | [Catch the Falling Stars](lesson-3-2-catch-the-falling-stars/README.md) | Поймай падающие звёзды | Level 10 — Star Catcher |
| 3.3 | [Polish](lesson-3-3-polish/README.md) | Полировка | Level 11 — Polish Pro |

**Previous / Предыдущее:** [Block 2 — Player Controls & Animations](../block-2-player-controls-animations/README.md)

**Next / Дальше:** Course 3 complete — show your **Catch the Falling Stars** game!

---

## Block 3 readiness checklist

Tick every box to graduate Course 3.

- [ ] `rect.colliderect()` collects a coin and relocates it
- [ ] Capstone: stars spawn, fall, get caught, score updates, restart works
- [ ] Polish: high score (session), difficulty ramp, optional catch/miss sounds

---

## For parents and teachers

**Block 3 is the Course 3 finale.** Lesson 3.2 is the **capstone** (~45–50 min); 3.1 and 3.3 stay ~30–40 min. Homework remains **self-mark + quiz** (no automated display checker).

**Display needed:** Same as Blocks 1–2 — graphical desktop required. Sound in 3.3 needs working audio (optional — game still runs without speakers).

**Common stuck points:** forgetting to move the coin/star after a hit (infinite score); using `KEYDOWN` for paddle motion; not resetting `misses` / `score` on restart; mixer errors if speakers/drivers are odd — wrap Sound load in `try/except`.

---

*Collide, catch, polish — then take a bow!*
