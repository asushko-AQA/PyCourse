# Урок 3.2: if, elif, else

> **Курс:** Python Basics · **Блок:** Выбор и повторение · **~30–45 мин**  
> [Выбор языка](README.md) · [English →](en.md)

---

## Заголовок

**Уровень 12 — Развилка на квестовой тропе**

---

## Объяснение

В уроке 3.1 ты **печатал** True или False. Теперь ты **действуешь** по этим результатам с помощью **`if`** — это развилка на квестовой тропе.

| Ключевое слово | Когда выполняется |
|----------------|-------------------|
| `if` | Первая проверка — если True, выполняется этот блок |
| `elif` | «Иначе если» — пробуем следующую проверку |
| `else` | Запасной вариант, если ничего выше не подошло |

**Правила, на которых спотыкаются все:**

1. Ставь **двоеточие** `:` в конце каждой строки `if`, `elif` и `else`
2. Делай **отступ** у кода внутри каждой ветки (4 пробела)

```python
if choice == "left":
    print("Crystal found!")
elif choice == "right":
    print("Robot guide!")
else:
    print("Snack break!")
```

Выполняется **только одна** ветка — побеждает первая подходящая.

---

### Шаг 1: Открой choose_path.py

Открой [starter/choose_path.py](starter/choose_path.py). Строка с `input()` уже готова. Трёх веток не хватает — они отмечены `# TODO 1`, `# TODO 2` и `# TODO 3`.

---

### Шаг 2: Перейди в папку урока

**Путь A — репозиторий PyCourse:**

```text
cd course-1-python-basics\block-3-making-choices\lesson-3-2-if-elif-else
```

**Путь B:** Скопируй `choose_path.py` куда угодно. Перед запуском выполни `cd` в эту папку.

---

### Шаг 3: Запусти стартер как есть

```text
python starter\choose_path.py
```

**Mac/Linux:** используй прямые слэши — `python starter/choose_path.py`. Список файлов — `ls` вместо `dir`.

**Введи:** `left`

Веток пока нет, поэтому печатается только строка-напоминание:

```text
=== CHOOSE YOUR PATH ===
You stand at a fork in the quest trail.
Go left or right? (left/right): left
(No branches yet — write your if / elif / else above this line!)
Thanks for choosing!
```

---

### Шаг 4: Напиши три ветки

Под комментариями TODO напиши `if`, `elif` и `else` — той же формы, что пример в объяснении, с сообщениями из TODO:

- `if choice == "left":` → сообщение про кристалл
- `elif choice == "right":` → сообщение про робота-проводника
- `else:` → сообщение про перекус

Каждая из этих строк заканчивается двоеточием `:`, а каждый `print()` внутри ветки начинается с 4 пробелов. Потом **удали** строку-напоминание `print("(No branches yet ...")`.

---

### Шаг 5: Запусти и выбери путь

Запусти ту же команду, что в шаге 3.

**Введи:** `left`

**Ожидаемый вывод:**

```text
=== CHOOSE YOUR PATH ===
You stand at a fork in the quest trail.
Go left or right? (left/right): left
You find a glowing crystal! +10 quest points.
Thanks for choosing!
```

**Введи:** `right` — строка про робота-проводника. **Введи:** что угодно другое — строка про перекус.

---

## Пример кода

Готовая история — эталон [solution/choose_path.py](solution/choose_path.py):

```python
# choose_path.py — reference solution

print("=== CHOOSE YOUR PATH ===")
print("You stand at a fork in the quest trail.")

choice = input("Go left or right? (left/right): ")

if choice == "left":
    print("You find a glowing crystal! +10 quest points.")
elif choice == "right":
    print("You meet a friendly robot guide. It waves hello.")
else:
    print("You sit down for a snack. Adventure can wait!")

print("Thanks for choosing!")
```

**Осторожно:** `==` сравнивает текст **точно**, буква за буквой — `"Left" == "left"` даёт `False`. В быстром упражнении 3 ты увидишь это сам и исправишь.

---

## Запуск кода

```text
cd course-1-python-basics\block-3-making-choices\lesson-3-2-if-elif-else
python starter\choose_path.py
```

Попробуй ввести `left`, `right` и `snack`. С `right` ты увидишь:

```text
=== CHOOSE YOUR PATH ===
You stand at a fork in the quest trail.
Go left or right? (left/right): right
You meet a friendly robot guide. It waves hello.
Thanks for choosing!
```

С `snack` перед `Thanks for choosing!` появится `You sit down for a snack. Adventure can wait!`.

---

## Быстрые упражнения

1. **Угадай** — до запуска запиши, что напечатается для `left` и для `pizza`.
2. **Третий путь** — добавь `elif choice == "straight":` с новым сообщением между `right` и `else`.
3. **Проверка регистра** — введи `Left` (с большой L). Какая ветка сработает? Ты получишь строку про перекус, потому что для Python `"Left"` и `"left"` — разный текст. **Исправь:** добавь `.lower()` (из урока 2.4) в конец строки с вводом — `choice = input("Go left or right? (left/right): ").lower()`. Запусти снова и введи `Left` — теперь ты находишь кристалл!

---

## Задание для практики

**Название квеста:** Расширь тропу

1. Допиши TODO 1–3 в `starter/choose_path.py` — вывод должен совпасть с шагом 5 для `left` и с разделом «Запуск кода» для `right`.
2. Добавь приветственную строку перед `input()`.
3. Добавь третью ветку с `elif` (например, `"straight"` → сцена с мостом).
4. Измени сообщение о кристалле: используй f-строку со словом `"crystal"`.

**Эталон:** [solution/choose_path.py](solution/choose_path.py)

---

## Уголок отладки

**Проблема:** `SyntaxError: invalid syntax` на строке с `if`.

**Причина:** Ты забыл **двоеточие** в конце: `if choice == "left"` нужно `:` → `if choice == "left":`

**Исправление:** Добавь `:` после каждого `if`, `elif` и `else`. Сохрани и запусти снова.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. Сколько веток `if` / `elif` / `else` выполняется за один запуск?
   - **a)** Только **одна** — срабатывает первая подходящая
   - **b)** Все каждый раз
   - **c)** Ровно две
   - **d)** Ни одна — они только печатают True/False

2. Что должно быть в конце строки `if choice == "left"`?
   - **a)** Ничего лишнего
   - **b)** Двоеточие `:`
   - **c)** Точка с запятой `;`
   - **d)** Знак равенства `=`

3. Когда выполняется ветка `else`?
   - **a)** Только когда пользователь вводит `left`
   - **b)** Никогда — это просто украшение
   - **c)** Когда ни одно условие `if` или `elif` не подошло
   - **d)** Всегда, до любого `if`

4. Что означает `elif`?
   - **a)** «Конец цикла если» — остановка while
   - **b)** «Равно если» — присваивание
   - **c)** «Каждая строка если» — выполнить все ветки
   - **d)** «Иначе если» — следующая проверка, если первая была False

5. Код внутри ветки `if` должен быть…
   - **a)** С отступом (4 пробела) под строкой `if`
   - **b)** На той же строке, что и `if`
   - **c)** ВСЕ ЗАГЛАВНЫМИ
   - **d)** В кавычках

---

<details><summary>Нажми, чтобы показать ответы</summary>

1. **a)** Выполняется только первая подходящая ветка.
2. **b)** После каждого `if`, `elif` и `else` нужно двоеточие.
3. **c)** `else` — запасной вариант, если ничего выше не подошло.
4. **d)** `elif` проверяет следующее условие.
5. **a)** Код ветки с отступом (4 пробела в примерах).

</details>

---

## Что дальше

→ [Урок 3.3: циклы for и while](../lesson-3-3-for-and-while-loops/README.md) — повторяй действия с обратным отсчётом и таблицами!

---

[← Выбор языка](README.md)
