# Урок 2.4: Статика и CSS

> **Курс:** Веб-приложения на Python · **Блок:** Красота и интерактив · **~30 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Стилизованная студия — CSS и url_for**

---

## Объяснение

HTML говорит браузеру, *что* показать. **CSS** говорит, *как* это выглядит.

Flask отдаёт CSS из папки **`static/`** рядом с `app.py`. Подключи его через **`url_for`**:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

**Адаптивная** вёрстка подстраивается под узкий экран с помощью `@media (max-width: 480px)`.

---

### Шаг 1: Подключи таблицу стилей

В [starter/templates/base.html](starter/templates/base.html) добавь тег `<link>` внутрь `<head>`.

---

### Шаг 2: Как записывается правило CSS

CSS — это список правил. У каждого одна и та же форма: **селектор**, фигурные скобки и строки `свойство: значение;`:

```css
selector {
    property: value;
}
```

Селектор называет HTML, который ты меняешь. `body` — вся страница. `nav` — меню. `nav a` — ссылка внутри меню. `nav a:hover` — та же ссылка, когда на неё наведена мышь. `h1` — большой заголовок. `button` и `input[type="text"]` — кнопка и текстовое поле (их ты стилизуешь в бонусе).

Вот правило страницы и цвета этого урока. `#f4f7fb` — мягкий серо-голубой фон, `#222` — тёмный текст. `max-width` вместе с `margin: 2rem auto` держит текст в колонке по центру:

```css
body {
    background: #f4f7fb;
    color: #222;
    max-width: 640px;
    margin: 2rem auto;
}
```

Каждому другому селектору — свой блок `{ }`, и после каждого свойства ставь `;`:

- `nav` — `border-bottom: 2px solid #4a90d9;` (синяя линия под меню)
- `nav a` — `color: #4a90d9;` (тот же синий) и `font-weight: bold;`
- `h1` — `color: #2c5282;` (более глубокий синий)

`@media (max-width: 480px)` — правило только для узкого экрана, как у телефона. Внутри поставь `body` `margin: 1rem;` и `padding: 0.5rem;`, чтобы текст всё ещё помещался.

**Цвета для бонуса:** у `button` — `background: #4a90d9;` и `color: white;`. У `input[type="text"]` — `border: 1px solid #ccc;`.

---

### Шаг 3: Оформи страницу

Допиши `# TODO` в [starter/static/style.css](starter/static/style.css) правилами из шага 2. Стартер остаётся твоим файлом — в [solution/static/style.css](solution/static/style.css) загляни только после своей попытки.

- Цвет фона и `max-width` у `body`
- Цвета ссылок меню (`nav` и `nav a`)
- Правило `@media` для маленького экрана

---

### Шаг 4: Добавь маршрут About

```python
@app.route("/about")
def about():
    return render_template(
        "about.html",
        page_title="About",
        tagline="CSS makes plain HTML look like a real website.",
    )
```

Home и About оба наследуют `base.html` и делят один CSS.

---

### Шаг 5: Запусти приложение

**1. Активируй venv.** Терминал VS Code стартует в корне проекта (там лежит `.venv`). Активируй:

```text
.venv\Scripts\Activate.ps1
```

**Командная строка (cmd):** `.venv\Scripts\activate.bat` · **macOS/Linux:** `source .venv/bin/activate`

В начале строки терминала должно появиться `(.venv)`.

**2. Зайди в папку урока и запусти:**

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-4-static-files-css
python starter\app.py
```

**macOS/Linux:**

```text
cd course-2-web-apps/block-2-making-it-beautiful-interactive/lesson-2-4-static-files-css
python starter/app.py
```

**Путь B:** скопируй `starter/` в свою папку-мастерскую (рядом с `.venv`) и запусти `python app.py` из копии. См. [STUDENT-MAP](../STUDENT-MAP.ru.md).

Зайди на `/` и `/about`. Серо-голубой фон (`#f4f7fb`) и синее меню значат, что CSS загрузился.

---

## Пример кода

**Файл: [solution/templates/base.html](solution/templates/base.html)** (ссылка на CSS)

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

**Файл: [solution/app.py](solution/app.py)**

```python
@app.route("/")
def home():
    return render_template(
        "home.html",
        page_title="Home",
        headline="Welcome to My Styled Studio",
    )
```

Стили лежат в [solution/static/style.css](solution/static/style.css).

---

## Запуск кода

С активным `(.venv)`, из корня проекта:

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-4-static-files-css
python starter\app.py
```

**macOS/Linux:**

```text
cd course-2-web-apps/block-2-making-it-beautiful-interactive/lesson-2-4-static-files-css
python starter/app.py
```

Открой `http://127.0.0.1:5000/` и `/about`.

**Ожидаемый результат:** серо-голубой фон, оформленное меню и читаемая типографика (не «голый» HTML).

---

## Быстрые упражнения

1. **Смени цвет** — измени `background` у `body`. Обнови страницу.
2. **Инспектор** — DevTools → Network → статус `style.css` должен быть 200.
3. **Узкий экран** — сожми окно. Меняются ли отступы на 480px?

---

## Задание для практики

**Квест:** Своя цветовая тема

1. Допиши TODO в `base.html`, `style.css` и `app.py`.
2. Выбери свою палитру.
3. **Бонус:** оформи `<button>` и `<input>`, как в решении.

**Эталон:** [solution/](solution/)

---

## Уголок отладки

**Проблема:** Страница выглядит как голый HTML — нет цветов.

**Причина:** CSS не подключён или нет файла `static/style.css`.

**Исправление:** Проверь `url_for('static', filename='style.css')` в `base.html` и что файл `static/style.css` существует.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. Главная задача **CSS** в этом уроке?
   - **a)** Активация виртуального окружения
   - **b)** Цвета, шрифты, вёрстка — как выглядит страница
   - **c)** Хранение маршрутов Python
   - **d)** Полная замена HTML

2. Где должен лежать `style.css` во Flask-проекте?
   - **a)** В папке `.venv`
   - **b)** Только на USB-накопителе
   - **c)** В папке `static/` рядом с `app.py`
   - **d)** Только внутри `templates/base.html` как текст

3. Зачем в шаблоне `{{ url_for('static', filename='style.css') }}`?
   - **a)** Читать POST-данные формы
   - **b)** Задать `app.secret_key`
   - **c)** Описать динамический маршрут `<name>`
   - **d)** Flask строит правильную ссылку на CSS-файл

4. HTML говорит браузеру *что* показать. CSS говорит *что*?
   - **a)** *Как* это должно выглядеть
   - **b)** Какие пакеты pip установить
   - **c)** Какой порт открыть
   - **d)** Как запустить `python app.py`

5. Чем помогает правило `@media (max-width: 480px)`?
   - **a)** Удаляет flash-сообщения
   - **b)** Подстраивает стили на узком экране (адаптивная вёрстка)
   - **c)** Блокирует загрузку всего CSS
   - **d)** Превращает GET-формы в POST

---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **b)** CSS оформляет страницу — цвета, отступы, шрифты.
2. **c)** Flask автоматически отдаёт файлы из `static/`.
3. **d)** `url_for` генерирует правильный путь `/static/style.css`.
4. **a)** HTML = структура; CSS = внешний вид.
5. **b)** Media queries подстраивают вёрстку под маленькие экраны.

</details>

---

## Что дальше

→ [Урок 2.5: Flash и проверка](../lesson-2-5-flash-and-validation/README.md) — понятные ошибки и итоговый калькулятор на форме.

---

*У твоих страниц появился стиль. Ещё один урок — и Блок 2 готов!*
