# Lesson 0.1: Virtual Environments & pip

> **Course:** Web Applications with Python  
> **Block:** Environment Setup  
> **Time:** ~30–45 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level 0 — Your Isolated Web Toolbox |
| **[Русский →](ru.md)** | Уровень 0 — Изолированный веб-инструментарий |

---

## What you'll build / Что ты создашь

**EN:** A `.venv` folder in your project, Flask installed with `pip`, and a quick `check_setup.py` run that confirms your workshop is ready.

**RU:** Папку `.venv` в проекте, Flask установленный через `pip`, и быстрый запуск `check_setup.py`, подтверждающий готовность мастерской.

## What you'll learn / Что ты узнаешь

- Why virtual environments keep project tools separate (isolated toolbox)
- Creating a `.venv` with `python -m venv`
- Activating and deactivating a venv (Windows PowerShell, cmd, Mac/Linux)
- Installing packages with `pip install`

## Before you start / Перед стартом

- [ ] Completed [Course 1 Block 5 readiness checklist](../../../course-1-python-basics/block-5-creative-turtle/README.md#block-5-readiness-checklist)
- [ ] Python 3.12+ works (`python --version` in a terminal)
- [ ] VS Code installed with the Python extension

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/check_setup.py](starter/check_setup.py) | Optional check script (with TODOs) |
| [solution/check_setup.py](solution/check_setup.py) | Reference check script |

## Quick drills / Быстрые упражнения

1. Run `pip list` after installing Flask — spot `Flask` in the list before running the check script.
2. Deactivate with `deactivate`, run `check_setup.py` again — see how the wrong Python can miss Flask.
3. Reactivate and run again — back to `venv ready`.

---

**Previous / Предыдущий блок:** [Block 0 index](../README.md) · [Course 1 Block 5](../../../course-1-python-basics/block-5-creative-turtle/README.md)

**Next lesson / Следующий урок:** [Lesson 0.2 — How the Web Works](../lesson-0-2-how-the-web-works/README.md)
