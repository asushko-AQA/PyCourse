# Lesson 2.1: Keyboard Events

> **Course:** Game Development with Python  
> **Block:** Player Controls & Animations  
> **Time:** ~30–35 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level 5 — Key Captain |
| **[Русский →](ru.md)** | Уровень 5 — Капитан клавиш |

---

## What you'll build / Что ты создашь

**EN:** A gold player square you steer with the **arrow keys**. Hold a key — keep moving. Release — stop. The square stays inside the window.

**Expected window (sketch):**

```text
+---------------------------+
|                           |
|         [##]  <- arrows   |
|      hold = keep moving   |
|                           |
+---------------------------+
```

**RU:** Золотой квадрат-герой, которым ты рулишь **стрелками**. Держишь клавишу — едешь. Отпустил — стоп. Квадрат не уезжает за край окна.

## What you'll learn / Что ты узнаешь

- `pygame.key.get_pressed()` for **held** keys (continuous move)
- Arrow key constants: `K_LEFT`, `K_RIGHT`, `K_UP`, `K_DOWN`
- Combine with `speed * dt` from Lesson 1.4
- Clamp position so the player stays on screen

## Before you start / Перед стартом

- [ ] [Lesson 1.4](../../block-1-getting-started-pygame/lesson-1-4-delta-time-smooth-movement/README.md) — delta time
- [ ] Block 1 readiness checklist ticked

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | Skeleton — TODOs for key movement |
| [solution/game.py](solution/game.py) | Reference with clamp |

## Quick drills / Быстрые упражнения

1. Change `speed` from `250` to `400` — turbo captain!
2. Also allow `K_a` / `K_d` for left/right (bonus layout).
3. Print `keys[pygame.K_SPACE]` once to see `True`/`False` while held.

---

**Previous / Предыдущий урок:** [Lesson 1.4 — Delta Time](../../block-1-getting-started-pygame/lesson-1-4-delta-time-smooth-movement/README.md)

**Next lesson / Следующий урок:** [Lesson 2.2 — Images & Sprites](../lesson-2-2-images-sprites/README.md)
