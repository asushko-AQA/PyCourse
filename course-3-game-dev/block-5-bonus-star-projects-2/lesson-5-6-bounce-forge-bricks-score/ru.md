# Урок 5.6: Кирпичи и счёт

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~36 min**  
> [Choose language](README.md) · **[English →](en.md)**

<!-- meta
homework: starter/game.py
minutes: 36
-->

---

## Title

**Уровень ★18 — Угольные кирпичи**

---

## Объяснение

Цикл по `bricks[:]`, столкновение, сравни с прошлой позицией — бок или верх, затем удали кирпич.

- Ряды из строк (`"1110101"`)
- Сохраняй `prev_ball_x/y` перед движением
- Меняй `vx` с боков; `vy` сверху/снизу
- `score += 10` за кирпич

---

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-6-bounce-forge-bricks-score
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
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-6-bounce-forge-bricks-score
python solution\game.py
```

**Expected output (visual):** Runnable Bounce Forge milestone for lesson 5.6.

---

## Quick Drills

1. Slow `ball_vx` to half — still bounces?
2. Log `hit_frac` when the paddle strikes.
3. Count bricks left on the HUD.

---

## Задание для практики

**Quest name:** Угольные кирпичи

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

1. Кирпичи хранятся как…
   - **a)** Список `pygame.Rect`
   - **b)** Таблица маршрутов Flask
   - **c)** Перья Turtle
   - **d)** Только RGB

2. Зачем `prev_ball_x`?
   - **a)** Сторона удара (верх или бок)
   - **b)** Пути PNG
   - **c)** Заменить dt
   - **d)** HTML викторины

3. Удар сверху обычно меняет…
   - **a)** Только счёт
   - **b)** Знак `ball_vy`
   - **c)** Ширину окна
   - **d)** paddle.x

4. После удаления кирпича…
   - **a)** Break после первого за кадр
   - **b)** Удалять все
   - **c)** Не трогать vx
   - **d)** Без счёта

5. Урок 5.7 добавит…
   - **a)** Полная игра: уровни, состояния, рекорд
   - **b)** Блок 0
   - **c)** django
   - **d)** Одна стена

---

<details><summary>Click to reveal answers</summary>

1. **a)** Rect для рисования и столкновений.
2. **a)** Нужен прошлый кадр.
3. **b)** Вертикальный отскок.
4. **c)** Один кирпич за кадр.
5. **a)** Цельный Bounce Forge.
</details>


## Что дальше

→ [Урок 5.7 — Bounce Forge целиком](../lesson-5-7-bounce-forge-complete/README.md)

---

*Искры в кузнице.*

[← Choose language](README.md)
