# Урок 0.1: Виртуальные окружения и pip

> **Курс:** Веб-приложения на Python · **Блок:** Настройка окружения · **~30–45 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Уровень 0 — Изолированный веб-инструментарий**

---

## Объяснение

Добро пожаловать в **Веб-мастерскую**! В Курсе 1 ты запускал скрипты Python на компьютере. В Курсе 2 ты будешь создавать **веб-приложения** — программы, которые общаются с браузером. Сначала нужен отдельный, чистый набор инструментов для веб-проекта.

**Виртуальное окружение** (venv) — это папка (обычно `.venv`), в которой хранятся пакеты **только для одного проекта**. Представь подписанный ящик с инструментами: для игры — один набор, для веба — другой. Без venv команда `pip install` может смешивать пакеты в глобальный Python и вызывать конфликты версий.

**`pip`** — установщик пакетов Python. В активированном venv команда `pip install flask` ставит Flask **только** в ящик этого проекта.

**Комментарии:** строки с `#` — заметки для людей, Python их пропускает. В [starter/check_setup.py](starter/check_setup.py) ты увидишь `# TODO` — места, где **ты** дописываешь код.

**Путь A — репозиторий PyCourse:**

```text
cd course-2-web-apps\block-0-environment-setup\lesson-0-1-virtual-environments
```

**Путь B — своя папка:** создай пустую папку (например `my-web-workshop`), открой её в VS Code и выполняй те же команды.

---

### Шаг 1: Открой папку урока в VS Code

Открой папку урока в VS Code. Открой встроенный терминал: **Terminal → New Terminal**.

Проверь Python:

```text
python --version
```

Должно быть `Python 3.12` или новее.

---

### Шаг 2: Создай виртуальное окружение

Из папки урока выполни:

```text
python -m venv .venv
```

Появится папка `.venv` — твой изолированный ящик с инструментами. Это может занять несколько секунд.

**Ожидаемый результат:** в списке файлов появилась папка `.venv`. Заглядывать внутрь не обязательно.

---

### Шаг 3: Активируй venv

Активация говорит терминалу использовать Python из `.venv`, а не глобальный.

**Windows PowerShell:**

```text
.venv\Scripts\Activate.ps1
```

Если красная ошибка про запрет скриптов, выполни **один раз** (потом снова активируй):

```text
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Windows Command Prompt (cmd):**

```text
.venv\Scripts\activate.bat
```

**Mac / Linux:**

```text
source .venv/bin/activate
```

**Ожидаемый результат:** в начале строки приглашения появится `(.venv)` — ящик активен.

Чтобы **деактивировать** (для тренировки):

```text
deactivate
```

---

### Шаг 4: Установи Flask через pip

Когда в приглашении видно `(.venv)`:

```text
pip install flask
```

**Ожидаемый вывод (последние строки могут отличаться):**

```text
Successfully installed Flask-3.x.x ...
```

Проверь список пакетов:

```text
pip list
```

Найди строку с `Flask`.

---

### Шаг 5: Допиши check_setup.py

Открой [starter/check_setup.py](starter/check_setup.py). Выполни три пункта `# TODO`:

1. Импортируй `flask` внутри блока `try`
2. Если импорт успешен — напечатай `"venv ready"`
3. При `ImportError` — напечатай понятные шаги по настройке

**Подсказка — структура:**

```python
import importlib.metadata

def main():
    try:
        import flask
        print("venv ready")
        print(f"Flask version: {importlib.metadata.version('flask')}")
    except ImportError:
        print("Flask is not installed yet.")
        # напечатай шаги по порядку
```

---

### Шаг 6: Запусти проверочный скрипт

При активном venv:

```text
python starter\check_setup.py
```

**Mac/Linux:** `python starter/check_setup.py`

**Ожидаемый вывод:**

```text
venv ready
Flask version: 3.x.x
```

Если видишь шаги настройки — перечитай Шаг 3 и Шаг 4: Flask, скорее всего, не установлен в **активном** venv.

---

## Пример кода

**Файл: [solution/check_setup.py](solution/check_setup.py)** (после выполнения TODO)

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

```text
cd course-2-web-apps\block-0-environment-setup\lesson-0-1-virtual-environments
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install flask
python starter\check_setup.py
```

**Mac/Linux:** `source .venv/bin/activate` и прямые слэши в путях.

---

## Быстрые упражнения

1. **Найди venv** — с активным venv выполни `pip list`. Деактивируй и снова `pip list`. Flask не должен быть в глобальном списке.
2. **Не тот ящик** — деактивируй, запусти `python starter\check_setup.py`. Увидишь подсказку? Снова активируй и запусти.
3. **Имя папки** — оставь `.venv`; следующие уроки ожидают это имя.

---

## Практическое задание

**Квест:** Инспектор мастерской

1. Выполни все TODO в [starter/check_setup.py](starter/check_setup.py), чтобы поведение совпадало с решением.
2. Добавь строку `print("Toolbox active!")` при успешном импорте Flask.
3. Запусти скрипт дважды: с активным venv и после `deactivate`. Сравни вывод.

**Бонус:** в блоке `except` добавь четвёртую подсказку: `print("  4. Make sure (.venv) shows in your terminal prompt")`.

**Эталонное решение:** [solution/check_setup.py](solution/check_setup.py)

---

## Разбор ошибок

**Проблема:** `ImportError: No module named 'flask'` даже после `pip install flask`.

**Причина:** venv, скорее всего, **не активирован**. Flask установился в другое место, или скрипт запущен глобальным Python.

**Решение:** снова активируй (Шаг 3), убедись что видно `(.venv)`, выполни `pip install flask` ещё раз, затем `python starter\check_setup.py`.

---

**Проблема:** PowerShell пишет, что `Activate.ps1` нельзя загрузить — скрипты отключены.

**Причина:** в некоторых настройках Windows локальные скрипты заблокированы.

**Решение:** `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`, затем снова активация.

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

→ [Урок 0.2: Как работает веб](../lesson-0-2-how-the-web-works/README.md) — браузер, сервер и URL в одной картине.

---

*Изолированный ящик готов. Дальше — экскурсия по тому, как устроен веб!*

[← Выбрать язык](README.md)
