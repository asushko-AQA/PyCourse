# Урок 5.18: Merge Magic целиком

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~40 min**  
> [Выбери язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 40
-->

---

## Заголовок

**Уровень ★30 — Merge Magic Pro**

---

## Объяснение

Доведи кузницу до полного цикла:

| Фаза | `state` | Действие |
|-------|---------|----------|
| Заголовок | `START` | **SPACE** — старт |
| Игра | `PLAYING` / `WON` | стрелки; **U** — один undo |
| Победа | `WON` | плитка **2048** — **C** продолжить или **SPACE** заново |
| Конец | `OVER` | нет ходов — **SPACE** рестарт |

**`best_score`** — лучший счёт за сессию.

Перед успешным ходом сохраняй **`undo_snapshot`** (копия доски + счёт) — только **один** шаг назад.

---

### Шаг 1: Открой стартер

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-18-merge-magic-complete
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
if not can_move(board): state = OVER
```

---

## Запуск кода

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-18-merge-magic-complete
python solution\game.py
```

**Expected output (visual):** Runnable Merge Magic milestone for lesson 5.18.

---

## Быстрые упражнения

1. Принудительно `state = OVER` и проверь SPACE.
2. Достигни 2048 — работает ли **C**?
3. Загляни в [solution/game.py](solution/game.py) за undo_snapshot.


---

## Задание для практики

**Quest name:** Merge Magic Pro

1. Доделай TODO в [starter/game.py](starter/game.py).
2. Самопроверка: окно соответствует цели урока?
3. **Бонус:** добавь подпись HUD со счётом или подсказкой.

**Самопроверка:** Окно ~5 с без ошибок? ✓

**Эталон:** [solution/game.py](solution/game.py)

---

## Уголок отладки

**Проблема:** Undo не работает

**Причина:** Снимок не сохраняется перед ходом.

**Исправление:** Сохраняйте undo_snapshot при changed is True.


---

## Проверь себя

1. `best_score` хранит…
   - **a)** Лучший счёт сессии
   - **b)** Кэш pip
   - **c)** Только блок 1
   - **d)** Ничего

2. Game over когда…
   - **a)** Нет хода, меняющего доску
   - **b)** Счёт 0
   - **c)** Окно закрыто
   - **d)** Flask

3. Победа 2048 — **C**…
   - **a)** Продолжить после баннера
   - **b)** Удалить доску
   - **c)** Выйти из pygame
   - **d)** Браузер

4. `undo_snapshot` даёт…
   - **a)** Один шаг назад
   - **b)** Бесконечную историю
   - **c)** Только мины
   - **d)** Course 2

5. Следующая ★ игра…
   - **a)** Twin Cards (скоро)
   - **b)** Только Course 2
   - **c)** Эссе блок 0
   - **d)** Без pygame

---

<details><summary>Показать ответы</summary>


1. **a)** Лучший счёт сессии.


2. **a)** Нет хода, меняющего доску.


3. **a)** Продолжить после баннера.


4. **a)** Один шаг назад.


5. **a)** Twin Cards (скоро).


</details>



## Что дальше

→ [Блок 5 — Twin Cards (скоро)](../README.md)

---

*Куй яркие руны.*

[Выбери язык](README.md)
