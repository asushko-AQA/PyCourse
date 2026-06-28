# Урок 5.3: Функции и Turtle

> **Курс:** Основы Python и командная строка · **Блок:** Творческий Python с Turtle · **~30–45 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

---

## Заголовок

**Уровень 21 — Строитель снежинок**

---

## Объяснение

Ты уже знаешь **функции** из Блока 4 — переиспользуемые «рецепты» с параметрами. Теперь соедини функции с turtle, чтобы нарисовать **ветку снежинки**: главный ствол и боковую ветку из одного рецепта `draw_branch(length)`.

```python
def draw_branch(length):
    t.forward(length)
    t.backward(length)
```

Всё с **отступом** под `def` принадлежит функции. Вызови её **два раза** с поворотами между вызовами:

```python
draw_branch(100)
t.left(60)
draw_branch(70)
```

Функция рисует линию вперёд и назад — черепашка возвращается к «суставу» и может повернуться для следующей ветки.

---

### Шаг 1: Открой snowflake.py

Открой [starter/snowflake.py](starter/snowflake.py). Заполни TODO после `draw_branch`.

---

### Шаг 2: Запуск

**Путь A:**

```text
cd course-1-python-basics\block-5-creative-turtle\lesson-5-3-functions-and-turtle
python starter\snowflake.py
```

**Путь B:** Скопируй `snowflake.py` в свою папку. См. [STUDENT-MAP](../../STUDENT-MAP.ru.md).

**Ожидаемый результат (визуально):**

- Голубая ветка в форме **буквы Y** на белом холсте (ствол вверх, боковая ветка под 60°).
- Окно turtle открыто, пока не закроешь его или не нажмёшь **Ctrl+C** в терминале.

---

## Пример кода

**Файл: [starter/snowflake.py](starter/snowflake.py)**

```python
import turtle

t = turtle.Turtle()
t.speed(3)
t.color("deepskyblue")
t.width(3)


def draw_branch(length):
    t.forward(length)
    t.backward(length)


t.left(90)

draw_branch(100)

t.left(60)
draw_branch(70)

turtle.done()
```

---

## Запуск кода

```text
cd course-1-python-basics\block-5-creative-turtle\lesson-5-3-functions-and-turtle
python starter\snowflake.py
```

**Ожидаемый результат (визуально):** Голубая ветка Y; окно остаётся открытым.

---

## Быстрые упражнения

1. **Длиннее ствол** — измени первый вызов на `draw_branch(150)`.
2. **Толще линии** — попробуй `t.width(5)`.
3. **Бонус-узоры** — открой [exercises/branch_variations.ru.md](exercises/branch_variations.ru.md) для идеи шестилучевой снежинки.

---

## Практическое задание

**Квест:** Строитель снежинок

1. Убедись, что `draw_branch` с правильным отступом и вызывается **два раза** с `left()` между вызовами.
2. Запусти и проверь форму Y.
3. **Бонус:** Добавь вторую боковую ветку с `t.right(120)` и третьим `draw_branch(70)`.

**Эталонное решение:** [solution/snowflake.py](solution/snowflake.py)

---

## Уголок отладки

**Проблема:** Черепашка рисует не там — ветки торчат из случайных мест, а не из одного центра.

**Причина:** Код внутри `def draw_branch` **без отступа**. Python думает, что `forward` и `backward` выполняются на верхнем уровне, а не в функции.

**Неправильно:**

```python
def draw_branch(length):
t.forward(length)
t.backward(length)
```

**Ошибка:** `IndentationError: expected an indented block after function definition`

**Исправление:** Сделай отступ **четыре пробела** у каждой строки внутри функции:

```python
def draw_branch(length):
    t.forward(length)
    t.backward(length)
```

Сохрани и запусти снова.

---

## Проверь себя

Выбери лучший ответ на каждый вопрос. Сначала попробуй без подсказок!

1. Что делает `draw_branch(length)` внутри функции?
   - **a)** Только `forward(length)`
   - **b)** `forward(length)`, затем `backward(length)` — черепашка возвращается к «суставу»
   - **c)** Меняет заголовок окна
   - **d)** Снова импортирует turtle

2. Зачем вызвать `draw_branch(100)`, повернуть, затем `draw_branch(70)`?
   - **a)** Два вызова одного рецепта — главный ствол и боковая ветка снежинки (форма Y)
   - **b)** Потому что функцию можно запустить только раз за файл
   - **c)** Чтобы исправить SyntaxError
   - **d)** Чтобы быстрее закрыть окно turtle

3. Строки внутри `def draw_branch(length):` должны быть…
   - **a)** У левого края без пробелов
   - **b)** С **отступом** (четыре пробела) под строкой `def`
   - **c)** Заглавными буквами
   - **d)** Перед `import turtle`

4. Если `forward` и `backward` **без отступа** под `def`, какая ошибка?
   - **a)** KeyError
   - **b)** `IndentationError: expected an indented block after function definition`
   - **c)** IndexError
   - **d)** Ошибки нет — Python сам догадается

5. Где должна жить итоговая папка галереи `my_gallery/` в Блоке 5?
   - **a)** Только внутри `starter/`
   - **b)** В **корне проекта**, с `gallery.py`, скопированным из starter урока
   - **c)** Внутри окна turtle
   - **d)** В `course-2-web-apps`

---

<details><summary>Нажми, чтобы увидеть ответы</summary>

1. **b)** Вперёд и назад возвращают черепашку к точке ветвления для следующего поворота.
2. **a)** Один рецепт, разные длины — многоразовая функция для каждой ветки буквы Y.
3. **b)** Всё под `def` с отступом — иначе Python не считает это телом функции.
4. **b)** После `def` Python требует блок с отступом.
5. **b)** `my_gallery/` в корне проекта; скопируй туда `gallery.py` для звезды и снежинки в одном окне.

</details>

---

## Что дальше

→ [Курс 2: Веб-приложения на Python](../../../../course-2-web-apps/README.md) — Курс 1 завершён! Дальше: Flask и веб-страницы.

---

*Курс 1 пройден — ты рисуешь кодом, используешь циклы, цвет и функции. Впереди веб-приложения!*

[← Выбрать язык](README.md)
