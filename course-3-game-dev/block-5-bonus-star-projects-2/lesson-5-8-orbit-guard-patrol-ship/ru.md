# Урок 5.8: Патрульный корабль и выстрелы

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~32 min**  
> [Choose language](README.md) · **[English →](en.md)**

<!-- meta
homework: starter/game.py
minutes: 32
-->

---

## Title

**Уровень ★20 — Патрульный выстрел**

---

## Объяснение

- Двигай `ship_x` стрелками внизу экрана; не выезжай за края.
- `player_bolts` — **список словарей** с `x`, `y`, `vy` (минус = вверх).
- Таймер `COOLDOWN`, чтобы SPACE не стрелял без остановки.
- Удаляй болты списком: выше `PLAY_TOP` или ниже `HEIGHT`.

---

### Шаг 1: Открой стартер

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-8-orbit-guard-patrol-ship
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
player_bolts.append({"x": ship_x, "y": SHIP_Y, "vy": -BOLT_SPEED})
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-8-orbit-guard-patrol-ship
python solution\game.py
```

**Expected output (visual):** Рабочая веха Orbit Guard для урока 5.8.

---

## Быстрые упражнения

1. Print `len(player_bolts)` after each shot.
2. Log `formation_x` when the grid steps down.
3. Skim [solution/game.py](solution/game.py) for orbit colors.

---

## Задание для практики

**Квест:** Патрульный выстрел

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

1. `player_bolts` stores…
   - **a)** A list of bolt dicts
   - **b)** Only one integer
   - **c)** Flask routes
   - **d)** PNG filenames

2. Negative `vy` means the bolt moves…
   - **a)** Up the screen
   - **b)** Only sideways
   - **c)** Into the ship
   - **d)** Never

3. `COOLDOWN` prevents…
   - **a)** Spam firing every frame
   - **b)** Drawing stars
   - **c)** Installing pygame
   - **d)** Reading keyboard

4. You remove off-screen bolts by…
   - **a)** Filtering the list by y range
   - **b)** Deleting pygame
   - **c)** Renaming files
   - **d)** Using Turtle

5. Lesson 5.9 adds…
   - **a)** Invader grid marching
   - **b)** Flask forms
   - **c)** Turtle art
   - **d)** pip uninstall


---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **a)** Each bolt is a small dict in a list.
2. **a)** Upward motion in screen coordinates.
3. **a)** Cooldown spaces out shots.
4. **a)** Keep only bolts between top and bottom.
5. **a)** Enemy formation next.

</details>


## Что дальше

→ [Урок 5.9 — Формация захватчиков](../lesson-5-9-orbit-guard-invader-formation/README.md)

---

*Защищай орбиту кодом.*

[← Choose language](README.md)
