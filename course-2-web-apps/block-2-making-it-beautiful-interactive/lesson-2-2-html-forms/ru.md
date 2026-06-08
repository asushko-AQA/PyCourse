# Урок 2.2: HTML-формы (GET/POST)

> **Курс:** Веб-приложения на Python · **Блок:** Красота и интерактив · **~30 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Form Lab — GET и POST**

---

## Объяснение

| Метод | Где данные | Flask |
|-------|------------|-------|
| GET | В URL (`?name=Alex`) | `request.args.get("name")` |
| POST | В теле запроса | `request.form.get("text")` |

Два мини-приложения: **`/greet`** (GET) и **`/message`** (POST-эхо).

---

### Шаг 1: GET-приветствие

```python
@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "").strip()
    ...
```

Форма: `<form method="get" action="/greet">` с `<input name="name">`.

---

### Шаг 2: POST-эхо

```python
@app.route("/message", methods=["GET", "POST"])
def message():
    if request.method == "POST":
        text = request.form.get("text", "").strip()
```

**TODO в starter:** оба маршрута и формы в шаблонах.

---

### Шаг 3: Запуск

**Путь A:**

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-2-html-forms
python starter\app.py
```

**Путь B:** Скопируй `starter/` — [STUDENT-MAP](../STUDENT-MAP.ru.md).

**Mac/Linux:** `python starter/app.py`

GET меняет URL; POST — нет.

---

## Практическое задание

**Квест:** Доделай Form Lab. **Эталон:** [solution/](solution/)

---

## Уголок отладки

**Проблема:** `Method Not Allowed` — неверный `methods=[...]` у маршрута.

---

## Что дальше

→ [Урок 2.3: Mad-Libs](../lesson-2-3-madlibs-capstone/README.md)
