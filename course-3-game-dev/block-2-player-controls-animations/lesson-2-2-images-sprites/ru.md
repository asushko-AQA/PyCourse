# Урок 2.2: Изображения и спрайты

> **Курс:** Разработка игр на Python · **Блок:** Управление игроком и анимации · **~30–40 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 35
-->

---

## Title

**Уровень 6 — Призыватель спрайтов**

---

## Объяснение

**Спрайт** — картинка на игровом окне: герой, монета, звезда. В Pygame:

1. **Загрузить** картинку в `Surface`
2. Следить за местом через **`Rect`**
3. Каждый кадр **blit** (штамповать) на экран

```python
player = pygame.image.load("player.png").convert_alpha()
player_rect = player.get_rect()
screen.blit(player, player_rect)
```

`.convert_alpha()` ускоряет отрисовку и сохраняет прозрачность PNG.

**Совет про путь:** если запускаешь из другой папки, `"player.png"` может не найтись. В starter используется `os.path` рядом со скриптом — загрузка работает надёжнее.

---

### Шаг 1: Проверь, что player.png на месте

В [starter/](starter/) должны быть `game.py` **и** `player.png`. Открой [starter/game.py](starter/game.py).

---

### Шаг 2: Загрузи картинку один раз (до цикла)

```python
HERE = os.path.dirname(os.path.abspath(__file__))
player = pygame.image.load(os.path.join(HERE, "player.png")).convert_alpha()
player_rect = player.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT // 2)
```

Загружай **один раз** вне цикла — каждый кадр грузить медленно и бессмысленно.

---

### Шаг 3: Blit вместо draw.rect

После `screen.fill(...)`:

```python
screen.blit(player, player_rect)
```

Убери временный `draw.rect`.

---

### Шаг 4: Двигай rect стрелками (уже набросано)

В starter уже двигаются `player_rect.x` / `.y` и есть `clamp_ip`. Оставь это — меняешь только **как** рисуешь героя.

---

### Шаг 5: Запуск

```text
cd course-3-game-dev\block-2-player-controls-animations\lesson-2-2-images-sprites
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Ожидаемый результат (визуально):** Бирюзовый корабль-спрайт вместо квадрата; стрелки двигают; на экране остаётся.

---

## Пример кода

**Файл: [solution/game.py](solution/game.py)**

```python
import pygame
import os

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Summoner")

clock = pygame.time.Clock()
running = True

HERE = os.path.dirname(os.path.abspath(__file__))
player = pygame.image.load(os.path.join(HERE, "player.png")).convert_alpha()
player_rect = player.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT // 2)

speed = 250

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= int(speed * dt)
    if keys[pygame.K_RIGHT]:
        player_rect.x += int(speed * dt)
    if keys[pygame.K_UP]:
        player_rect.y -= int(speed * dt)
    if keys[pygame.K_DOWN]:
        player_rect.y += int(speed * dt)

    player_rect.clamp_ip(screen.get_rect())

    screen.fill((15, 18, 32))
    screen.blit(player, player_rect)
    pygame.display.flip()

pygame.quit()
```

---

## Запуск кода

```text
cd course-3-game-dev\block-2-player-controls-animations\lesson-2-2-images-sprites
python starter\game.py
```

**Ожидаемый результат (визуально):** Спрайт-корабль едет стрелками; без золотого квадрата, когда blit подключён.

---

## Быстрые упражнения

1. **Больше корабль** — `pygame.transform.scale(player, (72, 72))` после загрузки (пересобери `player_rect`).
2. **Зеркало** — при движении влево blit перевёрнутой копии.
3. **Декор** — второй маленький blit в углу как «звезда».

---

## Задание для практики

**Квест:** Призыватель спрайтов

1. Закрой TODO в [starter/game.py](starter/game.py): загрузи `player.png`, blit, убери запасной rect.
2. Проверь, что стрелки и `clamp_ip` работают.
3. **Бонус:** Замени `player.png` на свой арт 48×48 (или со scale) — имя файла оставь или обнови путь.

**Самопроверка:** PNG виден? Прозрачность ок? Клавиши работают? ✓

**Эталонное решение:** [solution/game.py](solution/game.py)

---

## Уголок отладки

**Проблема:** `FileNotFoundError: No such file or directory: 'player.png'`

**Причина:** Python ищет файл относительно **текущей папки** (откуда вызвал `python`), а не всегда рядом с `game.py`.

**Исправление:** Используй шаблон starter с `HERE = os.path.dirname(...)` **или** сделай `cd` в папку, где лежат и `game.py`, и `player.png`.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. Что делает `screen.blit(player, player_rect)`?
   - **a)** Удаляет файл картинки
   - **b)** Штампует картинку на экран в позиции rect
   - **c)** Устанавливает Pygame
   - **d)** Закрывает окно

2. Зачем `.convert_alpha()` после загрузки PNG?
   - **a)** Чтобы рисовать быстрее и сохранить прозрачность
   - **b)** Чтобы удалить Turtle
   - **c)** Чтобы создать venv
   - **d)** Чтобы перевернуть экран

3. Где загружать картинку?
   - **a)** Каждый кадр внутри цикла
   - **b)** Один раз до игрового цикла
   - **c)** После `pygame.quit()`
   - **d)** Только в README

4. Что даёт `player.get_rect()`?
   - **a)** Rect размером с картинку (для позиции)
   - **b)** RGB одного пикселя
   - **c)** Новый шрифт
   - **d)** Дельта-время

5. `player_rect.clamp_ip(screen.get_rect())` …
   - **a)** Играет звук
   - **b)** Держит rect спрайта внутри окна
   - **c)** Грузит другой PNG
   - **d)** Ставит FPS = 1

---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **b)** Blit копирует поверхность на поверхность дисплея.
2. **a)** Convert готовит поверхность к быстрым blit с альфой.
3. **b)** Загрузи один раз; blit — много раз.
4. **a)** Rect, который можно двигать и clamp.
5. **b)** Clamp держит героя на экране.

</details>

---

## Что дальше

→ [Урок 2.3: Счёт и вывод текста](../lesson-2-3-score-text-rendering/README.md) — живой счёт на HUD через `font.render`.

---

*Корабль явился. Дальше — зажжём счёт на табло!*

[← Выбрать язык](README.md)
