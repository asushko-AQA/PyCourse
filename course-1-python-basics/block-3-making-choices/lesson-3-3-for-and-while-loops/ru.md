# Урок 3.3: циклы for и while

> **Курс:** Python Basics · **Блок:** Выбор и повторение · **~45 мин**  
> [Выбор языка](README.md) · [English →](en.md)

---

## Заголовок

**Уровень 13 — Обратный отсчёт и марш**

---

## Объяснение

Иногда нужна **кнопка повтора**. Два вида циклов:

| Цикл | Аналогия | Когда использовать |
|------|----------|-------------------|
| `while` | Таймер | Повторять **пока** условие True |
| `for` + `range()` | Марш по точкам | Повторить **фиксированное** число раз |

**Два скрипта — запускай по отдельности!**

---

## Часть A — countdown.py (while)

```python
counter = 5
while counter > 0:
    print(counter)
    counter = counter - 1
print("Blastoff!")
```

**Путь A:**

```text
cd course-1-python-basics\block-3-making-choices\lesson-3-3-for-and-while-loops
python starter\countdown.py
```

**Mac/Linux:** используй прямые слэши — `python starter/countdown.py`. Список файлов — `ls` вместо `dir`.

**Ожидаемый вывод:**

```text
=== COUNTDOWN ===
5
4
3
2
1
Blastoff!
```

---

## Часть B — times_table.py (for)

```python
number = 3
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
```

**Запуск:**

```text
python starter\times_table.py
```

**Ожидаемый вывод:**

```text
=== TIMES TABLE ===
3 x 1 = 3
...
3 x 10 = 30
Table complete!
```

`range(1, 11)` даёт числа 1–10; **stop** не включается.

---

## Пример кода

**while:** [starter/countdown.py](starter/countdown.py)  
**for:** [starter/times_table.py](starter/times_table.py)

---

## Запуск кода

Запусти **оба** скрипта из папки урока или своей копии.

---

## Быстрые упражнения

1. Начни отсчёт с `10`.
2. Поставь `number = 7` в times_table.
3. Добавь `print("Get ready...")` перед while.

---

## Практическое задание

1. Замени `"Blastoff!"` на `"Liftoff!"`.
2. Печатай только чётные строки таблицы (`if i % 2 == 0:`).
3. См. [exercises/loop_drills.ru.md](exercises/loop_drills.ru.md).

**Эталоны:** [solution/countdown.py](solution/countdown.py) · [solution/times_table.py](solution/times_table.py)

---

## Уголок отладки

**Проблема:** Терминал печатает `5` бесконечно.

**Причина:** **Бесконечный цикл** — забыл обновить `counter` внутри `while`.

**Исправление:** Добавь `counter = counter - 1`. **Ctrl+C** останавливает зависший цикл.

---

## Что дальше

→ [Урок 3.4: паттерны циклов](../lesson-3-4-loop-patterns/README.md)

---

[← Выбор языка](README.md)
