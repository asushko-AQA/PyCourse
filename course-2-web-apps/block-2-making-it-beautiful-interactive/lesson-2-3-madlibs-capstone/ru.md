# Урок 2.3: Mad-Libs (итог)

> **Курс:** Веб-приложения на Python · **Блок:** Красота и интерактив · **~35–45 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Уровень 11 — Веб-фабрика историй**

---

## Объяснение

Первый **веб-итог**! Соедини шаблоны и POST-формы в приложение Mad-Libs — как `madlibs.py` из Курса 1, только в браузере.

Создай **`my_web_madlibs/`** в **корне проекта** — это папка, которую ты открываешь в VS Code, рядом с `.venv` (а в Пути A ещё и рядом с `course-2-web-apps/`).

**Путь A:** Открой `PyCourse` в VS Code и открой терминал — он уже стартует в `PyCourse`. Скопируй [starter/](starter/) этого урока в новую папку `my_web_madlibs`:

```text
Copy-Item -Recurse course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-3-madlibs-capstone\starter my_web_madlibs
```

**Командная строка (cmd):** `xcopy /E /I course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-3-madlibs-capstone\starter my_web_madlibs`  
**macOS/Linux:** `cp -r course-2-web-apps/block-2-making-it-beautiful-interactive/lesson-2-3-madlibs-capstone/starter my_web_madlibs`

Удобнее мышкой? В проводнике VS Code щёлкни правой кнопкой папку `starter` урока → **Copy**, щёлкни правой кнопкой пустое место под `PyCourse` → **Paste**, затем переименуй копию в `my_web_madlibs`.

Проверка: теперь есть `my_web_madlibs/app.py` и `my_web_madlibs/templates/madlibs.html`.

**Путь B:** В папке мастерской (рядом с `.venv`) создай `my_web_madlibs/` и положи туда `starter/app.py` и `starter/templates/` этого урока — та же идея, что у `my_adventure/`. См. [STUDENT-MAP](../STUDENT-MAP.ru.md).

---

### Шаг 1: Одна страница, одна форма

В `madlibs.html` есть форма, а история показывается ниже, когда `story` не пустая:

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

**TODO в starter:** прочитай четыре поля и собери историю через f-строку.

---

### Шаг 3: Запуск из my_web_madlibs

**1. Активируй venv.** Терминал VS Code стартует в корне проекта (там лежит `.venv`). Активируй:

```text
.venv\Scripts\Activate.ps1
```

**Командная строка (cmd):** `.venv\Scripts\activate.bat` · **macOS/Linux:** `source .venv/bin/activate`

В начале строки терминала должно появиться `(.venv)`.

**2. Зайди в папку итога и запусти** (те же команды на Windows, macOS/Linux и в Пути B):

```text
cd my_web_madlibs
python app.py
```

Открой `http://127.0.0.1:5000/`.

**Пример слов:** robot, dance, sparkly, moon base

---

### Шаг 4: Сделай по-своему

Поменяй шаблон истории или добавь пятое поле для слова. Оставь схему: форма → POST → история на той же странице.

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

Когда `(.venv)` уже активен, из корня проекта:

```text
cd my_web_madlibs
python app.py
```

**Ожидаемый вывод (терминал):**

```text
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

1. Открой `http://127.0.0.1:5000/`
2. Введи **Adjective** `sparkly`, **Noun** `robot`, **Verb** `dance`, **Place** `moon base` и нажми **Create Story**

**Ожидаемый вывод (браузер, под формой):**

```text
Your Story
One sunny day, a sparkly robot decided to dance all the way to moon base. The crowd cheered. The end!
```

**Ожидаемый результат:** твой абзац Mad-Libs появится под **Your Story**. Останови сервер сочетанием **Ctrl+C**, когда закончишь.

---

## Быстрые упражнения

1. **Карта полей** — сопоставь каждый `name="..."` с его `request.form.get(...)`.
2. **Пустое существительное** — отправь форму с одним пустым полем. Что выведется?
3. **Новое предложение** — перепиши историю про школу или спорт.

---

## Задание для практики

**Название квеста:** Твой веб Mad-Libs

1. Скопируй [starter/](starter/) в **`my_web_madlibs/`** в корне проекта.
2. Доделай все строки TODO в `app.py` и `madlibs.html`.
3. Напиши свой шаблон истории из двух предложений.
4. Проверь игру тремя разными наборами слов.

**Эталон:** [solution/](solution/)

---

## Уголок отладки

**Проблема:** Форма отправляется, но место для истории остаётся пустым

**Причина:** Переменная `story` так и не была задана внутри блока `if request.method == "POST":`.

**Решение:** Собери `story = f"..."` до `return render_template("madlibs.html", story=story)`.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. Куда копировать стартовый код для капстоуна?
   - **a)** В `my_web_madlibs/` в корне проекта
   - **b)** Внутрь `.venv/Scripts/`
   - **c)** Только в закладки браузера
   - **d)** В `course-1-python-basics/`

2. Форма Mad-Libs с `method="post"`. Куда попадают слова при отправке?
   - **a)** Сразу в `pip list`
   - **b)** В тело запроса — читаем через `request.form.get(...)`
   - **c)** Только в URL как `?noun=robot`
   - **d)** В `static/style.css`

3. Когда собирать переменную `story`?
   - **a)** Только в консоли браузера
   - **b)** После `deactivate`
   - **c)** В блоке `if request.method == "POST":` после чтения полей
   - **d)** До `app = Flask(__name__)`

4. Что делает `{% if story %}` в шаблоне?
   - **a)** Удаляет форму после одного использования
   - **b)** Устанавливает Jinja2 через pip
   - **c)** Сам меняет GET на POST
   - **d)** Показывает блок истории только если `story` не пустая

5. Каждый `<input name="noun">` должен совпадать с чем в `app.py`?
   - **a)** С тем же именем в `request.form.get("noun")`
   - **b)** С номером порта Flask
   - **c)** Со строкой `secret_key`
   - **d)** Только с именем декоратора `@app.route`

---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **a)** Итоговые папки — в корне проекта, как другие `my_*`.
2. **b)** POST отправляет поля в теле запроса, не в URL.
3. **c)** История собирается только после получения слов из формы.
4. **d)** Шаблон показывает результат, когда `story` не пустая.
5. **a)** Атрибут `name` в HTML = ключ в `request.form.get(...)`.

</details>

---

## Что дальше

→ [Урок 2.4: CSS и статика](../lesson-2-4-static-files-css/README.md) — подключи таблицу стилей через `url_for`.

---

*Твоя веб-фабрика историй открыта. Пора добавить стиль!*
