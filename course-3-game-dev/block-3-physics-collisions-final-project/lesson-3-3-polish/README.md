# Lesson 3.3: Polish

> **Course:** Game Development with Python  
> **Block:** Physics & Collisions (Final Project)  
> **Time:** ~30–40 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level 11 — Polish Pro |
| **[Русский →](ru.md)** | Уровень 11 — Мастер полировки |

---

## What you'll build / Что ты создашь

**EN:** Upgrade Catch the Falling Stars with **session high score**, **difficulty ramp** (faster falls), and **optional catch/miss sounds**.

**RU:** Улучши Catch the Falling Stars: **рекорд сессии**, **рост сложности** (быстрее падение) и **опциональные звуки** ловли/промаха.

## What you'll learn / Что ты узнаешь

- In-memory `high_score` that survives rounds (not files — keep it simple)
- `fall_speed = BASE + score * k` ramp
- `pygame.mixer.Sound` with try/except so missing audio never crashes

## Before you start / Перед стартом

- [ ] [Lesson 3.2](../lesson-3-2-catch-the-falling-stars/README.md) — working catch game
- [ ] Speakers optional (game runs silent if Sound fails)

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | Capstone base; TODOs for polish |
| [starter/star.png](starter/star.png) | Star sprite |
| [starter/catch.wav](starter/catch.wav) / [miss.wav](starter/miss.wav) | Tiny beeps |
| [solution/game.py](solution/game.py) | Polished game |

## Quick drills / Быстрые упражнения

1. Change ramp to `score * 20` for a fiercer climb.
2. Show “NEW BEST!” on Game Over when `score == high_score` and `score > 0`.
3. Mute test: rename wav files and confirm the game still runs.

---

**Previous / Предыдущий урок:** [Lesson 3.2 — Catch the Falling Stars](../lesson-3-2-catch-the-falling-stars/README.md)

**Next / Дальше:** [Block 3 index](../README.md) — tick the graduation checklist!
