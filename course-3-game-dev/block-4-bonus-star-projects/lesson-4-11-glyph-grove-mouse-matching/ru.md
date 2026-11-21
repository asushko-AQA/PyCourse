# Урок 4.11: Мышь и совпадения

> **Курс:** Разработка игр на Python · **Блок:** Бонус ★ Проекты · **~35–40 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 38
-->

---

## Title

**Уровень ★11 — Выбор пары**

---

## Объяснение

В курсе 3 ты часто использовал **клавиатуру**. В **Glyph Grove** нужны **клики мыши**:

```python
if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
    pos = event.pos
```

**Попадание в плитку:**

```python
if tile_rect(tile).collidepoint(pos):
    ...
```

Проверяй плитки с **большим `layer` первыми** — как на экране.

---

### Шаг 1: Правило «свободной» плитки

Плитку можно убрать, если она **свободна**:

1. **Сверху никого** — нет плитки с бо́льшим `layer` на том же `row`/`col`.
2. **Открытый бок** — слева **или** справа на том же слое нет соседа.

Заблокированные плитки рисуй **тусклее**.

---

### Шаг 2: Два клика — пара

```python
selected = None

def try_match(first, second, tiles):
    if first is None:
        return second
    if first["kind"] == second["kind"] and is_free(first, tiles) and is_free(second, tiles):
        first["removed"] = True
        second["removed"] = True
        return None
    return second
```

---

### Шаг 3: Запуск

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-11-glyph-grove-mouse-matching
python starter\game.py
```

**Ожидаемый результат (на экране):** Подсветка выбора; пары исчезают.

---

## Пример кода

**Файл: [solution/game.py](solution/game.py)**

```python
if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
    hit = tile_at_point(event.pos, tiles)
    if hit is not None:
        selected = try_match(selected, hit, tiles)
```

---

## Запуск кода

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-11-glyph-grove-mouse-matching
python solution\game.py
```

**Ожидаемый результат (на экране):** Счётчик ходов; поле можно очистить.

---

## Быстрые упражнения

1. Печатай `event.pos` при клике — Y растёт вниз?
2. Клик по закрытой плитке — совпадение не должно сработать.
3. Два разных знака — второй клик меняет выбор.

---

## Задание для практики

**Квест:** Выбор пары

1. Реализуй `is_covered`, `has_open_side`, `is_free` в [starter/game.py](starter/game.py).
2. Подключи `MOUSEBUTTONDOWN`.
3. **Бонус:** жёлтая рамка у `selected`.

**Самопроверка:** Убираешь только **свободные** пары? ✓

**Эталон:** [solution/game.py](solution/game.py)

---

## Уголок отладки

**Проблема:** Клики не попадают.

**Причина:** Неверный `tile_rect` или порядок слоёв.

**Решение:** Как в 4.10; в `tile_at_point` — `sorted(..., reverse=True)` по `layer`.

---

## Проверь себя

1. `collidepoint` нужен…
   - **a)** `Rect` и координаты мыши
   - **b)** Имя маршрута Flask
   - **c)** `pip uninstall`
   - **d)** Только путь к файлу

2. `MOUSEBUTTONDOWN`, `button == 1` — это…
   - **a)** Обычно левая кнопка мыши
   - **b)** Клавиша Escape
   - **c)** Только колесо
   - **d)** Событие QUIT

3. «Покрыта» значит…
   - **a)** Сверху плитка с большим слоем на той же клетке
   - **b)** Цвет чёрный
   - **c)** Квиз не пройден
   - **d)** Отрицательный счёт

4. «Открытый бок» — это…
   - **a)** Нет соседа слева ИЛИ справа на том же слое
   - **b)** Плитка смотрит на север
   - **c)** Полноэкранный режим
   - **d)** Две клавиатуры

5. Урок 4.12 добавит…
   - **a)** Таймер, подсказку, shuffle, титул, лучшее время
   - **b)** Удаление мыши
   - **c)** Миграции Django
   - **d)** Только print

---

<details><summary>Показать ответы</summary>

1. **a)** Проверка Rect.
2. **a)** Левый клик.
3. **a)** Верхний слой блокирует.
4. **a)** Проверка боков.
5. **a)** Полный Glyph Grove.

</details>

---

## Что дальше

→ [Урок 4.12 — Glyph Grove целиком](../lesson-4-12-glyph-grove-complete/README.md)

---

*Кликай аккуратно — края важны.*

[← Выбрать язык](README.md)