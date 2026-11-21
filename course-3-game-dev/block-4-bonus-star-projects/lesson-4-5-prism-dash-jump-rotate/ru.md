# Урок 4.5: Прыжок, гравитация и вращение

> **Курс:** Разработка игр на Python · **Блок:** Бонус ★ Проекты · **~35–40 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 38
-->

---

## Title

**Уровень ★5 — Вращение в воздухе**

---

## Explanation

Авто-бегун скучнеет без **прыжка**. В Prism Dash та же вертикальная физика, что в Sky Hopper — но прыгаешь только когда **на земле**.

| Часть | Идея в коде |
|-------|-------------|
| Гравитация | `vel_y += GRAVITY * dt` |
| Прыжок | `KEYDOWN` SPACE + `grounded` → `vel_y = JUMP_V` |
| Приземление | Прилипни: `player_y` к `GROUND_Y` (или к верху платформы в 4.6) |
| Вращение | `angle += ROT_SPEED * dt`, пока **не** на земле |

Нарисуй куб на маленьком `Surface`, поверни через `pygame.transform.rotate`, затем `blit` по центру — это «геометрический» вид без картинок.

---

### Step 1: Условие прыжка

```python
if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and grounded:
    vel_y = JUMP_V
    grounded = False
```

---

### Step 2: Гравитация + движение

```python
vel_y += GRAVITY * dt
player_y += vel_y * dt
```

---

### Step 3: Прилипание к земле

```python
def snap_ground() -> None:
    global player_y, vel_y, grounded
    grounded = False
    if player_y + CUBE_SIZE >= GROUND_Y - 1:
        player_y = GROUND_Y - CUBE_SIZE
        vel_y = 0
        grounded = True
```

---

### Step 4: Вращение в воздухе

```python
if grounded:
    angle = 0.0
else:
    angle = (angle + ROT_SPEED * dt) % 360
```

---

### Step 5: Запуск

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-5-prism-dash-jump-rotate
python starter\game.py
```

**Ожидаемый результат (визуально):** Неоновый куб прыгает по прокручивающейся земле; крутится в воздухе; SPACE в полёте ничего не делает.

---

## Code Example

```python
tile = pygame.Surface((CUBE_SIZE, CUBE_SIZE), pygame.SRCALPHA)
pygame.draw.rect(tile, (255, 110, 210), tile.get_rect(), border_radius=6)
rotated = pygame.transform.rotate(tile, -angle)
surface.blit(rotated, rotated.get_rect(center=(PLAYER_X, center_y)))
```

---

## Code Execution

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-5-prism-dash-jump-rotate
python starter\game.py
```

**Ожидаемый результат (визуально):** Демо прыжка и вращения; HUD показывает на земле / в воздухе.

---

## Quick Drills

1. **Лунный прыжок** — `GRAVITY = 800`, `JUMP_V = -650`.
2. **Без двойного прыжка** — убедись, что SPACE в воздухе ничего не делает.
3. **Сброс на 0°** — на земле только `angle = 0` (не диагональ).

---

## Practice Task

**Название квеста:** Вращение в воздухе

1. Закрой все TODO в [starter/game.py](starter/game.py).
2. Куб вращается только в воздухе.
3. **Бонус:** короткая белая вспышка при прыжке.

**Самопроверка:** Один прыжок на одно приземление? Ноги «встают» на землю без проваливания? ✓

**Эталон:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Проблема:** Бесконечные прыжки в воздухе.

**Причина:** Нет `and grounded` на SPACE или `grounded` никогда не становится `False`.

**Fix:** Сразу при прыжке ставь `grounded = False`; `True` — только в snap.

---

## Quick Check

1. Прыжок должен срабатывать, когда…
   - **a)** SPACE на `KEYDOWN` и `grounded`
   - **b)** SPACE удерживается каждый кадр в воздухе
   - **c)** Только ПКМ мыши
   - **d)** Только на экране game over

2. `JUMP_V = -520` значит…
   - **a)** Сильный импульс вверх (минус = вверх)
   - **b)** Скорость прокрутки
   - **c)** Урон от шипа
   - **d)** Размер шрифта

3. Прилипание к земле задаёт…
   - **a)** `player_y = GROUND_Y - CUBE_SIZE`
   - **b)** `world_x = 0` всегда
   - **c)** `pipes.clear()`
   - **d)** Режим отладки Flask

4. Вращение в воздухе использует…
   - **a)** `pygame.transform.rotate`
   - **b)** Только `pip install`
   - **c)** `render_template`
   - **d)** Turtle `forward`

5. В уроке 4.5 Prism Dash пока…
   - **a)** Нет смертельных шипов (они в 4.6)
   - **b)** Полная сетка «Тетриса»
   - **c)** Сетевой мультиплеер
   - **d)** Нет прокрутки

---

<details><summary>Нажми, чтобы показать ответы</summary>

1. **a)** Прыжок только с земли.
2. **a)** Та же конвенция знаков, что в Sky Hopper.
3. **a)** Ноги совпадают с полом.
4. **a)** Крутишь поверхность куба.
5. **a)** Шипы — в следующем уроке.

</details>

---

## What's Next

→ [Урок 4.6 — Prism Dash целиком](../lesson-4-6-prism-dash-complete/README.md) — шипы, полоса прогресса, попытки, полный игровой цикл!

---

*Прыгнул раз — крутанулся — приземлился чётко.*

[← Выбрать язык](README.md)