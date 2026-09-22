# Lesson 1.4: Delta Time & Smooth Movement

> **Course:** Game Development with Python  
> **Block:** Getting Started with Pygame  
> **Time:** ~30–40 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level 4 — Time Slider |
| **[Русский →](ru.md)** | Уровень 4 — Ползунок времени |

---

## What you'll build / Что ты создашь

**EN:** The same sliding box as Lesson 1.3, but motion uses **delta time** (`dt`) so speed is measured in **pixels per second** — smooth on fast and slow machines.

**Expected window (sketch):**

```text
+---------------------------+
|                           |
|   [~~]  slides at 200 px/s|
|   dt = clock.tick(60)/1000|
|                           |
+---------------------------+
```

**RU:** Та же скользящая коробка, но движение через **дельту времени** (`dt`) — скорость в **пикселях в секунду**, плавно на любом ПК.

## What you'll learn / Что ты узнаешь

- Why `x += 3` each frame feels different at 30 FPS vs 120 FPS
- `dt = clock.tick(60) / 1000` (seconds since last frame)
- `x += speed * dt` with `speed` in pixels/second
- Keep position as a `float`, cast to `int` when drawing

## Before you start / Перед стартом

- [ ] [Lesson 1.3](../lesson-1-3-shapes-coordinates/README.md) — moving rect with `x` / `y`
- [ ] Block 1 readiness almost complete — this is the last lesson!

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | Skeleton — TODOs for `dt` and `speed * dt` |
| [solution/game.py](solution/game.py) | Reference solution |

## Quick drills / Быстрые упражнения

1. Change `speed` from `200` to `50` — slow cruise.
2. Try `clock.tick(30)` and then `clock.tick(120)` — with `dt`, travel speed should feel similar.
3. Print `dt` once per second (optional challenge) to see typical values ~0.016.

---

**Previous / Предыдущий урок:** [Lesson 1.3 — Shapes & Coordinates](../lesson-1-3-shapes-coordinates/README.md)

**Next lesson / Следующий урок:** Block 2 — Player Controls *(planned)* · [Block 1 index](../README.md)
