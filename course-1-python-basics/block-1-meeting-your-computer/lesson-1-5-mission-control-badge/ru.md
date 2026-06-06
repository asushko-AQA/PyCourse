# Урок 1.5: Значок диспетчера миссии (итог Блока 1)

> **Курс:** Основы Python и командная строка · **Блок:** Знакомство с компьютером · **~45 мин**  
> [Choose language / Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Уровень 5 — Значок диспетчера миссии**

---

## Объяснение

Ты установил Python. Прошёл лабиринт папок. Освоил запуск. Чинил баги как детектив.

Теперь **всё вместе** в одной миссии — и ты получаешь **Значок диспетчера миссии**.

Итог Блока 1 — без новых тем, только доказательство, что ты умеешь:

1. Создать папку
2. Написать многострочный скрипт
3. `cd` и `dir`
4. `python badge.py`
5. Сломать код специально, прочитать ошибку и починить

Перед стартом отметь [чеклист готовности Блока 1](../../README.md#block-1-readiness-checklist).

---

### Шаг 1: Папка миссии

**Лучше всего:** в проводнике VS Code — правый клик по **корню проекта** (например `PyCourse`) → **New Folder** → **`my_mission`**.

**Или в терминале** — сначала корень проекта:

```text
cd Documents\PyCourse
```

*(Подстрой путь — как в заголовке VS Code.)*

```text
mkdir my_mission
```

**Ожидается:** папка `my_mission` **рядом** с `course-1-python-basics`, не внутри урока.

---

### Шаг 2: Каркас значка

Открой [starter/badge.py](starter/badge.py) — там `# TODO`. Замени на свои `print()`.

Создай `badge.py` **внутри** `my_mission`.

---

### Шаг 3: Напиши скрипт

**5–8** строк `print()`:

- Строка 1: заголовок — `print("=== MISSION CONTROL BADGE ===")`
- Строка 2: твоё имя
- Строка 3: навык из Блока 1
- Строка 4: любимая команда терминала
- Строка 5: победное сообщение
- Строки 6–8 (по желанию): шутка или «ASCII-арт»

Пример после работы: [solution/badge.py](solution/badge.py) — **после** своей версии.

---

### Шаг 4: Сохрани

**Ctrl+S**. Имя `badge.py`, не `.py.txt`.

---

### Шаг 5: Перейди в my_mission

Из **корня проекта**:

```text
cd my_mission
```

Если создал на рабочем столе:

```text
cd Desktop\my_mission
```

*(Путь должен совпадать с тем, где реально лежит папка.)*

```text
dir
```

**Ожидается:** в списке `badge.py`.

---

### Шаг 6: Запуск

```text
python badge.py
```

**Mac/Linux:** используй прямые слэши в путях. Список файлов — `ls` вместо `dir`.

**Ожидается:** 5–8 строк твоего текста. **Значок получен!**

---

### Шаг 7: Сломай и почини

1. Удали одну закрывающую `"` в `print()` специально.
2. Сохрани. Запусти снова.
3. Прочитай **SyntaxError**, найди строку.
4. Почини. Запусти — снова чистый вывод.

---

## Пример кода

**Каркас: [starter/badge.py](starter/badge.py)**

```python
# badge.py
# Mission Control Badge — fill in your TODO lines below!

# TODO: Print a title banner (line 1)

# TODO: Print your name (line 2)

# TODO: Print one skill you learned in Block 1 (line 3)

# TODO: Print one command you can use in the terminal (line 4)

# TODO: Print a victory message (line 5)
```

**Эталон: [solution/badge.py](solution/badge.py)**

```python
print("=== MISSION CONTROL BADGE ===")
print("Name: Alex the Creator")
print("Skill unlocked: Navigate folders with cd and dir")
print("Favorite command: python badge.py")
print("Block 1 complete — ready for variables!")
print("Why do programmers prefer dark mode? Because light attracts bugs!")
```

---

## Запуск кода

```text
mkdir my_mission
cd my_mission
```

Создай и сохрани `badge.py`, затем:

```text
dir
python badge.py
```

**Ожидается:** минимум 5 строк твоего текста.

```text
python --version
```

**Ожидается:**

```text
Python 3.12.x
```

---

## Быстрые упражнения

Отметь каждый пункт [чеклиста Блока 1](../../README.md#block-1-readiness-checklist).

Пустые пункты? Вернись к нужному уроку.

---

## Задание для практики

**Квест:** Значок диспетчера миссии

1. Папка `my_mission/`
2. `badge.py` — 5–8 своих `print()`
3. `cd my_mission`, `dir` — файл на месте
4. `python badge.py` — успех
5. Один баг специально → ошибка → исправление → снова запуск
6. Покажи вывод другу, родителю или учителю

**Бонус:**

- Скриншот терминала.
- Ещё одна шутка в `badge.py`.
- Полный [чеклист](../../README.md#block-1-readiness-checklist) — готов к Блоку 2!

---

## Уголок отладки

**Проблема:** «Раньше работало, теперь нет».

**Причины:**

1. Не нажал **Сохранить** (Ctrl+S)
2. Терминал в **старой** папке, не в `my_mission`

**Решение:**

1. Сохрани файл.
2. `cd my_mission`, `dir` — есть `badge.py`?
3. `python badge.py` снова.

---

## Что дальше

→ [Урок 2.1: Переменные](../../block-2-talking-to-python/lesson-2-1-variables/README.md) — начало Блока 2!

→ [Оглавление Блока 1](../../README.md)

---

*Значок диспетчера миссии: получен. Блок 1 завершён. Добро пожаловать в гильдию, Создатель!*

[← Выбрать язык](README.md)
