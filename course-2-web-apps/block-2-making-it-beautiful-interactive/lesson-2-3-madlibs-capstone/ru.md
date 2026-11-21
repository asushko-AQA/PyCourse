# Урок 2.3: Mad-Libs (итог)

> **Курс:** Веб-приложения на Python · **Блок:** Красота и интерактив · **~35–45 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Уровень 11 — Веб-фабрика историй**

---

## Объяснение

Первый **веб-итог**! Mad-Libs в браузере — как `madlibs.py` из Курса 1.

Создай **`my_web_madlibs/`** в корне проекта.

**Путь A:**

```text
cd Documents\PyCourse
mkdir my_web_madlibs
```

Скопируй [starter/](starter/) в `my_web_madlibs/`.

**Путь B:** На Рабочем столе — см. [STUDENT-MAP](../STUDENT-MAP.ru.md).

---

### Шаг 1–2: Форма и история

`madlibs.html` — форма и блок `{% if story %}`. В POST читай `noun`, `verb`, `adjective`, `place` и собери f-строку.

**TODO в starter:** поля в HTML и логика в `app.py`.

---

### Шаг 3: Запуск

```text
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
2. Введи слова и нажми **Create Story**

**Ожидаемый результат:** под **Your Story** появится твой абзац Mad-Libs.

---

## Быстрые упражнения

1. **Сопоставь поля** — каждый `name="..."` связан с `request.form.get(...)`.
2. **Пустое существительное** — отправь с пустым полем. Что выведется?
3. **Новое предложение** — перепиши историю про школу или спорт.

---

## Задание для практики

**Квест:** Скопируй в `my_web_madlibs/`, доделай TODO, свой шаблон истории. **Эталон:** [solution/](solution/)

---

## Уголок отладки

**Проблема:** История пустая — переменная `story` не задана в блоке POST.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. Куда копировать стартовый код для капстоуна?
   - **a)** В `my_web_madlibs/` в корне проекта
   - **b)** Внутрь `.venv/Scripts/`
   - **c)** Только в закладки браузера
   - **d)** В `course-1-python-basics/`

2. Форма Mad-Libs с `method="post"`. Куда попадают слова при отправке?
   - **a)** В тело запроса — читаем через `request.form.get(...)`
   - **b)** Только в URL как `?noun=robot`
   - **c)** В `static/style.css`
   - **d)** Сразу в `pip list`

3. Когда собирать переменную `story`?
   - **a)** В блоке `if request.method == "POST":` после чтения полей
   - **b)** До `app = Flask(__name__)`
   - **c)** Только в консоли браузера
   - **d)** После `deactivate`

4. Что делает `{% if story %}` в шаблоне?
   - **a)** Показывает блок истории только если `story` не пустая
   - **b)** Удаляет форму после одного использования
   - **c)** Устанавливает Jinja2 через pip
   - **d)** Сам меняет GET на POST

5. Каждый `<input name="noun">` должен совпадать с чем в `app.py`?
   - **a)** С тем же именем в `request.form.get("noun")`
   - **b)** С номером порта Flask
   - **c)** Со строкой `secret_key`
   - **d)** Только с именем декоратора `@app.route`

---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **a)** Итоговые папки — в корне проекта, как другие `my_*`.
2. **a)** POST отправляет поля в теле запроса, не в URL.
3. **a)** История собирается только после получения слов из формы.
4. **a)** Шаблон показывает результат, когда `story` не пустая.
5. **a)** Атрибут `name` в HTML = ключ в `request.form.get(...)`.

</details>

---

## Что дальше

→ [Урок 2.4: CSS и статика](../lesson-2-4-static-files-css/README.md)
