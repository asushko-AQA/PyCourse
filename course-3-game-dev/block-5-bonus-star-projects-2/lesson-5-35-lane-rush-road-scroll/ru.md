# Урок 5.35: Прокрутка дороги и полосы

> **Курс:** Разработка игр на Python · **Блок:** Бонус ★ проекты II · **~34 мин**  
> [Выбор языка](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 34
-->

---

## Title

**Уровень ★47 — Неоновые полосы**

---

## Explanation

**Lane Rush** — ★ проект **№10** в Блоке 5 — **гонка-уклонение сверху**: неоновая машина внизу экрана, **дорога прокручивается**, полосы повторяются (только фигуры).

В этом уроке: **смещение полос `scroll_offset`, смена полос, плавный сдвиг влево-вправо с `dt`.**

### Step 1: Открой стартовый файл

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-35-lane-rush-road-scroll
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Ожидаемый результат (визуально):** Тёмная дорога; допиши TODO для полос и lerp.

---

### Step 2: Сравни с решением

Смотри [solution/game.py](solution/game.py).

---

## Code Example

**Файл: [solution/game.py](solution/game.py)**:

```python
scroll_offset = (scroll_offset + SCROLL_SPEED * dt) % STRIPE_H
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-35-lane-rush-road-scroll
python solution\game.py
```

**Mac/Linux:** `python solution/game.py`

**Ожидаемый результат (визуально):** Жёлтые полосы едут вниз; машина плавно меняет полосу.

---

## Quick Drills

1. Выведи `scroll_offset` — зачем `% STRIPE_H`?
2. Измени `LANE_LERP`.
3. Ширина одной полосы при `ROAD_WIDTH = 360` и `NUM_LANES = 4`?

---

## Practice Task

**Квест:** Неоновые полосы

1. Допиши TODO в [starter/game.py](starter/game.py).
2. Самопроверка: полосы двигаются, машина lerпит между полосами?
3. **Бонус:** новый цвет разделителей полос.

**Самопроверка:** Окно ~5 с без ошибок? ✓

**Эталон:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Проблема:** Полосы дёргаются

**Причина:** Нет `% STRIPE_H` после прибавления скорости.

**Исправление:** `scroll_offset = (scroll_offset + SCROLL_SPEED * dt) % STRIPE_H`

---

## Quick Check

1. Modulo для `scroll_offset` даёт…
   - **a)** Бесшовное повторение
   - **b)** Заморозку
   - **c)** Только Flask
   - **d)** Без pygame
2. Центр полосы `2`…
   - **a)** `ROAD_LEFT + lane * LANE_W + LANE_W / 2`
   - **b)** Только `HEIGHT`
   - **c)** Градусы Turtle
   - **d)** `pip install`
3. Lerp с `dt` делает смену полосы…
   - **a)** Плавной при любом FPS
   - **b)** Только телепорт
   - **c)** Удаляет топливо
   - **d)** Без клавиш
4. LEFT/RIGHT должны…
   - **a)** Менять `player_lane` от 0 до NUM_LANES-1
   - **b)** Выходить из pygame
   - **c)** Запускать Flask
   - **d)** Сливать руны
5. Следующий урок…
   - **a)** Спавн трафика и столкновения
   - **b)** Установка Course 1
   - **c)** HTML-формы
   - **d)** Сапёр

---

<details><summary>Показать ответы</summary>

1. **a)** Бесшовное повторение
2. **a)** `ROAD_LEFT + lane * LANE_W + LANE_W / 2`
3. **a)** Плавной при любом FPS
4. **a)** Менять `player_lane` от 0 до NUM_LANES-1
5. **a)** Спавн трафика и столкновения

</details>

## What's Next

→ [Урок 5.36 — Поток машин](../lesson-5-36-lane-rush-traffic-spawn/README.md)

---

*Держись полосы — или перестраивайся быстро!*

[Выбор языка](README.md)