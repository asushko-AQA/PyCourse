# Lesson 1.3: Shapes & Coordinates

> **Course:** Game Development with Python  
> **Block:** Getting Started with Pygame  
> **Time:** ~30–35 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level 3 — Box Voyager |
| **[Русский →](ru.md)** | Уровень 3 — Капитан координат |

---

## What you'll build / Что ты создашь

**EN:** A golden rectangle that slides to the right across a dark sky. When it leaves the screen, it wraps back to the left.

**Expected window (sketch):**

```text
+---------------------------+
|                           |
|      [##]----->           |
|   gold box moves by x+=   |
|                           |
+---------------------------+
  (0,0) top-left origin
```

**RU:** Золотой прямоугольник едет вправо по тёмному небу. Уйдя за край, снова появляется слева.

## What you'll learn / Что ты узнаешь

- Pygame coordinates: `(0, 0)` is **top-left**; `x` right, `y` down
- `pygame.draw.rect(screen, color, (x, y, w, h))`
- Move by changing `x` / `y` each frame
- Simple wrap when the box leaves the window

## Before you start / Перед стартом

- [ ] [Lesson 1.2](../lesson-1-2-game-window-colors/README.md) — fill + RGB
- [ ] Comfortable with variables from Course 1

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | Skeleton — TODOs for move + draw |
| [solution/game.py](solution/game.py) | Reference with wrap |

## Quick drills / Быстрые упражнения

1. Change `speed` from `3` to `8` — faster voyage!
2. Move down instead: `y = y + speed` (and wrap on `HEIGHT`).
3. Draw a second smaller box at a fixed position.

---

**Previous / Предыдущий урок:** [Lesson 1.2 — Game Window & Colors](../lesson-1-2-game-window-colors/README.md)

**Next lesson / Следующий урок:** [Lesson 1.4 — Delta Time & Smooth Movement](../lesson-1-4-delta-time-smooth-movement/README.md)
