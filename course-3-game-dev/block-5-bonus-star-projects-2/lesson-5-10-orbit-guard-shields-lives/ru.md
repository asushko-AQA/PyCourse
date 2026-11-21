# Урок 5.10: Щиты, жизни и счёт

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~36 min**  
> [Choose language](README.md) · **[English →](en.md)**

<!-- meta
homework: starter/game.py
minutes: 36
-->

---

## Title

**Уровень ★22 — Стена щитов**

---

## Объяснение

- Болт игрока попал во врага → удали оба, `score += 100`.
- Случайный захватчик по таймеру стреляет `enemy_bolts` вниз.
- Попадание в корабль → `lives -= 1`; щиты — сетка блоков с HP.
- `collidepoint` на блоках щита гасит болты до корабля.

---

### Шаг 1: Открой стартер

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-10-orbit-guard-shields-lives
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
if inv.collidepoint(bx, by): invaders.remove(inv); score += 100
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-10-orbit-guard-shields-lives
python solution\game.py
```

**Expected output (visual):** Рабочая веха Orbit Guard для урока 5.10.

---

## Быстрые упражнения

1. Print `len(player_bolts)` after each shot.
2. Log `formation_x` when the grid steps down.
3. Skim [solution/game.py](solution/game.py) for orbit colors.

---

## Задание для практики

**Квест:** Стена щитов

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

1. Enemy bolts move with…
   - **a)** Positive vy (down)
   - **b)** Only vx
   - **c)** Turtle degrees
   - **d)** Flask POST

2. Shields wear down when…
   - **a)** Bolt collidepoint hits a block
   - **b)** Player scores 100
   - **c)** Window closes
   - **d)** Stars spawn

3. `lives` drops when…
   - **a)** Enemy bolt hits the ship rect
   - **b)** You shoot a shield
   - **c)** Formation marches
   - **d)** You win

4. Removing a hit invader uses…
   - **a)** list.remove on invaders
   - **b)** pip uninstall
   - **c)** Deleting pygame
   - **d)** Renaming ru.md

5. Lesson 5.11 adds…
   - **a)** Waves, UFO bonus, full states
   - **b)** Only one enemy
   - **c)** No score
   - **d)** Flask deploy


---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **a)** Downward motion like falling shots.
2. **a)** HP on each shield cell decreases.
3. **a)** Ship rectangle collision with enemy bolt.
4. **a)** Mutate the invader list in place.
5. **a)** Full Orbit Guard polish next.

</details>


## Что дальше

→ [Урок 5.11 — Orbit Guard целиком](../lesson-5-11-orbit-guard-complete/README.md)

---

*Защищай орбиту кодом.*

[← Choose language](README.md)
