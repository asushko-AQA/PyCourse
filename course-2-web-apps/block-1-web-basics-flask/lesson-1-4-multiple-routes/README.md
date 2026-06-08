# Lesson 1.4: Multiple Routes & URL Calculator

> **Course:** Web Applications with Python  
> **Block:** Web Basics with Flask  
> **Time:** ~30–45 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level 4 — Mini-Site: Home, About, Jokes + URL Calculator |
| **[Русский →](ru.md)** | Уровень 4 — Мини-сайт: Home, About, Jokes + URL-калькулятор |

---

## What you'll build / Что ты создашь

**EN:** A three-page mini-site (Home, About, Jokes) plus a URL calculator at `/add/3/5` that shows `3 + 5 = 8`.

**RU:** Мини-сайт из трёх страниц (Home, About, Jokes) и URL-калькулятор `/add/3/5`, который показывает `3 + 5 = 8`.

## What you'll learn / Что ты узнаешь

- Add several routes to one Flask app
- Return simple HTML with links between pages
- Use **typed** URL variables (`<int:a>`) for numbers
- Build a calculator route without a form (preview for Block 2)

## Before you start / Перед стартом

- [ ] Completed [Lesson 1.3](../lesson-1-3-dynamic-routes/README.md) — `/hello/<name>` works
- [ ] Activated your `.venv`
- [ ] Know basic HTML tags: `<h1>`, `<p>`, `<a href='...'>`

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/app.py](starter/app.py) | Starter mini-site with TODOs |
| [solution/app.py](solution/app.py) | Reference solution |

## Quick drills / Быстрые упражнения

1. Click every link on the home page — About, Jokes, calculator examples.
2. Change `/add/10/7` in the URL — does the sum update?
3. Count your routes — you should have at least four besides `/`.

*(Full drills are in [en.md](en.md) / [ru.md](ru.md).)*

---

**Previous lesson / Предыдущий урок:** [Lesson 1.3 — Dynamic Routes](../lesson-1-3-dynamic-routes/README.md)

**Next lesson / Следующий урок:** [Lesson 2.1 — HTML Templates](../../block-2-making-it-beautiful-interactive/lesson-2-1-html-templates/README.md)
