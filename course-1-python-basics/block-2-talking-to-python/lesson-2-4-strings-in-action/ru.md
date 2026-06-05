# Урок 2.4: Строки в действии

> **Курс:** Основы Python и командная строка · **Блок:** Разговор с Python · **~30–45 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Уровень 9 — Фабрика историй**

---

## Объяснение

Добро пожаловать в **Фабрику историй**! Строки — не просто коробки, а глина, которую можно лепить. Три инструмента:

| Инструмент | Что делает | Пример |
|------------|------------|--------|
| `.upper()` | ВСЕ ЗАГЛАВНЫЕ | `"hi".upper()` → `HI` |
| `.lower()` | все строчные | `"HI".lower()` → `hi` |
| `[0:3]` | срез первых 3 букв | `"Alex"[0:3]` → `Ale` |

Это урок с **новым скриптом** — `madlibs.py`. Это не продолжение `greeting.py` из Урока 2.2.

---

### Шаг 1: Собери слова через input()

Спроси героя, смешное существо, место и суперсилу — четыре коробки для боевой истории.

---

### Шаг 2: Преобразуй в истории

```python
short_creature = creature[0:3]

print(f"{hero} battled a {creature.lower()} in {place}.")
print(f"The creature's first three letters: {short_creature}")
print(f"{hero} used {power.upper()} to win!")
```

- `.lower()` для имени существа — смешно, но читаемо.
- `.upper()` для суперсилы — финальный удар звучит эпично.
- `[0:3]` — первые три буквы существа для быстрого превью.

---

### Шаг 3: Запусти madlibs.py

**Путь A:**

```text
cd course-1-python-basics\block-2-talking-to-python\lesson-2-4-strings-in-action
python starter\madlibs.py
```

**Путь B:** Скопируй `madlibs.py` в любую свою папку, `cd` туда, затем `python madlibs.py`. См. [STUDENT-MAP](../../STUDENT-MAP.ru.md).

**Mac/Linux:** `python starter/madlibs.py` (прямые слэши).

**Пример ввода:** Sam, dragon, castle, laser

**Ожидаемый вывод (история зависит от слов):**

```text
=== STORY FACTORY ===
Sam battled a dragon in castle.
The creature's first three letters: dra
Sam used LASER to win!
The end.
```

---

## Пример кода

См. [starter/madlibs.py](starter/madlibs.py) — четыре ввода, `.upper()`, `.lower()` и один срез.

---

## Быстрые упражнения

1. **Прогноз upper** — что даст `"minecraft".upper()`? Проверь в Python.
2. **Срез** — заполни [exercises/slice_challenge.ru.md](exercises/slice_challenge.ru.md).
3. **Повтор** — сыграй в madlibs три раза с разными темами.

---

## Практическое задание

**Название квеста:** Твой шаблон истории

1. Заполни все TODO в [starter/madlibs.py](starter/madlibs.py).
2. Запусти со своими смешными словами.
3. **Бонус:** Напиши **новый** шаблон из 3 предложений в копии файла — `.upper()` на одном слове и срез на другом.

**Эталонное решение:** [solution/madlibs.py](solution/madlibs.py)

---

## Уголок отладки

**Проблема:** `IndexError: string index out of range` на `creature[5]` (один индекс, не срез)

**Причина:** Запрошена позиция буквы, которой нет. У трёхбуквенного слова индексы только 0, 1, 2.

**Исправление:** Используй срез `[0:3]` — он безопасно останавливается в конце.

---

## Что дальше

→ [Урок 2.5: Пакет данных создателя](../lesson-2-5-creator-data-pack/README.md) — собери все навыки Блока 2 в итоговый квест.

---

*Фабрика историй открыта. Остался один квест до конца Блока 2!*

[← Выбрать язык](README.md)
