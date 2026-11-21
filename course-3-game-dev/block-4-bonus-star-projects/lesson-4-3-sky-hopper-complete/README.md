# Lesson 4.3: Sky Hopper Complete

> **Course:** Game Development with Python  
> **Block:** Bonus ★ Star Projects *(optional)*  
> **Time:** ~40–45 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level ★3 — Sky Hopper Pro |
| **[Русский →](ru.md)** | Уровень ★3 — Мастер Sky Hopper |

---

## What you'll build / Что ты создашь

**EN:** Ship **Sky Hopper** — the full bonus mini-game: **title → play → game over → restart**, session **high score**, and gateways that **speed up** as you score.

**RU:** Готовый **Sky Hopper**: **титул → игра → game over → рестарт**, **рекорд сессии**, врата **ускоряются** со счётом.

## What you'll learn / Что ты узнаешь

- Reuse Lesson 2.4 **game states** in a flap game
- Update `high_score` when a round ends
- Difficulty ramp: `scroll_speed = BASE_SCROLL + score * 8`

## Before you start / Перед стартом

- [ ] [Lesson 4.2](../lesson-4-2-scrolling-gateways/README.md) — gateways + score

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [starter/game.py](starter/game.py) | Skeleton states; TODO full loop |
| [solution/game.py](solution/game.py) | Complete Sky Hopper ★ project |

## Quick drills / Быстрые упражнения

1. Show “NEW BEST!” when you beat `high_score`.
2. Cap speed: `min(scroll_speed, 320)`.
3. Change caption to your own game name (keep it original!).

---

**Previous / Предыдущий урок:** [Lesson 4.2](../lesson-4-2-scrolling-gateways/README.md)

**Next / Дальше:** [Block 4 index](../README.md) — ★ project #2 (lessons 4.4–4.6) coming in a future update!