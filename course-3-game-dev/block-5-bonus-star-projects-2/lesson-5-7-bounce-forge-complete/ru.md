# Урок 5.7: Bounce Forge целиком

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~40 min**  
> [Choose language](README.md) · **[English →](en.md)**

<!-- meta
homework: starter/game.py
minutes: 40
-->

---

## Title

**Уровень ★19 — Bounce Forge Pro**

---

## Объяснение

Соедини 5.4–5.6. После уровня — следующий или `WIN`. Скорость от уровня и счёта. Титл: SPACE — Breakout, P — Pong.

- `LEVEL_PATTERNS` — строки рядов
- `state` как в Glow Worm 5.3
- `high_score` в Breakout
- `P` — Pong: две ракетки, до 5 очков

---

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-7-bounce-forge-complete
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
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-7-bounce-forge-complete
python solution\game.py
```

**Expected output (visual):** Runnable Bounce Forge milestone for lesson 5.7.

---

## Quick Drills

1. Slow `ball_vx` to half — still bounces?
2. Log `hit_frac` when the paddle strikes.
3. Count bricks left on the HUD.

---

## Задание для практики

**Quest name:** Bounce Forge Pro

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

1. `LEVEL_PATTERNS` хранит…
   - **a)** Строки 0/1 для рядов кирпичей
   - **b)** Имена PNG
   - **c)** URL Flask
   - **d)** Только углы Turtle

2. `high_score` обновляют, когда…
   - **a)** Каждый pygame.init
   - **b)** Текущий счёт выше
   - **c)** Только при WIN
   - **d)** Никогда

3. Pong на двоих:…
   - **a)** Две ракетки; Q/E для верхней
   - **b)** Только мышь
   - **c)** Без шара
   - **d)** HTTP GET

4. Все уровни пройдены —…
   - **a)** Всегда GAME_OVER
   - **b)** Flask debug
   - **c)** state = WIN
   - **d)** score = 0

5. Следующий ★ проект —…
   - **a)** Orbit Guard (скоро)
   - **b)** Калькулятор курса 2
   - **c)** Блок 0
   - **d)** Удалить pygame

---

<details><summary>Click to reveal answers</summary>

1. **a)** ASCII-карты кирпичей.
2. **b)** Лучший за сессию.
3. **a)** Вторая ракетка по P.
4. **c)** Экран победы.
5. **a)** См. README блока.
</details>


## Что дальше

→ [Урок 5.8 — Патрульный корабль](../lesson-5-8-orbit-guard-patrol-ship/README.md) — старт **Orbit Guard** ★ №3!

---

*Искры в кузнице.*

[← Choose language](README.md)
