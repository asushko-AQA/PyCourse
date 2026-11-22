# Урок 3.1: Логические значения и сравнения

> **Курс:** Python Basics · **Блок:** Выбор и повторение · **~30 мин**  
> [Выбор языка](README.md) · [English →](en.md)

---

## Заголовок

**Уровень 11 — Квест «Правда или ложь»**

---

## Объяснение

Добро пожаловать на **Квестовые ворота**! Python отвечает **`True`** (прошёл) или **`False`** (не прошёл), когда ты сравниваешь значения.

| Оператор | Значение | Пример |
|----------|----------|--------|
| `==` | равно | `5 == 5` → `True` |
| `!=` | не равно | `3 != 3` → `False` |
| `>` | больше | `10 > 7` → `True` |
| `<` | меньше | `4 < 2` → `False` |
| `>=` | больше или равно | `5 >= 5` → `True` |
| `<=` | меньше или равно | `2 <= 9` → `True` |

**`and`** — оба должны быть True. **`or`** — хотя бы один True:

```python
print(True and False)   # False
print(True or False)    # True
```

**`not`** переворачивает True ↔ False — как перевернуть штамп квеста:

```python
print("not False:", not False)   # True
print("not (5 == 3):", not (5 == 3))   # True — 5 == 3 is False, not False is True
```

**Пока без `if`** — только печатаем результаты сравнений. `if` будет в уроке 3.2.

---

### Шаг 1: Открой скрипт

Открой [starter/true_false_quiz.py](starter/true_false_quiz.py).

---

### Шаг 2: Перейди в папку урока

**Путь A:**

```text
cd course-1-python-basics\block-3-making-choices\lesson-3-1-booleans
```

**Путь B:** Скопируй `true_false_quiz.py` в свою папку и выполни `cd` туда.

---

### Шаг 3: Запусти

```text
python starter\true_false_quiz.py
```

**Mac/Linux:** используй прямые слэши — `python starter/true_false_quiz.py`. Список файлов — `ls` вместо `dir`.

**Ожидаемый вывод:**

```text
=== TRUE OR FALSE QUEST ===
5 == 5: True
5 == 3: False
10 > 7: True
4 < 2: False
'cat' == 'cat': True
5 >= 5: True
3 != 3: False
True and False: False
True or False: True
Predict each line before you run!
```

---

## Пример кода

```python
print("5 == 5:", 5 == 5)
print("10 > 7:", 10 > 7)
print("True and False:", True and False)
```

---

## Запуск кода

```text
cd course-1-python-basics\block-3-making-choices\lesson-3-1-booleans
python starter\true_false_quiz.py
```

---

## Быстрые упражнения

1. Угадай каждый True/False до запуска.
2. Замени `10 > 7` на `3 > 7` — угадай, запусти.
3. Добавь `print("100 == 99:", 100 == 99)`.

---

## Задание для практики

1. Добавь три новых сравнения с `==`, `<`, `!=`.
2. Добавь строку с `and`.
3. Добавь строку с `or`.

**Эталон:** [solution/true_false_quiz.py](solution/true_false_quiz.py)

---

## Уголок отладки

**Проблема:** `if 5 = 5:` → `SyntaxError`.

**Причина:** Один `=` — **присваивание** (`name = "Alex"`). Два `==` — **сравнение**.

**Исправление:** Для сравнения используй `==`.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. Чему равно `5 == 5`?
   - **a)** Ошибка
   - **b)** `False`
   - **c)** `5`
   - **d)** `True`

2. Чему равно `3 != 3`?
   - **a)** `False`
   - **b)** `True`
   - **c)** `3`
   - **d)** `0`

3. Один знак `=` используют для…
   - **a)** Сравнения двух значений
   - **b)** Присваивания — положить значение в переменную
   - **c)** Сложения чисел
   - **d)** Печати True или False

4. Чему равно `True and False`?
   - **a)** `True`
   - **b)** `None`
   - **c)** `False`
   - **d)** `"True and False"`

5. Чему равно `True or False`?
   - **a)** Ошибка
   - **b)** `False`
   - **c)** `None`
   - **d)** `True`

---

<details><summary>Нажми, чтобы показать ответы</summary>

1. **d)** `==` проверяет равенство; `5 == 5` → `True`.
2. **a)** `!=` значит «не равно»; `3` равно `3`, значит `False`.
3. **b)** Один `=` присваивает (`name = "Alex"`); два `==` сравнивают.
4. **c)** `and` требует **оба** True; один False — результат False.
5. **d)** `or` требует **хотя бы один** True; True or False → True.

</details>

---

## Что дальше

→ [Урок 3.2: if, elif, else](../lesson-3-2-if-elif-else/README.md)

---

[← Выбор языка](README.md)
