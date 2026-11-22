# Урок 2.5: Flash и проверка форм

> **Курс:** Веб-приложения на Python · **Блок:** Красота и интерактив · **~35–45 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Уровень 12 — Калькулятор с дружелюбными ошибками**

---

## Объяснение

Финал Блока 2! Собери **калькулятор на форме** — пару к URL-калькулятору Блока 1 (`/add/3/5`). Числа вводят в форму, а не в адресную строку.

Если поля пустые, покажи **flash-сообщение** — короткую заметку, которая появляется один раз при следующей загрузке страницы.

Создай **`my_web_calc/`** в **корне проекта** (рядом с `my_web_madlibs/`).

**Путь A:** терминал VS Code уже открыт в папке `PyCourse`. Если в приглашении нет `(.venv)`, сначала включи ящик с инструментами из урока 0.1 (он лежит в этой папке):

**Windows:** `.venv\Scripts\Activate.ps1`  
**macOS:** `source .venv/bin/activate`

Потом создай папку итогового проекта — ты уже в `PyCourse`:

```text
mkdir my_web_calc
```

Скопируй [starter/](starter/) в `my_web_calc/`.

**Путь B:** Та же идея папки на Рабочем столе — см. [STUDENT-MAP](../STUDENT-MAP.ru.md).

---

### Шаг 1: Задай secret_key

```python
app.secret_key = "learning-flash-key"
```

Flash нужен секрет для локальных сессий. Для практики подойдёт любая случайная строка.

---

### Шаг 2: Проверь ввод и посчитай

```python
@app.route("/", methods=["GET", "POST"])
def calc():
    total = None
    if request.method == "POST":
        raw_a = request.form.get("a", "").strip()
        raw_b = request.form.get("b", "").strip()
        if not raw_a or not raw_b:
            flash("Please enter both numbers.")
        else:
            try:
                num_a = int(raw_a)
                num_b = int(raw_b)
                total = num_a + num_b
            except ValueError:
                flash("Use whole numbers only (like 3 or 10).")
    return render_template("calc.html", total=total)
```

**TODO в starter:** заполни блок POST в `app.py`.

---

### Шаг 3: Покажи flash в calc.html

```html
{% for message in get_flashed_messages() %}
<p class="error"><strong>{{ message }}</strong></p>
{% endfor %}
```

Результат появляется на той же странице, когда `total` задан:

```html
{% if total is not none %}
<h2>Result</h2>
<p><strong>{{ total }}</strong></p>
{% endif %}
```

---

### Шаг 4: Запуск из my_web_calc

Пока `(.venv)` включён (если в приглашении его нет, сначала активируй окружение в корне `PyCourse`):

**Windows:**

```text
cd my_web_calc
python app.py
```

**macOS:**

```text
cd my_web_calc
python3 app.py
```

Или проверь каркас урока:

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-5-flash-and-validation
python starter\app.py
```

**Mac/Linux:** `python starter/app.py`

1. Введи `7` и `5` → результат `12`
2. Оставь поле пустым → flash-ошибка, без падения

---

## Пример кода

**Файл: [solution/app.py](solution/app.py)**

```python
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "learning-flash-key"


@app.route("/", methods=["GET", "POST"])
def calc():
    total = None
    if request.method == "POST":
        raw_a = request.form.get("a", "").strip()
        raw_b = request.form.get("b", "").strip()
        if not raw_a or not raw_b:
            flash("Please enter both numbers.")
        else:
            try:
                num_a = int(raw_a)
                num_b = int(raw_b)
                total = num_a + num_b
            except ValueError:
                flash("Use whole numbers only (like 3 or 10).")
    return render_template("calc.html", total=total)
```

Flash-сообщения выводятся в [solution/templates/calc.html](solution/templates/calc.html) через `get_flashed_messages()`.

---

## Запуск кода

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-5-flash-and-validation
python starter\app.py
```

**Mac/Linux:** `python starter/app.py`

1. Открой `http://127.0.0.1:5000/`, введи `7` и `5` — в **Result** будет `12`
2. Отправь с пустым полем — появится дружелюбное сообщение (flash), без падения

---

## Быстрые упражнения

1. **Flash один раз** — вызови ошибку, затем введи правильные числа. Старая ошибка остаётся?
2. **Сравни** — URL-калькулятор Блока 1 и этот калькулятор на форме.
3. **Плохой ввод** — введи `abc` и `2`. Какое flash-сообщение?

---

## Задание для практики

**Квест:** Твой веб-калькулятор

1. Скопируй [starter/](starter/) в **`my_web_calc/`** в корне проекта.
2. Заполни все строки TODO.
3. Измени текст flash-сообщений под себя.
4. **Бонус:** добавь вычитание с выпадающим списком.

**Эталон:** [solution/](solution/)

---

## Уголок отладки

**Проблема:** `RuntimeError: The session is unavailable because no secret key was set`

**Причина:** `flash()` вызван без `app.secret_key`.

**Исправление:** Добавь `app.secret_key = "any-random-string"` после создания приложения Flask.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. Зачем `flash()` нужен `app.secret_key`?
   - **a)** Flash использует локальные сессии; секретный ключ это включает
   - **b)** Чтобы сменить цвет фона в CSS
   - **c)** Чтобы заменить `request.form`
   - **d)** Потому что сложение работает только с секретом

2. Когда вызывать `flash("Please enter both numbers.")`?
   - **a)** Каждый раз при старте сервера
   - **b)** Когда обязательное поле пустое после POST
   - **c)** Перед активацией `.venv`
   - **d)** Только при заходе через GET

3. Пользователь ввёл `abc` в поле числа. Что должно произойти?
   - **a)** Удаление `calc.html`
   - **b)** Форма молча игнорируется навсегда
   - **c)** Дружелюбная flash-ошибка — без страшного падения
   - **d)** Автоматический переход в Курс 3

4. Чем форм-калькулятор отличается от `/add/3/5` из Блока 1?
   - **a)** Работает только без шаблонов
   - **b)** Не использует Python
   - **c)** Не может показывать ошибки
   - **d)** Числа вводят в форму, а не в URL

5. Где в шаблоне **показать** flash-сообщения?
   - **a)** `{% for message in get_flashed_messages() %}`
   - **b)** Только `{% extends "flash.html" %}`
   - **c)** `request.args.get("message")`
   - **d)** Внутри `static/style.css`

---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **a)** Для сессий нужен секретный ключ, чтобы хранить flash.
2. **b)** Показывай понятные ошибки при неудачной проверке.
3. **c)** Лови плохой ввод и вызывай `flash()`, а не падай.
4. **d)** Формы убирают числа из URL — как в настоящих приложениях.
5. **a)** `get_flashed_messages()` возвращает сообщения для однократного показа.

</details>

---

## Что дальше

→ [Чеклист Блока 2](../README.md#block-2-readiness-checklist)  
→ [Чеклист выпуска Курса 2](../../STUDENT-MAP.ru.md#чеклист-выпуска-курса-2)  
→ [Курс 3: Разработка игр](../../../course-3-game-dev/README.md) — дальше Pygame!

---

*Блок 2 пройден — шаблоны, формы, CSS и проверка. Настоящие веб-приложения, собранные тобой!*

[← Выбрать язык](README.md)
