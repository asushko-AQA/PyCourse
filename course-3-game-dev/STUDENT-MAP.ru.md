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
│   └── block-2-player-controls-animations/
│       ├── lesson-2-1-keyboard-events/
│       ├── lesson-2-2-images-sprites/
│       ├── lesson-2-3-score-text-rendering/
│       └── lesson-2-4-game-states/
└── .venv/                           ← ТЫ создаёшь (или переиспользуешь из Курса 2)
```

---

## Путь B — нет полного репозитория?

| Урок | Вместо длинного `cd`… |
|------|------------------------|
| 1.1–2.4 | Скопируй папку `starter/` куда угодно; активируй venv с Pygame; `cd` туда перед запуском |

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
- [ ] 3.1–3.3 — *(позже)*

---

## Чек-лист выпуска Курса 3 (весь курс)

1. [ ] Все уроки Блоков 1–3 отмечены  
2. [ ] Капстоун **Catch the Falling Stars** работает целиком  
3. [ ] Родитель или учитель сыграл один раунд  

→ [Оглавление Курса 3](README.md)

---

[← Курс 2](../course-2-web-apps/README.md)
