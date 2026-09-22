# Lesson 2.2: Images & Sprites

> **Course:** Game Development with Python  
> **Block:** Player Controls & Animations  
> **Time:** ~30–40 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level 6 — Sprite Summoner |
| **[Русский →](ru.md)** | Уровень 6 — Призыватель спрайтов |

---

## What you'll build / Что ты создашь

**EN:** Load `player.png` and **blit** it instead of `draw.rect`. Arrow keys still move the hero — now as a tiny ship sprite.

**Expected window (sketch):**

```text
+---------------------------+
|                           |
|         |>                |
|     (PNG sprite blitted)  |
|                           |
+---------------------------+
```

**RU:** Загрузи `player.png` и выведи через **blit** вместо `draw.rect`. Стрелки по-прежнему двигают героя — теперь это маленький спрайт-корабль.

## What you'll learn / Что ты узнаешь

- `pygame.image.load(...)` + `.convert_alpha()` for PNGs with transparency
- `Surface.get_rect()` and `screen.blit(image, rect)`
- Keep assets next to `game.py` (or use `os.path` so paths work)
- `rect.clamp_ip` to stay on screen

## Before you start / Перед стартом

- [ ] [Lesson 2.1](../lesson-2-1-keyboard-events/README.md) — arrow-key movement
- [ ] `player.png` is in the same folder as your `game.py` (starter already has it)

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | Skeleton — TODOs for load + blit |
| [starter/player.png](starter/player.png) | Tiny placeholder ship sprite |
| [solution/game.py](solution/game.py) | Reference load + blit |
| [solution/player.png](solution/player.png) | Same sprite for the solution |

## Quick drills / Быстрые упражнения

1. Scale the sprite: `player = pygame.transform.scale(player, (64, 64))` after load.
2. Flip horizontally when moving left (`transform.flip`).
3. Draw a second static decoration blit in a corner.

---

**Previous / Предыдущий урок:** [Lesson 2.1 — Keyboard Events](../lesson-2-1-keyboard-events/README.md)

**Next lesson / Следующий урок:** [Lesson 2.3 — Score & Text Rendering](../lesson-2-3-score-text-rendering/README.md)
