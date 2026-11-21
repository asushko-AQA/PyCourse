# Lesson 4.2: Scrolling Gateways

> **Course:** Game Development with Python  
> **Block:** Bonus ★ Star Projects *(optional)*  
> **Time:** ~35–40 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level ★2 — Gateway Glider |
| **[Русский →](ru.md)** | Уровень ★2 — Скользящий через врата |

---

## What you'll build / Что ты создашь

**EN:** Add **scrolling green gateways** (pipe pairs with a gap). Fly through, **score +1** per gateway, **crash** on walls or sky/floor.

**RU:** **Зелёные врата** (пара препятствий с проходом). Пролетай — **+1 к счёту**; удар — **crash**.

## What you'll learn / Что ты узнаешь

- Spawn and scroll obstacles with `dt`
- `colliderect` for gateway hits
- Score once per gateway with a `scored` flag

## Before you start / Перед стартом

- [ ] [Lesson 4.1](../lesson-4-1-sky-hopper-gravity-flap/README.md) — gravity + flap

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [starter/game.py](starter/game.py) | Physics from 4.1; TODO pipes |
| [solution/game.py](solution/game.py) | Scroll, score, crash + R reset |

## Quick drills / Быстрые упражнения

1. `GAP = 180` for an easier passage.
2. `SCROLL = 140` for slower gates.
3. Flash the score text yellow when you pass a gateway.

---

**Previous / Предыдущий урок:** [Lesson 4.1](../lesson-4-1-sky-hopper-gravity-flap/README.md)

**Next / Дальше:** [Lesson 4.3 — Sky Hopper Complete](../lesson-4-3-sky-hopper-complete/README.md)