# Урок 2.1: HTML-шаблоны

> **Курс:** Веб-приложения на Python · **Блок:** Красота и интерактив · **~30 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Studio Pages — общий шаблон**

---

## Объяснение

В Блоке 1 ты возвращал HTML одной длинной строкой. **Шаблоны** — это отдельные HTML-файлы в папке `templates/`. Flask заполняет их с помощью **Jinja2**.

Представь `base.html` как рамку для картины: в ней ссылки меню и пустое место (`{% block content %}`), где каждая страница рисует своё содержимое.

**Новый термин:** `render_template("home.html", page_title="Home")` — Flask находит файл, прогоняет его через Jinja2 и отправляет готовый HTML в браузер.

---

### Шаг 1: Изучи base.html

В [starter/templates/base.html](starter/templates/base.html) — общее меню навигации. Дочерние страницы **расширяют** (extends) его:

```html
{% extends "base.html" %}
{% block content %}
<h1>{{ headline }}</h1>
{% endblock %}
```

---

### Шаг 2: Маршрут Home

```python
@app.route("/")
def home():
    return render_template(
        "home.html",
        page_title="Home",
        headline="Welcome to My Studio",
    )
```

Переменные, которые ты передаёшь из Python, превращаются в `{{ headline }}` в HTML.

---

### Шаг 3: Добавь маршруты About и Jokes

**TODO в starter:** добавь маршруты `/about` и `/jokes` со своими шаблонами. Передай текст шутки через переменные — та же идея, что в Уроке 1.4 Блока 1, только с файлами шаблонов вместо одной длинной строки.

---

### Шаг 4: Запусти приложение

**1. Активируй venv.** В VS Code открой папку, где лежит твой `.venv` (**Путь A:** папка `PyCourse`; **Путь B:** твоя папка-мастерская, например `web_workshop`). Открой терминал (**Terminal → New Terminal**) — он сразу запускается в этой папке. Активируй:

```text
.venv\Scripts\Activate.ps1
```

**Командная строка (cmd):** `.venv\Scripts\activate.bat` · **macOS/Linux:** `source .venv/bin/activate`

В начале строки терминала должно появиться `(.venv)`.

**2. Перейди в папку starter и запусти.**

**Путь A:**

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-1-html-templates\starter
python app.py
```

**macOS/Linux:** `cd course-2-web-apps/block-2-making-it-beautiful-interactive/lesson-2-1-html-templates/starter`, затем `python app.py`

**Путь B:** Скопируй всю папку `starter/` этого урока (вместе с `templates/` внутри) в свою папку-мастерскую, рядом с `.venv`, и переименуй её в `lesson-2-1`. Затем `cd lesson-2-1` и `python app.py`. См. [STUDENT-MAP](../STUDENT-MAP.ru.md).

Открой `http://127.0.0.1:5000/` и нажми **About** и **Jokes**.

**Ожидаемый результат:** у всех трёх страниц одно и то же меню; меняется только содержимое в середине.

---

## Пример кода

**Файл: [solution/app.py](solution/app.py)**

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "home.html",
        page_title="Home",
        headline="Welcome to My Studio",
    )


@app.route("/about")
def about():
    return render_template(
        "about.html",
        page_title="About",
        bio="I am learning Flask and building pages with templates!",
    )


if __name__ == "__main__":
    app.run(port=5000, debug=True)
```

Дочерние шаблоны лежат в `solution/templates/` — каждый расширяет [solution/templates/base.html](solution/templates/base.html).

---

## Запуск кода

С активным `(.venv)`, из папки, открытой в VS Code:

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-1-html-templates\starter
python app.py
```

**macOS/Linux:** `cd course-2-web-apps/block-2-making-it-beautiful-interactive/lesson-2-1-html-templates/starter`, затем `python app.py` · **Путь B:** `cd lesson-2-1`, затем `python app.py`

**Ожидаемый вывод (терминал):**

```text
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Открой `http://127.0.0.1:5000/`, затем **About** и **Jokes**.

**Ожидаемый вывод (браузер, главная страница):**

```text
Home | About | Jokes
Welcome to My Studio
Use the links above to visit About and Jokes.
```

**Ожидаемый результат:** общее меню на каждой странице; меняется только середина. Останови сервер клавишами **Ctrl+C**, когда закончишь.

---

## Быстрые упражнения

1. **Где блок** — найди `{% block content %}` в `base.html`. Что туда попадает?
2. **Новая переменная** — передай `bio="..."` в `about.html` и покажи её в `<p>`.
3. **Четвёртая страница** — добавь `/contact` с новым дочерним шаблоном (бонус: добавь ссылку в меню).

---

## Задание для практики

**Квест:** Доделай Studio Pages

1. Выполни все TODO в `app.py` и дочерних шаблонах.
2. Открой `/`, `/about` и `/jokes`.
3. **Бонус:** Напиши свою шутку в шаблоне Jokes.

**Эталон:** [solution/](solution/)

---

## Уголок отладки

**Проблема:** `TemplateNotFound: home.html`

**Причина:** Flask ищет шаблоны в папке `templates/`, которая лежит **прямо рядом с `app.py`**, — а не в той папке, где сейчас находится терминал.

**Решение:** Проверь, что файл лежит по пути `templates/home.html` рядом с `app.py` (если копировал `app.py`, скопируй и его папку `templates/`). Проверь написание: папка называется `templates` с буквой **s** на конце, а имя файла должно точно совпадать с `render_template("home.html", ...)`.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. Зачем выносить HTML в `templates/`, а не в одну длинную строку в `app.py`?
   - **a)** Браузеры больше не показывают строки
   - **b)** pip сам устанавливает шаблоны
   - **c)** Удобнее читать, править и переиспользовать общий каркас
   - **d)** Flask после Блока 1 не отдаёт строки

2. Что делает `render_template("home.html", headline="Welcome")`?
   - **a)** Скачивает home.html из интернета
   - **b)** Копирует CSS в терминал
   - **c)** Активирует виртуальное окружение
   - **d)** Подставляет переменные в шаблон и отправляет HTML в браузер

3. В Jinja2 что значит `{{ headline }}`?
   - **a)** Показать значение переменной `headline` из Python
   - **b)** Запустить функцию Python
   - **c)** Закомментировать HTML
   - **d)** Ссылка на `static/style.css`

4. Для чего `{% block content %}` в `base.html`?
   - **a)** Номер порта (5000)
   - **b)** Место, куда дочерняя страница вставляет свой уникальный контент
   - **c)** Список пакетов pip
   - **d)** Секретный ключ Flask

5. Дочерний шаблон начинается с `{% extends "base.html" %}`. Это значит?
   - **a)** Запускать приложение без `app.run()`
   - **b)** Отправлять формы только через GET
   - **c)** Переиспользовать общую рамку (меню, разметку) из `base.html`
   - **d)** Удалить `base.html` после сохранения

---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **c)** Шаблоны отделяют вёрстку от логики Python.
2. **d)** `render_template` подставляет данные в HTML-файлы.
3. **a)** Двойные фигурные скобки выводят значение переменной.
4. **b)** Дочерние шаблоны заполняют блок `content`.
5. **c)** `extends` наследует каркас родителя.

</details>

---

## Что дальше

→ [Урок 2.2: HTML-формы](../lesson-2-2-html-forms/README.md) — отправляем данные через GET и POST.

---

*Один каркас — много страниц. Твоя студия обретает форму!*
