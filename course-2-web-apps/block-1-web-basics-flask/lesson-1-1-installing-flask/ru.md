# Урок 1.1: Установка Flask

> **Курс:** Веб-приложения на Python · **Блок:** Основы Flask · **~30 мин**  
> [Choose language / Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Уровень 1 — Проверка Flask: готова ли Route Lab?**

---

## Объяснение

Добро пожаловать в **Route Lab** — Блок 1 Курса 2! Ты уже создал **виртуальное окружение** (`.venv`) и установил Flask в [Блоке 0, Урок 0.1](../../block-0-environment-setup/lesson-0-1-virtual-environments/README.md). Этот урок — **быстрая проверка**, а не повторение темы venv.

Представь venv как **личный ящик с инструментами** для веб-проекта. Flask лежит в этом ящике. Перед каждым уроком Flask сначала **открой ящик** — это называется **активация** venv.

---

### Шаг 1: Открой проект в VS Code

1. Открой VS Code.
2. **File → Open Folder** — выбери папку `PyCourse` (или свою папку с `.venv`).
3. **Terminal → New Terminal** (или **Ctrl + `**).

---

### Шаг 2: Активируй venv (краткое напоминание)

**Windows PowerShell** (чаще всего в VS Code):

```text
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt (cmd):**

```text
.venv\Scripts\activate.bat
```

**macOS / Linux:**

```text
source .venv/bin/activate
```

**Как понять, что сработало:** в начале строки появится `(.venv)`.

**Нет `.venv`?** Вернись к [Уроку 0.1](../../block-0-environment-setup/lesson-0-1-virtual-environments/README.md), создай окружение, выполни `pip install flask`, затем возвращайся сюда.

---

### Шаг 3: Убедись, что Flask установлен

При активном `(.venv)` выполни:

```text
pip list
```

Найди в списке **Flask** с номером версии (например `3.0.0`).

**Flask нет в списке?** Установи сейчас:

```text
pip install flask
```

---

### Шаг 4: Открой скрипт проверки

Открой [starter/check_flask.py](starter/check_flask.py). Выполни три TODO:

1. `import flask` в начале файла
2. `print("Flask import OK!")`
3. Выведи версию Flask через `importlib.metadata.version("flask")`

**Подсказка для строки с версией:**

```python
import importlib.metadata

print(f"Flask version: {importlib.metadata.version('flask')}")
```

---

### Шаг 5: Перейди в папку урока

**Путь A — репозиторий PyCourse:**

```text
cd course-2-web-apps\block-1-web-basics-flask\lesson-1-1-installing-flask
```

**Путь B — своя копия:** `cd` в папку, где лежит `check_flask.py`.

---

### Шаг 6: Запусти проверку

```text
python starter\check_flask.py
```

**Ожидаемый вывод:**

```text
Flask import OK!
Flask version: 3.x.x
```

(Номер версии может отличаться — это нормально.)

---

## Быстрые упражнения

1. Выполни `pip list` — обведи **Flask** на стикере.
2. Запусти скрипт — обе строки без ошибок.
3. Введи `deactivate`, запусти снова — увидишь `ModuleNotFoundError`? Активируй venv и повтори.

---

## Попробуй сам

### Задание 1 (обязательное)

Добавь ещё один `print()` с текстом `Route Lab ready!` после строки с версией. Запусти скрипт снова.

### Задание 2 (бонус)

Выполни `pip show flask` в терминале. Найди строку **Location** — там pip сохранил Flask внутри venv.

---

## Уголок отладки

**Проблема:** `ModuleNotFoundError: No module named 'flask'`

**Причина:** venv не активирован или Flask не установлен в этом venv.

**Решение:** Выполни `.\.venv\Scripts\Activate.ps1` (или команду для своей ОС), затем `pip install flask`, затем снова запусти скрипт.

---

**Проблема:** `running scripts is disabled on this system` при активации (PowerShell)

**Причина:** Windows заблокировал скрипт активации.

**Решение:** Попроси взрослого один раз выполнить: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` — затем активируй снова.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. Этот урок в основном проверяет готовность Flask — а не повтор какого шага из Блока 0?
   - **a)** Создание и использование виртуального окружения
   - **b)** Графика Turtle
   - **c)** Mad-Libs в терминале
   - **d)** Установка Pygame

2. Если при активном `(.venv)` в `pip list` есть Flask — где он установлен?
   - **a)** Внутри venv этого проекта
   - **b)** Только на сайте компании Flask
   - **c)** В кэше браузера
   - **d)** В каждой папке на рабочем столе

3. `python starter\check_flask.py` даёт `ModuleNotFoundError: No module named 'flask'`. Самое вероятное решение?
   - **a)** Активировать venv, `pip install flask`, запустить снова
   - **b)** Удалить `.venv` и больше не использовать pip
   - **c)** Сменить порт на 8080
   - **d)** Добавить `@app.route` в проверочный скрипт

4. Что должен вывести `check_flask.py` при успехе?
   - **a)** `Flask import OK!` и строку с версией Flask
   - **b)** Только `Hello, Web World!` в браузере
   - **c)** Список всех сайтов интернета
   - **d)** Ничего — тишина значит успех

5. Зачем в уроках Flask сначала активируют `.venv`?
   - **a)** Чтобы Python использовал ящик, где лежит Flask
   - **b)** Потому что Flask работает только по вторникам
   - **c)** Чтобы автоматически включить `debug=True`
   - **d)** Потому что без этого нельзя создать маршруты

---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **a)** Блок 0 учил venv + pip; этот урок проверяет, что Flask на месте.
2. **a)** Активный venv + `pip list` показывает пакеты в этом окружении.
3. **a)** Обычно venv не активен или Flask туда не ставили.
4. **a)** Проверочный скрипт подтверждает импорт и печатает версию.
5. **a)** Flask должен импортироваться из активного venv проекта.

</details>

---

## Что дальше

→ [Урок 1.2: Первая веб-страница](../lesson-1-2-first-web-page/README.md) — покажи **Hello, Web World!** в браузере.

---

*Flask в твоём ящике инструментов. Следующая остановка — настоящая веб-страница!*

[← Выбрать язык](README.md)
