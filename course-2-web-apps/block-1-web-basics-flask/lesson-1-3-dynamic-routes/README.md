# Lesson 1.3: Dynamic Routes

> **Course:** Web Applications with Python  
> **Block:** Web Basics with Flask  
> **Time:** ~30 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level 3 — Personal Greetings with `/hello/<name>` |
| **[Русский →](ru.md)** | Уровень 3 — Личные приветствия с `/hello/<name>` |

---

## What you'll build / Что ты создашь

**EN:** A Flask page that greets anyone by name — visit `/hello/Alex` or `/hello/YourName` and see a custom message.

**RU:** Flask-страница с приветствием по имени — зайди на `/hello/Alex` или `/hello/ТвоёИмя` и увидишь личное сообщение.

## What you'll learn / Что ты узнаешь

- Add a **variable part** to a URL path (`<name>`)
- Pass URL data into a route function as a parameter
- Use an f-string to build a personalized response

## Before you start / Перед стартом

- [ ] Completed [Lesson 1.2](../lesson-1-2-first-web-page/README.md) — ran a Flask app in the browser
- [ ] Activated your `.venv`
- [ ] Comfortable stopping the server with `Ctrl+C`

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/app.py](starter/app.py) | Starter app with TODO |
| [solution/app.py](solution/app.py) | Reference solution |

## Quick drills / Быстрые упражнения

1. Visit `/hello/World` — does it say `Hello, World!`?
2. Change the name in the URL bar — refresh and watch the greeting change.
3. Try `/hello/` with nothing after it — what error do you see?

*(Full drills are in [en.md](en.md) / [ru.md](ru.md).)*

---

**Previous lesson / Предыдущий урок:** [Lesson 1.2 — First Web Page](../lesson-1-2-first-web-page/README.md)

**Next lesson / Следующий урок:** [Lesson 1.4 — Multiple Routes](../lesson-1-4-multiple-routes/README.md)
