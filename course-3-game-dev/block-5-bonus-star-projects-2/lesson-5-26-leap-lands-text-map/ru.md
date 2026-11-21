# Урок 5.26: Текстовая карта и плитки

> **Course:** Game Development with Python · **Block:** Bonus ★ Star Projects II · **~34 min**  
> [Выбери язык](README.md) · [English →](en.md)

<!-- meta
homework: starter/game.py
minutes: 34
-->

---

## Название

**Level ★38 — Картограф**

---

## Объяснение

**Leap Lands** — Block 5 ★ project **#8** — is a twilight **mini platformer** with shape-only art (no image files).

Maps are **lists of strings**: `#` ground, `=` platform, `C` coin, `S` spawn, `F` flag, `^` spike, `E` enemy patrol (later lessons).

This lesson focuses on: **уровень из строк (`#` `=` `S`), плитки, раздельная коллизия по осям.**

### Step 1: Open the starter

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-26-leap-lands-text-map
python starter\game.py
```

**Mac/Linux:** `python starter/game.py`

**Expected output (visual):** Night-sky window; finish TODOs for this lesson's goal.

---

### Step 2: Compare the solution

Study [solution/game.py](solution/game.py) for the full pattern.

---

## Пример кода

**File: [solution/game.py](solution/game.py)**:

```python
player, grounded = move_and_resolve(player, solids, dx, dy)
```

---

## Запуск кода

```text
cd course-3-game-dev\block-5-bonus-star-projects-2\lesson-5-26-leap-lands-text-map
python solution\game.py
```

**Mac/Linux:** `python solution/game.py`

**Expected output (visual):** Runnable Leap Lands milestone for lesson 5.26.

---

## Быстрые упражнения

1. Print `grounded` when moving — when is it `True`?
2. Tweak `GRAVITY` or `JUMP_V` and rerun.
3. Name three map characters and what they mean.

---

## Задание для практики

**Квест:** Картограф

1. Finish TODOs in [starter/game.py](starter/game.py).
2. Self-mark: does the window match this lesson's goal?
3. **Bonus stretch:** draw a faint starfield behind the tiles.

**Self-mark:** Window runs ~5s without errors? ✓

**Reference solution:** [solution/game.py](solution/game.py)

---

## Уголок отладки

**Problem:** Player falls through the floor

**Cause:** Skipping axis-separated collision or never setting `grounded`.

**Fix:** After moving on **Y**, push the player up to `tile.top` when landing.

---

## Проверь себя

1. `dt` keeps motion smooth because…
   - **a)** Speed scales with frame time
   - **b)** It disables input
   - **c)** It only works on Linux
   - **d)** It removes gravity
2. Jump should happen only when…
   - **a)** `grounded` is True
   - **b)** In the air always
   - **c)** `vel_y < 0`
   - **d)** On Flask server
3. `#` in the map is…
   - **a)** Solid ground
   - **b)** A coin
   - **c)** A flag
   - **d)** Background JPG
4. Axis-separated collision is…
   - **a)** Move X, resolve, move Y, resolve
   - **b)** Random teleport
   - **c)** Turtle only
   - **d)** SQL DELETE
5. Next lesson adds…
   - **a)** монеты, шипы и жизни
   - **b)** pip freeze
   - **c)** Course 1 Turtle
   - **d)** Only print()

---

<details><summary>Click to reveal answers</summary>

1. **a)** Speed scales with frame time.

2. **a)** On the ground.

3. **a)** Solid ground.

4. **a)** Separate X then Y.

5. **a)** Next arc step.

</details>

## Что дальше

→ [Урок 5.27 — Coins, Spikes & Lives](../lesson-5-27-leap-lands-coins-lives/README.md)

---

*Вперёд по платформам!*

[Выбери язык](README.md)
