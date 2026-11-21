# Урок 5.21: Twin Cards целиком

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~35 мин**  
> [Выбери язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 35
-->

---

## Заголовок

**Уровень ★33 — Twin Cards Pro**

---

## Объяснение

**Twin Cards** — спокойная игра на память: переворачивай по две карты и ищи **космические символы**, нарисованные фигурами Pygame — без скачанных картинок.

Каждая карта — **словарь** в списке:

| Ключ | Значение |
|------|----------|
| `col`, `row` | Позиция в сетке |
| `symbol` | Id пары (0 … n−1) |
| `face_up` | Символ виден? |
| `matched` | Пара уже найдена? |

В этом уроке: **Ходы и время, 3 размера, звёзды победы, рекорд сессии, анимация.**

### Шаг 1: Открой стартер

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-21-twin-cards-complete
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Ожидаемый результат (на экране):** Сетка карт; допиши TODO под цель урока.

---

### Шаг 2: Сравни с решением

Смотри [solution/game.py](solution/game.py) для полного образца.

---

## Пример кода

**Файл: [solution/game.py](solution/game.py)**:

```python
deck = list(range(pair_count)) * 2
random.shuffle(deck)
```

---

## Запуск кода

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-21-twin-cards-complete
python solution\game.py
```

**Ожидаемый результат (на экране):** Рабочий этап Twin Cards для урока 5.21.

---

## Быстрые упражнения

1. Выведи `len(deck)` — всегда ли `cols * rows`?
2. Посчитай каждый `symbol` — ровно **два** раза?
3. Поменяй цвет в `SYMBOL_COLORS` и перезапусти.

---

## Задание для практики

**Квест:** Twin Cards Pro

1. Допиши TODO в [starter/game.py](starter/game.py).
2. Самопроверка: окно делает то, что нужно в уроке?
3. **Бонус:** строка HUD с размером сетки.

**Самопроверка:** Окно ~5 с без ошибок? ✓

**Эталон:** [solution/game.py](solution/game.py)

---

## Уголок отладки

**Проблема:** На всех картах один символ

**Причина:** В `build_deck` забыли удвоить id перед перемешиванием.

**Исправление:** `list(range(pair_count)) * 2`, затем `random.shuffle(deck)`.

---

## Проверь себя

1. Колода 4×3 — это…
   - **a)** 12 карт (6 пар)
   - **b)** Только 6 карт
   - **c)** 8 пар
   - **d)** Без shuffle

2. `random.shuffle`…
   - **a)** Перемешивает список на месте
   - **b)** Создаёт Flask
   - **c)** Удаляет pygame
   - **d)** Только строки

3. `face_up=False` — …
   - **a)** Рисуем рубашку
   - **b)** Удаляем ряд
   - **c)** Turtle
   - **d)** HTTP POST

4. Каждый `symbol` встречается…
   - **a)** Ровно два раза
   - **b)** Один раз
   - **c)** Ноль раз
   - **d)** Всегда четыре

5. Следующий урок — …
   - **a)** Переворот по клику
   - **b)** Только pip
   - **c)** Flask из курса 2
   - **d)** Удаление списков

---

<details><summary>Показать ответы</summary>

1. **a)** 12 карт (6 пар).

2. **a)** Перемешивает список на месте.

3. **a)** Рубашка карты.

4. **a)** Ровно два раза.

5. **a)** Переворот по клику (по плану блока).

</details>

## Что дальше

→ [Урок 5.22 — Сетка и ходы](../lesson-5-22-tic-tac-bot-grid-turns/README.md) — **Tic-Tac-Bot** ★ №7!

---

*Мозги и звёзды!*

[Выбери язык](README.md)
