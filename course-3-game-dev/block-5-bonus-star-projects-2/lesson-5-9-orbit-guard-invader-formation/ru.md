# Урок 5.9: Формация захватчиков

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~34 min**  
> [Choose language](README.md) · **[English →](en.md)**

<!-- meta
homework: starter/game.py
minutes: 34
-->

---

## Title

**Уровень ★21 — Марш захватчиков**

---

## Объяснение

- `formation_x`, `formation_y` сдвигают всю сетку; пересобирай `invaders` каждый шаг.
- `march_dir` — `1` или `-1`; у края разворачивай и добавляй `step_down` к `formation_y`.
- Сетка `COLS` × `ROWS` из `pygame.Rect` (рисуем эллипсы).
- Болты пока проходят сквозь врагов — столкновения в 5.10.

---

### Шаг 1: Открой стартер

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-9-orbit-guard-invader-formation
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Окно Orbit Guard; допиши TODO под цель урока.

---

### Шаг 2: Сравни с решением

Изучи [solution/game.py](solution/game.py) — корабль, марш, щиты или волны.

---

## Code Example

**Файл: [solution/game.py](solution/game.py)** — ключевой фрагмент:

```python
formation_x += march_dir * march_speed * dt
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-9-orbit-guard-invader-formation
python solution\game.py
```

**Expected output (visual):** Рабочая веха Orbit Guard для урока 5.9.

---

## Быстрые упражнения

1. Print `len(player_bolts)` after each shot.
2. Log `formation_x` when the grid steps down.
3. Skim [solution/game.py](solution/game.py) for orbit colors.

---

## Задание для практики

**Квест:** Марш захватчиков

1. Допиши TODO в [starter/game.py](starter/game.py).
2. Самопроверка: окно ведёт себя как в уроке?
3. **Бонус:** добавь мерцание звёзд на фоне (см. solution).

**Самопроверка:** Окно ~5 с без ошибок? ✓

**Эталон:** [solution/game.py](solution/game.py)

---

## Уголок отладки

**Problem:** Bolts never disappear.

**Cause:** Forgot to filter `player_bolts` after moving.

**Fix:** Reassign the list with a comprehension checking `PLAY_TOP < y < HEIGHT`.

**Problem:** Formation teleports off-screen.

**Cause:** Not flipping `march_dir` at margins.

**Fix:** When `formation_x` passes margin, multiply `march_dir` by -1 and add `step_down`.


---

## Проверь себя

1. When the formation hits the side you…
   - **a)** Flip march_dir and step down
   - **b)** Delete pygame
   - **c)** Stop the clock
   - **d)** Hide the ship

2. `build_invaders()` should run…
   - **a)** After formation offsets change
   - **b)** Only once per game ever
   - **c)** Before pygame.init
   - **d)** Never

3. `march_dir` is typically…
   - **a)** 1 or -1 for left/right
   - **b)** A pygame Surface
   - **c)** Player score
   - **d)** A file path

4. Invaders are drawn as…
   - **a)** Original ellipse shapes
   - **b)** Copyrighted bitmaps
   - **c)** HTML tables
   - **d)** Flask templates

5. Lesson 5.10 adds…
   - **a)** Collisions, shields, enemy fire
   - **b)** Only Turtle
   - **c)** Database queries
   - **d)** Removing lists


---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **a)** Classic Space Invaders sidestep + drop.
2. **a)** Rects must follow the marching offset.
3. **a)** Sign tells which way the block slides.
4. **a)** Shape-only art — no stolen sprites.
5. **a)** Combat layer next.

</details>


## Что дальше

→ [Урок 5.10 — Щиты, жизни и счёт](../lesson-5-10-orbit-guard-shields-lives/README.md)

---

*Защищай орбиту кодом.*

[← Choose language](README.md)
