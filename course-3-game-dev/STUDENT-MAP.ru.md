# Карта ученика — папки Курса 3

> **Курс:** Разработка игр на Python  
> [English →](STUDENT-MAP.md)

Эта карта поможет, если урок пишет `cd course-3-game-dev\...`, а у тебя другая структура папок.

---

## Дерево папок PyCourse (Путь A)

```text
PyCourse/
├── course-1-python-basics/          ← обязательный фундамент
├── course-2-web-apps/               ← полезно (venv), но не обязательно
├── course-3-game-dev/
│   ├── README.md                    ← оглавление Курса 3
│   ├── STUDENT-MAP.ru.md
│   ├── block-1-getting-started-pygame/
│   │   ├── lesson-1-1-install-pygame-game-loop/
│   │   ├── lesson-1-2-game-window-colors/
│   │   ├── lesson-1-3-shapes-coordinates/
│   │   └── lesson-1-4-delta-time-smooth-movement/
│   ├── block-2-player-controls-animations/
│   │   ├── lesson-2-1-keyboard-events/
│   │   ├── lesson-2-2-images-sprites/
│   │   ├── lesson-2-3-score-text-rendering/
│   │   └── lesson-2-4-game-states/
│   ├── block-3-physics-collisions-final-project/
│   │   ├── lesson-3-1-collision-detection/
│   │   ├── lesson-3-2-catch-the-falling-stars/
│   │   └── lesson-3-3-polish/
│   └── block-4-bonus-star-projects/  ← опциональный ★ бонус после Блока 3
│       ├── lesson-4-1-sky-hopper-gravity-flap/
│       ├── lesson-4-2-scrolling-gateways/
│       ├── lesson-4-3-sky-hopper-complete/
│       ├── lesson-4-4-prism-dash-auto-scroll/
│       ├── lesson-4-5-prism-dash-jump-rotate/
│       ├── lesson-4-6-prism-dash-complete/
│       ├── lesson-4-7-shard-stack-grid-cells/
│       ├── lesson-4-8-shard-stack-falling-pieces/
│       ├── lesson-4-9-shard-stack-complete/
│       ├── lesson-4-10-glyph-grove-tiles-layout/
│       ├── lesson-4-11-glyph-grove-mouse-matching/
│       └── lesson-4-12-glyph-grove-complete/
│   └── block-5-bonus-star-projects-2/  ← опциональный ★ II после Блока 4
│       ├── lesson-5-1-glow-worm-grid-segments/
│       ├── lesson-5-2-glow-worm-food-growth/
│       ├── lesson-5-3-glow-worm-complete/
│       ├── lesson-5-4-bounce-forge-ball-walls/
│       ├── lesson-5-5-bounce-forge-paddle-lives/
│       ├── lesson-5-6-bounce-forge-bricks-score/
│       └── lesson-5-7-bounce-forge-complete/
└── .venv/                           ← ТЫ создаёшь (или переиспользуешь из Курса 2)
```

---

## Путь B — нет полного репозитория?

| Урок | Вместо длинного `cd`… |
|------|------------------------|
| 1.1–5.37 | Скопируй папку `starter/` куда угодно; активируй venv с Pygame; `cd` туда перед запуском |

---

## Напоминание про виртуальное окружение

С Курса 2 пакеты ставим **внутрь** `.venv`, не глобально.

```text
python -m venv .venv
.venv\Scripts\Activate.ps1          # Windows PowerShell
pip install pygame
```

**Mac/Linux:** `source .venv/bin/activate`, затем `pip install pygame`.

Можно взять `.venv` из Курса 2 и просто сделать `pip install pygame`.

---

## Чек-лист прогресса

- [ ] 1.1 — Pygame установлен; окно открывается и закрывается крестиком
- [ ] 1.2 — Фон заливается цветом; цвет меняется каждый кадр
- [ ] 1.3 — Прямоугольник двигается по окну через `x` / `y`
- [ ] 1.4 — Движение через `dt = clock.tick(60) / 1000` (плавно на любом ПК)
- [ ] 2.1 — Стрелки двигают игрока через `get_pressed`
- [ ] 2.2 — PNG-спрайт загружается через `pygame.image.load` и `blit`
- [ ] 2.3 — Счёт выводится через `font.render` + `blit`
- [ ] 2.4 — Есть start → playing → game over; SPACE перезапускает
- [ ] 3.1 — `rect.colliderect()` собирает монету и переносит её
- [ ] 3.2 — Капстоун: звёзды появляются, падают, ловятся, счёт обновляется, перезапуск работает
- [ ] 3.3 — Полировка: рекорд (сессия), рост сложности, опциональные звуки catch/miss

### Опциональный ★ Блок 4 — Sky Hopper

- [ ] 4.1 — Гравитация и взмах, птица из фигур
- [ ] 4.2 — Прокрутка ворот, счёт, crash
- [ ] 4.3 — Полный Sky Hopper: титул / игра / game over, рекорд, рамп скорости

### Опциональный ★ Блок 4 — Prism Dash

- [ ] 4.4 — Прокрутка `world_x`; куб на фиксированном X
- [ ] 4.5 — Прыжок с земли; вращение в воздухе
- [ ] 4.6 — Полный Prism Dash: строка уровня, шипы, прогресс %, попытки, лучший %

### Опциональный ★ Блок 4 — Shard Stack

- [ ] 4.7 — 2D-список `grid`; рисование колодца и смещений
- [ ] 4.8 — `can_move`, таймер падения, `lock_piece`
- [ ] 4.9 — Полный Shard Stack: поворот, линии, счёт, рекорд

### Опциональный ★ Блок 4 — Glyph Grove

- [ ] 4.10 — Словари плиток; слои; знаки через шрифт
- [ ] 4.11 — Мышь; правило «свободной» плитки; пары
- [ ] 4.12 — Полный Glyph Grove: подсказка, shuffle, таймер, лучшее время

### Опциональный ★ Блок 5 II — Glow Worm

- [ ] 5.1 — Список `segments`; `(col, row)`; направление; шаг по таймеру
- [ ] 5.2 — Еда; рост хвоста; стена и самоудар
- [ ] 5.3 — Полный Glow Worm: титул / игра / game over, счёт, ускорение, рекорд сессии

### Опциональный ★ Блок 5 II — Bounce Forge

- [ ] 5.4 — `ball_vx` / `ball_vy` и отскоки от стен (искра)
- [ ] 5.5 — Ракетка-наковальня, угол `hit_frac`, жизни
- [ ] 5.6 — Список кирпичей `Rect`, сторона удара, счёт
- [ ] 5.7 — Полный Bounce Forge: уровни, рекорд, Pong по **P**

---

## Чек-лист выпуска Курса 3 (весь курс)

1. [ ] Все уроки Блоков 1–3 отмечены  
2. [ ] Капстоун **Catch the Falling Stars** работает целиком  
3. [ ] Родитель или учитель сыграл один раунд  

**★ Бонус:** пройди Блок 4 и покажи **Sky Hopper**, **Prism Dash**, **Shard Stack** и **Glyph Grove** — все четыре ★ аркады блока 4!

**★ II Бонус:** продолжи в Блоке 5 с **Glow Worm** и **Bounce Forge** (ещё ★ игры — *скоро* на README блока).

→ [Оглавление Курса 3](README.md)

---

[← Курс 2](../course-2-web-apps/README.md)
