# Урок 5.30: Ходьба со светильником

> **Курс:** Разработка игр на Python · **Блок:** Бонус ★ Star Projects II · **~32 мин**  
> [Выбор языка](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 32
-->

---

## Title

**Уровень ★42 — Шаг светильника**

---

## Explanation

**Night Swarm** — ★ проект **№9** в Блоке 5 — спокойная **вид сверху** история: хранитель фонаря отгоняет **тени** **сферами света** (только фигуры, без жёсткой графики).

В этом уроке: **движение в 8 направлениях через `Vector2`, нормализация и границы арены с `dt`.**

### Шаг 1: Открой стартер

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-30-night-swarm-lantern-move
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Ожидаемый результат (визуально):** Окно сумеречной арены; доделай TODO под цель урока.

---

### Шаг 2: Сравни с решением

Посмотри [solution/game.py](solution/game.py) как эталон.

---

## Code Example

**Файл: [solution/game.py](solution/game.py)**:

```python
move = move.normalize()
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-30-night-swarm-lantern-move
python solution\game.py
```

**Mac/Linux:** `python solution/game.py`

**Ожидаемый результат (визуально):** Рабочий этап Night Swarm для урока 5.30.

---

## Quick Drills

1. Выведи вектор движения до `normalize()` — когда длина > 1?
2. Поменяй `PLAYER_SPEED` и почувствуй разницу при том же `dt`.
3. Назови один ключ из `UPGRADE_POOL` и что он усиливает.

---

## Practice Task

**Квест:** Дрейф фонаря

1. Закрой TODO в [starter/game.py](starter/game.py).
2. Самопроверка: окно соответствует цели урока?
3. **Бонус:** перекрась сетку арены.

**Самопроверка:** Окно ~5 с без ошибок? ✓

**Эталон:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Проблема:** По диагонали быстрее, чем по прямой

**Причина:** `(1,1)` без нормализации даёт длину √2.

**Исправление:** `move.normalize()`, если `move.length_squared() > 0`.

---

## Quick Check

1. `normalize()` нужен, чтобы…
   - **a)** Диагональ не была быстрее
   - **b)** Удалить pygame
   - **c)** Выключить dt
   - **d)** Загрузить PNG
2. 8 направлений собирают ввод из…
   - **a)** WASD и стрелок
   - **b)** Только мыши
   - **c)** SQL
   - **d)** pip list
3. Границы арены держат героя…
   - **a)** Внутри поля
   - **b)** Вне экрана
   - **c)** Только во Flask
   - **d)** Без цвета
4. `dt` в движении значит…
   - **a)** Скорость не зависит от FPS
   - **b)** Удалить таймер
   - **c)** Только Windows
   - **d)** Черепаха
5. Следующий урок добавит…
   - **a)** спавн теней и HP
   - **b)** Шаблоны Flask
   - **c)** Turtle из Курса 1
   - **d)** Кирпичи

---

<details><summary>Показать ответы</summary>

1. **a)** Диагональ не была быстрее
2. **a)** WASD и стрелок
3. **a)** Внутри поля
4. **a)** Скорость не зависит от FPS
5. **a)** спавн теней и HP

</details>

## What's Next

→ [Урок 5.31 — Тени и полоска HP](../lesson-5-31-night-swarm-shadow-spawns/README.md)

---

*Пусть фонарь горит ярко!*

[Выбор языка](README.md)
