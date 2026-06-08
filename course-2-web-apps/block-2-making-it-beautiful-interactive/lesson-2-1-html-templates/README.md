# Lesson 2.1: HTML Templates

> **Course:** Web Applications with Python · **Block:** Making It Beautiful & Interactive · **Time:** ~30 min

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Studio Pages — shared layout |
| **[Русский →](ru.md)** | Studio Pages — общий шаблон |

---

## What you'll build / Что ты создашь

**EN:** A mini-site with a shared `base.html` layout and child pages (`home.html`, `about.html`) rendered with `render_template`.

**RU:** Мини-сайт с общим `base.html` и дочерними страницами через `render_template`.

## What you'll learn / Что ты узнаешь

- `render_template` — send an HTML file to the browser
- Jinja2 `{% extends %}` and `{% block %}` — reuse one layout
- Passing variables from Python into HTML (`{{ page_title }}`)

## Before you start / Перед стартом

- [ ] Completed [Lesson 1.4](../../block-1-web-basics-flask/lesson-1-4-multiple-routes/README.md)
- [ ] Virtual environment active with Flask installed

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/app.py](starter/app.py) | Flask app skeleton |
| [starter/templates/](starter/templates/) | Base + child HTML templates |
| [solution/](solution/) | Reference solution |

---

**Previous / Предыдущий:** [Lesson 1.4 — Multiple Routes](../../block-1-web-basics-flask/lesson-1-4-multiple-routes/README.md)

**Next / Следующий:** [Lesson 2.2 — HTML Forms](../lesson-2-2-html-forms/README.md)
