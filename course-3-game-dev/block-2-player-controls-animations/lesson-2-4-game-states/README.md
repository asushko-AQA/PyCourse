# Lesson 2.4: Game States

> **Course:** Game Development with Python  
> **Block:** Player Controls & Animations  
> **Time:** ~35–40 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level 8 — Stage Director |
| **[Русский →](ru.md)** | Уровень 8 — Режиссёр сцен |

---

## What you'll build / Что ты создашь

**EN:** Three screens in one program: **Start** → **Playing** (15-second round) → **Game Over**, then back to Start with SPACE.

**Expected flow (sketch):**

```text
[ Title + Press SPACE ] --SPACE--> [ Move + Score + Timer ]
                                         |
                                    time up
                                         v
                               [ Game Over + SPACE ]
                                         |
                                      SPACE
                                         v
                               [ Title again ]
```

**RU:** Три экрана в одной программе: **Старт** → **Игра** (раунд 15 секунд) → **Game Over**, затем снова Старт по SPACE.

## What you'll learn / Что ты узнаешь

- A `state` string (or constants) controlling what one frame does
- `KEYDOWN` for menu confirm (SPACE / RETURN) vs `get_pressed` for play
- Reset score / timer / position when starting a round
- Draw different UI per state

## Before you start / Перед стартом

- [ ] [Lesson 2.3](../lesson-2-3-score-text-rendering/README.md) — font + score
- [ ] Comfortable with `if` / `elif` from Course 1

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | Skeleton — TODOs for state switches |
| [solution/game.py](solution/game.py) | Full start → play → over loop |

## Quick drills / Быстрые упражнения

1. Change `TIME_LIMIT` from `15` to `30` for a longer round.
2. On Game Over, show a cheeky message if `score < 20`.
3. Allow `ESC` on Start to quit (`running = False`).

---

**Previous / Предыдущий урок:** [Lesson 2.3 — Score & Text Rendering](../lesson-2-3-score-text-rendering/README.md)

**Next / Дальше:** [Block 2 index](../README.md) — tick the readiness checklist! Block 3 is planned next.
