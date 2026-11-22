# Урок 0.1: Виртуальные окружения и pip

> **Курс:** Веб-приложения на Python · **Блок:** Настройка окружения · **~30–45 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Уровень 0 — Изолированный веб-инструментарий**

---

## Объяснение

Добро пожаловать в **Веб-мастерскую**! В Курсе 1 ты запускал скрипты Python на компьютере. В Курсе 2 ты будешь создавать **веб-приложения** — программы, которые общаются с браузером. Сначала нужен отдельный, чистый набор инструментов для веб-проектов.

**Виртуальное окружение** (venv) — это папка (обычно `.venv`), в которой хранятся пакеты **только для одного проекта**. Представь подписанные ящики с инструментами: для игр — один, для веба — другой. Без venv команда `pip install` смешивает пакеты в глобальном Python, и версии могут конфликтовать.

**`pip`** — установщик пакетов Python. В **активированном** venv команда `pip install flask` ставит Flask **только** в ящик этого проекта.

**Комментарии:** строки с `#` — заметки для людей, Python их пропускает. В `check_setup.py` ты увидишь `# TODO` — места, где **ты** пишешь код.

### Где живёт `.venv`?

Ты создаёшь **один** `.venv` на весь курс. Он лежит в папке, которую ты открываешь в VS Code:

**Путь A — репозиторий PyCourse:** сама папка `PyCourse` — та, в которой лежат `course-1-python-basics` и `course-2-web-apps`. Твоё окружение будет `PyCourse\.venv`.

**Путь B — своя папка:** создай новую папку на рабочем столе, например `web_workshop`. Твоё окружение будет `web_workshop\.venv`. Сразу скопируй [starter/check_setup.py](starter/check_setup.py) в `web_workshop` — ты запустишь его в Шаге 6.

```text
PyCourse/                      web_workshop/
├── .venv/        ← Path A     ├── .venv/        ← Path B
├── course-1-python-basics/    └── check_setup.py
└── course-2-web-apps/
```

Никогда не создавай `.venv` внутри папки урока. Каждый урок Курса 2 начинается одинаково: открой эту папку в VS Code → активируй `.venv` → **потом** `cd` в папку урока.

**Venv нельзя переносить.** Если переименовать или переместить папку, в которой лежит `.venv`, окружение сломается. Удали старую папку `.venv` и повтори Шаги 2–4, чтобы создать новое.

---

### Шаг 1: Открой свою папку в VS Code

1. **File → Open Folder** — выбери `PyCourse` (Путь A) или `web_workshop` (Путь B).
2. **Terminal → New Terminal**. Терминал откроется в этой папке.

Проверь Python:

```text
python --version
```

Должно быть `Python 3.12` или новее.

**Mac/Linux:** если команда `python` не найдена, в Шагах 1–2 пиши `python3`. Когда venv активен, обычный `python` работает.

---

### Шаг 2: Создай `.venv`

В том же терминале (ты всё ещё в открытой папке):

```text
python -m venv .venv
```

Появится папка `.venv` — твой изолированный ящик с инструментами. Это может занять несколько секунд. Оставь имя `.venv` — следующие уроки ожидают именно его.

**Ожидаемый результат:** в списке файлов VS Code появилась папка `.venv`. Заглядывать внутрь не обязательно.

---

### Шаг 3: Активируй venv

Активация говорит терминалу использовать Python из `.venv`, а не глобальный.

**Windows PowerShell:**

```text
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt (cmd):**

```text
.venv\Scripts\activate.bat
```

**Mac/Linux:**

```text
source .venv/bin/activate
```

**Ожидаемый результат:** в начале строки приглашения появится `(.venv)` — ящик открыт.

**Красная ошибка PowerShell про запуск скриптов?** Смотри [Уголок отладки](#уголок-отладки) — или используй **cmd** и `activate.bat`.

---

### Шаг 4: Установи Flask через pip

Когда в приглашении видно `(.venv)`:

```text
pip install flask
```

**Ожидаемый вывод (последняя строка, детали могут отличаться):**

```text
Successfully installed ... flask-3.x.x ...
```

Проверь список пакетов:

```text
pip list
```

Найди строку с `Flask`.

---

### Шаг 5: Допиши check_setup.py

Открой `check_setup.py` — Путь A: [starter/check_setup.py](starter/check_setup.py); Путь B: копию в папке `web_workshop`. Тебе понадобятся два новых инструмента.

**Инструмент 1 — `try` / `except`: страховочная сетка.** Python пробует выполнить код под `try:`. Если там случилась ошибка, Python прыгает в `except` вместо того, чтобы упасть. Попробуй маленькое демо:

```python
try:
    import unicorn_magic
    print("unicorn_magic found!")
except ImportError:
    print("No unicorn_magic here — but no crash either!")
```

**Вывод:**

```text
No unicorn_magic here — but no crash either!
```

Пакета `unicorn_magic` не существует, поэтому `import` не срабатывает и выполняется блок `except ImportError:`. (Python называет эту ошибку `ModuleNotFoundError` — это разновидность `ImportError`, поэтому `except ImportError:` её ловит.)

**Инструмент 2 — узнать номер версии.** Модуль `importlib` встроен в Python. Эта строка печатает, какую версию Flask установил pip:

```python
import importlib.metadata

print(f"Flask version: {importlib.metadata.version('flask')}")
```

**Твоя задача — три строки `# TODO` в `main()`:**

1. Под `try:` напиши `import flask`.
2. Там же, под `try:`, напечатай `"venv ready"` и строку с версией Flask.
3. Под `except ImportError:` напечатай понятные шаги: активируй `.venv`, выполни `pip install flask`, запусти скрипт снова.

**Застрял?** Повтори форму демо с `unicorn_magic` и подставь `flask`.

---

### Шаг 6: Запусти проверочный скрипт

При активном `(.venv)`, из папки, которую ты открыл в Шаге 1:

**Путь A — репозиторий PyCourse:**

```text
python course-2-web-apps\block-0-environment-setup\lesson-0-1-virtual-environments\starter\check_setup.py
```

**Путь B — своя папка:**

```text
python check_setup.py
```

**Mac/Linux:** используй прямые слэши: `python course-2-web-apps/block-0-environment-setup/lesson-0-1-virtual-environments/starter/check_setup.py`

**Ожидаемый вывод:**

```text
venv ready
Flask version: 3.x.x
```

(Номер версии может отличаться — это нормально.) Видишь шаги настройки? Перечитай Шаги 3 и 4: Flask, скорее всего, не установлен в **активном** venv.

---

### Шаг 7: Деактивируй и сравни

```text
deactivate
```

`(.venv)` исчезнет из приглашения. Снова выполни команду из Шага 6 (Mac/Linux: `python3` вместо `python`). Теперь ошибку ловит страховочная сетка:

```text
Flask is not installed yet.
Steps:
  1. Activate your .venv (see lesson steps)
  2. Run: pip install flask
  3. Run this script again
```

(Если всё равно видишь `venv ready` — Flask установлен ещё и вне venv, это нормально.)

Перед тем как продолжить, снова активируй venv (Шаг 3).

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

**Путь A** — в папке `PyCourse` (Windows PowerShell):

```text
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install flask
python course-2-web-apps\block-0-environment-setup\lesson-0-1-virtual-environments\starter\check_setup.py
```

**Путь B** — в папке `web_workshop`: те же три первые команды, затем `python check_setup.py`.

**cmd:** `.venv\Scripts\activate.bat` · **Mac/Linux:** `python3 -m venv .venv`, затем `source .venv/bin/activate` и прямые слэши в путях.

**Ожидаемый вывод (venv активен, Flask установлен):**

```text
venv ready
Flask version: 3.x.x
```

---

## Быстрые упражнения

1. **Найди Flask** — с активным venv выполни `pip list` и найди `Flask`. Выполни `deactivate`, затем снова `pip list`: в глобальном списке Flask быть не должно. (Если вне venv команда `pip` вообще не найдена — это доказывает то же самое!) Снова активируй venv.
2. **Не тот ящик** — деактивируй, запусти `check_setup.py` и прочитай шаги настройки. Снова активируй, запусти ещё раз — опять `venv ready`.
3. **Два терминала, две команды** — запиши на стикер команды активации для PowerShell **и** для cmd. С одной из них начинается каждый урок Курса 2.

---

## Задание для практики

**Квест:** Табличка мастерской

1. Выполни все TODO в `check_setup.py`, чтобы вывод совпадал с эталонным решением.
2. После строки `Flask version` добавь ещё одну: `print("My web workshop is open!")`
3. Запусти скрипт дважды: с активным venv и после `deactivate`. Сравни вывод и покажи его родителю или учителю.

**Ожидаемый вывод (venv активен):**

```text
venv ready
Flask version: 3.x.x
My web workshop is open!
```

**Бонус:** в блоке `except` добавь четвёртую подсказку: `print("  4. Make sure (.venv) shows in your terminal prompt")`

**Эталонное решение:** [solution/check_setup.py](solution/check_setup.py)

---

## Уголок отладки

**Проблема:** `check_setup.py` печатает `Flask is not installed yet.`, хотя ты выполнил `pip install flask`. (Скрипт без `try`/`except` упал бы с ошибкой `ModuleNotFoundError: No module named 'flask'`.)

**Причина:** venv **не активирован**. Flask установился в другой Python, или скрипт запущен глобальным Python.

**Решение:** снова активируй venv (Шаг 3), убедись, что видно `(.venv)`, ещё раз выполни `pip install flask` и запусти скрипт.

---

**Проблема:** PowerShell пишет `Activate.ps1 cannot be loaded because running scripts is disabled on this system`.

**Причина:** настройки безопасности Windows блокируют локальные скрипты PowerShell.

**Решение:** сначала спроси родителя или учителя — эта команда меняет настройку Windows для твоей учётной записи. Затем выполни её **один раз** и снова активируй venv:

```text
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Нет разрешения? Используй **cmd** и `.venv\Scripts\activate.bat`.

---

**Проблема:** активация не срабатывает: PowerShell пишет `The term '.venv\Scripts\Activate.ps1' is not recognized`, а Mac/Linux — `.venv/bin/activate: No such file or directory`.

**Причина:** терминал находится не в той папке, где лежит `.venv` — например, ты уже сделал `cd` в папку урока.

**Решение:** закрой терминал и открой новый (**Terminal → New Terminal**) — он откроется в папке, которую ты открыл в VS Code. Сначала активируй venv там, потом делай `cd`.

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
   - **a)** Сам открывает Flask в браузере
   - **b)** Копирует Flask во все Python-проекты на ПК
   - **c)** Ставит Flask только внутрь этого venv
   - **d)** Удаляет Flask с компьютера

4. Зачем активировать venv перед запуском `check_setup.py`?
   - **a)** Потому что `.py` запускаются только после активации
   - **b)** Чтобы скрипт работал в два раза быстрее
   - **c)** Потому что VS Code иначе не откроет терминал
   - **d)** Чтобы Python нашёл Flask, установленный в venv

5. Что делает `deactivate`?
   - **a)** Выключает venv и возвращает обычный Python в терминале
   - **b)** Навсегда удаляет папку `.venv`
   - **c)** Удаляет Flask из интернета
   - **d)** Закрывает VS Code

---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **a)** venv — ящик инструментов проекта; пакеты отделены от других проектов.
2. **b)** `(.venv)` в приглашении значит, что окружение активно.
3. **c)** `pip install` в активном venv ставит пакеты только туда.
4. **d)** Без активации Python может не видеть пакеты из `.venv`.
5. **a)** `deactivate` выходит из venv — снова системный Python.

</details>

---

## Что дальше

→ [Урок 0.2: Как работает веб](../lesson-0-2-how-the-web-works/README.md) — браузер, сервер и URL в одной картине.

---

*Изолированный ящик готов. Дальше — экскурсия по тому, как устроен веб!*

[← Выбрать язык](README.md)
