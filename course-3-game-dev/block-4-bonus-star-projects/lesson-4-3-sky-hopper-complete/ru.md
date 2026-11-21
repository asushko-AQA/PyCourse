# Урок 4.3: Sky Hopper целиком

> **Курс:** Разработка игр на Python · **Блок:** Бонус ★ Проекты · **~40–45 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 42
-->

---

## Title

**Уровень ★3 — Мастер Sky Hopper**

---

## Explanation

Ты собрал **физику** (4.1) и **ворота** (4.2). Осталось подключить **состояния игры**, как в уроке 2.4:

| Состояние | Что видит игрок |
|-----------|-----------------|
| `start` | Титул, рекорд, SPACE — старт |
| `playing` | Взмах, прокрутка, счёт |
| `game_over` | Итог, рекорд, SPACE — назад на титул |

При аварии обновляй **`high_score`** (память сессии — как в 3.3).  
**Рамп сложности:** `scroll_speed = BASE_SCROLL + score * 8`.

---

### Step 1: `start_round()` и `crash()`

Сброс `score`, птицы, `pipes`, `scroll_speed`; `state = PLAYING`.  
В `crash()` сравни `score` с `high_score`, затем `state = GAME_OVER`.

---

### Step 2: События

```python
if state == START and event.key in (pygame.K_SPACE, pygame.K_RETURN):
    start_round()
elif state == PLAYING and event.key == pygame.K_SPACE:
    vel_y = FLAP_STRENGTH
elif state == GAME_OVER and event.key in (pygame.K_SPACE, pygame.K_RETURN):
    state = START
```

---

### Step 3: Цикл PLAYING

Перенеси логику труб из 4.2, вызывай `crash()` вместо `crashed`.  
Физика только при `state == PLAYING`.

---

### Step 4: Запуск

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-3-sky-hopper-complete
python starter\game.py
```

**Ожидаемый результат:** Полный Sky Hopper для показа друзьям.

---

## Code Example

```python
scroll_speed = BASE_SCROLL + score * 8
for pipe in pipes:
    pipe["x"] -= int(scroll_speed * dt)

if score > high_score:
    high_score = score  # в crash() в конце раунда
```

---

## Code Execution

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-3-sky-hopper-complete
python starter\game.py
```

**Ожидаемый результат:** Титул → игра → game over → титул; рекорд между раундами.

---

## Quick Drills

1. Смешной подзаголовок на титуле.
2. Потолок `scroll_speed = 300`.
3. Красная вспышка фона 0.2 с при crash.

---

## Practice Task

**Квест:** Мастер Sky Hopper

1. Закрой все TODO в [starter/game.py](starter/game.py).
2. Побей **рекорд** дважды за сессию.
3. **Бонус:** сохрани рекорд в `sky_hopper_best.txt`.

**Самопроверка:** Три состояния? Рекорд на game over? HUD скорости растёт? ✓

**Эталон:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Проблема:** Сразу PLAYING или нет выхода с титула.

**Причина:** `state` не в `KEYDOWN` или физика на всех состояниях.

**Fix:** Физика только в `elif state == PLAYING:`.

---

## Quick Check

1. Когда обновляем `high_score`?
   - **a)** Каждый кадр на титуле
   - **b)** В конце раунда, если счёт выше
   - **c)** При import pygame
   - **d)** Никогда

2. Рамп сложности — это…
   - **a)** Быстрее прокрутка ворот со счётом
   - **b)** Окно сжимается в ноль
   - **c)** Убрать `dt`
   - **d)** Перейти на Flask

3. После game over SPACE…
   - **a)** Возврат на титул
   - **b)** Мгновенный выход Python
   - **c)** Удаление pipes с диска
   - **d)** Открыть браузер

4. Графика Sky Hopper…
   - **a)** Фигуры, нарисованные в коде
   - **b)** Чужие коммерческие спрайты
   - **c)** Только SVG из сети
   - **d)** Обязательно 3D

5. Следующий ★ проект займёт уроки…
   - **a)** 4.4 – 4.6
   - **b)** 5.1 – 5.3
   - **c)** 1.1 – 1.3
   - **d)** 99.1 – 99.9

---

<details><summary>Нажми, чтобы показать ответы</summary>

1. **b)** Конец раунда.
2. **a)** Скорость прокрутки.
3. **a)** Титул для реигры.
4. **a)** Свои фигуры.
5. **a)** Следующий слот в README блока.

</details>

---

## What's Next

→ [Урок 4.4 — Автопрокрутка и бег](../lesson-4-4-prism-dash-auto-scroll/README.md) — старт ★ проекта **№2**, **Prism Dash**!  
→ Или [оглавление Блока 4](../README.md) со всеми ★ играми.  
→ Покажи **Sky Hopper** тому, кто играл в Catch the Falling Stars!

---

*★ Sky Hopper — первый проект завершён.*

[← Выбрать язык](README.md)