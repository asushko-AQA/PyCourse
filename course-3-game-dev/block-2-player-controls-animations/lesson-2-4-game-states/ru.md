# Урок 2.4: Состояния игры

> **Курс:** Разработка игр на Python · **Блок:** Управление игроком и анимации · **~35–40 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 35
-->

---

## Title

**Уровень 8 — Режиссёр сцен**

---

## Объяснение

Настоящая игра — не бесконечный цикл «всегда играем». Есть **сцены**:

| Состояние | Что видит игрок | Типичный ввод |
|-----------|-----------------|---------------|
| `start` | Заголовок + «Press SPACE» | SPACE → начать |
| `playing` | Движение, счёт, таймер | Стрелки (удержание) |
| `game_over` | Финальный счёт + подсказка | SPACE → титул |

Одна переменная режиссирует шоу:

```python
state = "start"  # или константы START / PLAYING / GAME_OVER
```

Каждый кадр: события → обновление **только в playing** → рисунок под текущий `state`.

**Меню любят `KEYDOWN`.** Непрерывное движение — по-прежнему `get_pressed()`. Не путай!

В уроке короткий таймер **15 секунд**, чтобы быстро дойти до Game Over при проверке.

---

### Шаг 1: Открой starter/game.py

Открой [starter/game.py](starter/game.py). Рисование трёх экранов набросано. TODO: старт в `START`, SPACE, переход в `GAME_OVER` по таймеру.

---

### Шаг 2: Начни с титульного экрана

```python
state = START
```

(Не `PLAYING` — это был временный дефолт в starter.)

---

### Шаг 3: SPACE меняет состояние

В цикле событий, на `KEYDOWN`:

```python
if state == START and event.key in (pygame.K_SPACE, pygame.K_RETURN):
    state = PLAYING
    score = 0.0
    play_time = 0.0
    x, y = 295.0, 215.0
elif state == GAME_OVER and event.key in (pygame.K_SPACE, pygame.K_RETURN):
    state = START
```

Сброс счёта / времени / позиции делает каждый раунд честным.

---

### Шаг 4: Время вышло → game over

В ветке `PLAYING`:

```python
if play_time >= TIME_LIMIT:
    state = GAME_OVER
```

---

### Шаг 5: Запусти полный цикл

```text
cd course-3-game-dev\block-2-player-controls-animations\lesson-2-4-game-states
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Ожидаемый результат (визуально):** Титул → SPACE → игра со счётом и таймером → через ~15с Game Over → SPACE → снова титул.

---

## Пример кода

**Файл: [solution/game.py](solution/game.py)**

```python
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stage Director")

clock = pygame.time.Clock()
running = True

font_big = pygame.font.Font(None, 64)
font_small = pygame.font.Font(None, 32)

START = "start"
PLAYING = "playing"
GAME_OVER = "game_over"

state = START

x = 295.0
y = 215.0
box_w = 50
box_h = 50
speed = 250
score = 0.0
play_time = 0.0
TIME_LIMIT = 15.0

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if state == START and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                state = PLAYING
                score = 0.0
                play_time = 0.0
                x, y = 295.0, 215.0
            elif state == GAME_OVER and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                state = START

    screen.fill((12, 14, 28))

    if state == START:
        title = font_big.render("Key Captain", True, (255, 220, 80))
        hint = font_small.render("Press SPACE to start", True, (200, 200, 220))
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30)))

    elif state == PLAYING:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x = x - speed * dt
        if keys[pygame.K_RIGHT]:
            x = x + speed * dt
        if keys[pygame.K_UP]:
            y = y - speed * dt
        if keys[pygame.K_DOWN]:
            y = y + speed * dt

        x = max(0, min(x, WIDTH - box_w))
        y = max(0, min(y, HEIGHT - box_h))

        play_time = play_time + dt
        score = play_time * 10

        if play_time >= TIME_LIMIT:
            state = GAME_OVER

        pygame.draw.rect(screen, (255, 200, 50), (int(x), int(y), box_w, box_h))
        score_surf = font_small.render(f"Score: {int(score)}", True, (255, 255, 255))
        screen.blit(score_surf, (16, 12))
        time_left = max(0, TIME_LIMIT - play_time)
        timer_surf = font_small.render(f"Time: {time_left:.1f}", True, (180, 220, 255))
        screen.blit(timer_surf, (16, 48))

    elif state == GAME_OVER:
        over = font_big.render("Game Over", True, (255, 100, 100))
        final = font_small.render(f"Final score: {int(score)}", True, (255, 255, 255))
        hint = font_small.render("Press SPACE for title", True, (200, 200, 220))
        screen.blit(over, over.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50)))
        screen.blit(final, final.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10)))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50)))

    pygame.display.flip()

pygame.quit()
```

---

## Запуск кода

```text
cd course-3-game-dev\block-2-player-controls-animations\lesson-2-4-game-states
python starter\game.py
```

**Ожидаемый результат (визуально):** Полный автомат состояний — титул, игра, game over, возврат.

---

## Быстрые упражнения

1. **Длиннее раунд** — `TIME_LIMIT = 30`.
2. **Фраза** — если на Game Over `score < 20`, blit «Тренируйся ещё!».
3. **ESC выход** — на Start `K_ESCAPE` ставит `running = False`.

---

## Задание для практики

**Квест:** Режиссёр сцен

1. Закрой TODO в [starter/game.py](starter/game.py): `state = START`, переходы SPACE, таймаут → `GAME_OVER`.
2. Пройди полный круг: титул → игра → over → титул.
3. **Бонус:** С Game Over SPACE сразу в `PLAYING` (без титула) — или оставь титул; решение опиши в комментарии.

**Самопроверка:** Все три экрана? SPACE в обе стороны? Таймер заканчивает раунд? ✓

**Эталонное решение:** [solution/game.py](solution/game.py)

---

## Уголок отладки

**Проблема:** SPACE во время игры мигает меню, или титул сразу проскакивает.

**Причина:** Для меню использовал `get_pressed()[K_SPACE]` (True много кадров) или забыл сменить `state` / starter остался на `PLAYING`.

**Исправление:** Подтверждение меню → только **`KEYDOWN`**. Непрерывное движение → `get_pressed`. Начальный `state = START`. Сбрасывай счёт/время при входе в `PLAYING`.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. Зачем переменная `state`?
   - **a)** Чтобы ставить шрифты
   - **b)** Чтобы одна программа показывала разные экраны / поведение
   - **c)** Чтобы удалить `dt`
   - **d)** Чтобы заменить Python

2. Лучший ввод для «Press SPACE to start»?
   - **a)** `get_pressed` каждый кадр без осторожности
   - **b)** Событие `KEYDOWN` (один раз)
   - **c)** Только мышь
   - **d)** `pip install space`

3. Зачем сбрасывать `score` и `play_time` при входе в PLAYING?
   - **a)** Чтобы каждый раунд начинался заново
   - **b)** Потому что Pygame запрещает старые переменные
   - **c)** Чтобы закрыть окно
   - **d)** Чтобы грузить PNG

4. Что делать, когда `play_time >= TIME_LIMIT`?
   - **a)** Установить Turtle
   - **b)** Переключить `state` на game over
   - **c)** Удалить шрифт
   - **d)** Зависнуть без UI

5. Движение стрелками в PLAYING должно использовать…
   - **a)** Только `QUIT`
   - **b)** `get_pressed()` для удержания
   - **c)** `render` без blit
   - **d)** Второй `pygame.init()`

---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **b)** Состояния аккуратно разделяют титул, игру и game over.
2. **b)** Одноразовый KEYDOWN не повторяет переход каждый кадр.
3. **a)** Честные повторяемые раунды.
4. **b)** Время вышло → экран game over.
5. **b)** Удержание стрелок по-прежнему через get_pressed.

</details>

---

## Что дальше

→ [Оглавление Блока 2](../README.md) — отметь чек-лист готовности Блока 2!  
→ **Блок 3 (план):** столкновения, **Catch the Falling Stars**, полировка.

---

*Занавес Блока 2 — ты срежиссировал всё шоу!*

[← Выбрать язык](README.md)
