# Урок 4.3: Словари

> **Курс:** Основы Python и командная строка · **Блок:** Организация кода · **~30–45 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Уровень 17 — Лист статов персонажа**

---

## Объяснение

Списки используют **номера слотов** (0, 1, 2…). **Словарь** использует **именные метки** — у каждого значения есть **ключ**, который ты выбираешь:

```python
character = {
    "name": "Alex",
    "level": 5,
    "hp": 42,
}
```

Это как лист персонажа с подписанными коробками: `"name"`, `"level"`, `"hp"`.

Читай значение через квадратные скобки:

```python
print(character["hp"])
```

**Путь A — репозиторий PyCourse:**

```text
cd course-1-python-basics\block-4-organizing-code\lesson-4-3-dictionaries
```

**Путь B — своя папка:** Скопируй [starter/character_stats.py](starter/character_stats.py) куда угодно. Запускай из этой папки.

---

### Шаг 1: Открой character_stats.py

Открой [starter/character_stats.py](starter/character_stats.py). Три стата уже заполнены.

---

### Шаг 2: Напечатай известные ключи

Скрипт использует `character["name"]`, `character["level"]` и `character["hp"]`. Измени значения и запусти снова.

---

### Шаг 3: Безопасный поиск через .get()

Что если `"magic"` ещё нет на листе? Скобки `[]` вызовут `KeyError`. **`.get()`** возвращает значение по умолчанию:

```python
magic = character.get("magic", 0)
print(f"Magic: {magic}")
```

Если `"magic"` нет — получишь `0` без падения.

---

### Шаг 4: Запусти скрипт

```text
python starter\character_stats.py
```

**Mac/Linux:** используй прямые слэши — `python starter/character_stats.py`. Список файлов — `ls` вместо `dir`.

**Ожидаемый вывод:**

```text
=== CHARACTER STATS ===
Name: Alex
Level: 5
HP: 42
Magic: 0
Special skill: none
Edit the dict keys above, then run again!
```

---

## Пример кода

**Файл: [starter/character_stats.py](starter/character_stats.py)**

```python
character = {
    "name": "Alex",
    "level": 5,
    "hp": 42,
}

print("=== CHARACTER STATS ===")
print(f"Name: {character['name']}")
print(f"Level: {character['level']}")
print(f"HP: {character['hp']}")

magic = character.get("magic", 0)
print(f"Magic: {magic}")

skill = character.get("skill", "none")
print(f"Special skill: {skill}")
```

---

## Запуск кода

```text
cd course-1-python-basics\block-4-organizing-code\lesson-4-3-dictionaries
python starter\character_stats.py
```

Ввод с клавиатуры не нужен — вывод появится сразу.

---

## Быстрые упражнения

1. **Добавь MP** — впиши `"mp": 10` в словарь и напечатай `f"MP: {character['mp']}"`.
2. **Ловушка опечатки** — замени `"hp"` на `"hpp"` в одной строке print. Запусти. Прочитай `KeyError`. Исправь.
3. **Сила по умолчанию** — добавь `"power": 7` и выведи через `.get("power", 1)`.

---

## Практическое задание

**Название квеста:** Лист твоего героя

1. Замени все три стата на своего героя (реального или вымышленного).
2. Добавь два новых ключа — `"class"` и `"gold"`.
3. Используй `.get()` для `"pet"` со значением `"none"`, даже если ключа `"pet"` нет.

**Бонусный квест:** См. [exercises/phonebook_lookup.ru.md](exercises/phonebook_lookup.ru.md) — мини-телефонная книга.

**Эталонное решение:** [solution/character_stats.py](solution/character_stats.py)

---

## Отладка

**Проблема:** `KeyError: 'magc'` при записи `character["magc"]`.

**Причина:** Ключи словаря должны совпадать **точно** — важна каждая буква. Ты запросил `"magc"`, а есть только `"magic"` (или ключа вообще нет).

**Исправление:** Проверь имя ключа в `{ }`. Используй `.get("magic", 0)`, когда ключа может не быть.

---

## Что дальше

→ [Урок 4.4: Текстовое приключение (итог)](../lesson-4-4-text-adventure-capstone/README.md) — объедини функции, списки и словари в одной игре.

---

*Лист статов с подписанными коробками готов. Дальше — приключение по комнатам!*

[← Выбрать язык](README.md)
