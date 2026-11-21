# Lesson 5.4: Ball & Wall Bounces

> **Course:** Game Development with Python  
> **Block:** Bonus ★ Star Projects II *(optional)*  
> **Time:** ~30-37 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level ★16 — Spark Ball |
| **[Русский →](ru.md)** | Уровень ★16 — Искровой шар |

---

## What you'll build / Что ты создашь

**EN:** **Bounce Forge** — project **#2** in Block 5 — starts as a **Pong / Breakout-style** forge. Today the **spark ball** moves with a **velocity vector** `(vx, vy)` and **bounces** off the window walls.

**RU:** **Bounce Forge** — проект **№2** в Блоке 5 — аркада в стиле **Pong / Breakout**. Сегодня **искровой шар** движется по **вектору скорости** `(vx, vy)` и **отскакивает** от стен окна.

## What you'll learn / Что ты узнаешь

- `ball_vx`, `ball_vy` as floats; position += velocity * `dt`
- Flip velocity sign when the circle touches an edge
- `BALL_R` radius — bounce when center is `R` pixels from the wall
- Forge palette: dark background + orange spark circles

## Before you start / Перед стартом

- [ ] [Block 5 overview](../README.md) — Bounce Forge roadmap
- [ ] [Lesson 5.3 — Glow Worm Complete](../lesson-5-3-glow-worm-complete/README.md)

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

**Previous / Предыдущее:** [Lesson 5.3 — Glow Worm Complete](../lesson-5-3-glow-worm-complete/README.md)

**Next / Дальше:** [Lesson 5.5 — Paddle & Lives](../lesson-5-5-bounce-forge-paddle-lives/README.md)
