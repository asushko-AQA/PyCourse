# Урок 0.1: Виртуальные окружения и pip

> **Курс:** Веб-приложения на Python · **Блок:** Настройка окружения · **~30–45 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Уровень 0 — Изолированный веб-инструментарий**

---

## Объяснение

Добро пожаловать в **Веб-мастерскую**! Прежде чем собирать страницы в браузере, нужен чистый ящик для инструментов вроде Flask.

**Виртуальное окружение** (`.venv`) — подписанный ящик только для этого проекта. Пакеты из `pip` остаются внутри и не смешиваются с другими проектами на компьютере.

**Один ящик на весь Курс 2.** Создай `.venv` в папке, которую открываешь в VS Code. В репозитории PyCourse это **корень проекта** (`PyCourse`). Урок 1.1 и капстоуны `my_web_madlibs/` и `my_web_calc/` активируют **тот же** `.venv`. Не создавай второй `.venv` внутри папки урока.

**Путь A — репозиторий PyCourse:** **File → Open Folder** → `PyCourse`. **Terminal → New Terminal** уже стартует там. Если приглашение заканчивается на `PyCourse`, ты на месте. **Не** делай `cd` в папку урока до `python -m venv .venv`.

**Путь B — своя папка:** создай папку (например `web_workshop`), открой **её** в VS Code и скопируй туда [starter/check_setup.py](starter/check_setup.py). Все команды ниже выполняются в открытой папке. `.venv` лежит рядом с этой копией.

Один раз проверь Python: `python --version` должен показать `Python 3.12` или новее. На macOS, если `python` не найден, используй `python3 --version` и дальше в уроке пиши `python3` вместо `python`.

---

### Шаг 1: Создай `.venv`

В терминале VS Code (корень `PyCourse` для пути A, своя папка для пути B):

```text
python -m venv .venv
```

Папка `.venv` появится **здесь**. Это может занять несколько секунд.

---

### Шаг 2: Активируй venv

**Windows PowerShell** (обычный терминал VS Code):

```text
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt (cmd):**

```text
.venv\Scripts\activate.bat
```

**macOS / Linux:**

```text
source .venv/bin/activate
```

Когда активация сработала, в начале приглашения часто видно `(.venv)`. После этого можно менять папки — ящик остаётся открытым.

---

### Шаг 3: Установи Flask через pip

```text
pip install flask
```

`pip` — установщик пакетов Python. Он скачивает Flask только в твой `.venv`.

---

### Шаг 4: Два новых инструмента и проверочный скрипт

Открой [starter/check_setup.py](starter/check_setup.py). Каркас уже содержит `try` / `except`. Тебе нужно дописать `print` на местах `# TODO`.

**`try` / `except`** — страховочная сетка. Python выполняет блок `try`. Если `import flask` не удался, возникает `ImportError`, и выполнение прыгает в `except`, а не падает с ошибкой. Там ты печатаешь шаги настройки.

**`importlib.metadata.version("flask")`** узнаёт версию установленного Flask и возвращает текст вроде `3.1.3`. Вставь его в f-строку: `print(f"Flask version: {importlib.metadata.version('flask')}")`.

Допиши строки `# TODO` внутри `main()`. Форма уже есть в файле:

```python
import importlib.metadata


def main():
    try:
        import flask
        # TODO: print "venv ready"
        # TODO: print the version with importlib.metadata.version("flask")
    except ImportError:
        print("Flask is not installed yet.")
        # TODO: print "Steps:" and three numbered lines
        # (activate .venv, pip install flask, run this script again)
```

**Путь A — Windows** (из `PyCourse`, когда уже видно `(.venv)`):

```text
cd course-2-web-apps\block-0-environment-setup\lesson-0-1-virtual-environments
python starter\check_setup.py
```

**Путь A — macOS:**

```text
cd course-2-web-apps/block-0-environment-setup/lesson-0-1-virtual-environments
python starter/check_setup.py
```

**Путь B:** ты скопировал `check_setup.py` рядом с `.venv`, поэтому запусти `python check_setup.py`.

**Ожидаемый вывод (venv активен, Flask установлен):**

```text
venv ready
Flask version: 3.x.x
```

---

### Шаг 5: Деактивация (по желанию)

```text
deactivate
```

Приглашение снова обычное. Запусти ту же команду `python starter\check_setup.py` ещё раз (macOS: `python3 starter/check_setup.py`) — дружелюбное сообщение подскажет, что делать. Перед следующим уроком активируй venv снова.

---

## Пример кода

**Файл: [solution/check_setup.py](solution/check_setup.py)** (после TODO)

```python
import importlib.metadata


def main():
    try:
        import flask

        print("venv ready")
        print(f"Flask version: {importlib.metadata.version('flask')}")
    except ImportError:
        print("Flask is not installed yet.")
        print("Steps:")
        print("  1. Activate your .venv (see lesson steps)")
        print("  2. Run: pip install flask")
        print("  3. Run this script again")


main()
```

---

## Запуск кода

Запускай из папки, которую открыл (`PyCourse` для пути A). Создай и активируй `.venv` **там**, затем зайди в урок и запусти скрипт.

**Windows PowerShell:**

```text
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install flask
cd course-2-web-apps\block-0-environment-setup\lesson-0-1-virtual-environments
python starter\check_setup.py
```

**macOS / Linux:**

```text
python3 -m venv .venv
source .venv/bin/activate
pip install flask
cd course-2-web-apps/block-0-environment-setup/lesson-0-1-virtual-environments
python3 starter/check_setup.py
```

**Ожидаемый вывод (venv активен, Flask установлен):**

```text
venv ready
Flask version: 3.x.x
```

---

## Быстрые упражнения

1. Выполни `pip list` и найди `Flask` в списке.
2. Введи `deactivate` и снова `pip list`. Во втором списке Flask быть не должно. Активируй ещё раз.
3. Пока видно `(.venv)`, выполни `where python` (Windows) или `which python` (macOS). В пути должно быть `.venv`. Если переименуешь или перенесёшь папку проекта, удали `.venv` и повтори шаги 1–3. Перенесённый ящик хранит старые пути и перестаёт работать.

---

## Задание для практики

**Квест:** Наклейка мастерской

1. Когда печатается `venv ready`, добавь в скрипт ещё строку: `print("My web workshop is open!")`
2. Запусти снова и покажи вывод родителям или учителю.

**Эталонное решение:** [solution/check_setup.py](solution/check_setup.py)

---

## Уголок отладки

**Проблема:** `Activate.ps1` cannot be loaded because running scripts is disabled.

**Причина:** настройки Windows блокируют некоторые скрипты PowerShell.

**Решение:** попроси родителя или учителя, затем **один раз** выполни в PowerShell и активируй снова:

```text
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Или не используй PowerShell: в **cmd** запусти `.venv\Scripts\activate.bat`.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. На что похоже **виртуальное окружение** (`.venv`) в этом уроке?
   - **a)** Папка, где пакеты только для этого проекта
   - **b)** Особый браузер для проверки сайтов
   - **c)** Резервная копия всех твоих Python-файлов
   - **d)** Команда, которая удаляет старые пакеты

2. Когда venv **активен**, что часто видно в начале строки терминала?
   - **a)** `[Flask]`
   - **b)** `(.venv)`
   - **c)** `>>> `
   - **d)** `C:\Windows\`

3. Что делает `pip install flask` в **активированном** venv?
   - **a)** Ставит Flask только внутрь этого venv
   - **b)** Удаляет Flask с компьютера
   - **c)** Сам открывает Flask в браузере
   - **d)** Копирует Flask во все Python-проекты на ПК

4. Зачем активировать venv перед `python starter\check_setup.py`?
   - **a)** Чтобы Python нашёл Flask, установленный в venv
   - **b)** Потому что `.py` запускаются только после активации
   - **c)** Чтобы скрипт работал в два раза быстрее
   - **d)** Потому что VS Code иначе не откроет терминал

5. Что делает `deactivate`?
   - **a)** Выключает venv и возвращает обычный Python в терминале
   - **b)** Навсегда удаляет папку `.venv`
   - **c)** Удаляет Flask из интернета
   - **d)** Закрывает VS Code

---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **a)** venv — ящик инструментов проекта; пакеты отделены от других проектов.
2. **b)** `(.venv)` в приглашении значит, что окружение активно.
3. **a)** `pip install` в активном venv ставит пакеты только туда.
4. **a)** Без активации Python может не видеть пакеты из `.venv`.
5. **a)** `deactivate` выходит из venv — снова системный Python.

</details>

---

## Что дальше

→ [Урок 0.2: Как работает веб](../lesson-0-2-how-the-web-works/README.md) — что происходит, когда ты открываешь URL.

---

*Ящик готов. Дальше — как на самом деле устроен веб!*

[← Выбрать язык](README.md)
