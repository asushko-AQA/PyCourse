# Урок 2.5: Flash и проверка форм

> **Курс:** Веб-приложения на Python · **Блок:** Красота и интерактив · **~35–45 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Уровень 12 — Калькулятор с дружелюбными ошибками**

---

## Объяснение

Финал Блока 2! **Калькулятор на форме** — пара к URL-калькулятору Блока 1.

Создай **`my_web_calc/`** в корне проекта.

**Путь A:**

```text
mkdir my_web_calc
```

Скопируй [starter/](starter/). **Путь B:** [STUDENT-MAP](../STUDENT-MAP.ru.md).

---

### Ключевые шаги

1. `app.secret_key = "..."` для flash
2. Читай `a` и `b` из `request.form`
3. `flash("...")` при пустых полях или нечисловом вводе
4. Покажи `total` в `calc.html`

**TODO в starter:** блок POST в `app.py`.

---

### Запуск

```text
python starter\app.py
```

**Mac/Linux:** `python starter/app.py`

`7` + `5` → `12`; пустое поле → flash-ошибка.

---

## Практическое задание

**Квест:** Скопируй в `my_web_calc/`, доделай TODO. **Эталон:** [solution/](solution/)

---

## Уголок отладки

**Проблема:** `no secret key was set` — добавь `app.secret_key`.

---

## Что дальше

→ [Чеклист Блока 2](../README.md#block-2-readiness-checklist)  
→ [Чеклист выпуска Курса 2](../../../STUDENT-MAP.ru.md#чеклист-выпуска-курса-2)  
→ [Курс 3: Разработка игр](../../../../course-3-game-dev/README.md) — дальше Pygame!
