# Урок 5.11: Orbit Guard целиком

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~40 min**  
> [Choose language](README.md) · **[English →](en.md)**

<!-- meta
homework: starter/game.py
minutes: 40
-->

---

## Title

**Уровень ★23 — Orbit Guard Pro**

---

## Объяснение

- Состояния: `START`, `PLAYING`, `WAVE_CLEAR`, `GAME_OVER`, `VICTORY` (как Glow Worm 5.3).
- Четыре волны; `march_speed` растёт, когда врагов меньше.
- Бонусное **НЛО** сверху — выстрел +350 и `high_score` за сессию.
- SPACE на титуле — старт; после волны — следующая; лучший счёт в памяти.

---

### Шаг 1: Открой стартер

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-11-orbit-guard-complete
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
high_score = max(high_score, score)
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-11-orbit-guard-complete
python solution\game.py
```

**Expected output (visual):** Рабочая веха Orbit Guard для урока 5.11.

---

## Быстрые упражнения

1. Print `len(player_bolts)` after each shot.
2. Log `formation_x` when the grid steps down.
3. Skim [solution/game.py](solution/game.py) for orbit colors.

---

## Задание для практики

**Квест:** Orbit Guard Pro

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

1. `WAVE_CLEAR` means…
   - **a)** All invaders destroyed this wave
   - **b)** Flask error
   - **c)** Ship deleted
   - **d)** No pygame

2. `high_score` updates when…
   - **a)** Current score exceeds it
   - **b)** Every frame always
   - **c)** Only on START
   - **d)** Never

3. UFO bonus gives roughly…
   - **a)** +350 points
   - **b)** Extra life always
   - **c)** Free pip install
   - **d)** No effect

4. More waves generally mean…
   - **a)** Faster march / tougher grid
   - **b)** Slower pygame
   - **c)** No shields
   - **d)** Less code

5. Next ★ roadmap project is…
   - **a)** Mine Whisper (5.12 сетка)
   - **b)** Course 1 turtle only
   - **c)** Block 0 essays
   - **d)** Removing lists


---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **a)** Pause before the next wave.
2. **a)** Session best like other ★ games.
3. **a)** Shoot the crossing UFO.
4. **a)** Difficulty ramp across waves.
5. **a)** See block README item 4.

</details>


## Что дальше

→ [Урок 5.12 — Сетка кристаллов](../lesson-5-12-mine-whisper-crystal-grid/README.md) — **Mine Whisper** ★ №4!

---

*Защищай орбиту кодом.*

[← Choose language](README.md)
