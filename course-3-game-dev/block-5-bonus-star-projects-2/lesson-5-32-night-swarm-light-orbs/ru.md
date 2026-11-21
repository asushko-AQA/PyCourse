# Урок 5.32: Авто-сферы света

> **Курс:** Разработка игр на Python · **Блок:** Бонус ★ Star Projects II · **~36 мин**  
> [Выбор языка](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 36
-->

---

## Title

**Уровень ★44 — Страж сфер**

---

## Explanation

**Night Swarm** — ★ проект **№9** в Блоке 5 — спокойная **вид сверху** история: хранитель фонаря отгоняет **тени** **сферами света** (только фигуры, без жёсткой графики).

В этом уроке: **выбор ближайшей цели, список снарядов, HP теней, выпадение кристаллов опыта.**

### Шаг 1: Открой стартер

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-32-night-swarm-light-orbs
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
idx = nearest_enemy_index(px, py, enemies)
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-32-night-swarm-light-orbs
python solution\game.py
```

**Mac/Linux:** `python solution/game.py`

**Ожидаемый результат (визуально):** Рабочий этап Night Swarm для урока 5.32.

---

## Quick Drills

1. Выведи вектор движения до `normalize()` — когда длина > 1?
2. Поменяй `PLAYER_SPEED` и почувствуй разницу при том же `dt`.
3. Назови один ключ из `UPGRADE_POOL` и что он усиливает.

---

## Practice Task

**Квест:** Лучник сфер

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

1. Авто-атака целится в…
   - **a)** Ближайшую тень
   - **b)** Случайный угол
   - **c)** Текст HUD
   - **d)** Старую монету
2. Снаряды хранят в…
   - **a)** Списке словарей
   - **b)** Таблице SQL
   - **c)** Одном int
   - **d)** Маршруте Flask
3. Когда HP тени 0…
   - **a)** Выпадает кристалл XP
   - **b)** Кирпич
   - **c)** Конец курса
   - **d)** Удаление pygame
4. Движение сферы…
   - **a)** pos += vel * dt
   - **b)** Только Turtle
   - **c)** CSS
   - **d)** HTML формы
5. Следующий урок добавит…
   - **a)** выбор улучшений
   - **b)** Ракетку Pong
   - **c)** Слияние 2048
   - **d)** Перемешку глифов

---

<details><summary>Показать ответы</summary>

1. **a)** Ближайшую тень
2. **a)** Списке словарей
3. **a)** Выпадает кристалл XP
4. **a)** pos += vel * dt
5. **a)** выбор улучшений

</details>

## What's Next

→ [Урок 5.33 — Опыт и улучшения](../lesson-5-33-night-swarm-level-up/README.md)

---

*Пусть фонарь горит ярко!*

[Выбор языка](README.md)
