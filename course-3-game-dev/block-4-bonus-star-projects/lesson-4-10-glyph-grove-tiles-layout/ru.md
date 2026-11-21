# Урок 4.10: Плитки и раскладка

> **Курс:** Разработка игр на Python · **Блок:** Бонус ★ Проекты · **~30–35 мин**  
> [Выбрать язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 32
-->

---

## Title

**Уровень ★10 — Плитки сада**

---

## Объяснение

Проект **#4** в блоке 4 — **Glyph Grove**: головоломка на **совпадение плиток** со **своими символами** (цвет + знак Unicode, не настоящие плитки маджонга).

Пока ты играл с **клавиатурой**. Скоро добавим **мышь**. Сначала — одна плитка как **словарь**:

```python
tile = {
    "id": 0,
    "kind": "★",
    "kind_index": 3,
    "row": 2,
    "col": 4,
    "layer": 1,
    "removed": False,
}
```

- `row` / `col` — место на сетке  
- `layer` — высота слоя (выше рисуется сверху)  
- `kind` — знак, который должен совпасть с парой

---

### Шаг 1: Раскладка + перемешанные пары

```python
LAYOUT = [(0, 2, 0), (0, 2, 1), ...]  # (layer, row, col)
kinds = GLYPHS * 2
random.shuffle(kinds)
```

Каждая позиция получает одну плитку; знаки идут **парами**, чтобы поле можно было разобрать.

---

### Шаг 2: Сетка → пиксели

```python
x = BOARD_X + col * TILE_W + layer * LAYER_DX
y = BOARD_Y + row * TILE_H + layer * LAYER_DY
```

Небольшой сдвиг `LAYER_DX` даёт ощущение стопки слоёв.

---

### Шаг 3: Рисуем знак

```python
glyph = font_glyph.render(tile["kind"], True, (25, 28, 40))
surface.blit(glyph, (gx, gy))
```

`pygame.font.Font(None, 52)` — встроенный шрифт, без картинок.

---

### Шаг 4: Запуск

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-10-glyph-grove-tiles-layout
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Ожидаемый результат (на экране):** Слои плиток с цветными знаками после TODO.

---

## Пример кода

**Файл: [solution/game.py](solution/game.py)**

```python
for i, (layer, row, col) in enumerate(LAYOUT):
    tiles.append({"kind": kinds[i], "layer": layer, "row": row, "col": col, ...})
for tile in tiles:
    draw_tile(screen, tile)
```

---

## Запуск кода

```text
cd course-3-game-dev\block-4-bonus-star-projects\lesson-4-10-glyph-grove-tiles-layout
python solution\game.py
```

**Ожидаемый результат (на экране):** 24 плитки в трёх слоях; пары знаков `◆ ● ▲ ★ ✚ ☘`.

---

## Быстрые упражнения

1. Поменяй `GLYPHS[0]` — цвет всё ещё подходит?
2. Выведи `len(LAYOUT)` — почему число чётное?
3. Поставь `LAYER_DX = 0` — стопка выглядит плоской?

---

## Задание для практики

**Квест:** Плитки сада

1. Закрой TODO в [starter/game.py](starter/game.py).
2. В каждой ячейке раскладки виден знак по центру.
3. **Бонус:** сортируй `tiles` по `layer` перед рисованием.

**Самопроверка:** Видны три слоя? ✓

**Эталон:** [solution/game.py](solution/game.py)

---

## Уголок отладки

**Проблема:** Пустой экран.

**Причина:** `build_tiles` возвращает `[]`.

**Решение:** Соедини `LAYOUT` и перемешанные `kinds`.

---

## Проверь себя

1. Место плитки хранится в…
   - **a)** Ключах `row`, `col`, `layer`
   - **b)** Только в JPG
   - **c)** Секретном ключе Flask
   - **d)** Градусах Turtle

2. `GLYPHS * 2` перед shuffle — это…
   - **a)** Каждый знак дважды (пары)
   - **b)** Окно в 2 раза шире
   - **c)** Выход из pygame
   - **d)** Отключение клавиш

3. `font_glyph.render` даёт…
   - **a)** `Surface` для `blit`
   - **b)** HTTP-ответ
   - **c)** Всегда SyntaxError
   - **d)** CSV-файл

4. Больший `layer` рисуют…
   - **a)** Поверх нижних слоёв
   - **b)** До `pygame.init`
   - **c)** Только по воскресеньям
   - **d)** Без цвета

5. Урок 4.11 добавит…
   - **a)** Мышь и правило «свободной» плитки
   - **b)** Только Flask-формы
   - **c)** Удаление pygame
   - **d)** Снежинки Turtle

---

<details><summary>Показать ответы</summary>

1. **a)** Координаты в словаре.
2. **a)** Пары знаков.
3. **a)** Поверхность с текстом.
4. **a)** Порядок отрисовки важен.
5. **a)** Мышь дальше.

</details>

---

## Что дальше

→ [Урок 4.11 — Мышь и совпадения](../lesson-4-11-glyph-grove-mouse-matching/README.md)

---

*Свои знаки — своё искусство.*

[← Выбрать язык](README.md)