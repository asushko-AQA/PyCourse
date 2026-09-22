# Lesson 3.1: Collision Detection

> **Course:** Game Development with Python  
> **Block:** Physics & Collisions (Final Project)  
> **Time:** ~30–35 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level 9 — Coin Collector |
| **[Русский →](ru.md)** | Уровень 9 — Сборщик монет |

---

## What you'll build / Что ты создашь

**EN:** A blue player box that collects a golden **coin**. Each touch adds a point and the coin jumps to a new random spot.

**Expected (sketch):**

```text
[ Player (arrows) ] ----colliderect----> [ Coin ]
                                              |
                                         score += 1
                                         coin moves
```

**RU:** Синий прямоугольник-игрок собирает золотую **монету**. Касание даёт очко, монета прыгает в новое случайное место.

## What you'll learn / Что ты узнаешь

- `Rect.colliderect(other)` — True when two rectangles overlap
- Relocate a collectible after a hit (avoid “infinite score” while overlapping)
- Reuse `get_pressed`, `dt`, and `font.render` from Block 2

## Before you start / Перед стартом

- [ ] [Lesson 2.4](../../block-2-player-controls-animations/lesson-2-4-game-states/README.md) — game states (ideas you’ll reuse soon)
- [ ] Comfortable with `Rect`, arrows, and score text

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | Movement + coin draw; TODO collision |
| [starter/coin.png](starter/coin.png) | Coin sprite |
| [solution/game.py](solution/game.py) | Full collect loop |

## Quick drills / Быстрые упражнения

1. Print `score` to the terminal each time you collect (temporary debug).
2. Make the coin larger (scale) or use a yellow `draw.circle` fallback.
3. Only allow collecting when holding SPACE (extra challenge).

---

**Previous / Предыдущий урок:** [Lesson 2.4 — Game States](../../block-2-player-controls-animations/lesson-2-4-game-states/README.md)

**Next / Дальше:** [Lesson 3.2 — Catch the Falling Stars](../lesson-3-2-catch-the-falling-stars/README.md)
