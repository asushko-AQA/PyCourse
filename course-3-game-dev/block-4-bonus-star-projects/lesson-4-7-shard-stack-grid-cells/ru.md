# Урок 4.7: Сетка и клетки

> **Курс:** Разработка игр на Python · **Блок:** Бонус ★ Проекты · **~30–35 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 32
-->

---

## Title

**Уровень ★7 — Кристальная яма**

---

## Explanation

Проект **№3** в Блоке 4 — **Shard Stack**: своя головоломка со **цветными квадратами-осколками** (оригинальное имя; без чужих плиток).

В Курсе 1 ты учил **списки** (`inventory = ["sword", "potion"]`). Игровое поле — **двумерный список**: список строк, в каждой строке — список столбцов.

```python
grid = [
    [0, 0, 0],
    [0, 0, 0],
    [1, 1, 0],
]
```

- Читаем: `grid[row][col]`
- `0` — пусто; другое значение — закреплённый осколок

`row` — **насколько низко** на экране (0 — верх).

---

### Step 1: Создай колодец

```python
COLS = 10
ROWS = 20
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
```

Внутренний цикл делает **одну строку**, внешний повторяет её **ROWS** раз.

---

### Step 2: Клетка → пиксели

```python
x = BOARD_X + col * CELL
y = BOARD_Y + row * CELL
pygame.draw.rect(surface, color, (x, y, CELL - 1, CELL - 1), border_radius=4)
```

---

### Step 3: Осколок как смещения

```python
T = [(0, 1), (1, 0), (1, 1), (1, 2)]
anchor_row, anchor_col = 2, 4
for dr, dc in T:
    draw_cell(surface, anchor_row + dr, anchor_col + dc, PURPLE)
```

---

### Step 4: Запуск

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-7-shard-stack-grid-cells
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Ожидаемый вывод (визуально):** Пустая сетка; в решении — демо-замки + фиолетовая T.

---

## Code Example

**Файл: [solution/game.py](solution/game.py)**

```python
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
```

---

## Code Execution

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-7-shard-stack-grid-cells
python solution\game.py
```

**Ожидаемый вывод (визуально):** Рамка 10×20, пример нижнего ряда, T-осколок.

---

## Quick Drills

1. `grid[19][5] = 1` — загорается только низ по центру.
2. Светло-серые линии для пустых клеток.
3. На HUD выведи `len(grid)` и `len(grid[0])`.

---

## Practice Task

**Квест:** Кристальная яма

1. Доделай TODO в [starter/game.py](starter/game.py).
2. Видно **пусто** vs **заблокировано**.
3. **Бонус:** чередуй оттенок пустых рядов.

**Самопроверка:** Везде `grid[row][col]`? ✓

**Эталон:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Проблема:** `NoneType` при `grid[row][col]`.

**Причина:** Забыли создать 2D-список.

**Решение:** Один раз при старте — list comprehension.

---

## Quick Check

1. `grid[3][7]` — это…
   - **a)** Строка 3, столбец 7
   - **b)** Шаблон Flask
   - **c)** Ширина пера Turtle
   - **d)** Путь к PNG

2. 2D-список здесь — это…
   - **a)** Список строк, в строке список столбцов
   - **b)** Только словари
   - **c)** HTML-таблица
   - **d)** Одна строка текста

3. `CELL` — это…
   - **a)** Размер клетки в пикселях
   - **b)** Импорт Flask
   - **c)** Громкость
   - **d)** Соль quiz hash

4. Смещения осколка — это…
   - **a)** Пары `(row, col)` от якоря
   - **b)** JPEG-координаты
   - **c)** Только print
   - **d)** `def main():`

5. В следующем уроке…
   - **a)** Таймер падения и стрелки
   - **b)** Формы Flask
   - **c)** Только Turtle
   - **d)** `pip uninstall pygame`

---

<details><summary>Нажми, чтобы показать ответы</summary>

1. **a)** Сначала строка, потом столбец.
2. **a)** Строки из списков столбцов.
3. **a)** Шаг сетки.
4. **a)** Список смещений.
5. **a)** Урок 4.8 — движение.

</details>

---

## What's Next

→ [Урок 4.8 — Падающие осколки](../lesson-4-8-shard-stack-falling-pieces/README.md) — таймер и `can_move`!

---

*Строки списков — башни из кода.*

[← Выбрать язык](README.md)