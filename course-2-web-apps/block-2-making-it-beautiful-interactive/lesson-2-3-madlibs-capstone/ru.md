# Урок 2.3: Mad-Libs (итог)

> **Курс:** Веб-приложения на Python · **Блок:** Красота и интерактив · **~35–45 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Уровень 11 — Веб-фабрика историй**

---

## Объяснение

Первый **веб-итог**! Mad-Libs в браузере — как `madlibs.py` из Курса 1.

Создай **`my_web_madlibs/`** в корне проекта.

**Путь A:**

```text
cd Documents\PyCourse
mkdir my_web_madlibs
```

Скопируй [starter/](starter/) в `my_web_madlibs/`.

**Путь B:** На Рабочем столе — см. [STUDENT-MAP](../STUDENT-MAP.ru.md).

---

### Шаг 1–2: Форма и история

`madlibs.html` — форма и блок `{% if story %}`. В POST читай `noun`, `verb`, `adjective`, `place` и собери f-строку.

**TODO в starter:** поля в HTML и логика в `app.py`.

---

### Шаг 3: Запуск

```text
python starter\app.py
```

**Mac/Linux:** `python starter/app.py`

---

## Практическое задание

**Квест:** Скопируй в `my_web_madlibs/`, доделай TODO, свой шаблон истории. **Эталон:** [solution/](solution/)

---

## Уголок отладки

**Проблема:** История пустая — переменная `story` не задана в блоке POST.

---

## Что дальше

→ [Урок 2.4: CSS и статика](../lesson-2-4-static-files-css/README.md)
