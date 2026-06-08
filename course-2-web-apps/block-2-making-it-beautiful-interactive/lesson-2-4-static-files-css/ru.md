# Урок 2.4: Статика и CSS

> **Курс:** Веб-приложения на Python · **Блок:** Красота и интерактив · **~30 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Стилизованная студия — CSS и url_for**

---

## Объяснение

CSS в папке **`static/`**. Подключение:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

`@media (max-width: 480px)` — адаптивность для узких экранов.

**TODO в starter:** `<link>` в `base.html`, стили в `style.css`, маршрут `/about`.

---

### Запуск

**Путь A:**

```text
cd course-2-web-apps\block-2-making-it-beautiful-interactive\lesson-2-4-static-files-css
python starter\app.py
```

**Путь B:** [STUDENT-MAP](../STUDENT-MAP.ru.md).

**Mac/Linux:** `python starter/app.py`

---

## Практическое задание

**Квест:** Своя цветовая тема. **Эталон:** [solution/](solution/)

---

## Уголок отладки

**Проблема:** Нет стилей — проверь `url_for` и наличие `static/style.css`.

---

## Что дальше

→ [Урок 2.5: Flash и проверка](../lesson-2-5-flash-and-validation/README.md)
