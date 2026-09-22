# Урок 3.2: Поймай падающие звёзды

> **Курс:** Разработка игр на Python · **Блок:** Физика и столкновения (финальный проект) · **~45–50 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 45
-->

---

## Title

**Уровень 10 — Ловец звёзд**

---

## Объяснение

Это **капстоун Курса 3** — игру можно показывать.

| Часть | Задача |
|-------|--------|
| Экран старта | Заголовок + SPACE |
| Игра | Платформа ВЛЕВО/ВПРАВО; звезда падает; поймал или промах |
| Game over | Финальный счёт + SPACE на титул |

Одна звезда за раз — код дружелюбный:

```python
star.y += int(fall_speed * dt)
if paddle.colliderect(star):
    score += 1
    reset_star()
elif star.top > HEIGHT:
    misses += 1
    reset_star()
```

Три промаха → `GAME_OVER`. Меню — **KEYDOWN**; платформа — **get_pressed**.

---

### Шаг 1: Открой starter/game.py

Открой [starter/game.py](starter/game.py). Рисуются титул / игра / over и движение платформы. TODO: старт с `START`, SPACE, падение + поймал/промах.

---

### Шаг 2: Начни с титульного экрана

```python
state = START
```

---

### Шаг 3: SPACE запускает / возвращает

```python
if event.type == pygame.KEYDOWN:
    if state == START and event.key in (pygame.K_SPACE, pygame.K_RETURN):
        start_round()
    elif state == GAME_OVER and event.key in (pygame.K_SPACE, pygame.K_RETURN):
        state = START
```

`start_round()` сбрасывает счёт, промахи, платформу и звезду.

---

### Шаг 4: Падение, ловля, промах

Внутри `PLAYING`:

```python
star.y += int(fall_speed * dt)

if paddle.colliderect(star):
    score += 1
    reset_star()
elif star.top > HEIGHT:
    misses += 1
    reset_star()
    if misses >= MAX_MISSES:
        state = GAME_OVER
```

---

### Шаг 5: Сыграй полный раунд

```text
cd course-3-game-dev\block-3-physics-collisions-final-project\lesson-3-2-catch-the-falling-stars
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Ожидаемый результат (на экране):** Титул → SPACE → звёзды падают → лови платформой → после 3 промахов Game Over → SPACE → титул.

---

## Пример кода

**Файл: [solution/game.py](solution/game.py)** — полный листинг (капстоун длиннее обычного). Ключевые идеи:

```python
def reset_star():
    star.midtop = (random.randint(20, WIDTH - 20), -40)

def start_round():
    global score, misses, state
    score = 0
    misses = 0
    paddle.midbottom = (WIDTH // 2, HEIGHT - 24)
    reset_star()
    state = PLAYING

# В PLAYING:
star.y += int(fall_speed * dt)
if paddle.colliderect(star):
    score += 1
    reset_star()
elif star.top > HEIGHT:
    misses += 1
    reset_star()
    if misses >= MAX_MISSES:
        state = GAME_OVER
```

Открой solution для полной runnable-программы (~120 строк).

---

## Запуск кода

```text
cd course-3-game-dev\block-3-physics-collisions-final-project\lesson-3-2-catch-the-falling-stars
python starter\game.py
```

**Ожидаемый результат (на экране):** Полный цикл Catch the Falling Stars с рестартом.

---

## Быстрые упражнения

1. **Легче** — `MAX_MISSES = 5`.
2. **Шире платформа** — `paddle_w = 140` (пересобери Rect).
3. **Похвала** — на Game Over, если `score >= 10`, выведи «Star hero!».

---

## Задание для практики

**Название квеста:** Ловец звёзд

1. Закрой все TODO в [starter/game.py](starter/game.py).
2. Доиграй до Game Over, вернись на титул и сыграй ещё раз.
3. **Бонус:** Чуть поднимай `fall_speed` после каждой ловли (рамп — подробнее в 3.3).

**Самопроверка:** Звезда падает? Ловля даёт очко? 3 промаха → Game Over? SPACE возвращает через титул? ✓

**Покажи:** Попроси родителя или друга сыграть один раунд!

**Эталонное решение:** [solution/game.py](solution/game.py)

---

## Уголок отладки

**Проблема:** Звезда не двигается, или счёт не растёт при «ловле».

**Причина:** Забыли `star.y += …`, неверный Rect, или `state` не переходит в `PLAYING`.

**Исправление:** Раскомментируй TODO падения и colliderect. Проверь `state = START`, затем SPACE → `start_round()`. Звезда стартует с `y = -40`.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. Что делает падение звезды плавным?
   - **a)** `pip install fall`
   - **b)** Прибавление `fall_speed * dt` к `star.y` каждый кадр
   - **c)** Только события `QUIT`
   - **d)** Удаление платформы

2. Лучшее определение «ловли» здесь?
   - **a)** `paddle.colliderect(star)` во время игры
   - **b)** Закрытие окна
   - **c)** Загрузка шрифта
   - **d)** Дважды `pygame.init()`

3. Что делать, когда `star.top > HEIGHT`?
   - **a)** Мгновенная победа
   - **b)** Засчитать промах (и возможно game over)
   - **c)** Установить Turtle
   - **d)** Зависнуть без UI

4. Переходы меню по SPACE должны использовать…
   - **a)** `KEYDOWN` (один раз)
   - **b)** Только `get_pressed` без осторожности
   - **c)** Только мышь
   - **d)** Только `random.randint`

5. Зачем вызывать `reset_star()` после ловли или промаха?
   - **a)** Чтобы открыть второе окно
   - **b)** Чтобы появилась следующая звезда сверху
   - **c)** Чтобы убрать `dt`
   - **d)** Чтобы удалить Pygame

---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **b)** Скорость падения × дельта-время.
2. **a)** Платформа пересекает звезду.
3. **b)** Промах (и проверка MAX_MISSES).
4. **a)** Одноразовый KEYDOWN для меню.
5. **b)** Следующая звезда появляется над экраном.

</details>

---

## Что дальше

→ [Урок 3.3 — Полировка](../lesson-3-3-polish/README.md) — звук, рекорд, рост сложности!

---

*Ты выпустил настоящую мини-игру — поклон!*

[← Выбрать язык](README.md)
