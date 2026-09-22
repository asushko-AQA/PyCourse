# Урок 2.3: Счёт и вывод текста

> **Курс:** Разработка игр на Python · **Блок:** Управление игроком и анимации · **~30–35 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 30
-->

---

## Title

**Уровень 7 — Писарь очков**

---

## Объяснение

Играм нужен **HUD** (табло) — счёт, жизни, таймер. В Pygame текст — ещё одна **Surface**:

```python
font = pygame.font.Font(None, 36)  # None = шрифт по умолчанию
score_surf = font.render(f"Score: {int(score)}", True, (255, 255, 255))
screen.blit(score_surf, (16, 12))
```

| Часть | Смысл |
|-------|-------|
| `Font(None, 36)` | Шрифт по умолчанию, высота ~36 px |
| `render(text, True, color)` | Собрать Surface; `True` = сглаживание |
| `blit(..., (x, y))` | Штамп текста (левый верх Surface) |

Пересобирай текст, когда число меняется (для одной строки HUD каждый кадр — нормально).

Практика урока: **держи RIGHT** — копи очки (`score += rate * dt`), чтобы счётчик рос на глазах.

---

### Шаг 1: Открой starter/game.py

Открой [starter/game.py](starter/game.py). Движение и опциональный спрайт готовы. TODO: создать **Font**, **render** + **blit** счёта.

---

### Шаг 2: Создай Font один раз

До цикла:

```python
font = pygame.font.Font(None, 36)
```

---

### Шаг 3: Render и blit каждый кадр

После отрисовки игрока, до `flip`:

```python
score_surf = font.render(f"Score: {int(score)}", True, (255, 255, 255))
screen.blit(score_surf, (16, 12))
```

Используй `int(score)`, чтобы не показывать уродливые дроби вроде `12.38471`.

---

### Шаг 4: Очки (уже в starter)

Удержание RIGHT добавляет `score_rate * dt`. Тебе нужно только **показать** число.

---

### Шаг 5: Запуск

```text
cd course-3-game-dev\block-2-player-controls-animations\lesson-2-3-score-text-rendering
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Ожидаемый результат (визуально):** Игрок двигается; слева сверху белый `Score: N` растёт, пока держишь RIGHT.

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
pygame.display.set_caption("Score Scribbler")

clock = pygame.time.Clock()
running = True

HERE = os.path.dirname(os.path.abspath(__file__))
player_rect = pygame.Rect(0, 0, 48, 48)
player_rect.center = (WIDTH // 2, HEIGHT // 2)
player_img = None
sprite_path = os.path.join(HERE, "player.png")
if os.path.isfile(sprite_path):
    player_img = pygame.image.load(sprite_path).convert_alpha()
    player_rect = player_img.get_rect(center=player_rect.center)

speed = 250
score = 0.0
score_rate = 10

font = pygame.font.Font(None, 36)

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
        score = score + score_rate * dt
    if keys[pygame.K_UP]:
        player_rect.y -= int(speed * dt)
    if keys[pygame.K_DOWN]:
        player_rect.y += int(speed * dt)

    player_rect.clamp_ip(screen.get_rect())

    screen.fill((18, 22, 38))
    if player_img is not None:
        screen.blit(player_img, player_rect)
    else:
        pygame.draw.rect(screen, (255, 200, 50), player_rect)

    score_surf = font.render(f"Score: {int(score)}", True, (255, 255, 255))
    screen.blit(score_surf, (16, 12))
    pygame.display.flip()

pygame.quit()
```

---

## Запуск кода

```text
cd course-3-game-dev\block-2-player-controls-animations\lesson-2-3-score-text-rendering
python starter\game.py
```

**Ожидаемый результат (визуально):** HUD-счёт обновляется при RIGHT; крестик закрывает.

---

## Быстрые упражнения

1. **Неоновый HUD** — цвет `(80, 255, 120)`.
2. **Вторая строка** — blit `f"Rate: {score_rate}"` в `(16, 48)`.
3. **Сброс** — по `KEYDOWN` на `K_r` ставь `score = 0`.

---

## Задание для практики

**Квест:** Писарь очков

1. Закрой TODO в [starter/game.py](starter/game.py): создай `font`, render + blit `Score: …`.
2. Убедись, что число растёт при удержании RIGHT.
3. **Бонус:** Счёт по центру сверху (`score_surf.get_rect(midtop=(WIDTH // 2, 12))`).

**Самопроверка:** Текст виден? Живой? Движение работает? ✓

**Эталонное решение:** [solution/game.py](solution/game.py)

---

## Уголок отладки

**Проблема:** Вызываешь `font.render(...)`, но текста нет — только игрок.

**Причина:** Забыл **`blit`** возвращённой Surface, или blit **до** `fill` (заливка закрашивает), или цвет совпал с фоном.

**Исправление:** После `fill` и игрока: `screen.blit(score_surf, (16, 12))`, затем `flip`. Яркий цвет, например белый.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. Что возвращает `font.render(...)`?
   - **a)** Целое число очков
   - **b)** Surface, которую можно blit
   - **c)** Новое окно
   - **d)** Событие клавиатуры

2. Зачем `Font(None, 36)`?
   - **a)** Удалить все шрифты
   - **b)** Шрифт по умолчанию примерно размера 36
   - **c)** Установить Pygame
   - **d)** Задать FPS

3. Зачем в строке показывать `int(score)`?
   - **a)** Дроби нельзя складывать
   - **b)** Аккуратное целое на HUD вместо длинных дробей
   - **c)** Pygame запрещает f-строки
   - **d)** Это закрывает окно

4. Когда создавать объект Font?
   - **a)** Один раз до цикла (обычно)
   - **b)** Только после `quit`
   - **c)** Внутри `pip`
   - **d)** Никогда — текст рисуется сам

5. Текст невидим после render — сначала проверь:
   - **a)** Сделал ли ты `blit` поверхности после `fill`?
   - **b)** Удалил ли Python?
   - **c)** Удалил ли `dt`?
   - **d)** Переименовал ли курс?

---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **b)** `render` строит Surface с нарисованными буквами.
2. **b)** `None` — шрифт по умолчанию; `36` — размер.
3. **b)** Счёт храни как float; на экран — красивое целое.
4. **a)** Создай один раз; render/blit по нужде каждый кадр.
5. **a)** Один render не рисует — рисует blit.

</details>

---

## Что дальше

→ [Урок 2.4: Состояния игры](../lesson-2-4-game-states/README.md) — титульный экран, игра и game over.

---

*Счёт поёт. Дальше — режиссируй всю сцену!*

[← Выбрать язык](README.md)
