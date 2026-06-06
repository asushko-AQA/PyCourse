# Урок 4.2: Списки

> **Курс:** Основы Python и командная строка · **Блок:** Организация кода · **~30–45 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Уровень 16 — Рюкзак приключений**

---

## Объяснение

Каждому искателю приключений нужен **рюкзак**. В Python **список** — упорядоченная коллекция, как слоты в сумке, где у каждого предмета есть номер — **индекс**.

```python
inventory = ["torch", "rope"]
```

- Индекс `0` — `"torch"` (первый предмет)
- Индекс `1` — `"rope"` (второй предмет)

Используй `.append()`, чтобы добавить предмет в конец:

```python
inventory.append("key")
```

**Путь A — репозиторий PyCourse:**

```text
cd course-1-python-basics\block-4-organizing-code\lesson-4-2-lists
```

**Путь B — своя папка:** Скопируй [starter/inventory.py](starter/inventory.py) куда угодно. Запускай из этой папки.

---

### Шаг 1: Открой inventory.py

Открой [starter/inventory.py](starter/inventory.py). Два предмета уже в рюкзаке.

---

### Шаг 2: Добавь предмет

Допиши или раскомментируй строку `.append("key")`. Список вырастет на один слот.

---

### Шаг 3: Напечатай нумерованный список

Используй цикл `for` с `range(len(inventory))`, чтобы пройти по каждому индексу:

```python
for i in range(len(inventory)):
    print(f"{i + 1}. {inventory[i]}")
```

Мы прибавляем 1 к `i`, чтобы игрок видел `1. torch`, а не `0. torch`.

---

### Шаг 4: Запусти скрипт

```text
python starter\inventory.py
```

**Mac/Linux:** используй прямые слэши — `python starter/inventory.py`. Список файлов — `ls` вместо `dir`.

**Ожидаемый вывод:**

```text
=== INVENTORY ===
1. torch
2. rope
3. key
You are carrying 3 items.
```

---

## Пример кода

**Файл: [starter/inventory.py](starter/inventory.py)**

```python
inventory = ["torch", "rope"]
inventory.append("key")

print("=== INVENTORY ===")

for i in range(len(inventory)):
    print(f"{i + 1}. {inventory[i]}")

print(f"You are carrying {len(inventory)} items.")
```

---

## Запуск кода

```text
cd course-1-python-basics\block-4-organizing-code\lesson-4-2-lists
python starter\inventory.py
```

Ввод с клавиатуры не нужен — вывод появится сразу.

---

## Быстрые упражнения

1. **Больше снаряжения** — `.append("map")` и `.append("potion")`. Сколько предметов теперь?
2. **Первый слот** — добавь `print("First item:", inventory[0])` перед циклом.
3. **Пустой список** — начни с `inventory = []` и добавь три предмета сам.

---

## Практическое задание

**Название квеста:** Полный набор искателя

1. Начни минимум с четырёх предметов в тему твоего приключения.
2. Напечатай заголовок `=== INVENTORY ===`.
3. После нумерованного списка выведи **последний** предмет отрицательным индексом: `inventory[-1]`.

**Бонусный квест:** См. [exercises/high_score.ru.md](exercises/high_score.ru.md) — список рекордов.

**Эталонное решение:** [solution/inventory.py](solution/inventory.py)

---

## Отладка

**Проблема:** `IndexError: list index out of range`, когда печатаешь `inventory[3]`, а в списке только три предмета (индексы 0, 1, 2).

**Причина:** Индексы списка начинаются с **0**. Список из 3 предметов имеет индексы `0`, `1` и `2` — не `3`.

**Исправление:** Используй `inventory[-1]` для последнего предмета или `len(inventory) - 1` для последнего индекса.

---

## Что дальше

→ [Урок 4.3: Словари](../lesson-4-3-dictionaries/README.md) — храни статы персонажа с подписанными ключами.

---

*Рюкзак организован. Дальше — словари со статами!*

[← Выбрать язык](README.md)
