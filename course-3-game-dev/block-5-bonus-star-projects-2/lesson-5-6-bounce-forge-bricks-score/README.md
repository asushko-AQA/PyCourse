# Lesson 5.6: Bricks & Score

> **Course:** Game Development with Python  
> **Block:** Bonus ★ Star Projects II *(optional)*  
> **Time:** ~34-41 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level ★18 — Ember Bricks |
| **[Русский →](ru.md)** | Уровень ★18 — Угольные кирпичи |

---

## What you'll build / Что ты создашь

**EN:** **Ember bricks** sit at the top as a `list` of `pygame.Rect`. Detect **which side** the ball hit, **remove** the brick, and **add score**.

**RU:** **Угольные кирпичи** сверху — `list` из `pygame.Rect`. Определи **сторону** удара, **удали** кирпич и **начисли счёт**.

## What you'll learn / Что ты узнаешь

- Build rows from string patterns (`"1110101"`)
- Save `prev_ball_x/y` before moving — better side guess
- Flip `vx` on left/right hits; flip `vy` on top/bottom
- `score += 10` per brick

## Before you start / Перед стартом

- [ ] [Block 5 overview](../README.md) — Bounce Forge roadmap
- [ ] [Lesson 5.5 — Paddle & Lives](../lesson-5-5-bounce-forge-paddle-lives/README.md)

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | Runnable skeleton with TODOs |
| [solution/game.py](solution/game.py) | Reference forge game |

## Quick drills / Быстрые упражнения

1. Print velocity after each wall bounce.
2. Change `BALL_R` — does the ball feel tighter?
3. Skim [solution/game.py](solution/game.py) for forge colors.

---

**Previous / Предыдущее:** [Lesson 5.5 — Paddle & Lives](../lesson-5-5-bounce-forge-paddle-lives/README.md)

**Next / Дальше:** [Lesson 5.7 — Bounce Forge Complete](../lesson-5-7-bounce-forge-complete/README.md)
