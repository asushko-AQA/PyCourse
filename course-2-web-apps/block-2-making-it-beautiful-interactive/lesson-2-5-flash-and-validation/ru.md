# Урок 2.5: Flash и проверка форм

> **Курс:** Веб-приложения на Python · **Блок:** Красота и интерактив · **~35–45 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Уровень 12 — Калькулятор с дружелюбными ошибками**

---

## Объяснение

Финал блока 2! Собери **калькулятор на форме** — пару к URL-калькулятору блока 1 (`/add/3/5`). Числа вводят в форму, а не в адресную строку.

Когда поля пустые, покажи **flash-сообщение** — короткую заметку, которая появляется один раз при следующей загрузке страницы.

Создай **`my_web_calc/`** в **корне проекта** — в папке, которую ты открываешь в VS Code, рядом с `.venv` и с `my_web_madlibs/`.

**Путь A:** открой `PyCourse` в VS Code и терминал — он уже стоит в `PyCourse`. Скопируй [starter/](starter/) урока в новую папку `my_web_calc`:

```text
Copy-Item -Recurse course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-5-flash-and-validation\starter my_web_calc
```

**Командная строка (cmd):** `xcopy /E /I course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-5-flash-and-validation\starter my_web_calc`  
**macOS/Linux:** `cp -r course-2-web-apps/block-2-making-it-beautiful-interactive/lesson-2-5-flash-and-validation/starter my_web_calc`

Удобнее мышью? В проводнике VS Code: правый клик по папке `starter` урока → **Copy**, правый клик по пустому месту под `PyCourse` → **Paste**, затем переименуй копию в `my_web_calc`.

Проверка: появились `my_web_calc/app.py` и `my_web_calc/templates/calc.html`.

**Путь B:** в своей папке-мастерской (рядом с `.venv`) создай `my_web_calc/` и положи туда `starter/app.py` и `starter/templates/` этого урока. См. [STUDENT-MAP](../STUDENT-MAP.ru.md).

---

### Шаг 1: Задай secret_key

```python
app.secret_key = "learning-flash-key"
```

Flash нужен секрет для локальных сессий. Для практики подойдёт любая случайная строка.

---

### Шаг 2: Проверь ввод и посчитай

`int()` превращает текст из формы в целое число. Если ввести `abc`, `int("abc")` не справится, и Python поднимет `ValueError` — ошибку, из-за которой страница упадёт. Положи рискованные строки в блок `try`: когда случится `ValueError`, Python перейдёт в `except ValueError`, и ты вызовешь `flash` с понятной заметкой вместо падения.

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

**TODO в starter:** допиши блок POST в `app.py`.

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

**1. Активируй venv.** Терминал VS Code стартует в корне проекта (там лежит `.venv`). Активируй:

```text
.venv\Scripts\Activate.ps1
```

**Командная строка (cmd):** `.venv\Scripts\activate.bat` · **macOS/Linux:** `source .venv/bin/activate`

В начале строки терминала должно появиться `(.venv)`.

**2. Зайди в папку капстоуна и запусти** (те же команды на Windows, macOS/Linux и в пути B):

```text
cd my_web_calc
python app.py
```

Открой `http://127.0.0.1:5000/`.

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

Flash-сообщения рисуются в [solution/templates/calc.html](solution/templates/calc.html) через `get_flashed_messages()`.

---

## Запуск кода

С активным `(.venv)`, из корня проекта:

```text
cd my_web_calc
python app.py
```

1. Открой `http://127.0.0.1:5000/`, введи `7` и `5` — **Result** показывает `12`
2. Отправь форму с пустым полем — появляется понятная ошибка (flash), без падения

---

## Быстрые упражнения

1. **Flash один раз** — вызови ошибку, потом отправь правильные числа. Старая ошибка остаётся?
2. **Сравни** — URL-калькулятор блока 1 и этот калькулятор на форме.
3. **Плохой ввод** — введи `abc` и `2`. Какое flash-сообщение появится?

---

## Задание для практики

**Квест:** Твой веб-калькулятор

1. Скопируй [starter/](starter/) в **`my_web_calc/`** в корне проекта.
2. Допиши все строки TODO.
3. Поменяй текст flash-сообщения на свой.
4. **Бонус:** добавь вычитание через выпадающий список.

**Эталон:** [solution/](solution/)

---

## Уголок отладки

**Проблема:** `RuntimeError: The session is unavailable because no secret key was set`

**Причина:** `flash()` вызван без `app.secret_key`.

**Исправление:** Добавь `app.secret_key = "any-random-string"` сразу после создания приложения Flask.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. Зачем `flash()` нужен `app.secret_key`?
   - **a)** Чтобы заменить `request.form`
   - **b)** Потому что сложение работает только с секретом
   - **c)** Flash использует локальные сессии; секретный ключ это включает
   - **d)** Чтобы сменить цвет фона в CSS

2. Когда вызывать `flash("Please enter both numbers.")`?
   - **a)** Каждый раз при старте сервера
   - **b)** Перед активацией `.venv`
   - **c)** Только при заходе через GET
   - **d)** Когда обязательное поле пустое после POST

3. Пользователь ввёл `abc` в поле числа. Что должно произойти?
   - **a)** Дружелюбная flash-ошибка — без страшного падения
   - **b)** Форма молча игнорируется навсегда
   - **c)** Удаление `calc.html`
   - **d)** Автоматический переход в Курс 3

4. Чем форм-калькулятор отличается от `/add/3/5` из Блока 1?
   - **a)** Работает только без шаблонов
   - **b)** Числа вводят в форму, а не в URL
   - **c)** Не использует Python
   - **d)** Не может показывать ошибки

5. Где в шаблоне **показать** flash-сообщения?
   - **a)** `request.args.get("message")`
   - **b)** Внутри `static/style.css`
   - **c)** `{% for message in get_flashed_messages() %}`
   - **d)** Только `{% extends "flash.html" %}`

---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **c)** Для сессий нужен секретный ключ, чтобы хранить flash.
2. **d)** Показывай понятные ошибки при неудачной проверке.
3. **a)** Лови плохой ввод и вызывай `flash()`, а не падай.
4. **b)** Формы убирают числа из URL — как в настоящих приложениях.
5. **c)** `get_flashed_messages()` возвращает сообщения для однократного показа.

</details>

---

## Что дальше

→ [Чеклист Блока 2](../README.md#block-2-readiness-checklist)  
→ [Чеклист выпуска Курса 2](../../STUDENT-MAP.ru.md#чеклист-выпуска-курса-2)  
→ [Курс 3: Разработка игр](../../../course-3-game-dev/README.md) — дальше Pygame!

---

*Блок 2 позади — шаблоны, формы, CSS и проверка ввода. Настоящие веб-приложения, собранные тобой!*
