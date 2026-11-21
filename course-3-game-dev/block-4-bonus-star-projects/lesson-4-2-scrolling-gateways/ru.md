# Урок 4.2: Прокручивающиеся врата

> **Курс:** Разработка игр на Python · **Блок:** Бонус ★ Проекты · **~35–40 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 38
-->

---

## Title

**Уровень ★2 — Скользящий через врата**

---

## Explanation

Пора сделать Sky Hopper **настоящим вызовом**. Каждые **ворота** — два зелёных прямоугольника и **проход** посередине — как в классических flap-играх, но **своя графика**.

| Часть | Идея |
|-------|------|
| Список труб | `pipes.append({"x", "gap_y", "scored"})` |
| Прокрутка | `pipe["x"] -= int(SCROLL * dt)` |
| Счёт | Если `pipe["x"] + PIPE_W < bird.left` и не `scored` → `score += 1` |
| Удар | `colliderect` с верхом/низом или вылет за экран |

`gap_y` — **центр прохода**, случайный для разнообразия.

---

### Step 1: `spawn_pipe()`

```python
def spawn_pipe() -> None:
    gap_y = random.randint(GAP // 2 + 40, HEIGHT - GAP // 2 - 40)
    pipes.append({"x": WIDTH + PIPE_W, "gap_y": gap_y, "scored": False})
```

Вызови один раз до цикла и снова, когда последняя труба далеко слева.

---

### Step 2: Прокрутка и очистка

```python
for pipe in pipes:
    pipe["x"] -= int(SCROLL * dt)
pipes = [p for p in pipes if p["x"] > -PIPE_W]
if not pipes or pipes[-1]["x"] < WIDTH - PIPE_SPACING:
    spawn_pipe()
```

---

### Step 3: Столкновения и счёт

`pipe_rects(pipe)` даёт верх/низ. Удар → `crashed = True`.  
Проход → `scored = True`, чтобы не считать дважды.

---

### Step 4: Запуск

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-2-scrolling-gateways
python starter\game.py
```

**Ожидаемый результат:** Врата едут влево; счёт растёт; при ударе — «Press R».

---

## Code Example

```python
for pipe in pipes:
    top, bottom = pipe_rects(pipe)
    if bird.colliderect(top) or bird.colliderect(bottom):
        crashed = True
    if not pipe["scored"] and pipe["x"] + PIPE_W < bird.left:
        pipe["scored"] = True
        score += 1
```

---

## Code Execution

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-2-scrolling-gateways
python starter\game.py
```

**Ожидаемый результат:** Играбельный заезд со счётом и сбросом.

---

## Quick Drills

1. Шире проход — `GAP = 190`.
2. Реже трубы — больше `PIPE_SPACING`.
3. Звезда на кадр, когда `scored` стало True.

---

## Practice Task

**Квест:** Скользящий через врата

1. Закрой TODO в [starter/game.py](starter/game.py).
2. Набери **3+** очка за жизнь.
3. **Бонус:** фиолетовые ворота каждые 5 очков.

**Самопроверка:** Плавная прокрутка? Счёт +1 за ворота? Crash останавливает физику? ✓

**Эталон:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Проблема:** Счёт прыгает на 10 за ворота.

**Причина:** Нет флага `scored`.

**Fix:** `pipe["scored"] = True` при первом проходе.

---

## Quick Check

1. `gap_y` — это…
   - **a)** Центр безопасного прохода по Y
   - **b)** Имя PNG птицы
   - **c)** Секрет Flask
   - **d)** Цвет пера Turtle

2. Прокрутка…
   - **a)** `pipe["x"] -= int(SCROLL * dt)`
   - **b)** только `sleep`
   - **c)** `pip install flask`
   - **d)** удаление pygame

3. Когда растёт `score`?
   - **a)** Каждый кадр
   - **b)** Один раз за проход ворот
   - **c)** Только при QUIT
   - **d)** Никогда

4. `colliderect` проверяет…
   - **a)** Птицу и прямоугольники труб
   - **b)** Почту и пароль
   - **c)** Два URL
   - **d)** Заголовки markdown

5. Урок 4.3 добавит…
   - **a)** Экраны старт/game over + рекорд и рамп
   - **b)** Django ORM
   - **c)** Удаление pygame
   - **d)** Только циклы Курса 1

---

<details><summary>Нажми, чтобы показать ответы</summary>

1. **a)** Центр прохода.
2. **a)** Движение влево с dt.
3. **b)** Раз за ворота.
4. **a)** Столкновения.
5. **a)** Полный цикл игры.

</details>

---

## What's Next

→ [Урок 4.3 — Sky Hopper целиком](../lesson-4-3-sky-hopper-complete/README.md) — титул, game over, рекорд!

[← Выбрать язык](README.md)