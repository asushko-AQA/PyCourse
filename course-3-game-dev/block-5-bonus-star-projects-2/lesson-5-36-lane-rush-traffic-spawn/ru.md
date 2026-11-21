# Урок 5.36: Поток машин и дистанция

> **Курс:** Разработка игр на Python · **Блок:** Бонус ★ проекты II · **~36 мин**  
> [Выбор языка](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 36
-->

---

## Title

**Уровень ★48 — Поток машин**

---

## Explanation

**Lane Rush** — ★ проект **№10** — **уклонение сверху** на прокручивающейся дороге.

В этом уроке: **спавн машин по таймеру в случайных полосах, движение вниз, столкновение `colliderect` завершает заезд, счёт дистанции.**

### Step 1: Старт

```text
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

---

## Code Example

```python
if pr.colliderect(tr):
    game_over = True
```

---

## Code Execution

```text
python solution\game.py
```

**Mac/Linux:** `python solution/game.py`

**Ожидаемый результат (визуально):** Поток машин, столкновение, `R` — рестарт.

---

## Practice Task

**Квест:** Поток машин

1. TODO в [starter/game.py](starter/game.py).
2. Самопроверка: увернулся хотя бы от одной машины?

**Эталон:** [solution/game.py](solution/game.py)

---

## Quick Check

1. Полоса спавна…
   - **a)** `rng.randint(0, NUM_LANES - 1)`
   - **b)** Только мышь
   - **c)** Flask
   - **d)** Turtle
2. Машины едут…
   - **a)** Вниз с `TRAFFIC_SPEED * dt`
   - **b)** Только в меню
   - **c)** Никогда
   - **d)** В JSON
3. Столкновение…
   - **a)** `Rect.colliderect`
   - **b)** `pip list`
   - **c)** SQL
   - **d)** HTML
4. Дистанция растёт…
   - **a)** От скорости прокрутки
   - **b)** От заголовка окна
   - **c)** От git push
   - **d)** От мин
5. Дальше…
   - **a)** Топливо, монеты, near-miss, лучший заезд, финал Блока 5
   - **b)** Деплой Course 2
   - **c)** Shard Stack
   - **d)** Block 0

---

<details><summary>Показать ответы</summary>

1. **a)** `rng.randint(0, NUM_LANES - 1)`
2. **a)** Вниз с `TRAFFIC_SPEED * dt`
3. **a)** `Rect.colliderect`
4. **a)** От скорости прокрутки
5. **a)** Топливо, монеты, near-miss, лучший заезд, финал Блока 5

</details>

## What's Next

→ [Урок 5.37 — Lane Rush целиком](../lesson-5-37-lane-rush-complete/README.md)

[Выбор языка](README.md)