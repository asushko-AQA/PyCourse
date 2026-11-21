# Урок 5.33: Опыт и улучшения

> **Курс:** Разработка игр на Python · **Блок:** Бонус ★ Star Projects II · **~36 мин**  
> [Выбор языка](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 36
-->

---

## Title

**Уровень ★45 — Яркий выбор**

---

## Explanation

**Night Swarm** — ★ проект **№9** в Блоке 5 — спокойная **вид сверху** история: хранитель фонаря отгоняет **тени** **сферами света** (только фигуры, без жёсткой графики).

В этом уроке: **сбор кристаллов → XP, пауза level-up, 3 случайных улучшения из словаря (клавиши 1–3).**

### Шаг 1: Открой стартер

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-33-night-swarm-level-up
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
level_choices = pick_level_up_choices(UPGRADE_POOL, 3, rng)
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-33-night-swarm-level-up
python solution\game.py
```

**Mac/Linux:** `python solution/game.py`

**Ожидаемый результат (визуально):** Рабочий этап Night Swarm для урока 5.33.

---

## Quick Drills

1. Выведи вектор движения до `normalize()` — когда длина > 1?
2. Поменяй `PLAYER_SPEED` и почувствуй разницу при том же `dt`.
3. Назови один ключ из `UPGRADE_POOL` и что он усиливает.

---

## Practice Task

**Квест:** Искра улучшения

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

1. Улучшения удобно хранить в…
   - **a)** Словаре по id
   - **b)** Одном bool
   - **c)** requirements.txt
   - **d)** Ветках git
2. Экран level-up должен…
   - **a)** Паузить бой до выбора
   - **b)** Сразу выходить
   - **c)** Не рисовать
   - **d)** Игнорировать клавиши
3. Три случайных варианта…
   - **a)** Перемешать и взять 3
   - **b)** Всегда одни и те же
   - **c)** Ноль улучшений
   - **d)** Бесконечный урон
4. Сбор кристалла…
   - **a)** Добавляет xp
   - **b)** Удаляет игрока
   - **c)** Закрывает окно
   - **d)** Запускает Flask
5. Следующий урок добавит…
   - **a)** таймер выживания и все состояния
   - **b)** Только print()
   - **c)** CSS Курса 2
   - **d)** Снежинку Turtle

---

<details><summary>Показать ответы</summary>

1. **a)** Словаре по id
2. **a)** Паузить бой до выбора
3. **a)** Перемешать и взять 3
4. **a)** Добавляет xp
5. **a)** таймер выживания и все состояния

</details>

## What's Next

→ [Урок 5.34 — Night Swarm целиком](../lesson-5-34-night-swarm-complete/README.md)

---

*Пусть фонарь горит ярко!*

[Выбор языка](README.md)
