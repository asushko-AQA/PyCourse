# Lesson 1.1: Install Pygame & Game Loop

> **Course:** Game Development with Python  
> **Block:** Getting Started with Pygame  
> **Time:** ~35–40 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level 1 — Window Wizard |
| **[Русский →](ru.md)** | Уровень 1 — Мастер окна |

---

## What you'll build / Что ты создашь

**EN:** A `game.py` script that opens a 640×480 Pygame window (deep blue), keeps the game loop running at 60 FPS, and closes cleanly when you click the X.

**Expected window (sketch):**

```text
+---------------------------+
|                           |
|     deep blue window      |
|     title bar: My First…  |
|                           |
+---------------------------+
         [X] closes cleanly
```

**RU:** Скрипт `game.py` — окно Pygame 640×480 (тёмно-синее), игровой цикл 60 FPS, чистое закрытие по крестику.

## What you'll learn / Что ты узнаешь

- Create/activate a `.venv` and `pip install pygame`
- Classic game loop: init → while running → events → draw → flip → tick
- Handle `pygame.QUIT` so the window closes cleanly
- `pygame.display.set_mode`, `set_caption`, `flip`, `clock.tick`

## Before you start / Перед стартом

- [ ] Course 1 complete (especially loops and conditionals)
- [ ] You know how to run `python file.py` from the terminal
- [ ] *(Helpful)* Course 2 Lesson 0.1 — virtual environments

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | Skeleton with TODO comments |
| [solution/game.py](solution/game.py) | Reference solution |

## Quick drills / Быстрые упражнения

1. Change `(640, 480)` to `(800, 600)` — predict the new size before you run.
2. Change the fill color `(30, 30, 80)` to `(80, 0, 0)` — deep red!
3. Comment out `pygame.display.flip()` once — what do you see? Put it back.

---

**Previous / Предыдущий урок:** [Course 3 index](../../README.md)

**Next lesson / Следующий урок:** [Lesson 1.2 — Game Window & Colors](../lesson-1-2-game-window-colors/README.md)
