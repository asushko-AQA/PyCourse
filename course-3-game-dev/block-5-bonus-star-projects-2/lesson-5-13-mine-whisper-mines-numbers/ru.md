# Урок 5.13: Шахты и соседние числа

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~34 min**  
> [Выбери язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 34
-->

---

## Title

**Уровень ★25 — Скрытое эхо**

---

## Объяснение

После **первого левого клика** вызови `place_mines`: **безопасная зона** (клетка + 8 соседей) без мин.

Затем для каждой клетки заполни `neighbors` через `count_neighbor_mines`.

При открытии: цифра `1`–`8` или красный кристалл, если попал на мину.

---

### Шаг 1: Открой стартер

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-13-mine-whisper-mines-numbers
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Purple crystal board; finish TODOs for this lesson's goal.

---

### Step 2: Compare the solution

Study [solution/game.py](solution/game.py) for the full pattern.

---

## Пример кода

**File: [solution/game.py](solution/game.py)**:

```python
board[r][c]["neighbors"] = count_neighbor_mines(board, c, r)
```

---

## Запуск кода

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-13-mine-whisper-mines-numbers
python solution\game.py
```

**Expected output (visual):** Runnable Mine Whisper milestone for lesson 5.13.

---

## Быстрые упражнения

1. Print the picked `(col, row)` each click.
2. Change `CELL` — does the board still align with clicks?
3. Skim [solution/game.py](solution/game.py) for whisper colors.

---

## Задание для практики

**Quest name:** Счётчик эха

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: does the window match this lesson's goal?
3. **Bonus stretch:** add a tiny HUD label with grid size.

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Уголок отладки

**Problem:** Везде 0

**Cause:** Не посчитали соседей.

**Fix:** После мин пройдись по клеткам и вызови `count_neighbor_mines`.


---

## Проверь себя

1. Мины ставятся…
   - **a)** После первого безопасного клика
   - **b)** До pygame.init
   - **c)** При import
   - **d)** Никогда

2. `neighbors` считает…
   - **a)** Мины в 8 соседях
   - **b)** Только FPS
   - **c)** Клавиши
   - **d)** Маршруты Flask

3. Безопасный первый клик —…
   - **a)** Клетка и соседи без мин
   - **b)** Без random
   - **c)** Без сетки
   - **d)** Беск. жизни

4. Открытая мина —…
   - **a)** Красный кристалл
   - **b)** HTML
   - **c)** pip
   - **d)** Ничего

5. В 5.14 будет…
   - **a)** Заливка и флажки
   - **b)** Только print()
   - **c)** Turtle
   - **d)** Удаление dict

---

<details><summary>Нажми, чтобы увидеть ответы</summary>


1. **a)** После первого безопасного клика.

2. **a)** Мины в 8 соседях.

3. **a)** Клетка и соседи без мин.

4. **a)** Красный кристалл.

5. **a)** Заливка и флажки.


</details>



## Что дальше

→ [Урок 5.14 — Заливка и флажки](../lesson-5-14-mine-whisper-flood-flags/README.md)

---

*Listen to the crystals.*

[Выбери язык](README.md)
