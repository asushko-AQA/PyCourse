# Lesson 4.4: Auto Scroll & Runner

> **Course:** Game Development with Python  
> **Block:** Bonus ★ Star Projects *(optional)*  
> **Time:** ~30–35 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level ★4 — Neon Cruiser |
| **[Русский →](ru.md)** | Уровень ★4 — Неоновый бегун |

---

## What you'll build / Что ты создашь

**EN:** **Prism Dash** starts here — a neon cube that **runs in place** while the **world scrolls** left. No jumping yet; just the auto-runner feel from shapes only.

**RU:** **Prism Dash** начинается здесь — неоновый куб **бежит на месте**, а **мир прокручивается** влево. Пока без прыжков — только ощущение авто-раннера из фигур.

## What you'll learn / Что ты узнаешь

- `world_x` scroll counter + `SCROLL * dt`
- Screen position: `tile_x - world_x` (hero stays at `PLAYER_X`)
- Draw platforms from a simple string pattern (`#` = block)

## Before you start / Перед стартом

- [ ] [Lesson 4.3](../lesson-4-3-sky-hopper-complete/README.md) — finished ★ project #1 *(recommended)*
- [ ] [Lesson 1.4](../../../block-1-getting-started-pygame/lesson-1-4-delta-time-smooth-movement/README.md) — `dt` motion

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | Neon cube + ground; TODO scroll |
| [solution/game.py](solution/game.py) | Scrolling skyline demo |

## Quick drills / Быстрые упражнения

1. Change `SCROLL` from `220` to `320` — how fast does the world feel?
2. Add a second decor symbol (`.` = tiny star) in `DECOR`.
3. Tint the ground stripe when `world_x` passes every `500` pixels.

---

**Previous / Предыдущий урок:** [Lesson 4.3 — Sky Hopper Complete](../lesson-4-3-sky-hopper-complete/README.md)

**Next / Дальше:** [Lesson 4.5 — Jump, Gravity & Spin](../lesson-4-5-prism-dash-jump-rotate/README.md)