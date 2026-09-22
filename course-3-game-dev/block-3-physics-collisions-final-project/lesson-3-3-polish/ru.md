# Урок 3.3: Полировка

> **Курс:** Разработка игр на Python · **Блок:** Физика и столкновения (финальный проект) · **~30–40 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 35
-->

---

## Title

**Уровень 11 — Мастер полировки**

---

## Объяснение

У выпущенной игры должно быть **ощущение**. Три слоя полировки поверх урока 3.2:

| Полировка | Как |
|-----------|-----|
| Рекорд | Переменная `high_score` — обновляй в конце раунда |
| Рост сложности | `fall_speed = BASE_FALL + score * 12` |
| Звук | `pygame.mixer.Sound("catch.wav")` внутри try/except |

Рекорд держим **в памяти** (сбросится при закрытии окна). Запись в файл — приятный stretch позже.

```python
if score > high_score:
    high_score = score
```

Звуки **опциональны**: если микшер или файлы не сработали, `play_safe` просто ничего не делает.

---

### Шаг 1: Открой starter/game.py

Открой [starter/game.py](starter/game.py). Игра-ловушка уже работает. TODO: mixer + Sound, формула рампа, обновление `high_score`, звуки на ловлю/промах.

---

### Шаг 2: Инициализируй mixer и загрузи звуки

```python
pygame.mixer.init()
try:
    catch_sound = pygame.mixer.Sound(os.path.join(HERE, "catch.wav"))
    miss_sound = pygame.mixer.Sound(os.path.join(HERE, "miss.wav"))
except pygame.error:
    catch_sound = None
    miss_sound = None
```

---

### Шаг 3: Разгони падение

```python
fall_speed = BASE_FALL + score * 12
star.y += int(fall_speed * dt)
```

Выше счёт → быстрее звёзды. Честнее, чем вечная одна скорость.

---

### Шаг 4: Обнови рекорд при game over

```python
if misses >= MAX_MISSES:
    if score > high_score:
        high_score = score
    state = GAME_OVER
```

Показывай `high_score` на титуле и Game Over (уже набросано).

---

### Шаг 5: Играй звуки безопасно

```python
def play_safe(sound):
    if sound is not None:
        sound.play()

# при ловле:
play_safe(catch_sound)
# при промахе:
play_safe(miss_sound)
```

---

### Шаг 6: Запуск

```text
cd course-3-game-dev\block-3-physics-collisions-final-project\lesson-3-3-polish
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Ожидаемый результат (экран + опциональный звук):** На титуле High score; игра усложняется; бипы при ловле/промахе, если есть колонки; лучший счёт обновляется после раунда.

---

## Пример кода

**Файл: [solution/game.py](solution/game.py)** — акценты полировки:

```python
pygame.mixer.init()
# load catch.wav / miss.wav with try/except → catch_sound, miss_sound

high_score = 0
BASE_FALL = 160

# while PLAYING:
fall_speed = BASE_FALL + score * 12
star.y += int(fall_speed * dt)

if paddle.colliderect(star):
    score += 1
    play_safe(catch_sound)
    reset_star()
elif star.top > HEIGHT:
    misses += 1
    play_safe(miss_sound)
    reset_star()
    if misses >= MAX_MISSES:
        if score > high_score:
            high_score = score
        state = GAME_OVER
```

---

## Запуск кода

```text
cd course-3-game-dev\block-3-physics-collisions-final-project\lesson-3-3-polish
python starter\game.py
```

**Ожидаемый результат (на экране):** Отполированный Catch the Falling Stars с рампом и рекордом (+ звуки, если доступны).

---

## Быстрые упражнения

1. **Жёсткий рамп** — `score * 20`.
2. **NEW BEST!** — дополнительный текст, когда побил рекорд.
3. **Тихий режим** — временно `None` для обоих звуков; игра всё равно должна работать.

---

## Задание для практики

**Название квеста:** Мастер полировки

1. Закрой TODO в [starter/game.py](starter/game.py): звуки, рамп, обновление рекорда.
2. Побей свой high score хотя бы раз за сессию.
3. **Бонус:** сохрани `high_score` в `highscore.txt` через `open` / `write` (необязательно).

**Самопроверка:** Рекорд живёт между раундами (пока не вышел)? Звёзды ускоряются? Звуки опциональны, но загружены безопасно? ✓

**Эталонное решение:** [solution/game.py](solution/game.py)

---

## Уголок отладки

**Проблема:** `pygame.error` про mixer / sound или краш на старте.

**Причина:** Микшер не инициализирован, неверный путь или нет аудиоустройства.

**Исправление:** Один раз `pygame.mixer.init()`. Загрузку Sound оберни в `try/except pygame.error`. Используй `play_safe`. Проверь, что `catch.wav` / `miss.wav` рядом с `game.py`.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. Где этот урок по умолчанию хранит рекорд?
   - **a)** Только в облачной БД
   - **b)** В переменной текущей сессии
   - **c)** Внутри `coin.png`
   - **d)** В Turtle

2. Что делает рост сложности здесь?
   - **a)** Удаляет платформу
   - **b)** Увеличивает скорость падения с ростом счёта
   - **c)** Убирает `dt`
   - **d)** Навсегда включает fullscreen

3. Зачем try/except вокруг загрузки Sound?
   - **a)** Чтобы отсутствие звука не роняло игру
   - **b)** Чтобы дважды ставить Python
   - **c)** Чтобы рисовать Rect
   - **d)** Чтобы пропустить `flip`

4. Когда обновлять `high_score`?
   - **a)** Каждый кадр даже на титуле
   - **b)** Когда раунд кончился и `score` лучше рекорда
   - **c)** Только на QUIT
   - **d)** Никогда

5. `play_safe(None)` должен…
   - **a)** Громко упасть
   - **b)** Ничего не делать (без звука)
   - **c)** Закрыть Pygame
   - **d)** Обнулить `dt`

---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **b)** Переменная сессии (в памяти).
2. **b)** Быстрее падение при большем счёте.
3. **a)** Опциональный звук остаётся безопасным.
4. **b)** Сравнивай после конца раунда.
5. **b)** Защита от отсутствующего Sound.

</details>

---

## Что дальше

→ [Оглавление Блока 3](../README.md) — отметь чек-лист выпуска Курса 3!  
→ Ты закончил **Курс 3: Разработка игр на Python**. Покажи игру!

---

*Отполировано с гордостью — Курс 3 завершён!*

[← Выбрать язык](README.md)
