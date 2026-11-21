# Урок 5.15: Mine Whisper целиком

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~40 min**  
> [Выбери язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 40
-->

---

## Title

**Уровень ★27 — Mine Whisper Pro**

---

## Объяснение

Собери полный цикл:

| Фаза | `state` | Действие |
|------|---------|----------|
| Меню | `START` | **1/2/3** — сложность |
| Игра | `PLAYING` | открытие + флажки; таймер |
| Победа | `WON` | все безопасные открыты — **лучшее время** |
| Поражение | `LOST` | мина — показать все мины |

**HUD:** осталось мин и время.

---

### Шаг 1: Открой стартер

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-15-mine-whisper-complete
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
if player_won(grid):
    state = WON
    record_best()
```

---

## Запуск кода

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-15-mine-whisper-complete
python solution\game.py
```

**Expected output (visual):** Runnable Mine Whisper milestone for lesson 5.15.

---

## Быстрые упражнения

1. Print the picked `(col, row)` each click.
2. Change `CELL` — does the board still align with clicks?
3. Skim [solution/game.py](solution/game.py) for whisper colors.

---

## Задание для практики

**Quest name:** Mine Whisper Pro

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: does the window match this lesson's goal?
3. **Bonus stretch:** add a tiny HUD label with grid size.

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Уголок отладки

**Problem:** Таймер стоит

**Cause:** `elapsed` только в PLAYING.

**Fix:** Добавь `elapsed += dt` в PLAYING.


---

## Проверь себя

1. `best_times` хранит…
   - **a)** Лучшее время по сложности
   - **b)** pip cache
   - **c)** Блок 1
   - **d)** Ничего

2. Победа, когда…
   - **a)** Все безопасные открыты
   - **b)** Все с флажками
   - **c)** Score > 9999
   - **d)** Flask

3. 1/2/3 в меню…
   - **a)** Старт easy/medium/hard
   - **b)** Выход
   - **c)** Удалить grid
   - **d)** Браузер

4. Счётчик мин…
   - **a)** MINE_COUNT − флажки
   - **b)** FPS
   - **c)** seed
   - **d)** slug

5. Следующая ★ игра…
   - **a)** Merge Magic (скоро)
   - **b)** Course 2
   - **c)** Эссе
   - **d)** Без pygame

---

<details><summary>Нажми, чтобы увидеть ответы</summary>


1. **a)** Лучшее время по сложности.

2. **a)** Все безопасные открыты.

3. **a)** Старт easy/medium/hard.

4. **a)** MINE_COUNT − флажки.

5. **a)** Merge Magic (скоро).


</details>



## Что дальше

→ [Блок 5 — Merge Magic (скоро)](../README.md)

---

*Listen to the crystals.*

[Выбери язык](README.md)
