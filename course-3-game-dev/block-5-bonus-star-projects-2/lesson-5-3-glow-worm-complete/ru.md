# Урок 5.3: Glow Worm целиком

> **Курс:** Разработка игр на Python · **Блок:** Бонус ★ Проекты II · **~35–40 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 38
-->

---

## Title

**Уровень ★15 — Glow Worm Pro**

---

## Объяснение

Ты уже двигаешься, ешь и разбиваешься. Собери **маленький аркадный цикл**:

| Фаза | Значение `state` | Действие |
|------|------------------|----------|
| Титул | `START` | **SPACE** → `start_game()` |
| Игра | `PLAYING` | Стрелки; таймер двигает червяка |
| Конец | `GAME_OVER` | **SPACE** — новый заход; покажи счёт |

**Рекорд сессии `high_score`:** в `crash()`, если `score > high_score`, сохрани лучший результат до закрытия окна.

**Ускорение:** вместо фиксированного интервала считай `move_interval` от счёта:

```python
def move_interval_for_score() -> float:
    speedup = min(12, score // 3)
    return max(MIN_INTERVAL, BASE_INTERVAL - speedup * 0.012)
```

Каждые несколько искр интервал чуть короче — но не меньше `MIN_INTERVAL`.

**Полировка:** пульсация еды и головы через `pygame.time.get_ticks()`; полупрозрачные оверлеи на старте и game over (см. [solution/game.py](solution/game.py)).

**Победа:** если `spawn_food()` вернул `(-1, -1)` — поле заполнено, `state = GAME_OVER`.

---

### Step 1: `start_game()`

Сброс сегментов, направлений, еды, счёта, таймера, `move_interval = BASE_INTERVAL`, `state = PLAYING`.

---

### Step 2: `crash()`

Если `score > high_score` — обнови рекорд. `state = GAME_OVER`.

---

### Step 3: События

```python
if state in (START, GAME_OVER) and event.key == pygame.K_SPACE:
    start_game()
elif state == PLAYING:
    # стрелки → pending_dir
```

`move_timer` и `step_worm()` только при `state == PLAYING`.

---

### Step 4: Запуск

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-3-glow-worm-complete
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Ожидаемый вывод (визуально):** Титул → игра → конец со счётом и рекордом; скорость растёт со счётом.

---

## Code Example

**Файл: [solution/game.py](solution/game.py)**

```python
def start_game() -> None:
  ...
  state = PLAYING
```

---

## Code Execution

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-3-glow-worm-complete
python solution\game.py
```

**Ожидаемый вывод (визуально):** Полный Glow Worm: счёт и лучший на HUD; ускорение; SPACE без перезапуска Python.

---

## Quick Drills

1. Каждые 5 очков печатай `move_interval` — меньше?
2. Побей `high_score` и упади — новое число на экране?
3. Подзаголовок «Glow Worm» на титуле.

---

## Задание для практики

**Квест:** Glow Worm Pro

1. Доделай TODO в [starter/game.py](starter/game.py): ramp, `start_game`, `crash`, оверлеи, шаг только в `PLAYING`.
2. **START** и **GAME_OVER** — **SPACE**; в игре — стрелки.
3. HUD: **score** и **high_score**.
4. **Бонус:** пульс свечения как в решении.

**Самопроверка:** Три захода подряд без перезапуска Python? ✓

**Эталон:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Проблема:** Червяк ползёт на титуле.

**Причина:** `step_worm()` без проверки `state`.

**Решение:** Таймер только при `state == PLAYING`.

**Проблема:** Рекорд сбрасывается.

**Причина:** `high_score = 0` в `start_game()`.

**Решение:** В `start_game()` сбрасывай только заход; `high_score` не трогай.

**Проблема:** Скорость не меняется.

**Причина:** Старый фиксированный `MOVE_INTERVAL`.

**Решение:** После еды — `move_interval = move_interval_for_score()`.

---

## Проверь себя

1. `state == START` — это…
   - **a)** Ждём SPACE и `start_game()`
   - **b)** Режим отладки Flask
   - **c)** Рисует Turtle
   - **d)** Только пустая еда

2. `high_score` обновляется в…
   - **a)** `crash()` при новом максимуме
   - **b)** Каждом кадре
   - **c)** Только `spawn_food()`
   - **d)** Всегда в `pygame.quit()`

3. `move_interval_for_score()` делает червяка…
   - **a)** Быстрее с ростом счёта, с нижним пределом
   - **b)** Всегда медленнее
   - **c)** Невидимым
   - **d)** Без таймера

4. Логика роста из 5.2…
   - **a)** `pop()` только если не ели
   - **b)** Всегда укорачивать
   - **c)** Игнорировать `food`
   - **d)** Удалить Surface

5. После этого ★-проекта в Блоке 5…
   - **a)** **Bounce Forge** (скоро в индексе блока)
   - **b)** Калькулятор Flask
   - **c)** Установка Python
   - **d)** Без списков

---

<details><summary>Нажми, чтобы показать ответы</summary>

1. **a)** Экран привлечения.
2. **a)** В `crash()`.
3. **a)** Ускорение до `MIN_INTERVAL`.
4. **a)** Как в 5.2.
5. **a)** См. [README блока](../README.md).

</details>

---

## Что дальше

Поздравляем — **Glow Worm** готов как полноценный ★ мини-игра!

→ [Блок 5 ★ Проекты II](../README.md) — **Bounce Forge** и другие бонусы **скоро**.  
→ [Карта курса 3](../../STUDENT-MAP.ru.md) — все блоки одним взглядом.

---

*Неоновый след — настоящая аркада.*

[← Выбрать язык](README.md)