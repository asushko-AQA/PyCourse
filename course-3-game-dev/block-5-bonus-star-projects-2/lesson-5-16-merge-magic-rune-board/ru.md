# Урок 5.16: Руническая решётка и появление

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~32 min**  
> [Выбери язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 32
-->

---

## Заголовок

**Уровень ★28 — Руническая решётка**

---

## Объяснение

★ проект **№5** в Блоке 5 — **Merge Magic**: головоломка в **кузнице рун** (только фигуры и цифры).

Поле — **список списков** 4×4 с целыми числами:

```python
board[row][col] = 0  # 0 = пустая ячейка
```

- **`col`** — столбец, **`row`** — строка.
- `spawn_rune()` выбирает случайную пустую клетку и ставит **2** (90%) или **4** (10%).
- `RUNE_COLORS[value]` задаёт цвет плитки; в центре рисуем число.

---

### Шаг 1: Открой стартер

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-16-merge-magic-rune-board
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Glowing rune board; finish TODOs for this lesson's goal.

---

### Шаг 2: Сверься с решением

Изучи [solution/game.py](solution/game.py).

---

## Пример кода

**Файл: [solution/game.py](solution/game.py)**:

```python
board[r][c] = 2 if random.random() < 0.9 else 4
```

---

## Запуск кода

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-16-merge-magic-rune-board
python solution\game.py
```

**Expected output (visual):** Runnable Merge Magic milestone for lesson 5.16.

---

## Быстрые упражнения

1. Печатай `empty_cells()` после каждого spawn.
2. Поменяй цвет в `RUNE_COLORS` — плитка обновилась?
3. Загляни в [solution/game.py](solution/game.py) за темой рун.


---

## Задание для практики

**Quest name:** Сетка рун

1. Доделай TODO в [starter/game.py](starter/game.py).
2. Самопроверка: окно соответствует цели урока?
3. **Бонус:** добавь подпись HUD со счётом или подсказкой.

**Самопроверка:** Окно ~5 с без ошибок? ✓

**Эталон:** [solution/game.py](solution/game.py)

---

## Уголок отладки

**Проблема:** Все плитки одинаковые

**Причина:** Рисуете по `value`, но доска не заполняется.

**Исправление:** Вызовите `spawn_rune()` после сброса и нажмите **S** для проверки.


---

## Проверь себя

1. `board[row][col]` — это…
   - **a)** Сначала строка, потом столбец
   - **b)** Только Flask
   - **c)** Пути файлов
   - **d)** Turtle

2. `spawn_rune` нужна…
   - **a)** Хотя бы одна клетка со значением 0
   - **b)** Мина
   - **c)** HTTP
   - **d)** done()

3. Пустая клетка — значение…
   - **a)** 0
   - **b)** только 2
   - **c)** всегда 2048
   - **d)** None

4. RUNE_COLORS связывает…
   - **a)** Число → RGB
   - **b)** Счёт → Flask
   - **c)** Мышь → SQL
   - **d)** Сетка → pip

5. Урок 5.17 добавит…
   - **a)** Алгоритм merge_row
   - **b)** Только Turtle
   - **c)** Удаление pygame
   - **d)** Только Course 2

---

<details><summary>Показать ответы</summary>


1. **a)** Сначала строка, потом столбец.


2. **a)** Хотя бы одна клетка со значением 0.


3. **a)** 0.


4. **a)** Число → RGB.


5. **a)** Алгоритм merge_row.


</details>



## Что дальше

→ [Урок 5.17 — Сдвиг и слияние](../lesson-5-17-merge-magic-slide-merge/README.md)

---

*Куй яркие руны.*

[Выбери язык](README.md)
