# Lesson 1.2: First Web Page

> **Course:** Web Applications with Python  
> **Block:** Web Basics with Flask  
> **Time:** ~30 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level 2 — Hello, Web World! Your First Live Page |
| **[Русский →](ru.md)** | Уровень 2 — Hello, Web World! Твоя первая живая страница |

---

## What you'll build / Что ты создашь

**EN:** A tiny Flask app that serves **Hello, Web World!** in your browser at `http://127.0.0.1:5000`.

**RU:** Крошечное Flask-приложение, которое показывает **Hello, Web World!** в браузере по адресу `http://127.0.0.1:5000`.

## What you'll learn / Что ты узнаешь

- Create a Flask app object
- Map a URL path (`/`) to a Python function with `@app.route`
- Start the dev server and open it in a browser
- Stop the server with `Ctrl+C`

## Before you start / Перед стартом

- [ ] Completed [Lesson 1.1](../lesson-1-1-installing-flask/README.md) — Flask imports OK in venv
- [ ] Activated your `.venv` in the terminal
- [ ] Read [Lesson 0.2 — How the Web Works](../../block-0-environment-setup/lesson-0-2-how-the-web-works/README.md) (browser ↔ server idea)

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/app.py](starter/app.py) | Starter app with TODOs |
| [solution/app.py](solution/app.py) | Reference solution |

## Quick drills / Быстрые упражнения

1. Run `python starter\app.py` — leave the terminal "busy" (server running).
2. Open `http://127.0.0.1:5000` in your browser.
3. Press `Ctrl+C` in the terminal to stop the server.

*(Full drills are in [en.md](en.md) / [ru.md](ru.md).)*

---

**Previous lesson / Предыдущий урок:** [Lesson 1.1 — Installing Flask](../lesson-1-1-installing-flask/README.md)

**Next lesson / Следующий урок:** [Lesson 1.3 — Dynamic Routes](../lesson-1-3-dynamic-routes/README.md)
