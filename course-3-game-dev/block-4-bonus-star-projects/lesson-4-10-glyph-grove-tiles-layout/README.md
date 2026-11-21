# Lesson 4.10: Tiles & Layout

> **Course:** Game Development with Python  
> **Block:** Bonus ★ Star Projects *(optional)*  
> **Time:** ~30–35 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level ★10 — Garden Tiles |
| **[Русский →](ru.md)** | Уровень ★10 — Плитки сада |

---

## What you'll build / Что ты создашь

**EN:** **Glyph Grove** starts here — a calm **tile-matching** puzzle with **procedural glyph symbols** (no copied Mahjong art). Today you store tiles as **dicts**, place them on a **layered grid**, and draw glyphs with `font.render()`.

**RU:** **Glyph Grove** начинается здесь — головоломка на **совпадение плиток** со своими **символами**. Сегодня ты хранишь плитки в **словарях**, раскладываешь **слоями** и рисуешь знаки через `font.render()`.

## What you'll learn / Что ты узнаешь

- Tile dicts: `kind`, `row`, `col`, `layer`
- Shuffle **pairs** of glyph kinds onto fixed layout slots
- Pixel math: `BOARD_X + col * TILE_W + layer * LAYER_DX`

## Before you start / Перед стартом

- [ ] [Lesson 4.9](../lesson-4-9-shard-stack-complete/README.md) — finished ★ project #3 *(recommended)*
- [ ] [Lesson 2.3](../../../block-2-player-controls-animations/lesson-2-3-score-text-rendering/README.md) — `font.render` refresh

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | TODO: `build_tiles` + `draw_tile` |
| [solution/game.py](solution/game.py) | Layered garden layout on screen |

---

**Previous / Предыдущий урок:** [Lesson 4.9 — Shard Stack Complete](../lesson-4-9-shard-stack-complete/README.md)

**Next / Дальше:** [Lesson 4.11 — Mouse Pick & Matching](../lesson-4-11-glyph-grove-mouse-matching/README.md)