# Урок 3.4: паттерны циклов

> **Курс:** Python Basics · **Блок:** Выбор и повторение · **~30–45 мин**  
> [Выбор языка](README.md) · [English →](en.md)

---

## Заголовок

**Уровень 14 — Узор из звёзд**

---

## Объяснение

**Финал блока 3!** Вложенные циклы рисуют узоры в терминале.

```python
for row in range(1, 6):
    for star in range(row):
        print("*", end="")
    print()
```

- `range(1, 6)` → строки 1–5 (6 **не** включается)
- Внутренний цикл печатает `row` звёзд в строке
- `print()` без аргументов — новая строка
- `end=""` — звёзды в одной строке

---

### Шаг 1: Открой ascii_pattern.py

Открой [starter/ascii_pattern.py](starter/ascii_pattern.py).

---

### Шаг 2: Запусти

**Путь A:**

```text
cd course-1-python-basics\block-3-making-choices\lesson-3-4-loop-patterns
python starter\ascii_pattern.py
```

**Mac/Linux:** используй прямые слэши — `python starter/ascii_pattern.py`. Список файлов — `ls` вместо `dir`.

**Ожидаемый вывод:**

```text
=== ASCII PATTERN ===
*
**
***
****
*****
Pattern complete!
```

---

## Пример кода

См. [starter/ascii_pattern.py](starter/ascii_pattern.py) и [solution/ascii_pattern.py](solution/ascii_pattern.py).

---

## Запуск кода

```text
cd course-1-python-basics\block-3-making-choices\lesson-3-4-loop-patterns
python starter\ascii_pattern.py
```

---

## Быстрые упражнения

1. `range(1, 4)` — сколько строк?
2. Замени `"*"` на `"#"`.
3. Отметь [чеклист блока 3](../README.md#block-3-readiness-checklist).

---

## Практическое задание

1. Пирамида из **6** строк (`range(1, 7)`).
2. Попробуй **квадрат** 5×5 (см. [exercises/pattern_variations.ru.md](exercises/pattern_variations.ru.md)).
3. Отметь чеклист блока 3.

**Эталон:** [solution/ascii_pattern.py](solution/ascii_pattern.py)

---

## Уголок отладки

**Проблема:** Лишняя или недостающая строка.

**Причина:** **Off-by-one** — `range(1, 5)` даёт 4 строки, не 5. Число **stop** не входит.

**Исправление:** Для 5 строк — `range(1, 6)`.

---

## Что дальше

→ [Урок 4.1: функции](../../block-4-organizing-code/lesson-4-1-functions/README.md)

---

[← Выбор языка](README.md)
