# Lesson 4.1: Gravity & Flap

> **Course:** Game Development with Python  
> **Block:** Bonus ★ Star Projects *(optional)*  
> **Time:** ~30–35 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level ★1 — Breeze Bird |
| **[Русский →](ru.md)** | Уровень ★1 — Птица ветра |

---

## What you'll build / Что ты создашь

**EN:** **Sky Hopper** — a cute procedural bird in an open sky. **Gravity** pulls down; **SPACE** flaps up. No pipes yet — just flight feel.

**RU:** **Sky Hopper** — птица из фигур в открыбом небе. **Гравитация** тянет вниз; **SPACE** — взмах вверх. Без труб — только ощущение полёта.

## What you'll learn / Что ты узнаешь

- Vertical physics with `vel_y` and `GRAVITY * dt`
- One-shot input: `KEYDOWN` + SPACE for flap
- Draw a hero with circles and polygons (no PNG)

## Before you start / Перед стартом

- [ ] [Lesson 3.3](../../../block-3-physics-collisions-final-project/lesson-3-3-polish/README.md) — finished Course 3 capstone *(recommended)*
- [ ] [Lesson 1.4](../../../block-1-getting-started-pygame/lesson-1-4-delta-time-smooth-movement/README.md) — `dt` motion

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | Sky + bird drawn; TODO flap/gravity |
| [solution/game.py](solution/game.py) | Practice sky with working physics |

## Quick drills / Быстрые упражнения

1. Change `GRAVITY` from `720` to `900` — how does flight feel?
2. Make `FLAP_STRENGTH` stronger (more negative).
3. Add a second wing color on flap (hint: track a short `flap_flash` timer).

---

**Previous / Предыдущий урок:** [Block 4 index](../README.md) · [Lesson 3.3 — Polish](../../../block-3-physics-collisions-final-project/lesson-3-3-polish/README.md)

**Next / Дальше:** [Lesson 4.2 — Scrolling Gateways](../lesson-4-2-scrolling-gateways/README.md)