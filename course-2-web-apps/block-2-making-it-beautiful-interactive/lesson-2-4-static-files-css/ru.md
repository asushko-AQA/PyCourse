# Урок 2.4: Статика и CSS

> **Курс:** Веб-приложения на Python · **Блок:** Красота и интерактив · **~30 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Стилизованная студия — CSS и url_for**

---

## Объяснение

HTML говорит браузеру, *что* показать. **CSS** говорит, *как* это выглядит.

Flask отдаёт CSS из папки **`static/`** рядом с `app.py`. Подключи файл через **`url_for`**:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

**Адаптивная** вёрстка подстраивается под узкий экран с помощью `@media (max-width: 480px)`.

---

### Шаг 1: Подключи таблицу стилей

В [starter/templates/base.html](starter/templates/base.html) добавь тег `<link>` внутрь `<head>`.

---

### Шаг 2: Выучи правило CSS

**Селектор** называет часть страницы, которую ты оформляешь, например `body` или `nav a`. Вид пишется в фигурных скобках, одно свойство на строку: `{ property: value; }`.

```css
nav a {
    color: #4a90d9;
}
```

`nav a` значит «каждая ссылка внутри меню». `#4a90d9` — синий цвет, которым решение красит эти ссылки.

Считай `body` центрированным контейнером. В starter шрифт уже задан. Добавь остальное в тот же блок `body`:

- `background: #f4f7fb;` — светлый серо-голубой фон страницы
- `color: #222;` — тёмный текст
- `max-width: 640px;` — страница остаётся узкой колонкой, которую удобно читать
- `margin: 0 auto;` — `auto` центрирует колонку. В решении написано `margin: 2rem auto`: центрирование то же, плюс отступ сверху и снизу
- `padding: 1rem;` и `line-height: 1.5;` — воздух у краёв и строки, которые легче читать

В решении такие селекторы и цвета — по этому списку можно закрыть каждый TODO:

| Селектор | Что написать |
|----------|----------------|
| `body` | фон `#f4f7fb`, текст `#222`, `max-width: 640px`, `margin: 2rem auto`, `padding: 1rem`, `line-height: 1.5` |
| `nav` | `border-bottom: 2px solid #4a90d9` (синяя линия под меню) |
| `nav a` | `color: #4a90d9`, `font-weight: bold`, `text-decoration: none`, `margin-right: 1rem` |
| `nav a:hover` | `text-decoration: underline`, когда указатель на ссылке |
| `h1` | `color: #2c5282` |
| `button` | фон `#4a90d9`, текст `white`, `border: none`, `padding: 0.5rem 1rem`, `border-radius: 4px`, `cursor: pointer` |
| `input[type="text"]` | `border: 1px solid #ccc`, `padding: 0.4rem`, `border-radius: 4px`, `width: 100%`, `max-width: 280px` |

`@media` может менять правила на узком экране. Решение использует `@media (max-width: 480px)`, чтобы у `body` стало `margin: 1rem` и `padding: 0.5rem`.

---

### Шаг 3: Оформи страницу

Заполни TODO в [starter/static/style.css](starter/static/style.css) правилами из шага 2:

- Цвет фона и `max-width` у `body`
- Цвета ссылок в меню
- Правило `@media` для маленьких экранов

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

Home и About оба расширяют `base.html` и делят один и тот же CSS.

---

### Шаг 5: Запусти приложение

**Путь A:**

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-4-static-files-css
python starter\app.py
```

**Путь B:** Скопируй `starter/` — см. [STUDENT-MAP](../STUDENT-MAP.ru.md).

**Mac/Linux:** `python starter/app.py`

Зайди на `/` и `/about`. Серо-голубой фон и оформленное меню значат, что CSS загрузился.

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

Стили — в [solution/static/style.css](solution/static/style.css).

---

## Запуск кода

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-4-static-files-css
python starter\app.py
```

**Mac/Linux:** `python starter/app.py`

Открой `http://127.0.0.1:5000/` и `/about`.

**Ожидаемый результат:** серо-голубой фон, оформленное меню и читаемая типографика (не «голый» HTML).

---

## Быстрые упражнения

1. **Смени цвет** — измени `background` в `body`. Обнови страницу.
2. **Инспектор** — DevTools → Network → статус `style.css` должен быть 200.
3. **Узкий экран** — сожми окно. Меняются ли отступы на 480px?

---

## Задание для практики

**Квест:** Оформи свою студию

1. Заполни TODO в `base.html`, `style.css` и `app.py`.
2. Выбери свою цветовую тему.
3. **Бонус:** оформи `<button>` и `<input>`, как в решении.

**Эталон:** [solution/](solution/)

---

## Уголок отладки

**Проблема:** Страница выглядит как голый HTML — без цветов

**Причина:** CSS не подключён или нет файла `static/style.css`.

**Исправление:** Проверь `url_for('static', filename='style.css')` в `base.html` и что файл `static/style.css` существует.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. Главная задача **CSS** в этом уроке?
   - **a)** Цвета, шрифты, вёрстка — как выглядит страница
   - **b)** Хранение маршрутов Python
   - **c)** Полная замена HTML
   - **d)** Активация виртуального окружения

2. Где должен лежать `style.css` во Flask-проекте?
   - **a)** В папке `static/` рядом с `app.py`
   - **b)** Только внутри `templates/base.html` как текст
   - **c)** В папке `.venv`
   - **d)** Только на USB-накопителе

3. Зачем в шаблоне `{{ url_for('static', filename='style.css') }}`?
   - **a)** Flask строит правильную ссылку на CSS-файл
   - **b)** Читать POST-данные формы
   - **c)** Задать `app.secret_key`
   - **d)** Описать динамический маршрут `<name>`

4. HTML говорит браузеру *что* показать. CSS говорит *что*?
   - **a)** *Как* это должно выглядеть
   - **b)** Какие пакеты pip установить
   - **c)** Какой порт открыть
   - **d)** Как запустить `python app.py`

5. Чем помогает правило `@media (max-width: 480px)`?
   - **a)** Подстраивает стили на узком экране (адаптивная вёрстка)
   - **b)** Блокирует загрузку всего CSS
   - **c)** Превращает GET-формы в POST
   - **d)** Удаляет flash-сообщения

---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **a)** CSS оформляет страницу — цвета, отступы, шрифты.
2. **a)** Flask автоматически отдаёт файлы из `static/`.
3. **a)** `url_for` генерирует правильный путь `/static/style.css`.
4. **a)** HTML = структура; CSS = внешний вид.
5. **a)** Media queries подстраивают вёрстку под маленькие экраны.

</details>

---

## Что дальше

→ [Урок 2.5: Flash и проверка](../lesson-2-5-flash-and-validation/README.md) — дружелюбные ошибки и итоговый калькулятор на форме.

---

*У страниц появился стиль. Остался один урок, чтобы закрыть Блок 2!*

[← Выбрать язык](README.md)
