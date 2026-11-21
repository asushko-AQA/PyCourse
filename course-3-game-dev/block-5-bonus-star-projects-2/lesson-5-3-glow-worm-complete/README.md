# Lesson 5.3: Glow Worm Complete

> **Course:** Game Development with Python  
> **Block:** Bonus ★ Star Projects II *(optional)*  
> **Time:** ~35–40 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level ★15 — Glow Worm Pro |
| **[Русский →](ru.md)** | Уровень ★15 — Glow Worm Pro |

---

## What you'll build / Что ты создашь

**EN:** Ship **Glow Worm** as a mini arcade game: **start → play → game over** screens, **session best score**, and a **speed ramp** as you eat more sparks.

**RU:** Собери **Glow Worm** целиком: экраны **старт → игра → конец**, **рекорд сессии** и **ускорение** с ростом счёта.

## What you'll learn / Что ты узнаешь

- `state` strings: `START`, `PLAYING`, `GAME_OVER`
- `high_score` saved across runs in one session
- `move_interval_for_score()` — faster ticks, capped at `MIN_INTERVAL`
- SPACE on title and game-over overlays

## Before you start / Перед стартом

- [ ] [Lesson 5.2](../lesson-5-2-glow-worm-food-growth/README.md) — eat, grow, crash wired

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | States + speed ramp TODOs |
| [solution/game.py](solution/game.py) | Full Glow Worm arcade loop |

## Quick drills / Быстрые упражнения

1. Beat your `high_score` twice in one run — does the title show the new best?
2. At score 15, print `move_interval` — is it near `MIN_INTERVAL`?
3. Add a one-line hint on the start screen (“Arrows move · SPACE start”).

---

**Previous / Предыдущий урок:** [Lesson 5.2 — Food, Growth & Collisions](../lesson-5-2-glow-worm-food-growth/README.md)

**Next / Дальше:** [Block 5 ★ II — Bounce Forge coming soon](../README.md) · [Course 3 map](../../STUDENT-MAP.md)