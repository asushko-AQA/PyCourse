# Урок 2.1: События клавиатуры

> **Курс:** Разработка игр на Python · **Блок:** Управление игроком и анимации · **~30–35 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 30
-->

---

## Title

**Уровень 5 — Капитан клавиш**

---

## Объяснение

До сих пор коробка ехала **сама**. В настоящих играх ждут **тебя**.

В Pygame два стиля клавиатуры:

| Стиль | Когда | API |
|-------|-------|-----|
| Одно нажатие | Меню, прыжок один раз | `event.type == KEYDOWN` |
| **Удержание** | Идти / лететь, пока держишь | `pygame.key.get_pressed()` |

Для капитана, который летит, пока стрелка зажата, нужен **`get_pressed()`**:

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    x = x - speed * dt
```

`keys[...]` равен `True` каждый кадр, пока клавиша зажата. Складывай с **`speed * dt`**, чтобы движение оставалось плавным (урок 1.4).

---

### Шаг 1: Открой starter/game.py

Открой [starter/game.py](starter/game.py). Окно, `dt`, отрисовка и выход готовы. TODO: читать клавиши и двигать `x` / `y`.

---

### Шаг 2: Читай зажатые клавиши каждый кадр

После цикла событий:

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    x = x - speed * dt
if keys[pygame.K_RIGHT]:
    x = x + speed * dt
if keys[pygame.K_UP]:
    y = y - speed * dt
if keys[pygame.K_DOWN]:
    y = y + speed * dt
```

Помни: **вверх** уменьшает `y` (начало координат — слева сверху!).

---

### Шаг 3: Держи коробку на экране (clamp)

```python
x = max(0, min(x, WIDTH - box_w))
y = max(0, min(y, HEIGHT - box_h))
```

---

### Шаг 4: Запуск

```text
cd course-3-game-dev\block-2-player-controls-animations\lesson-2-1-keyboard-events
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Ожидаемый результат (визуально):** Золотой квадрат в центре; стрелки рулят; у краёв останавливается. Выход крестиком.

---

### Шаг 5: Совет про диагональ

LEFT+UP сразу — движение по диагонали: оба `if` срабатывают. Доп. код не нужен!

---

## Пример кода

**Файл: [solution/game.py](solution/game.py)**

```python
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Key Captain")

clock = pygame.time.Clock()
running = True

x = 295.0
y = 215.0
box_w = 50
box_h = 50
speed = 250

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    screen.fill((20, 24, 40))
    pygame.draw.rect(screen, (255, 200, 50), (int(x), int(y), box_w, box_h))
    pygame.display.flip()

pygame.quit()
```

---

## Запуск кода

```text
cd course-3-game-dev\block-2-player-controls-animations\lesson-2-1-keyboard-events
python starter\game.py
```

**Ожидаемый результат (визуально):** Управляемый золотой квадрат; края ограничивают; крестик закрывает окно.

---

## Быстрые упражнения

1. **Турбо** — `speed = 400`. Всё ещё управляемо?
2. **Двойник WASD** — также проверяй `K_a` / `K_d` / `K_w` / `K_s`.
3. **Медленный краул** — `speed = 80` и почувствуй разницу.

---

## Задание для практики

**Квест:** Капитан клавиш

1. Закрой TODO в [starter/game.py](starter/game.py): `get_pressed` + четыре стрелки.
2. Сделай clamp, чтобы квадрат не уезжал за окно.
3. **Бонус:** Меняй цвет, пока любая стрелка зажата.

**Самопроверка:** Стрелки двигают? Удержание продолжает движение? Края останавливают? ✓

**Эталонное решение:** [solution/game.py](solution/game.py)

---

## Уголок отладки

**Проблема:** Коробка только дёргается один раз при нажатии — не едет постоянно.

**Причина:** Обрабатываешь `KEYDOWN` в цикле событий (одно событие на нажатие), а не **`get_pressed()`** каждый кадр.

**Исправление:** После событий вызови `keys = pygame.key.get_pressed()` и используй `if keys[pygame.K_LEFT]:` каждый кадр.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. Какой вызов лучше для **непрерывного** движения при удержании клавиши?
   - **a)** Только `pygame.QUIT`
   - **b)** `pygame.key.get_pressed()`
   - **c)** `pip install keys`
   - **d)** `screen.fill(keys)`

2. Что значит `keys[pygame.K_UP] == True`?
   - **a)** Окно закрылось
   - **b)** Стрелка вверх сейчас зажата
   - **c)** Счёт вырос
   - **d)** Pygame не установился

3. Зачем умножать на `dt` при движении?
   - **a)** Чтобы закрыть окно
   - **b)** Чтобы скорость была в пикселях **в секунду**, плавно на любом FPS
   - **c)** Чтобы грузить картинки
   - **d)** Чтобы сменить заголовок

4. Увеличение `y` двигает игрока…
   - **a)** Вверх
   - **b)** Вниз
   - **c)** В venv
   - **d)** С клавиатуры

5. Что здесь делает clamp через `max` / `min`?
   - **a)** Ставит шрифты
   - **b)** Держит `x`/`y` внутри границ окна
   - **c)** Создаёт новую поверхность
   - **d)** Удаляет игровой цикл

---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **b)** `get_pressed()` сообщает о зажатых клавишах каждый кадр.
2. **b)** Флаг True, пока стрелка вверх зажата.
3. **b)** `speed * dt` — движение независимое от FPS.
4. **b)** В Pygame больше `y` — ниже на экране.
5. **b)** Clamp не даёт коробке уехать с поля.

</details>

---

## Что дальше

→ [Урок 2.2: Изображения и спрайты](../lesson-2-2-images-sprites/README.md) — заменим квадрат на настоящий спрайт.

---

*Штурвал у тебя. Дальше — дадим капитану лицо!*

[← Выбрать язык](README.md)
