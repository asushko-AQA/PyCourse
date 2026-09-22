# Block 2: Player Controls & Animations

> **Course:** Game Development with Python  
> **Block:** Player Controls & Animations  
> **Lessons:** 2.1 – 2.4 · **~2–2.5 hours total** · **Status: Draft**

**Folder map / Карта папок:** [STUDENT-MAP.md](../STUDENT-MAP.md) · [STUDENT-MAP.ru.md](../STUDENT-MAP.ru.md)

**Theme:** Control Deck — keyboard motion, sprites, score HUD, and screen states.

---

## Lessons / Уроки

| # | English | Русский | Level |
|---|---------|---------|-------|
| 2.1 | [Keyboard Events](lesson-2-1-keyboard-events/README.md) | События клавиатуры | Level 5 — Key Captain |
| 2.2 | [Images & Sprites](lesson-2-2-images-sprites/README.md) | Изображения и спрайты | Level 6 — Sprite Summoner |
| 2.3 | [Score & Text Rendering](lesson-2-3-score-text-rendering/README.md) | Счёт и вывод текста | Level 7 — Score Scribbler |
| 2.4 | [Game States](lesson-2-4-game-states/README.md) | Состояния игры | Level 8 — Stage Director |

**Previous / Предыдущее:** [Block 1 — Getting Started with Pygame](../block-1-getting-started-pygame/README.md)

**Next block / Следующий блок:** Block 3 — Physics & Collisions *(planned)*

---

## Block 2 readiness checklist

Tick every box before starting Block 3.

- [ ] Arrow keys move my player (held keys via `get_pressed`)
- [ ] I can load a PNG with `pygame.image.load` and `blit` it
- [ ] Score text appears with `font.render` + `blit`
- [ ] My game has **start → playing → game over** and restarts with SPACE

---

## For parents and teachers

**Block 2 turns the lab into a controllable mini-game.** Students still see a real window every lesson (~30–40 min). Homework remains **self-mark + quiz** (no automated display checker).

**Display needed:** Same as Block 1 — graphical desktop required.

**Common stuck points:** using one-shot `KEYDOWN` instead of `get_pressed` for continuous move; wrong path to `player.png`; forgetting to `blit` the rendered font surface; never switching `state` back to `START`.

---

*Take the controls — then dress the hero, keep score, and stage the show!*
