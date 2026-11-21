# Урок 5.5: Ракетка и жизни

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~35 min**  
> [Choose language](README.md) · **[English →](en.md)**

<!-- meta
homework: starter/game.py
minutes: 35
-->

---

## Title

**Уровень ★17 — Ракетка-наковальня**

---

## Объяснение

Когда шар падает на ракетку:

```python
hit_frac = (ball_x - paddle.centerx) / (paddle.width / 2)
ball_vx = hit_frac * speed * 0.9
ball_vy = -max(200, speed * 0.85)
```

Если шар ушёл ниже окна — минус жизнь и сброс в центр.

- Ракетка `pygame.Rect`; A/D или стрелки + `dt`
- `hit_frac` от -1 (левый край) до 1 (правый)
- Больше `ball_vx` при ударе по краю ракетки
- Счётчик `lives`; новый подача после промаха

---

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-5-bounce-forge-paddle-lives
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
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-5-bounce-forge-paddle-lives
python solution\game.py
```

**Expected output (visual):** Runnable Bounce Forge milestone for lesson 5.5.

---

## Quick Drills

1. Slow `ball_vx` to half — still bounces?
2. Log `hit_frac` when the paddle strikes.
3. Count bricks left on the HUD.

---

## Задание для практики

**Quest name:** Ракетка-наковальня

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

1. `hit_frac` около +1 — удар…
   - **a)** По правой части ракетки
   - **b)** Только по верхней стене
   - **c)** По углу кирпича
   - **d)** По клетке еды

2. Ракетку двигать через…
   - **a)** Только один KEYDOWN
   - **b)** `get_pressed()` + `dt` каждый кадр
   - **c)** Turtle.forward
   - **d)** Flask POST

3. `lives` уменьшается, когда…
   - **a)** Счёт 100
   - **b)** SPACE на титле
   - **c)** Шар ниже ракетки
   - **d)** pygame.QUIT

4. После промаха обычно…
   - **a)** Центр шара и подача вверх
   - **b)** Сразу pygame.quit
   - **c)** Удалить кирпичи
   - **d)** Вырастить хвост

5. Урок 5.6 добавит…
   - **a)** Список кирпичей, сторона, счёт
   - **b)** Шаблоны HTML
   - **c)** Урок venv
   - **d)** Только звуки

---

<details><summary>Click to reveal answers</summary>

1. **a)** Правый край → vx вправо.
2. **b)** Опрос клавиш каждый кадр.
3. **c)** Промах = минус жизнь.
4. **a)** Как в Breakout.
5. **a)** Дальше — кирпичи.
</details>


## Что дальше

→ [Урок 5.6 — Кирпичи и счёт](../lesson-5-6-bounce-forge-bricks-score/README.md)

---

*Искры в кузнице.*

[← Choose language](README.md)
