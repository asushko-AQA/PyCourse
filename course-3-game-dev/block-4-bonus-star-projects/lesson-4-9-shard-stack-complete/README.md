# Lesson 4.9: Shard Stack Complete

> **Course:** Game Development with Python  
> **Block:** Bonus ★ Star Projects *(optional)*  
> **Time:** ~40–45 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level ★9 — Shard Stack Pro |
| **[Русский →](ru.md)** | Уровень ★9 — Shard Stack Pro |

---

## What you'll build / Что ты создашь

**EN:** Full **Shard Stack**: rotate (UP), clear full lines, score + level speed-up, **next shard** preview, start / game over / session **high score**.

**RU:** Полный **Shard Stack**: поворот (UP), очистка линий, счёт и уровень, превью **следующего осколка**, start / game over / **рекорд сессии**.

## What you'll learn / Что ты узнаешь

- `rotate_cells` — 90° with simple wall nudge
- `clear_lines()` — drop rows when every cell is full
- Game states like Lessons 2.4 and 4.3

## Before you start / Перед стартом

- [ ] [Lesson 4.8](../lesson-4-8-shard-stack-falling-pieces/README.md) — falling + `can_move` works
- [ ] [Lesson 2.4](../../../block-2-player-controls-animations/lesson-2-4-game-states/README.md) — start → play → over

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | Complete game TODOs |
| [solution/game.py](solution/game.py) | Playable Shard Stack |

## Quick drills / Быстрые упражнения

1. Triple line clear — does score multiply by `level`?
2. Add an `L` shape to `SHAPES` and give it an orange color.
3. Show session best on the title screen after game over.

---

**Previous / Предыдущий урок:** [Lesson 4.8 — Falling Pieces & Controls](../lesson-4-8-shard-stack-falling-pieces/README.md)

**Next / Дальше:** [Block 4 index](../README.md) — ★ project **#3** done! Future **4.10+** is the next bonus game.