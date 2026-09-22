# Lesson 3.2: Catch the Falling Stars

> **Course:** Game Development with Python  
> **Block:** Physics & Collisions (Final Project)  
> **Time:** ~45–50 minutes (capstone)

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level 10 — Star Catcher |
| **[Русский →](ru.md)** | Уровень 10 — Ловец звёзд |

---

## What you'll build / Что ты создашь

**EN:** A complete mini-game you can show friends: **start → catch falling stars with a paddle → score & misses → game over → restart**.

**Expected flow:**

```text
[ Title + SPACE ] --> [ Paddle LEFT/RIGHT + falling star ]
                              |                 |
                           catch              miss (3x)
                              v                 v
                           score++         Game Over → SPACE → Title
```

**RU:** Полная мини-игра для показа друзьям: **старт → лови падающие звёзды платформой → счёт и промахи → game over → рестарт**.

## What you'll learn / Что ты узнаешь

- Spawn + fall motion with `dt`
- Catch vs miss using `colliderect` and `star.top > HEIGHT`
- Wire Block 2 **states** into a real game loop with restart

## Before you start / Перед стартом

- [ ] [Lesson 3.1](../lesson-3-1-collision-detection/README.md) — `colliderect`
- [ ] [Lesson 2.4](../../block-2-player-controls-animations/lesson-2-4-game-states/README.md) — start / playing / game over

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | Screens + paddle; TODOs for fall/catch/states |
| [starter/star.png](starter/star.png) | Star sprite |
| [solution/game.py](solution/game.py) | Complete Catch the Falling Stars |

## Quick drills / Быстрые упражнения

1. Change `MAX_MISSES` from `3` to `5` for an easier round.
2. Widen the paddle (`paddle_w = 140`).
3. Show “Almost!” on Game Over if `score >= 10`.

---

**Previous / Предыдущий урок:** [Lesson 3.1 — Collision Detection](../lesson-3-1-collision-detection/README.md)

**Next / Дальше:** [Lesson 3.3 — Polish](../lesson-3-3-polish/README.md)
