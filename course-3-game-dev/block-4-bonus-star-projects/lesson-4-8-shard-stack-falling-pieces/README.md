# Lesson 4.8: Falling Pieces & Controls

> **Course:** Game Development with Python  
> **Block:** Bonus ★ Star Projects *(optional)*  
> **Time:** ~35–40 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level ★8 — Drift Shard |
| **[Русский →](ru.md)** | Уровень ★8 — Падающий осколок |

---

## What you'll build / Что ты создашь

**EN:** One **T-shaped shard** falls on a **timer**. Arrow keys move left/right; DOWN nudges faster. **`can_move`**, **`lock_piece`**, and soft collision with the grid.

**RU:** Один **Т-образный осколок** падает по **таймеру**. Стрелки двигают влево/вправо; DOWN ускоряет. Функции **`can_move`**, **`lock_piece`**, столкновения с сеткой.

## What you'll learn / Что ты узнаешь

- Piece = list of `(row, col)` offsets + anchor `piece_row`, `piece_col`
- `fall_timer += dt` then `try_move(1, 0)` or `lock_piece()`
- Bounds + “locked cell” checks inside `can_move`

## Before you start / Перед стартом

- [ ] [Lesson 4.7](../lesson-4-7-shard-stack-grid-cells/README.md) — grid draws correctly
- [ ] [Lesson 2.1](../../../block-2-player-controls-animations/lesson-2-1-keyboard-events/README.md) — `KEYDOWN` vs `get_pressed`

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | Movement + fall TODOs |
| [solution/game.py](solution/game.py) | Falling T shard with lock |

## Quick drills / Быстрые упражнения

1. `FALL_INTERVAL = 0.25` — panic mode.
2. Wall kick left: print when `piece_col` hits `0`.
3. After lock, tint locked cells slightly darker.

---

**Previous / Предыдущий урок:** [Lesson 4.7 — Grid & Cells](../lesson-4-7-shard-stack-grid-cells/README.md)

**Next / Дальше:** [Lesson 4.9 — Shard Stack Complete](../lesson-4-9-shard-stack-complete/README.md)