# Lesson 5.1: Turtle Basics

> **Course:** Python Basics & Command Line Magic  
> **Block:** Creative Python with Turtle  
> **Time:** ~30–45 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level 19 — Shape Sketcher |
| **[Русский →](ru.md)** | Уровень 19 — Рисовальщик фигур |

---

## What you'll build / Что ты создашь

**EN:** A `shapes.py` script that opens a Turtle drawing window, draws a square and a triangle, and keeps the window open until you close it.

**Expected window (sketch):**

```text
    +--------+
    |        |   square (black line)
    |        |
    +--------+
          /\       triangle beside it
         /  \
        /____\
```

**RU:** Скрипт `shapes.py` — окно Turtle, квадрат и треугольник.

## What you'll learn / Что ты узнаешь

- `import turtle` and create a turtle with `turtle.Turtle()`
- Move with `forward()` and turn with `left()`
- Repeat steps with a `for` loop (four sides, then three)
- Keep the canvas open with `turtle.done()`

## Before you start / Перед стартом

- [ ] Completed [Block 4](../../block-4-organizing-code/README.md) and the [readiness checklist](../../block-4-organizing-code/README.md#block-4-readiness-checklist)
- [ ] You know loops from [Lesson 3.3](../../block-3-making-choices/lesson-3-3-for-and-while-loops/README.md)

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/shapes.py](starter/shapes.py) | Skeleton with TODO comments |
| [solution/shapes.py](solution/shapes.py) | Reference solution |

## Quick drills / Быстрые упражнения

1. Change `forward(100)` to `forward(50)` — predict how the shapes shrink before you run.
2. Change `left(90)` on the square to `left(72)` — what happens to the shape?
3. Comment out `turtle.done()` — run once, then put it back.

---

**Previous / Предыдущий урок:** [Block 4: Organizing Code](../../block-4-organizing-code/README.md)

**Next lesson / Следующий урок:** [Lesson 5.2 — Loops and Color](../lesson-5-2-loops-and-color/README.md)
