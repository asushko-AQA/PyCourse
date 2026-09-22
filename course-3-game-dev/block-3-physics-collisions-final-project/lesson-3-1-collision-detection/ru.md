# Урок 3.1: Обнаружение столкновений

> **Курс:** Разработка игр на Python · **Блок:** Физика и столкновения (финальный проект) · **~30–35 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 30
-->

---

## Title

**Уровень 9 — Сборщик монет**

---

## Объяснение

Игра оживает, когда объекты **касаются**. В Pygame у каждой картинки есть **Rect**. Два прямоугольника пересекаются, если:

```python
if player.colliderect(coin):
    # касание!
```

| Идея | Смысл |
|------|--------|
| `colliderect` | True, если прямоугольники перекрываются |
| После попадания | Перенеси монету — иначе очки сыпятся каждый кадр |
| Те же инструменты | Стрелки = `get_pressed`, движение = `speed * dt`, HUD = `font.render` |

Сегодня — мини **сборщик монет**: коснулся → `score += 1` → монета телепортируется.

---

### Шаг 1: Открой starter/game.py

Открой [starter/game.py](starter/game.py). Движение, картинка монеты и HUD уже есть. Твоя задача — TODO со **столкновением**.

---

### Шаг 2: Проверь пересечение

```python
if player.colliderect(coin):
    score += 1
```

Запусти и заметь: если **стоять на монете**, счёт взрывается. Дальше это чиним.

---

### Шаг 3: Перенеси монету после сбора

```python
if player.colliderect(coin):
    score += 1
    coin.center = (
        random.randint(40, WIDTH - 40),
        random.randint(40, HEIGHT - 120),
    )
```

Теперь одно касание = один чистый сбор.

---

### Шаг 4: Запуск

```text
cd course-3-game-dev\block-3-physics-collisions-final-project\lesson-3-1-collision-detection
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Ожидаемый результат (на экране):** Синий бокс двигается; золотая монета; `Coins: N` растёт на 1 за касание; монета прыгает.

---

## Пример кода

**Файл: [solution/game.py](solution/game.py)**

```python
import pygame
import os
import random

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Collector")

clock = pygame.time.Clock()
running = True

HERE = os.path.dirname(os.path.abspath(__file__))

player = pygame.Rect(0, 0, 48, 48)
player.center = (WIDTH // 2, HEIGHT - 60)
speed = 280

coin_img = pygame.image.load(os.path.join(HERE, "coin.png")).convert_alpha()
coin = coin_img.get_rect()
coin.center = (random.randint(40, WIDTH - 40), random.randint(40, HEIGHT - 120))

score = 0
font = pygame.font.Font(None, 36)

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= int(speed * dt)
    if keys[pygame.K_RIGHT]:
        player.x += int(speed * dt)
    if keys[pygame.K_UP]:
        player.y -= int(speed * dt)
    if keys[pygame.K_DOWN]:
        player.y += int(speed * dt)

    player.clamp_ip(screen.get_rect())

    if player.colliderect(coin):
        score += 1
        coin.center = (
            random.randint(40, WIDTH - 40),
            random.randint(40, HEIGHT - 120),
        )

    screen.fill((18, 22, 40))
    pygame.draw.rect(screen, (80, 200, 255), player)
    screen.blit(coin_img, coin)
    score_surf = font.render(f"Coins: {score}", True, (255, 255, 255))
    screen.blit(score_surf, (16, 12))
    hint = font.render("Touch the coin!", True, (180, 190, 210))
    screen.blit(hint, (16, 48))

    pygame.display.flip()

pygame.quit()
```

---

## Запуск кода

```text
cd course-3-game-dev\block-3-physics-collisions-final-project\lesson-3-1-collision-detection
python starter\game.py
```

**Ожидаемый результат (на экране):** Собираешь монеты; счёт +1 за касание; монета перемещается.

---

## Быстрые упражнения

1. **Отладочный print** — `print("got one!", score)` внутри ветки попадания (потом убери).
2. **Быстрее игрок** — попробуй `speed = 400`.
3. **Монета у краёв** — сузь `randint`, чтобы монета не пряталась под HUD.

---

## Задание для практики

**Название квеста:** Сборщик монет

1. Доделай TODO в [starter/game.py](starter/game.py): `colliderect` → очко → перенос монеты.
2. Собери минимум **5** монет за один запуск.
3. **Бонус:** `print("bling!")` в терминал при каждом сборе (звук — в 3.3).

**Самопроверка:** Монета уезжает после касания? Счёт +1 один раз (не каждый кадр)? Окно закрывается крестиком? ✓

**Эталонное решение:** [solution/game.py](solution/game.py)

---

## Уголок отладки

**Проблема:** Счёт скачет на сотни, пока стоишь на монете.

**Причина:** Перекрытие True каждый кадр; монету не убрали (или снова положили на игрока).

**Исправление:** После очка задай новый `coin.center` подальше. Можно требовать «отлипания» перед следующим сбором.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. Что вернёт `player.colliderect(coin)`, когда они пересекаются?
   - **a)** Файл PNG
   - **b)** `True`
   - **c)** Всегда `False`
   - **d)** Размер шрифта

2. Зачем переносить монету после сбора?
   - **a)** Чтобы снова ставить Pygame
   - **b)** Чтобы не начислять очки каждый кадр, пока идёт перекрытие
   - **c)** Чтобы удалить `dt`
   - **d)** Потому что Rect не может стоять

3. Непрерывное движение стрелками должно использовать…
   - **a)** Только `QUIT`
   - **b)** `get_pressed()` (удержание)
   - **c)** Только `mixer.Sound`
   - **d)** Второе окно

4. Где обычно лежит `coin.png` в этом уроке?
   - **a)** Рядом с `game.py` в `starter/` / `solution/`
   - **b)** Внутри `pygame.init`
   - **c)** Только на сайте
   - **d)** В Turtle Курса 1

5. Что здесь за AABB-столкновение?
   - **a)** Точное совпадение пикселей
   - **b)** Перекрытие выровненных прямоугольников (`colliderect`)
   - **c)** 3D-физика
   - **d)** Закрытие окна

---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **b)** Перекрытие → True.
2. **b)** Перенос, чтобы одно касание = одно очко.
3. **b)** Удержание стрелок → get_pressed.
4. **a)** Ассет рядом со скриптом (путь через `HERE`).
5. **b)** Простой тест «коробка на коробку».

</details>

---

## Что дальше

→ [Урок 3.2 — Поймай падающие звёзды](../lesson-3-2-catch-the-falling-stars/README.md) — полный капстоун мини-игры!

---

*Собрал монету? Готов к падающим звёздам!*

[← Выбрать язык](README.md)
