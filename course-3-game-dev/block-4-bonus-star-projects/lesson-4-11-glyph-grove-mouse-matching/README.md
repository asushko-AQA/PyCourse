# Lesson 4.11: Mouse Pick & Matching

> **Course:** Game Development with Python  
> **Block:** Bonus ★ Star Projects *(optional)*  
> **Time:** ~35–40 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level ★11 — Pair Pick |
| **[Русский →](ru.md)** | Уровень ★11 — Выбор пары |

---

## What you'll build / Что ты создашь

**EN:** Add **mouse clicks** to Glyph Grove: pick a tile with `MOUSEBUTTONDOWN`, highlight your choice, and remove **two free tiles** with the **same glyph**.

**RU:** Добавь **мышь**: клик `MOUSEBUTTONDOWN`, выделение плитки и удаление **двух свободных** плиток **одного знака**.

## What you'll learn / Что ты узнаешь

- `pygame.MOUSEBUTTONDOWN` and `event.pos`
- `rect.collidepoint(pos)` for hit-testing
- **Free tile rule:** nothing on top + open left **or** right side

## Before you start / Перед стартом

- [ ] [Lesson 4.10](../lesson-4-10-glyph-grove-tiles-layout/README.md) — tiles draw correctly

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | TODO: mouse + `is_free` |
| [solution/game.py](solution/game.py) | Click-to-match prototype |

---

**Previous / Предыдущий урок:** [Lesson 4.10](../lesson-4-10-glyph-grove-tiles-layout/README.md)

**Next / Дальше:** [Lesson 4.12 — Glyph Grove Complete](../lesson-4-12-glyph-grove-complete/README.md)