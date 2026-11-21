# Lesson 4.5: Jump, Gravity & Spin

> **Course:** Game Development with Python  
> **Block:** Bonus ★ Star Projects *(optional)*  
> **Time:** ~35–40 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level ★5 — Air Spin Cube |
| **[Русский →](ru.md)** | Уровень ★5 — Вращение в воздухе |

---

## What you'll build / Что ты создашь

**EN:** The cube **jumps** with gravity, **lands** on the ground with snap logic, and **spins** while airborne — still no deadly spikes.

**RU:** Куб **прыгает** с гравитацией, **приземляется** со snap-логикой и **крутится** в воздухе — пока без смертельных шипов.

## What you'll learn / Что ты узнаешь

- Grounded check: jump only when `grounded` is `True`
- `vel_y`, `GRAVITY * dt`, and `JUMP_V` impulse
- `pygame.transform.rotate` for a spinning cube

## Before you start / Перед стартом

- [ ] [Lesson 4.4](../lesson-4-4-prism-dash-auto-scroll/README.md) — scrolling `world_x`

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | Scroll works; TODO jump/spin |
| [solution/game.py](solution/game.py) | Jump + snap + rotation |

## Quick drills / Быстрые упражнения

1. `JUMP_V = -620` for a taller hop.
2. `ROT_SPEED = 450` for faster spins.
3. Flash cube white for 0.1s right after jump.

---

**Previous / Предыдущий урок:** [Lesson 4.4 — Auto Scroll](../lesson-4-4-prism-dash-auto-scroll/README.md)

**Next / Дальше:** [Lesson 4.6 — Prism Dash Complete](../lesson-4-6-prism-dash-complete/README.md)