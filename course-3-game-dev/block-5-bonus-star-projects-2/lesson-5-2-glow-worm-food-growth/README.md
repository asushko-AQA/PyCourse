# Lesson 5.2: Food, Growth & Collisions

> **Course:** Game Development with Python  
> **Block:** Bonus ★ Star Projects II *(optional)*  
> **Time:** ~32–38 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level ★14 — Spark Bite |
| **[Русский →](ru.md)** | Уровень ★14 — Искристый укус |

---

## What you'll build / Что ты создашь

**EN:** Your worm **chases glowing spark food**, **grows longer** when it eats, and **stops** on a wall or self crash. Press **SPACE** for a simple restart.

**RU:** Червяк **ловит искры-еду**, **растёт** после укуса и **останавливается** при ударе о стену или себя. **SPACE** — простой рестарт.

## What you'll learn / Что ты узнаешь

- `spawn_food()` on random empty cells
- Grow: **prepend head**, **skip** `pop()` when eating
- Wall / self hit → `alive = False`
- Pink **food** circles + score counter

## Before you start / Перед стартом

- [ ] [Lesson 5.1](../lesson-5-1-glow-worm-grid-segments/README.md) — grid move + timer works

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | Food + growth TODOs |
| [solution/game.py](solution/game.py) | Eat, crash, SPACE restart |

## Quick drills / Быстрые упражнения

1. Eat three sparks — does length increase by three?
2. Force a wall crash — does input stop until SPACE?
3. Log `grow` True/False inside `step_worm`.

---

**Previous / Предыдущий урок:** [Lesson 5.1 — Grid & Segments](../lesson-5-1-glow-worm-grid-segments/README.md)

**Next / Дальше:** [Lesson 5.3 — Glow Worm Complete](../lesson-5-3-glow-worm-complete/README.md)