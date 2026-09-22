# Lesson 2.3: Score & Text Rendering

> **Course:** Game Development with Python  
> **Block:** Player Controls & Animations  
> **Time:** ~30–35 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level 7 — Score Scribbler |
| **[Русский →](ru.md)** | Уровень 7 — Писарь очков |

---

## What you'll build / Что ты создашь

**EN:** A live **Score:** HUD in the top-left. Hold RIGHT to earn points. Text is drawn with `font.render` + `blit`.

**Expected window (sketch):**

```text
+---------------------------+
| Score: 42                 |
|         [##]              |
|   (hold RIGHT to earn)    |
|                           |
+---------------------------+
```

**RU:** Живой **Score:** в левом верхнем углу. Держи RIGHT — копи очки. Текст рисуется через `font.render` + `blit`.

## What you'll learn / Что ты узнаешь

- `pygame.font.Font(None, size)` — default font
- `font.render(text, antialias, color)` → Surface
- Blit the text surface each frame (rebuild when the number changes)
- Keep score as a float; show `int(score)` on screen

## Before you start / Перед стартом

- [ ] [Lesson 2.1](../lesson-2-1-keyboard-events/README.md) — keyboard move
- [ ] Optional: copy `player.png` from Lesson 2.2 into this starter (code works with a rect fallback)

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | Skeleton — TODOs for Font + render |
| [solution/game.py](solution/game.py) | Reference score HUD |

## Quick drills / Быстрые упражнения

1. Change HUD color to neon green `(80, 255, 120)`.
2. Add a second line: `Speed: {speed}`.
3. Reset score to `0` when you press `R` (`KEYDOWN`).

---

**Previous / Предыдущий урок:** [Lesson 2.2 — Images & Sprites](../lesson-2-2-images-sprites/README.md)

**Next lesson / Следующий урок:** [Lesson 2.4 — Game States](../lesson-2-4-game-states/README.md)
