# Урок 2.1: HTML-шаблоны

> **Курс:** Веб-приложения на Python · **Блок:** Красота и интерактив · **~30 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Studio Pages — общий шаблон**

---

## Объяснение

В Блоке 1 HTML был одной строкой. **Шаблоны** — отдельные файлы в `templates/`. Flask заполняет их через **Jinja2**.

`base.html` — рамка с меню и `{% block content %}`, куда каждая страница вставляет свой контент.

**Новый термин:** `render_template("home.html", page_title="Home")` — Flask обрабатывает шаблон и отправляет HTML в браузер.

---

### Шаг 1: Изучи base.html

Дочерние страницы **расширяют** базу:

```html
{% extends "base.html" %}
{% block content %}
<h1>{{ headline }}</h1>
{% endblock %}
```

---

### Шаг 2: Маршрут Home

```python
return render_template("home.html", page_title="Home", headline="Welcome to My Studio")
```

---

### Шаг 3: Добавь About и Jokes

**TODO в starter:** маршруты `/about` и `/jokes` с отдельными шаблонами.

---

### Шаг 4: Запуск

**Путь A:**

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-1-html-templates
python starter\app.py
```

**Путь B:** Скопируй `starter/` — см. [STUDENT-MAP](../STUDENT-MAP.ru.md).

**Mac/Linux:** `python starter/app.py`

**Ожидаемый результат:** общее меню на всех страницах, разный контент в середине.

---

## Быстрые упражнения

1. Найди `{% block content %}` в `base.html`.
2. Передай `bio="..."` в `about.html`.
3. **Бонус:** страница `/contact`.

---

## Практическое задание

**Квест:** Доделай Studio Pages — все TODO, три страницы работают. **Эталон:** [solution/](solution/)

---

## Уголок отладки

**Проблема:** `TemplateNotFound: home.html` — нет файла в `templates/` рядом с `app.py`.

---

## Что дальше

→ [Урок 2.2: HTML-формы](../lesson-2-2-html-forms/README.md)
