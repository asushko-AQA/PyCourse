# Урок 2.1: HTML-шаблоны

> **Курс:** Веб-приложения на Python · **Блок:** Красота и интерактив · **~30 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Studio Pages — общий шаблон**

---

## Объяснение

В Блоке 1 ты возвращал HTML одной большой строкой. **Шаблоны** — отдельные HTML-файлы в папке `templates/`. Flask заполняет их через **Jinja2**.

Представь `base.html` как рамку для картины: ссылки меню и пустое место (`{% block content %}`), куда каждая страница рисует свой контент.

**Новый термин:** `render_template("home.html", page_title="Home")` — Flask находит файл, запускает Jinja2 и отправляет готовый HTML в браузер.

---

### Шаг 1: Изучи base.html

В [starter/templates/base.html](starter/templates/base.html) лежит общее меню. Дочерние страницы его **расширяют**:

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

Переменные, которые ты передаёшь из Python, становятся `{{ headline }}` в HTML.

---

### Шаг 3: Добавь маршруты About и Jokes

**TODO в starter:** добавь маршруты `/about` и `/jokes` со своими шаблонами. Передай текст шутки переменными — та же идея, что в уроке 1.4 Блока 1, только теперь отдельные файлы шаблонов, а не одна длинная строка.

---

### Шаг 4: Запусти приложение

**Путь A:**

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-1-html-templates
python starter\app.py
```

**Путь B:** Скопируй всю папку `starter/` в свой проект. Активируй venv и запусти `python app.py`. См. [STUDENT-MAP](../STUDENT-MAP.ru.md).

**Mac/Linux:** `python starter/app.py`

Открой `http://127.0.0.1:5000/` и нажми **About** и **Jokes**.

**Ожидаемый результат:** у всех трёх страниц одно и то же меню; меняется только середина.

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

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-1-html-templates
python starter\app.py
```

**Mac/Linux:** `python starter/app.py`

Открой `http://127.0.0.1:5000/`, затем **About** и **Jokes**.

**Ожидаемый результат:** общая навигация на каждой странице; меняется только середина.

---

## Быстрые упражнения

1. **Место блока** — найди `{% block content %}` в `base.html`. Что туда попадает?
2. **Новая переменная** — передай `bio="..."` в `about.html` и покажи её в `<p>`.
3. **Четвёртая страница** — добавь `/contact` с новым дочерним шаблоном (бонус: ссылка в меню).

---

## Задание для практики

**Квест:** Доделай Studio Pages

1. Заполни все строки TODO в `app.py` и дочерних шаблонах.
2. Открой `/`, `/about` и `/jokes`.
3. **Бонус:** напиши свою шутку в шаблоне Jokes.

**Эталон:** [solution/](solution/)

---

## Уголок отладки

**Проблема:** `TemplateNotFound: home.html`

**Причина:** Flask ищет шаблоны в папке `templates/` рядом с `app.py`.

**Исправление:** Проверь, что файл `starter/templates/home.html` есть, и запускай `app.py` из папки урока (или копируй `templates/` вместе с приложением).

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. Зачем выносить HTML в `templates/`, а не в одну длинную строку в `app.py`?
   - **a)** Удобнее читать, править и переиспользовать общий каркас
   - **b)** Flask после Блока 1 не отдаёт строки
   - **c)** Браузеры больше не показывают строки
   - **d)** pip сам устанавливает шаблоны

2. Что делает `render_template("home.html", headline="Welcome")`?
   - **a)** Скачивает home.html из интернета
   - **b)** Подставляет переменные в шаблон и отправляет HTML в браузер
   - **c)** Копирует CSS в терминал
   - **d)** Активирует виртуальное окружение

3. В Jinja2 что значит `{{ headline }}`?
   - **a)** Закомментировать HTML
   - **b)** Запустить функцию Python
   - **c)** Показать значение переменной `headline` из Python
   - **d)** Ссылка на `static/style.css`

4. Для чего `{% block content %}` в `base.html`?
   - **a)** Номер порта (5000)
   - **b)** Список пакетов pip
   - **c)** Секретный ключ Flask
   - **d)** Место, куда дочерняя страница вставляет свой уникальный контент

5. Дочерний шаблон начинается с `{% extends "base.html" %}`. Это значит?
   - **a)** Переиспользовать общую рамку (меню, разметку) из `base.html`
   - **b)** Удалить `base.html` после сохранения
   - **c)** Запускать приложение без `app.run()`
   - **d)** Отправлять формы только через GET

---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **a)** Шаблоны отделяют вёрстку от логики Python.
2. **b)** `render_template` подставляет данные в HTML-файлы.
3. **c)** Двойные фигурные скобки выводят значение переменной.
4. **d)** Дочерние шаблоны заполняют блок `content`.
5. **a)** `extends` наследует каркас родителя.

</details>

---

## Что дальше

→ [Урок 2.2: HTML-формы](../lesson-2-2-html-forms/README.md) — отправка данных через GET и POST.

---

*Один каркас, много страниц — студия обретает форму!*

[← Выбрать язык](README.md)
