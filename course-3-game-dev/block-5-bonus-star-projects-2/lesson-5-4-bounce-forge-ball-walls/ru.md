# Урок 5.4: Мяч и отскоки от стен

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~32 min**  
> [Choose language](README.md) · **[English →](en.md)**

<!-- meta
homework: starter/game.py
minutes: 32
-->

---

## Title

**Уровень ★16 — Искровой шар**

---

## Объяснение

Храни `ball_x`, `ball_y`, `ball_vx`, `ball_vy`. Каждый кадр:

```python
ball_x += ball_vx * dt
ball_y += ball_vy * dt
bounce_walls()
```

В `bounce_walls()` подтяни позицию и через `abs()` направь скорость **от** стены.

- `ball_vx`, `ball_vy` как float; позиция += скорость * `dt`
- Меняй знак скорости у края окна
- Радиус `BALL_R` — отскок, когда центр в `R` пикселях от стены
- Палитра кузницы: тёмный фон + оранжевый шар

---

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-4-bounce-forge-ball-walls
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Forge window; finish TODOs to match the lesson goal.

---

### Step 2: Compare the solution

Study [solution/game.py](solution/game.py) for wall bounce, paddle angle, bricks, or full states — depending on this lesson.

---

## Code Example

**File: [solution/game.py](solution/game.py)** — key pattern from this lesson:

```python
ball_x += ball_vx * dt
ball_y += ball_vy * dt
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-4-bounce-forge-ball-walls
python solution\game.py
```

**Expected output (visual):** Runnable Bounce Forge milestone for lesson 5.4.

---

## Quick Drills

1. Slow `ball_vx` to half — still bounces?
2. Log `hit_frac` when the paddle strikes.
3. Count bricks left on the HUD.

---

## Задание для практики

**Quest name:** Искровой шар

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: does the forge window behave like the lesson goal?
3. **Bonus stretch:** extra spark particles on bounce (see 5.4 solution).

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** Ball sticks inside a brick.

**Cause:** No position nudge after flipping velocity.

**Fix:** Move ball one pixel out along the normal after bounce.

**Problem:** Paddle teleports off-screen.

**Cause:** Forgetting `paddle.clamp_ip(screen.get_rect())`.

**Fix:** Clamp after every movement step.

---

## Проверь себя

1. `ball_vx` и `ball_vy` вместе — это…
   - **a)** Двумерный вектор скорости
   - **b)** Секрет Flask
   - **c)** Толщина пера Turtle
   - **d)** Только координата y

2. Отскок от правой стены обычно…
   - **a)** Обнуляет только `ball_vy`
   - **b)** Делает `ball_vx` отрицательным (влево)
   - **c)** Удаляет pygame
   - **d)** Пропускает `dt`

3. Зачем умножать на `dt`?
   - **a)** Движение не зависит от FPS
   - **b)** Дважды ставить pygame
   - **c)** Рисовать кирпичи
   - **d)** Заменить списки

4. `BALL_R` нужен, чтобы…
   - **a)** Понять, когда круг коснулся стены
   - **b)** Хранить рекорд
   - **c)** Грузить PNG
   - **d)** Рендерить HTML

5. Урок 5.5 добавит…
   - **a)** Ракетку-наковальню, угол, жизни
   - **b)** Формы Flask
   - **c)** Снежинку Turtle
   - **d)** pip uninstall

---

<details><summary>Click to reveal answers</summary>

1. **a)** Вектор движения искры.
2. **b)** Горизонтальный отскок от края.
3. **a)** `dt` выравнивает скорость на медленных ПК.
4. **a)** Радиус для краёв окна.
5. **a)** Дальше — ракетка.
</details>


## Что дальше

→ [Урок 5.5 — Ракетка и жизни](../lesson-5-5-bounce-forge-paddle-lives/README.md)

---

*Искры в кузнице.*

[← Choose language](README.md)
