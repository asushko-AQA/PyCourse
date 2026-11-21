# Урок 4.1: Гравитация и взмах

> **Курс:** Разработка игр на Python · **Блок:** Бонус ★ Проекты · **~30–35 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 32
-->

---

## Title

**Уровень ★1 — Птица ветра**

---

## Explanation

Добро пожаловать в **Блок 4: бонусные ★ проекты** — необязательные аркадные игры **после** основного капстоуна.  
Проект №1 — **Sky Hopper**: игра с взмахом и **своей птицей из фигур** (без чужой графики).

| Сила | Идея в коде |
|------|-------------|
| Гравитация | Каждый кадр: `vel_y += GRAVITY * dt` |
| Взмах | По `KEYDOWN` + SPACE: `vel_y = FLAP_STRENGTH` (минус = вверх) |
| Позиция | `bird_y += vel_y * dt` |

Взмах — **импульс на одно нажатие**: используй `KEYDOWN`, не `get_pressed`.

---

### Step 1: Открой starter/game.py

Птица и облака уже рисуются. Найди четыре `TODO` про взмах и гравитацию.

---

### Step 2: Взмах по SPACE

Внутри цикла событий:

```python
if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    vel_y = FLAP_STRENGTH
```

---

### Step 3: Гравитация и движение

После цикла событий, каждый кадр:

```python
vel_y += GRAVITY * dt
bird_y += vel_y * dt
```

---

### Step 4: Держи птицу на экране (тренировка)

```python
if bird_y < bird_size:
    bird_y = bird_size
    vel_y = 0
if bird_y > HEIGHT - bird_size:
    bird_y = HEIGHT - bird_size
    vel_y = 0
```

В уроке 4.2 пол будет «смертью» — сейчас мягкий **отскок**, чтобы потренироваться.

---

### Step 5: Запуск

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-1-sky-hopper-gravity-flap
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Ожидаемый результат:** Птица в голубом небе; SPACE — взмах; HUD `vel_y` обновляется.

---

## Code Example

**Файл: [solution/game.py](solution/game.py)** — ядро физики:

```python
GRAVITY = 720
FLAP_STRENGTH = -280

vel_y += GRAVITY * dt
bird_y += vel_y * dt
# clamp top/bottom ...
bird.center = (BIRD_X, int(bird_y))
```

---

## Code Execution

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-1-sky-hopper-gravity-flap
python starter\game.py
```

**Ожидаемый результат:** Плавные дуги взмаха; между нажатиями птица падает.

---

## Quick Drills

1. **Тяжёлый мир** — `GRAVITY = 1000`.
2. **Супервзмах** — `FLAP_STRENGTH = -360`.
3. **Широкая птица** — `bird_size = 36`; поправь clamp.

---

## Practice Task

**Название квеста:** Птица ветра

1. Закрой все TODO в [starter/game.py](starter/game.py).
2. Пролети от пола до потолка без застреваний.
3. **Бонус:** темнее небо, когда `vel_y` растёт (опционально).

**Самопроверка:** SPACE даёт один взмах на нажатие? Без нажатий птица падает? HUD меняет `vel_y`? ✓

**Эталон:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Проблема:** Птица улетает за экран.

**Причина:** Забыли `* dt` или неверный знак гравитации.

**Fix:** Гравитация **положительная** (вниз). Умножай скорость и позицию на `dt`.

---

## Quick Check

1. Что значит `FLAP_STRENGTH = -280`?
   - **a)** Всегда влево
   - **b)** Сильный толчок вверх по SPACE
   - **c)** Удаляет трубы
   - **d)** Загружает PNG

2. Зачем `KEYDOWN` для взмаха?
   - **a)** Одно нажатие = один взмах
   - **b)** Только для Rect
   - **c)** Чтобы убрать `dt`
   - **d)** Для Turtle

3. Гравитация каждый кадр…
   - **a)** `vel_y += GRAVITY * dt`
   - **b)** `vel_y = 0`
   - **c)** только `screen.fill()`
   - **d)** `random` для счёта

4. В Pygame больший `y` двигает птицу…
   - **a)** Вверх
   - **b)** Вниз
   - **c)** В другой файл
   - **d)** Только на Linux

5. Уроки Блока 4…
   - **a)** Обязательны до Блока 1
   - **b)** Опциональный ★ бонус после Блока 3
   - **c)** Только Flask
   - **d)** На HTML

---

<details><summary>Нажми, чтобы показать ответы</summary>

1. **b)** Отрицательная скорость = вверх.
2. **a)** Импульс на нажатие.
3. **a)** Накапливаем падение.
4. **b)** Y растёт вниз.
5. **b)** Дополнительные проекты.

</details>

---

## What's Next

→ [Урок 4.2 — Прокручивающиеся врата](../lesson-4-2-scrolling-gateways/README.md) — трубы, проход и счёт!

---

*Взмахнул — полетел — учился.*

[← Выбрать язык](README.md)