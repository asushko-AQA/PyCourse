# Урок 2.2: HTML-формы (GET/POST)

> **Курс:** Веб-приложения на Python · **Блок:** Красота и интерактив · **~30 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Form Lab — GET и POST**

---

## Объяснение

**Форма** — способ, которым браузер отправляет данные на твой сервер.

| Метод | Куда попадают данные | Flask читает так |
|-------|----------------------|------------------|
| GET | Видно в URL (`?name=Alex`) | `request.args.get("name")` |
| POST | Спрятано в теле запроса | `request.form.get("text")` |

В уроке две мини-формы:

- **`/greet`** — только GET; имя появляется в URL
- **`/message`** — GET показывает форму, POST повторяет то, что ты ввёл

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

**TODO в starter:** добавь оба маршрута и доделай формы в шаблонах.

---

### Шаг 3: Запусти и сравни

**Путь A:**

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-2-html-forms
python starter\app.py
```

**Путь B:** Скопируй `starter/` — см. [STUDENT-MAP](../STUDENT-MAP.ru.md).

**Mac/Linux:** `python starter/app.py`

1. Открой `/greet`, отправь имя — смотри, как URL меняется на `?name=...`
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

HTML форм — в `solution/templates/`, см. [solution/templates/greet.html](solution/templates/greet.html).

---

## Запуск кода

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-2-html-forms
python starter\app.py
```

**Mac/Linux:** `python starter/app.py`

1. Открой `http://127.0.0.1:5000/greet`, введи имя — URL станет `?name=...`
2. Открой `http://127.0.0.1:5000/message`, отправь текст — URL остаётся `/message`

**Ожидаемый результат:** обе страницы показывают твой ввод в области результата.

---

## Быстрые упражнения

1. **Детектив URL** — отправь GET с именем `Sam`. Скопируй полный URL.
2. **Пустой POST** — отправь `/message` с пустым полем. Что произойдёт?
3. **Strip** — зачем вызываем `.strip()` у значений формы?

---

## Задание для практики

**Квест:** Вежливый приветствователь

1. Доделай TODO-маршруты и HTML форм в [starter/](starter/).
2. Измени тексты приветствия и эха под себя.
3. **Бонус:** добавь поле `color` в POST-форму и тоже выведи его.

**Эталон:** [solution/](solution/)

---

## Уголок отладки

**Проблема:** `Method Not Allowed` при отправке формы

**Причина:** Маршрут не разрешает этот HTTP-метод.

**Исправление:** Для GET-форм пиши `methods=["GET"]`, а если один URL и показывает форму, и принимает её — `methods=["GET", "POST"]`.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. При **GET**-форме на `/greet` где часто появляется имя после отправки?
   - **a)** В URL, например `?name=Alex`
   - **b)** Только на диске сервера, нигде не видно
   - **c)** В CSS-файле
   - **d)** В имени папки `.venv`

2. Какой код Flask читает GET-данные из URL?
   - **a)** `request.args.get("name")`
   - **b)** `request.form.get("name")`
   - **c)** `flash("name")`
   - **d)** `url_for('static', filename='name')`

3. Какой код Flask читает POST-данные из отправленной формы?
   - **a)** `request.form.get("text")`
   - **b)** `request.args.get("text")`
   - **c)** `importlib.metadata.version("text")`
   - **d)** `@app.route("<text>")`

4. Зачем `/message` может иметь `methods=["GET", "POST"]`?
   - **a)** GET показывает форму; POST обрабатывает данные на том же URL
   - **b)** Потому что GET и POST не работают с шаблонами
   - **c)** Чтобы установить Flask дважды
   - **d)** Чтобы в URL всегда было `?text=...`

5. Зачем вызывать `.strip()` у значений формы?
   - **a)** Убрать лишние пробелы в начале и конце ввода
   - **b)** Удалить форму из HTML
   - **c)** Автоматически превратить числа в float
   - **d)** Скрыть flash-сообщения

---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **a)** Данные GET-формы видны в query string.
2. **a)** `request.args` — для параметров в URL.
3. **a)** `request.form` — для полей POST.
4. **a)** Один URL показывает форму (GET) и обрабатывает её (POST).
5. **a)** `.strip()` убирает случайные пробелы во вводе.

</details>

---

## Что дальше

→ [Урок 2.3: Mad-Libs](../lesson-2-3-madlibs-capstone/README.md) — смешная история из полей формы.

---

*Формы — способ, которым гости разговаривают с твоим приложением. Дальше — фабрика историй!*

[← Выбрать язык](README.md)
