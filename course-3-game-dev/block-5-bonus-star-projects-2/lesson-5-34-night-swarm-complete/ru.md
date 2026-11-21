# Урок 5.34: Night Swarm целиком

> **Курс:** Разработка игр на Python · **Блок:** Бонус ★ Star Projects II · **~38 мин**  
> [Выбор языка](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 38
-->

---

## Title

**Уровень ★46 — Night Swarm Pro**

---

## Explanation

**Night Swarm** — ★ проект **№9** в Блоке 5 — спокойная **вид сверху** история: хранитель фонаря отгоняет **тени** **сферами света** (только фигуры, без жёсткой графики).

В этом уроке: **волны сложнее со временем, цель выжить 3 минуты, меню/level-up/пауза/победа/поражение, лучший результат сессии.**

### Шаг 1: Открой стартер

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-34-night-swarm-complete
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
state = "MENU"
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-34-night-swarm-complete
python solution\game.py
```

**Mac/Linux:** `python solution/game.py`

**Ожидаемый результат (визуально):** Рабочий этап Night Swarm для урока 5.34.

---

## Quick Drills

1. Выведи вектор движения до `normalize()` — когда длина > 1?
2. Поменяй `PLAYER_SPEED` и почувствуй разницу при том же `dt`.
3. Назови один ключ из `UPGRADE_POOL` и что он усиливает.

---

## Practice Task

**Квест:** Night Swarm Pro

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

1. Победа в этой сборке…
   - **a)** Выжить около 180 секунд
   - **b)** Одна монета
   - **c)** Слияние до 2048
   - **d)** Только мины
2. Рост сложности может…
   - **a)** Ускорять спавн
   - **b)** Убрать всех врагов
   - **c)** Выключить dt
   - **d)** Не рисовать
3. Лучший результат хранит…
   - **a)** Максимальное время выживания
   - **b)** Только заголовок
   - **c)** Файл .env
   - **d)** Хеш git
4. Пауза через…
   - **a)** ESC в игре
   - **b)** Только ПКМ
   - **c)** POST Flask
   - **d)** pip uninstall
5. Дальше по roadmap…
   - **a)** Lane Rush — уклонение
   - **b)** Установка Курса 1
   - **c)** Деплой Django
   - **d)** Только Turtle

---

<details><summary>Показать ответы</summary>

1. **a)** Выжить около 180 секунд
2. **a)** Ускорять спавн
3. **a)** Максимальное время выживания
4. **a)** ESC в игре
5. **a)** Lane Rush — уклонение

</details>

## What's Next

→ [Урок 5.35 — Прокрутка дороги и полосы](../lesson-5-35-lane-rush-road-scroll/README.md) — старт **Lane Rush** ★ №10!

---

*Пусть фонарь горит ярко!*

[Выбор языка](README.md)
