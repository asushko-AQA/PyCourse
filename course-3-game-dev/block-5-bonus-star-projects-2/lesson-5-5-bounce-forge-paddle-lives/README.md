# Lesson 5.5: Paddle & Lives

> **Course:** Game Development with Python  
> **Block:** Bonus ★ Star Projects II *(optional)*  
> **Time:** ~33-40 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level ★17 — Anvil Paddle |
| **[Русский →](ru.md)** | Уровень ★17 — Ракетка-наковальня |

---

## What you'll build / Что ты создашь

**EN:** Add the **anvil paddle** at the bottom. The ball **deflects** based on **where** it hits the paddle; miss the paddle and you **lose a life**.

**RU:** Добавь **ракетку-наковальню** снизу. Шар **отскакивает** от **места удара**; промах — **минус жизнь**.

## What you'll learn / Что ты узнаешь

- `pygame.Rect` paddle; move with A/D or arrows + `dt`
- `hit_frac` from -1 (left edge) to 1 (right edge)
- Steeper `ball_vx` when you hit the paddle edge
- `lives` counter; re-serve ball after a miss

## Before you start / Перед стартом

- [ ] [Block 5 overview](../README.md) — Bounce Forge roadmap
- [ ] [Lesson 5.4 — Ball & Wall Bounces](../lesson-5-4-bounce-forge-ball-walls/README.md)

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

**Previous / Предыдущее:** [Lesson 5.4 — Ball & Wall Bounces](../lesson-5-4-bounce-forge-ball-walls/README.md)

**Next / Дальше:** [Lesson 5.6 — Bricks & Score](../lesson-5-6-bounce-forge-bricks-score/README.md)
