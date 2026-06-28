# Lesson 4.3: Dictionaries

> **Course:** Python Basics & Command Line Magic  
> **Block:** Organizing Code  
> **Time:** ~30–45 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level 17 — Character Stat Sheet |
| **[Русский →](ru.md)** | Уровень 17 — Лист статов персонажа |

---

## What you'll build / Что ты создашь

**EN:** A `character_stats.py` script that stores `name`, `level`, and `hp` in a dictionary and uses `.get()` for safe lookups when a key might be missing.

**RU:** Скрипт `character_stats.py`, который хранит `name`, `level` и `hp` в словаре и использует `.get()` для безопасного поиска, когда ключа может не быть.

## What you'll learn / Что ты узнаешь

- What a dictionary is (labeled boxes with name tags, not numbered slots)
- Creating a dict with `{ "key": value }`
- Reading values with `dict["key"]`
- Safe lookup with `.get(key, default)`
- KeyError when you typo a key

## Before you start / Перед стартом

- [ ] Completed [Lesson 4.2](../lesson-4-2-lists/README.md)
- [ ] You remember strings vs integers from Block 2

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/character_stats.py](starter/character_stats.py) | Skeleton with TODO comments |
| [solution/character_stats.py](solution/character_stats.py) | Reference solution |
| [exercises/phonebook_lookup.md](exercises/phonebook_lookup.md) | Stretch challenge |

## Quick drills / Быстрые упражнения

1. Add `"mp": 10` to the dict and print it with an f-string.
2. Try `character["magc"]` on purpose — read the KeyError, then fix the typo.
3. Use `.get("mp", 0)` before adding `"mp"` — what prints?

---

**Previous / Предыдущий урок:** [Lesson 4.2 — Lists](../lesson-4-2-lists/README.md)

**Next lesson / Следующий урок:** [Lesson 4.4 — Text Adventure Capstone](../lesson-4-4-text-adventure-capstone/README.md)
