# Урок 2.3: Mad-Libs (итог)

> **Курс:** Веб-приложения на Python · **Блок:** Красота и интерактив · **~35–45 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Уровень 11 — Веб-фабрика историй**

---

## Объяснение

Твой первый **веб-итог**! Соедини шаблоны и POST-формы в приложение Mad-Libs — как `madlibs.py` из Курса 1, только в браузере.

Создай **`my_web_madlibs/`** в **корне проекта** (рядом с `course-2-web-apps/`).

**Путь A:** терминал VS Code уже открыт в папке `PyCourse`. Если в приглашении нет `(.venv)`, сначала включи ящик с инструментами из урока 0.1 (он лежит в этой папке):

**Windows:** `.venv\Scripts\Activate.ps1`  
**macOS:** `source .venv/bin/activate`

Потом создай папку итогового проекта — ты уже в `PyCourse`:

```text
mkdir my_web_madlibs
```

Скопируй [starter/](starter/) в `my_web_madlibs/` (`app.py` + `templates/`).

**Путь B:** Создай `my_web_madlibs` на Рабочем столе — та же идея, что `my_adventure/`. См. [STUDENT-MAP](../STUDENT-MAP.ru.md).

---

### Шаг 1: Одна страница, одна форма

В `madlibs.html` есть форма, а история появляется ниже, когда `story` не пустая:

```html
<form method="post">
    <input type="text" name="noun" placeholder="robot">
    <!-- verb, adjective, place -->
    <button type="submit">Create Story</button>
</form>

{% if story %}
<h2>Your Story</h2>
<p>{{ story }}</p>
{% endif %}
```

---

### Шаг 2: Собери историю при POST

```python
@app.route("/", methods=["GET", "POST"])
def madlibs():
    story = ""
    if request.method == "POST":
        noun = request.form.get("noun", "").strip()
        verb = request.form.get("verb", "").strip()
        adjective = request.form.get("adjective", "").strip()
        place = request.form.get("place", "").strip()
        story = (
            f"One sunny day, a {adjective} {noun} decided to {verb} "
            f"all the way to {place}. The crowd cheered. The end!"
        )
    return render_template("madlibs.html", story=story)
```

**TODO в starter:** прочитай четыре поля и собери историю в f-строке.

---

### Шаг 3: Запуск из my_web_madlibs

Пока `(.venv)` включён (если в приглашении его нет, сначала активируй окружение в корне `PyCourse`):

**Windows:**

```text
cd my_web_madlibs
python app.py
```

**macOS:**

```text
cd my_web_madlibs
python3 app.py
```

Или сначала проверь каркас урока:

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-3-madlibs-capstone
python starter\app.py
```

**Mac/Linux:** `python starter/app.py`

**Пример слов:** robot, dance, sparkly, moon base

---

### Шаг 4: Сделай по-своему

Поменяй шаблон истории или добавь пятое поле. Главное: форма → POST → история на той же странице.

---

## Пример кода

**Файл: [solution/app.py](solution/app.py)**

```python
@app.route("/", methods=["GET", "POST"])
def madlibs():
    story = ""
    if request.method == "POST":
        noun = request.form.get("noun", "something").strip() or "something"
        verb = request.form.get("verb", "move").strip() or "move"
        adjective = request.form.get("adjective", "silly").strip() or "silly"
        place = request.form.get("place", "somewhere").strip() or "somewhere"
        story = (
            f"One sunny day, a {adjective} {noun} decided to {verb} "
            f"all the way to {place}. The crowd cheered. The end!"
        )
    return render_template("madlibs.html", story=story)
```

Импорты и `app = Flask(__name__)` — в начале [solution/app.py](solution/app.py). Форма — в [solution/templates/madlibs.html](solution/templates/madlibs.html).

---

## Запуск кода

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-3-madlibs-capstone
python starter\app.py
```

**Mac/Linux:** `python starter/app.py`

1. Открой `http://127.0.0.1:5000/`
2. Введи примеры слов (robot, dance, sparkly, moon base) и нажми **Create Story**

**Ожидаемый результат:** под **Your Story** появится твой абзац Mad-Libs.

---

## Быстрые упражнения

1. **Сопоставь поля** — каждый `name="..."` связан с `request.form.get(...)`.
2. **Пустое существительное** — отправь с одним пустым полем. Что выведется?
3. **Новое предложение** — перепиши историю про школу или спорт.

---

## Задание для практики

**Квест:** Твой веб Mad-Libs

1. Скопируй [starter/](starter/) в **`my_web_madlibs/`** в корне проекта.
2. Заполни все строки TODO в `app.py` и `madlibs.html`.
3. Напиши свой шаблон истории из двух предложений.
4. Проверь тремя разными наборами слов.

**Эталон:** [solution/](solution/)

---

## Уголок отладки

**Проблема:** Форма отправляется, а место для истории остаётся пустым

**Причина:** Переменная `story` так и не была задана внутри блока `if request.method == "POST":`.

**Исправление:** Собери `story = f"..."` до `return render_template("madlibs.html", story=story)`.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. Куда копировать стартовый код для капстоуна?
   - **a)** Только в закладки браузера
   - **b)** Внутрь `.venv/Scripts/`
   - **c)** В `my_web_madlibs/` в корне проекта
   - **d)** В `course-1-python-basics/`

2. Форма Mad-Libs с `method="post"`. Куда попадают слова при отправке?
   - **a)** Сразу в `pip list`
   - **b)** Только в URL как `?noun=robot`
   - **c)** В `static/style.css`
   - **d)** В тело запроса — читаем через `request.form.get(...)`

3. Когда собирать переменную `story`?
   - **a)** В блоке `if request.method == "POST":` после чтения полей
   - **b)** До `app = Flask(__name__)`
   - **c)** Только в консоли браузера
   - **d)** После `deactivate`

4. Что делает `{% if story %}` в шаблоне?
   - **a)** Удаляет форму после одного использования
   - **b)** Показывает блок истории только если `story` не пустая
   - **c)** Устанавливает Jinja2 через pip
   - **d)** Сам меняет GET на POST

5. Каждый `<input name="noun">` должен совпадать с чем в `app.py`?
   - **a)** Со строкой `secret_key`
   - **b)** С номером порта Flask
   - **c)** С тем же именем в `request.form.get("noun")`
   - **d)** Только с именем декоратора `@app.route`

---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **c)** Итоговые папки — в корне проекта, как другие `my_*`.
2. **d)** POST отправляет поля в теле запроса, не в URL.
3. **a)** История собирается только после получения слов из формы.
4. **b)** Шаблон показывает результат, когда `story` не пустая.
5. **c)** Атрибут `name` в HTML = ключ в `request.form.get(...)`.

</details>

---

## Что дальше

→ [Урок 2.4: CSS и статика](../lesson-2-4-static-files-css/README.md) — подключи таблицу стилей через `url_for`.

---

*Веб-фабрика историй открыта. Пора добавить стиль!*

[← Выбрать язык](README.md)
