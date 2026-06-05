# Урок 1.4: Чтение сообщений об ошибках

> **Курс:** Основы Python и командная строка · **Блок:** Знакомство с компьютером · **~30–45 мин**  
> [Choose language / Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Уровень 4 — Академия детективов ошибок**

---

## Объяснение

У каждого героя бывают баги. Новички паникуют — детективы **читают улики**.

Ошибки — не «ты провалился». Это **подсказки**, что исправить.

Два типа ошибок в этом уроке:

1. **SyntaxError** — сломана **грамматика** кода (нет кавычки, нет `)`)
2. **can't open file** — **терминал** не находит файл (не та папка или имя)

**Как читать traceback:**

1. Прокрути **вниз** — сначала последняя строка
2. Найди **`File "...", line N`** — номер строки с ошибкой
3. В VS Code: **Ctrl+G**, введи N

---

### Шаг 1: Папка с делами

**Путь A — репозиторий PyCourse:**

```text
cd course-1-python-basics\block-1-meeting-your-computer\lesson-1-4-reading-error-messages
```

**Путь B — своя копия:** `cd` в папку, куда ты сохранил `lesson-1-4-reading-error-messages`. Внутри должны быть `starter/` и три файла дел.

```text
dir starter
```

**Ожидается:** `bug_missing_quote.py`, `bug_missing_paren.py`, `right_name.py`

---

### Шаг 2: Дело 1 — пропавшая кавычка

Открой `starter/bug_missing_quote.py`.

```text
python starter\bug_missing_quote.py
```

**Ожидаемая ошибка:**

```text
SyntaxError: unterminated string literal (detected at line 4)
```

Исправь кавычку на строке 4. Сохрани. Запусти снова.

**После исправления:**

```text
Hello, Detective!
Can you spot the missing quote?
```

---

### Шаг 3: Дело 2 — пропавшая скобка

```text
python starter\bug_missing_paren.py
```

**Ожидаемая ошибка:**

```text
SyntaxError: '(' was never closed
```

Добавь `)`. Сохрани. Запусти снова.

---

### Шаг 4: Дело 3 — неправильное имя файла

Файл на диске: **`right_name.py`**. Запусти **намеренно неправильно**:

```text
python starter\wrong_name.py
```

**Ожидаемая ошибка:**

```text
python: can't open file '...\wrong_name.py': [Errno 2] No such file or directory
```

Это не SyntaxError — Python даже не читал код.

**Исправление:**

```text
python starter\right_name.py
```

**Ожидаемый вывод:**

```text
You found the right file!
The filename on disk is: right_name.py
```

---

### Шаг 5: Перейти к строке N

1. Открой файл
2. **Ctrl+G**
3. Введи номер из ошибки
4. **Enter**

---

## Пример кода

Три файла в [starter/](starter/) — только `print()` и комментарии, до 15 строк.

**Дело 1 (до исправления):**

```python
print("Hello, Detective!)
```

**Дело 2 (до исправления):**

```python
print("This line is missing something..."
```

**Дело 3:** файл верный, ошибка в **команде** терминала.

Смотри [solution/](solution/) только после своих попыток!

---

## Запуск кода

Для каждого дела:

1. Запусти сломанную версию
2. Прочитай ошибку
3. Исправь код или команду
4. Запусти снова

**Финальная проверка:**

```text
python starter\bug_missing_quote.py
python starter\bug_missing_paren.py
python starter\right_name.py
```

*(Первые два файла ты должен исправить сам!)*

---

## Быстрые упражнения

1. Где ошибка? `print("Hello!)` или `print("Hello!")`?
2. В `line 4` — на какую строку прыгать?
3. Выйди из папки урока, запусти скрипт, прочитай ошибку, вернись `cd`.

---

## Задание для практики

**Квест:** Три дела

1. Исправь **все три** файла в [starter/](starter/) без подглядывания в [solution/](solution/).
2. Запиши в тетрадь: SyntaxError или can't open file?
3. Расскажи правило: сначала читай **последнюю строку** ошибки.

**Бонус:**

- [exercises/bug_bad_indent.py](exercises/bug_bad_indent.py) — **IndentationError** (лишние пробелы). Решение: [exercises/bug_bad_indent_solution.py](exercises/bug_bad_indent_solution.py).

**NameError** (опечатки в переменных) — в Блоке 2!

---

## Уголок отладки

**Проблема:** Вижу `line 4`, но не нахожу ошибку.

**Причины:** смотришь не ту строку или не сохранил файл.

**Решение:**

1. **Ctrl+G** → номер из ошибки
2. **Ctrl+S**
3. Запусти снова
4. [solution/](solution/) — только в крайнем случае

---

## Что дальше

→ [Урок 1.5: Значок диспетчера миссии](../lesson-1-5-mission-control-badge/README.md) — итог Блока 1!

---

*Ошибки — улики. Ты читаешь последнюю строку. Ты прыгаешь на номер строки. Значок детектива: получен.*

[← Выбрать язык](README.md)
