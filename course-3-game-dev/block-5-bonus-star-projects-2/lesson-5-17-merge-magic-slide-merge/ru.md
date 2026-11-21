# Урок 5.17: Сдвиг и слияние

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~36 min**  
> [Выбери язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 36
-->

---

## Заголовок

**Уровень ★29 — Скольжение рун**

---

## Объяснение

Главный ход — **сдвиг и слияние одной строки влево** в чистой функции `merge_row`.

Шаги для строки:

1. **`compress`** — сдвинуть ненулевые влево, дополнить `0`.
2. **Слияние** — соседи с одинаковым значением складываются; каждая пара — **не больше одного** слияния за ход.
3. Снова **`compress`**.

Другие направления — те же приёмы:

| Направление | Приём |
|-------------|-------|
| Вправо | разворот → влево → разворот |
| Вверх | транспонировать → влево → транспонировать |
| Вниз | транспонировать → разворот → влево → обратно |

**`spawn_rune()` только если доска изменилась.**

---

### Шаг 1: Открой стартер

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-17-merge-magic-slide-merge
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
merged, gained = merge_row(board[row])
```

---

## Запуск кода

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-17-merge-magic-slide-merge
python solution\game.py
```

**Expected output (visual):** Runnable Merge Magic milestone for lesson 5.17.

---

## Быстрые упражнения

1. `print(merge_row([2, 2, 4, 4]))` — какая строка и счёт?
2. Проверь move_up на столбце двоек.
3. Загляни в [solution/game.py](solution/game.py) за transpose.


---

## Задание для практики

**Quest name:** Одна строка влево

1. Доделай TODO в [starter/game.py](starter/game.py).
2. Самопроверка: окно соответствует цели урока?
3. **Бонус:** добавь подпись HUD со счётом или подсказкой.

**Самопроверка:** Окно ~5 с без ошибок? ✓

**Эталон:** [solution/game.py](solution/game.py)

---

## Уголок отладки

**Проблема:** Счёт растёт слишком быстро

**Причина:** Очки добавляются вне merge_row.

**Исправление:** Возвращайте gained из merge_row и добавляйте один раз за ход.


---

## Проверь себя

1. `merge_row` сливает пару…
   - **a)** Не больше одного раза за ход
   - **b)** Бесконечно
   - **c)** Только по диагонали
   - **d)** Никогда

2. Вправо = влево через…
   - **a)** Разворот строки
   - **b)** Flask
   - **c)** Удаление сетки
   - **d)** Turtle

3. Появление руны после стрелки когда…
   - **a)** Доска изменилась
   - **b)** Каждый кадр
   - **c)** Никогда
   - **d)** Счёт 0

4. `transpose` меняет…
   - **a)** Строки и столбцы
   - **b)** RGB и HSL
   - **c)** pip и venv
   - **d)** Кнопки мыши

5. Урок 5.18 добавит…
   - **a)** Победа 2048, undo, game over
   - **b)** Только установку Python
   - **c)** Списки Course 1
   - **d)** Без счёта

---

<details><summary>Показать ответы</summary>


1. **a)** Не больше одного раза за ход.


2. **a)** Разворот строки.


3. **a)** Доска изменилась.


4. **a)** Строки и столбцы.


5. **a)** Победа 2048, undo, game over.


</details>



## Что дальше

→ [Урок 5.18 — Merge Magic целиком](../lesson-5-18-merge-magic-complete/README.md)

---

*Куй яркие руны.*

[Выбери язык](README.md)
