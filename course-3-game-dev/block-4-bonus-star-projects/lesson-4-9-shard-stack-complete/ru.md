# Урок 4.9: Shard Stack целиком

> **Курс:** Разработка игр на Python · **Блок:** Бонус ★ Проекты · **~40–45 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 42
-->

---

## Title

**Уровень ★9 — Shard Stack Pro**

---

## Explanation

Есть **сетка** (4.7) и **падение** (4.8). Собираем полный цикл:

| Состояние | На экране |
|-----------|-----------|
| `start` | Титул, рекорд сессии, SPACE |
| `playing` | Падение, поворот, счёт, превью |
| `game_over` | Поле заполнено — SPACE на титул |

**Поворот 90° по часовой:**

```python
def rotate_cells(cells):
    return [(c, -r) for r, c in cells]
```

Если упёрся в стену — сдвинь `piece_col` на ±1.

**Очистка линий:**

```python
def clear_lines():
    kept = [row for row in grid if not all(row)]
    cleared = ROWS - len(kept)
    while len(kept) < ROWS:
        kept.insert(0, [0] * COLS)
    grid[:] = kept
    return cleared
```

**Счёт:** `cleared * 100 * level`. **Уровень:** каждые 10 линий; `fall_interval()` короче.

---

### Step 1: `lock_piece`

1. Цвета в `grid`
2. `clear_lines()`
3. `score`, `level`
4. `spawn_piece()` или `GAME_OVER`

---

### Step 2: Запуск

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-9-shard-stack-complete
python starter\game.py
```

**Ожидаемый вывод (визуально):** Играбельный stacker с ускорением.

---

## Code Example

```python
cleared = clear_lines()
if cleared:
    score += cleared * 100 * level
```

---

## Code Execution

```text
python solution\game.py
```

**Ожидаемый вывод (визуально):** Полный цикл + панель «Next».

---

## Quick Drills

1. Две линии сразу — скачок счёта?
2. Добавь фигуру `L` в `SHAPES`.
3. Четыре поворота → та же форма (в тетради).

---

## Practice Task

**Квест:** Shard Stack Pro

1. Все TODO в [starter/game.py](starter/game.py).
2. Очисти минимум **одну** линию.
3. **Бонус:** звук при очистке.

**Самопроверка:** UP крутит без клипа? Рекорд на титуле? ✓

**Эталон:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Проблема:** Линии исчезают, цвета сбились.

**Причина:** В grid хранятся флаги, а не RGB.

**Решение:** Те же кортежи цвета, что рисуешь на активном осколке.

---

## Quick Check

1. `rotate_cells` делает…
   - **a)** `(r,c)` → `(c,-r)` (90° по часовой)
   - **b)** Без изменений
   - **c)** Маршрут Flask
   - **d)** random

2. Полная строка — когда…
   - **a)** `all(row)` для непустых клеток
   - **b)** Только row 19
   - **c)** Счёт 0
   - **d)** Нет окна

3. Game over когда…
   - **a)** Новый осколок не `can_move` у спавна
   - **b)** WIDTH 640
   - **c)** Пропущен квиз
   - **d)** Turtle закрылась

4. `fall_interval()` с ростом уровня…
   - **a)** Уменьшается
   - **b)** Растёт вечно
   - **c)** Всегда 0
   - **d)** Отключает клавиатуру

5. Следующий ★-слот после 4.9…
   - **a)** Уроки 4.10–4.12
   - **b)** Курс 1, урок 0.1
   - **c)** Обязательный Блок 5
   - **d)** Устарело

---

<details><summary>Нажми, чтобы показать ответы</summary>

1. **a)** Поворот смещений.
2. **a)** Все клетки заняты.
3. **a)** Коллизия при спавне.
4. **a)** Ускорение.
5. **a)** Проект ★ №4.

</details>

---

## What's Next

→ [Блок 4](../README.md) — ★ проект **№3** готов!  
→ [Урок 4.10 — Плитки и раскладка](../lesson-4-10-glyph-grove-tiles-layout/README.md) — старт **Glyph Grove** (#4)!  
→ [Индекс блока 4](../README.md) — проект #3 готов!  
→ Сравни сетку с **Prism Dash**!

---

*★ Shard Stack — третий проект, готов.*

[← Выбрать язык](README.md)