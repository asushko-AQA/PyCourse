# Lesson 4.6: Prism Dash Complete

> **Course:** Game Development with Python  
> **Block:** Bonus ★ Star Projects *(optional)*  
> **Time:** ~40–45 minutes

---

## Choose your language / Выбери язык

| | |
|---|---|
| **[English →](en.md)** | Level ★6 — Prism Dash Pro |
| **[Русский →](ru.md)** | Уровень ★6 — Prism Dash Pro |

---

## What you'll build / Что ты создашь

**EN:** Full **Prism Dash** — level string with platforms and spikes, collision restart, **progress %** bar, **attempts** counter, start / play / win / game over, session **best %**, and a gentle **speed ramp**.

**RU:** Полный **Prism Dash** — уровень-строка с платформами и шипами, рестарт при столкновении, полоса **прогресса %**, счётчик **попыток**, start / play / win / game over, **лучший %** за сессию и плавный **рост скорости**.

## What you'll learn / Что ты узнаешь

- Encode a level: `_` ground, `#` platform, `^` spike
- `colliderect` with spikes → `die()` → attempts++
- Game states like Lessons 2.4 and 4.3

## Before you start / Перед стартом

- [ ] [Lesson 4.5](../lesson-4-5-prism-dash-jump-rotate/README.md) — jump + spin working

## Files in this lesson / Файлы урока

| File | Description |
|------|-------------|
| [en.md](en.md) | Full lesson in English |
| [ru.md](ru.md) | Полный урок на русском |
| [starter/game.py](starter/game.py) | Skeleton state machine; TODO level |
| [solution/game.py](solution/game.py) | Playable Prism Dash |

## Quick drills / Быстрые упражнения

1. Add two `^` spikes to `LEVEL` and re-test.
2. Draw checkpoint at 50% — respawn there on death (stretch).
3. Change speed ramp: `BASE_SCROLL + progress_pct() * 4`.

---

**Previous / Предыдущий урок:** [Lesson 4.5 — Jump & Spin](../lesson-4-5-prism-dash-jump-rotate/README.md)

**Next / Дальше:** [Block 4 index](../README.md) — ★ project **#2** done! Future **4.7** starts the next bonus game.