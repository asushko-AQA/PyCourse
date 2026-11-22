# Урок 2.2: f-строки и input()

> **Курс:** Основы Python и командная строка · **Блок:** Разговор с Python · **~30–45 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Уровень 7 — Спроси и ответь**

---

## Объяснение

В Уроке 2.1 ты сам заполнял волшебные коробки. Теперь **посетитель** заполняет их! `input()` — как микрофон: Python задаёт вопрос и ждёт ответа.

**f-строки** — свитки с пропусками. Переменные в `{фигурных скобках}` — Python подставляет реальные значения.

**Важно:** `input()` всегда возвращает **текст** (строку), даже если ты вводишь числа. В Уроке 2.3 научимся `int()` для математики.

---

### Шаг 1: Спроси через input()

```python
name = input("What is your name? ")
```

Текст в кавычках — **подсказка** (вопрос пользователю). После ввода и Enter ответ попадает в `name`.

---

### Шаг 2: Ответь f-строками

```python
print(f"Hello, {name}!")
```

Буква `f` перед кавычкой говорит Python: «замени `{name}` на реальное значение».

Без `f` Python печатает буквальный текст `{name}` — частая ошибка!

---

### Шаг 3: Открой greeting.py

Открой [starter/greeting.py](starter/greeting.py). В нём четыре TODO для тебя:

1. Замени `"Visitor"` на `input("What is your name? ")` — как в Шаге 1.
2. Замени `"?"` на `input()` с вопросом `"How old are you? "`.
3. Напиши `print()` с f-строкой, которая приветствует посетителя по `{name}`.
4. Напиши `print()` с f-строкой, которая показывает `{age}`.

Когда все четыре готовы, удали последнюю строку `print("Fill in the TODOs above, then delete this line!")` и сохрани файл (**Ctrl+S**).

---

### Шаг 4: cd и запуск

**Путь A:**

```text
cd course-1-python-basics\block-2-talking-to-python\lesson-2-2-f-strings-and-input
python starter\greeting.py
```

**Путь B:** Запускай из любой папки, где лежит `greeting.py`.

**Вводи при запросе:**

```text
What is your name? Alex
How old are you? 11
```

**Ожидаемый вывод:**

```text
Hello, Alex! Welcome to the Data Lab.
You said you are 11 years old.
```

Всё ещё видишь `Fill in the TODOs above, then delete this line!`? Вернись к Шагу 3 и доделай TODO.

---

## Пример кода

**Файл: [solution/greeting.py](solution/greeting.py)** — готовый приветственный бот с третьим вопросом и бонусной строкой:

```python
name = input("What is your name? ")
age = input("How old are you? ")
color = input("What is your favorite color? ")

print(f"Hello, {name}! Welcome to the Data Lab.")
print(f"You said you are {age} years old.")
print(f"Your favorite color is {color}. Nice choice!")
print(f"\n{name}, you are officially a Data Lab apprentice!")
```

---

## Запуск кода

```text
cd course-1-python-basics\block-2-talking-to-python\lesson-2-2-f-strings-and-input
python solution\greeting.py
```

**Mac/Linux:** `python solution/greeting.py` (прямые слэши).

**Вводи:** `Alex`, затем `11`, затем `blue`

**Ожидаемый вывод:**

```text
Hello, Alex! Welcome to the Data Lab.
You said you are 11 years old.
Your favorite color is blue. Nice choice!

Alex, you are officially a Data Lab apprentice!
```

---

## Быстрые упражнения

1. **Без f** — убери `f` из `print(f"Hello...`. Запусти. Увидишь буквальный `{name}`. Исправь.
2. **Третий вопрос** — добавь `color = input("What is your favorite color? ")` и ответ f-строкой.
3. **Прогноз** — до запуска запиши, что ожидаешь для своего имени и возраста.

---

## Практическое задание

**Название квеста:** Личный приветственный бот

1. Выполни все четыре TODO в [starter/greeting.py](starter/greeting.py) (Шаг 3).
2. Добавь третий вопрос — любимый цвет, игра или хобби — и ответь на него f-строкой, например `print(f"Your favorite color is {color}. Nice choice!")`.
3. Добавь многострочную f-строку с `\n` (сначала она печатает пустую строку):

```python
print(f"\n{name}, you are officially a Data Lab apprentice!")
```

**Ожидаемый вывод** (вводишь `Alex`, `11`, `blue`):

```text
Hello, Alex! Welcome to the Data Lab.
You said you are 11 years old.
Your favorite color is blue. Nice choice!

Alex, you are officially a Data Lab apprentice!
```

**Бонус:** Два вопроса в одной истории: имя + любимая еда.

**Эталонное решение:** [solution/greeting.py](solution/greeting.py)

---

## Уголок отладки

**Проблема:** Вывод показывает `Hello, {name}!` вместо `Hello, Alex!`

**Причина:** Забыта буква `f` перед строкой. Без неё `{name}` — просто текст, а не слот для переменной.

**Исправление:** Пиши `print(f"Hello, {name}!")` — `f` прямо перед открывающей кавычкой.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. Что всегда возвращает `input()`, даже если ты вводишь цифры?
   - **a)** Целое число
   - **b)** True или False
   - **c)** Ничего — только печатает
   - **d)** Текст (строку)

2. Зачем буква `f` в `print(f"Hello, {name}!")`?
   - **a)** Python подставляет `{name}` вместо реального значения
   - **b)** Делает весь текст заглавными
   - **c)** Превращает ввод в число
   - **d)** Останавливает программу

3. Ты пишешь `print("Hello, {name}!")` **без** `f`. Что на экране?
   - **a)** `Hello, Alex!` (с твоим именем)
   - **b)** Буквальный текст `Hello, {name}!`
   - **c)** Всегда SyntaxError
   - **d)** Пустая строка

4. Текст внутри `input("What is your name? ")` называется…
   - **a)** Частное от деления
   - **b)** Булево значение
   - **c)** Подсказка (prompt) — вопрос пользователю
   - **d)** Срез

5. Какая строка задаёт вопрос и сохраняет ответ в `color`?
   - **a)** `input(color) = "blue"`
   - **b)** `print(color = input)`
   - **c)** `color == input("blue")`
   - **d)** `color = input("What is your favorite color? ")`

---

<details><summary>Нажми, чтобы показать ответы</summary>

1. **d)** `input()` всегда возвращает строку; в Уроке 2.3 для математики — `int()`.
2. **a)** `f` включает подстановку переменных в `{фигурных скобках}`.
3. **b)** Без `f` `{name}` печатается как обычный текст.
4. **c)** Текст в кавычках — подсказка перед вводом.
5. **d)** `input()` справа, имя переменной слева от `=`.

</details>

---

## Что дальше

→ [Урок 2.3: Математические операторы](../lesson-2-3-math-operators/README.md) — превращай ввод в числа через `int()`.

---

*Ты умеешь спрашивать и отвечать. Дальше — калькуляторные заклинания!*

[← Выбрать язык](README.md)
