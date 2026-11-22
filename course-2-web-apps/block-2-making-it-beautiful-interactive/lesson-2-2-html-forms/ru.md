# Урок 2.2: HTML-формы (GET/POST)

> **Курс:** Веб-приложения на Python · **Блок:** Красота и интерактив · **~30 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Form Lab — GET и POST**

---

## Объяснение

**Форма** — это способ, которым браузер отправляет данные на твой сервер.

| Метод | Куда попадают данные | Чем читает Flask |
|-------|----------------------|------------------|
| GET | Видны в URL (`?name=Alex`) | `request.args.get("name")` |
| POST | Спрятаны в теле запроса | `request.form.get("text")` |

В этом уроке две мини-формы:

- **`/greet`** — только GET; имя появляется в URL
- **`/message`** — GET показывает форму, POST повторяет (эхо) то, что ты ввёл

---

### Шаг 1: GET-приветствие

```python
@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "").strip()
    message = ""
    if name:
        message = f"Hello, {name}! Nice to meet you."
    return render_template("greet.html", message=message, name=name)
```

Добавь форму в `greet.html`:

```html
<form method="get" action="/greet">
    <input type="text" name="name" placeholder="Your name">
    <button type="submit">Say hi</button>
</form>
```

---

### Шаг 2: POST-эхо сообщения

```python
@app.route("/message", methods=["GET", "POST"])
def message():
    text = ""
    reply = ""
    if request.method == "POST":
        text = request.form.get("text", "").strip()
        if text:
            reply = f"You said: {text}"
    return render_template("message.html", message=reply, text=text)
```

Добавь форму в `message.html` — `action` не нужен, потому что форма отправляется на тот же URL:

```html
<form method="post">
    <input type="text" name="text" placeholder="Your message">
    <button type="submit">Send</button>
</form>
```

**TODO в starter:** добавь оба маршрута и доделай формы в шаблонах.

---

### Шаг 3: Запусти и сравни

**1. Активируй venv.** В VS Code открой папку, где лежит твой `.venv` (**Путь A:** `PyCourse`; **Путь B:** твоя папка-мастерская). Терминал запускается в ней. Активируй:

```text
.venv\Scripts\Activate.ps1
```

**Командная строка (cmd):** `.venv\Scripts\activate.bat` · **macOS/Linux:** `source .venv/bin/activate`

В начале строки терминала должно появиться `(.venv)`.

**2. Перейди в папку starter и запусти.**

**Путь A:**

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-2-html-forms\starter
python app.py
```

**macOS/Linux:** `cd course-2-web-apps/block-2-making-it-beautiful-interactive/lesson-2-2-html-forms/starter`, затем `python app.py`

**Путь B:** Скопируй папку `starter/` этого урока в свою папку-мастерскую, рядом с `.venv`, и переименуй её в `lesson-2-2`. Затем `cd lesson-2-2` и `python app.py`. См. [STUDENT-MAP](../STUDENT-MAP.ru.md).

1. Открой `/greet`, отправь имя — посмотри, как URL меняется на `?name=...`
2. Открой `/message`, отправь текст — URL остаётся `/message`

**Ожидаемый результат:** обе страницы повторяют твой ввод в области результата.

---

## Пример кода

**Файл: [solution/app.py](solution/app.py)**

```python
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "").strip()
    message = ""
    if name:
        message = f"Hello, {name}! Nice to meet you."
    return render_template("greet.html", message=message, name=name)


@app.route("/message", methods=["GET", "POST"])
def message():
    text = ""
    reply = ""
    if request.method == "POST":
        text = request.form.get("text", "").strip()
        if text:
            reply = f"You said: {text}"
    return render_template("message.html", message=reply, text=text)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
```

HTML форм лежит в `solution/templates/` — см. [solution/templates/greet.html](solution/templates/greet.html).

---

## Запуск кода

С активным `(.venv)`, из папки, открытой в VS Code:

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-2-html-forms\starter
python app.py
```

**macOS/Linux:** `cd course-2-web-apps/block-2-making-it-beautiful-interactive/lesson-2-2-html-forms/starter`, затем `python app.py` · **Путь B:** `cd lesson-2-2`, затем `python app.py`

**Ожидаемый вывод (терминал):**

```text
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

1. Открой `http://127.0.0.1:5000/greet`, введи `Sam` — URL станет `/greet?name=Sam`
2. Открой `http://127.0.0.1:5000/message`, напиши `Hi there` и отправь — URL остаётся `/message`

**Ожидаемый вывод (браузер, под каждой формой):**

```text
Hello, Sam! Nice to meet you.
```

```text
You said: Hi there
```

**Ожидаемый результат:** обе страницы показывают твой ввод в области результата. Останови сервер клавишами **Ctrl+C**, когда закончишь.

---

## Быстрые упражнения

1. **Детектив URL** — отправь GET с именем `Sam`. Скопируй полный URL.
2. **Пустой POST** — отправь `/message` с пустым полем. Что произойдёт?
3. **Strip** — зачем вызываем `.strip()` у значений формы?

---

## Задание для практики

**Квест:** Вежливый приветствователь

1. Доделай TODO-маршруты и HTML форм в [starter/](starter/).
2. Измени текст приветствия и эха на свой.
3. **Бонус:** Добавь поле `color` в POST-форму и выведи его тоже.

**Эталон:** [solution/](solution/)

---

## Уголок отладки

**Проблема:** `Method Not Allowed` при отправке формы

**Причина:** Маршрут не разрешает этот HTTP-метод.

**Решение:** Пиши `methods=["GET"]` для GET-форм и `methods=["GET", "POST"]`, когда один и тот же URL обрабатывает оба метода.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. При **GET**-форме на `/greet` где часто появляется имя после отправки?
   - **a)** Только на диске сервера, нигде не видно
   - **b)** В CSS-файле
   - **c)** В имени папки `.venv`
   - **d)** В URL, например `?name=Alex`

2. Какой код Flask читает GET-данные из URL?
   - **a)** `request.args.get("name")`
   - **b)** `request.form.get("name")`
   - **c)** `flash("name")`
   - **d)** `url_for('static', filename='name')`

3. Какой код Flask читает POST-данные из отправленной формы?
   - **a)** `@app.route("<text>")`
   - **b)** `request.form.get("text")`
   - **c)** `request.args.get("text")`
   - **d)** `importlib.metadata.version("text")`

4. Зачем `/message` может иметь `methods=["GET", "POST"]`?
   - **a)** Чтобы установить Flask дважды
   - **b)** Чтобы в URL всегда было `?text=...`
   - **c)** GET показывает форму; POST обрабатывает данные на том же URL
   - **d)** Потому что GET и POST не работают с шаблонами

5. Зачем вызывать `.strip()` у значений формы?
   - **a)** Удалить форму из HTML
   - **b)** Автоматически превратить числа в float
   - **c)** Скрыть flash-сообщения
   - **d)** Убрать лишние пробелы в начале и конце ввода

---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **d)** Данные GET-формы видны в query string.
2. **a)** `request.args` — для параметров в URL.
3. **b)** `request.form` — для полей POST.
4. **c)** Один URL показывает форму (GET) и обрабатывает её (POST).
5. **d)** `.strip()` убирает случайные пробелы во вводе.

</details>

---

## Что дальше

→ [Урок 2.3: Mad-Libs](../lesson-2-3-madlibs-capstone/README.md) — смешная история из полей формы.

---

*Формы — это то, как посетители разговаривают с твоим приложением. Дальше — машина историй!*
