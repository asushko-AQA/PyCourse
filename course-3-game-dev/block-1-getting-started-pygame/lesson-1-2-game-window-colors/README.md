# Lesson 1.2: Game Window & Colors

> **Course:** Game Development with Python  
> **Block:** Getting Started with Pygame  
> **Time:** ~30–35 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level 2 — Color Caster |
| **[Русский →](ru.md)** | Уровень 2 — Заклинатель цвета |

---

## What you'll build / Что ты создашь

**EN:** A window whose background color is filled every frame; the red channel slowly cycles so the sky shifts over time.

**Expected window (sketch):**

```text
+---------------------------+
|                           |
|   shifting RGB sky fill   |
|   (color changes / frame) |
|                           |
+---------------------------+
```

**RU:** Окно с заливкой фона каждый кадр; канал красного медленно крутится — небо «дышит» цветом.

## What you'll learn / Что ты узнаешь

- RGB colors as `(r, g, b)` with each value 0–255
- `screen.fill((r, g, b))` every frame
- Changing color variables inside the game loop
- Keeping channels in range with `% 256`

## Before you start / Перед стартом

- [ ] Finished [Lesson 1.1](../lesson-1-1-install-pygame-game-loop/README.md) — window opens and quits cleanly
- [ ] Pygame installed in your active `.venv`

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | Skeleton with TODOs for fill + color nudge |
| [solution/game.py](solution/game.py) | Reference solution |

## Quick drills / Быстрые упражнения

1. Start with pure green `(0, 255, 0)` — then nudge `b` instead of `r`.
2. Try `r = (r + 5) % 256` — faster color shift!
3. Set all three channels to the same changing value — grayscale pulse.

---

**Previous / Предыдущий урок:** [Lesson 1.1 — Install Pygame & Game Loop](../lesson-1-1-install-pygame-game-loop/README.md)

**Next lesson / Следующий урок:** [Lesson 1.3 — Shapes & Coordinates](../lesson-1-3-shapes-coordinates/README.md)
