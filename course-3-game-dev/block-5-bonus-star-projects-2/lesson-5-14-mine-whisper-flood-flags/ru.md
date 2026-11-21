# Урок 5.14: Заливка и флажки

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~36 min**  
> [Выбери язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 36
-->

---

## Title

**Уровень ★26 — Шёпот заливки**

---

## Объяснение

Если у клетки `neighbors == 0`, пещера **шепчет открыться** — все связанные нули становятся открытыми.

**Картинка рекурсии:** шёпот в пещере — эхо передаётся в каждый «туннель», тот — соседям.

**Мягкая рекурсия** (см. solution) или **стек** (тот же результат):

```python
stack = [(col, row)]
while stack:
    c, r = stack.pop()
```

**Флажки:** кнопка мыши **3** (правый клик) переключает `flagged`.

---

### Шаг 1: Открой стартер

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-14-mine-whisper-flood-flags
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
while stack:
    c, r = stack.pop()
    # reveal zero cells and push neighbors
```

---

## Запуск кода

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-14-mine-whisper-flood-flags
python solution\game.py
```

**Expected output (visual):** Runnable Mine Whisper milestone for lesson 5.14.

---

## Быстрые упражнения

1. Print the picked `(col, row)` each click.
2. Change `CELL` — does the board still align with clicks?
3. Skim [solution/game.py](solution/game.py) for whisper colors.

---

## Задание для практики

**Quest name:** Шёпот заливки

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: does the window match this lesson's goal?
3. **Bonus stretch:** add a tiny HUD label with grid size.

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Уголок отладки

**Problem:** Открылся один ноль

**Cause:** Заливка остановилась.

**Fix:** При neighbors==0 добавляй 8 соседей в стек.


---

## Проверь себя

1. Заливка, когда…
   - **a)** neighbors==0
   - **b)** Выход
   - **c)** Score None
   - **d)** Никогда

2. Версия со стеком…
   - **a)** pop/push в list
   - **b)** Turtle
   - **c)** SQL
   - **d)** HTML

3. Правый клик…
   - **a)** flagged
   - **b)** Размер окна
   - **c)** pip
   - **d)** Flask

4. Рекурсия и стек должны…
   - **a)** Открыть те же клетки
   - **b)** Всегда отличаться
   - **c)** Удалить сетку
   - **d)** Пропустить мины

5. 5.15 добавит…
   - **a)** Таймер, сложность, победа
   - **b)** Одну клетку
   - **c)** Без pygame
   - **d)** Flask

---

<details><summary>Нажми, чтобы увидеть ответы</summary>


1. **a)** neighbors==0.

2. **a)** pop/push в list.

3. **a)** flagged.

4. **a)** Открыть те же клетки.

5. **a)** Таймер, сложность, победа.


</details>



## Что дальше

→ [Урок 5.15 — Mine Whisper целиком](../lesson-5-15-mine-whisper-complete/README.md)

---

*Listen to the crystals.*

[Выбери язык](README.md)
