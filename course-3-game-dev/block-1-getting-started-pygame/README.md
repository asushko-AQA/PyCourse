# Block 1: Getting Started with Pygame

> **Course:** Game Development with Python  
> **Block:** Getting Started with Pygame  
> **Lessons:** 1.1 – 1.4 · **~2–2.5 hours total** · **Status: Draft**

**Folder map / Карта папок:** [STUDENT-MAP.md](../STUDENT-MAP.md) · [STUDENT-MAP.ru.md](../STUDENT-MAP.ru.md)

**Theme:** Game Lab Bootcamp — open a window, paint it, move shapes, then make motion smooth.

---

## Lessons / Уроки

| # | English | Русский | Level |
|---|---------|---------|-------|
| 1.1 | [Install Pygame & game loop](lesson-1-1-install-pygame-game-loop/README.md) | Установка Pygame и игровой цикл | Level 1 — Window Wizard |
| 1.2 | [Game Window & Colors](lesson-1-2-game-window-colors/README.md) | Окно игры и цвета | Level 2 — Color Caster |
| 1.3 | [Shapes & Coordinates](lesson-1-3-shapes-coordinates/README.md) | Фигуры и координаты | Level 3 — Box Voyager |
| 1.4 | [Delta Time & Smooth Movement](lesson-1-4-delta-time-smooth-movement/README.md) | Дельта-время и плавное движение | Level 4 — Time Slider |

**Previous / Предыдущее:** [Course 2](../../course-2-web-apps/README.md) *(optional)* · [Course 1 Block 5 Turtle](../../course-1-python-basics/block-5-creative-turtle/README.md) *(recommended)*

**Next block / Следующий блок:** Block 2 — Player Controls & Animations *(planned)*

---

## Block 1 readiness checklist

Tick every box before starting Block 2.

- [ ] I can create/activate a `.venv` and run `pip install pygame`
- [ ] My game window opens and closes cleanly on the X button
- [ ] I can fill the screen with an RGB color and change it each frame
- [ ] I can draw a rectangle and move it by changing `x` / `y`
- [ ] I understand `dt = clock.tick(60) / 1000` and `x += speed * dt`

---

## For parents and teachers

**Block 1 is the Pygame bootstrap.** Students see a real game window every lesson (~30–40 min). Homework is **self-mark + quiz** (no automated display checker).

**Display needed:** Pygame needs a graphical desktop (or remote desktop). Headless CI will not show the window — that is expected.

**Common stuck points:** forgetting to activate the venv before `pip install`; window opening **behind** VS Code; missing `pygame.display.flip()`.

---

*Boot the Game Lab — then paint, move, and smooth!*
