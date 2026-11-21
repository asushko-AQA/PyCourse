# Урок 5.12: Сетка кристаллов и клики

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~32 min**  
> [Выбери язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 32
-->

---

## Title

**Уровень ★24 — Кристаллическая решётка**

---

## Объяснение

★ проект **№4** в Блоке 5 — **Mine Whisper**: спокойная головоломка в **кристаллической пещере** (только фигуры и цифры).

Поле — **двумерный список** (`grid`) из **словарей клеток**:

```python
grid[row][col] = {"revealed": False, "peek": False}
```

- **`col`** — столбец, **`row`** — строка.
- `mouse_to_cell(event.pos)` переводит пиксели в `(col, row)` через `BOARD_X`, `BOARD_Y`, `CELL`.

**Отрисовка:** скрытый кристалл — фиолетовая плитка; **peek** подсвечивает клетку под курсором.

---

### Шаг 1: Открой стартер

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-12-mine-whisper-crystal-grid
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Purple crystal board; finish TODOs for this lesson's goal.

---

### Step 2: Compare the solution

Study [solution/game.py](solution/game.py) for the full pattern.

---

## Пример кода

**File: [solution/game.py](solution/game.py)**:

```python
col = (mx - BOARD_X) // CELL
row = (my - BOARD_Y) // CELL
```

---

## Запуск кода

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-12-mine-whisper-crystal-grid
python solution\game.py
```

**Expected output (visual):** Runnable Mine Whisper milestone for lesson 5.12.

---

## Быстрые упражнения

1. Print the picked `(col, row)` each click.
2. Change `CELL` — does the board still align with clicks?
3. Skim [solution/game.py](solution/game.py) for whisper colors.

---

## Задание для практики

**Quest name:** Карта кликов по кристаллам

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: does the window match this lesson's goal?
3. **Bonus stretch:** add a tiny HUD label with grid size.

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Уголок отладки

**Problem:** HUD всегда (0, 0)

**Cause:** Не сохранили `picked`.

**Fix:** Присвой `picked = mouse_to_cell(event.pos)`.


---

## Проверь себя

1. `grid[row][col]` — это…
   - **a)** Сначала строка, потом столбец
   - **b)** Только Flask
   - **c)** Пути к файлам
   - **d)** Turtle

2. `mouse_to_cell` вернёт None, если…
   - **a)** Клик вне поля
   - **b)** Счёт ноль
   - **c)** Нет pygame
   - **d)** Всегда

3. В 5.12 в dict клетки…
   - **a)** Флаги revealed/peek
   - **b)** HTTP cookies
   - **c)** SQL
   - **d)** Только звук

4. BOARD_X и CELL нужны, чтобы…
   - **a)** Пиксели → координаты сетки
   - **b)** pip install
   - **c)** Docker
   - **d)** Печать quiz

5. В 5.13 добавим…
   - **a)** Случайные шахты и соседи
   - **b)** Только Turtle
   - **c)** Удаление списков
   - **d)** Flask

---

<details><summary>Нажми, чтобы увидеть ответы</summary>


1. **a)** Сначала строка, потом столбец.

2. **a)** Клик вне поля.

3. **a)** Флаги revealed/peek.

4. **a)** Пиксели → координаты сетки.

5. **a)** Случайные шахты и соседи.


</details>



## Что дальше

→ [Урок 5.13 — Шахты и соседние числа](../lesson-5-13-mine-whisper-mines-numbers/README.md)

---

*Listen to the crystals.*

[Выбери язык](README.md)
