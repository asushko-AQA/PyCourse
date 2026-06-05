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

Открой [starter/greeting.py](starter/greeting.py). Два вопроса и два ответа f-строками ждут тебя в TODO.

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
Type your answers when the terminal waits for you!
```

---

## Пример кода

```python
name = input("What is your name? ")
age = input("How old are you? ")

print(f"Hello, {name}! Welcome to the Data Lab.")
print(f"You said you are {age} years old.")
```

---

## Запуск кода

```text
python starter\greeting.py
```

Ответь на оба вопроса. Увидишь персональный вывод.

---

## Быстрые упражнения

1. **Без f** — убери `f` из `print(f"Hello...`. Запусти. Увидишь буквальный `{name}`. Исправь.
2. **Третий вопрос** — добавь `color = input("What is your favorite color? ")` и ответ f-строкой.
3. **Прогноз** — до запуска запиши, что ожидаешь для своего имени и возраста.

---

## Практическое задание

**Название квеста:** Личный приветственный бот

1. Заполни оба TODO f-строки в [starter/greeting.py](starter/greeting.py).
2. Добавь третий вопрос — любимый цвет, игра или хобби.
3. Добавь многострочную f-строку с `\n`:

```python
print(f"\n{name}, you are officially a Data Lab apprentice!")
```

**Бонус:** Два вопроса в одной истории: имя + любимая еда.

**Эталонное решение:** [solution/greeting.py](solution/greeting.py)

---

## Уголок отладки

**Проблема:** Вывод показывает `Hello, {name}!` вместо `Hello, Alex!`

**Причина:** Забыта буква `f` перед строкой. Без неё `{name}` — просто текст, а не слот для переменной.

**Исправление:** Пиши `print(f"Hello, {name}!")` — `f` прямо перед открывающей кавычкой.

---

## Что дальше

→ [Урок 2.3: Математические операторы](../lesson-2-3-math-operators/README.md) — превращай ввод в числа через `int()`.

---

*Ты умеешь спрашивать и отвечать. Дальше — калькуляторные заклинания!*

[← Выбрать язык](README.md)
