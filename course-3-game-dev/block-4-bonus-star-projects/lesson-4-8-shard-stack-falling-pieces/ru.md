# Урок 4.8: Падающие осколки и управление

> **Курс:** Разработка игр на Python · **Блок:** Бонус ★ Проекты · **~35–40 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 36
-->

---

## Title

**Уровень ★8 — Падающий осколок**

---

## Explanation

В 4.7 поле было статичным. Теперь **осколок падает**.

| Часть | Идея |
|-------|------|
| Якорь | `piece_row`, `piece_col` |
| Форма | список `PIECE_OFFSETS` |
| Таймер | `fall_timer += dt`; каждые `FALL_INTERVAL` — шаг вниз |
| Клавиши | стрелки в `KEYDOWN` |

```python
def can_move(dr, dc):
    for pr, pc in PIECE_OFFSETS:
        r = piece_row + pr + dr
        c = piece_col + pc + dc
        if c < 0 or c >= COLS or r >= ROWS:
            return False
        if r >= 0 and grid[r][c]:
            return False
    return True
```

Если вниз нельзя → **`lock_piece()`** пишет цвет в `grid` и спавнит сверху.

---

### Step 1: `try_move`

```python
if can_move(dr, dc):
    piece_row += dr
    piece_col += dc
    return True
return False
```

---

### Step 2: Таймер

```python
fall_timer += dt
if fall_timer >= FALL_INTERVAL:
    fall_timer = 0.0
    if not try_move(1, 0):
        lock_piece()
```

---

### Step 3: Мягкий сброс

`K_DOWN` — сразу `try_move(1, 0)` или `lock_piece()`.

---

### Step 4: Запуск

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-8-shard-stack-falling-pieces
python starter\game.py
```

**Ожидаемый вывод (визуально):** T падает, двигается, фиксируется внизу.

---

## Code Example

**Файл: [solution/game.py](solution/game.py)**

```python
if not try_move(1, 0):
    lock_piece()
```

---

## Code Execution

```text
python solution\game.py
```

**Ожидаемый вывод (визуально):** Стопка осколков на дне.

---

## Quick Drills

1. Почему `KEYDOWN`, а не `get_pressed`, для одного шага вниз?
2. Закрой столбец 0 — можно ли уйти вправо?
3. Логируй `can_move(1, 0)` над башней.

---

## Practice Task

**Квест:** Падающий осколок

1. Все TODO в [starter/game.py](starter/game.py).
2. Осколок не вылезает за стены.
3. **Бонус:** вспышка при `lock_piece`.

**Самопроверка:** Падение без удержания клавиш? ✓

**Эталон:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Проблема:** Проваливается сквозь пол.

**Причина:** Нет `lock_piece()` или `r >= ROWS` не блокирует.

**Решение:** `r >= ROWS` = нельзя; при неудаче вниз — lock.

---

## Quick Check

1. `FALL_INTERVAL` — это…
   - **a)** Секунды между авто-шагами вниз
   - **b)** Порт Flask
   - **c)** Размер спрайта
   - **d)** XP квиза

2. `can_move(0, -1)` проверяет…
   - **a)** Все клетки осколка для хода влево
   - **b)** Email
   - **c)** Только якорь
   - **d)** pip install

3. Если вниз нельзя…
   - **a)** `lock_piece()` и респawn
   - **b)** Удалить grid
   - **c)** `pygame.quit()`
   - **d)** Игнорировать

4. Зафиксированные клетки в…
   - **a)** 2D `grid`
   - **b)** Только PNG
   - **c)** Jinja
   - **d)** Turtle

5. Урок 4.9 добавит…
   - **a)** Поворот, линии, счёт, состояния
   - **b)** Только CSS Flask
   - **c)** Удаление сетки
   - **d)** Маджонг

---

<details><summary>Нажми, чтобы показать ответы</summary>

1. **a)** Ритм падения.
2. **a)** Все смещения.
3. **a)** Зафиксировать и заново.
4. **a)** Память сетки.
5. **a)** Полный Shard Stack.

</details>

---

## What's Next

→ [Урок 4.9 — Shard Stack целиком](../lesson-4-9-shard-stack-complete/README.md)!

---

*Падай ровно, двигайся точно.*

[← Выбрать язык](README.md)