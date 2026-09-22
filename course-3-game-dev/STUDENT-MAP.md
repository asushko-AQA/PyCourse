# Student Map — Course 3 Folder Guide

> **Course:** Game Development with Python  
> [Русский →](STUDENT-MAP.ru.md)

Use this map when a lesson says `cd course-3-game-dev\...` but your folder looks different.

---

## PyCourse folder tree (Path A)

```text
PyCourse/
├── course-1-python-basics/          ← prerequisite
├── course-2-web-apps/               ← optional (venv practice)
├── course-3-game-dev/
│   ├── README.md                    ← Course 3 index
│   ├── STUDENT-MAP.md
│   ├── block-1-getting-started-pygame/
│   │   ├── lesson-1-1-install-pygame-game-loop/
│   │   ├── lesson-1-2-game-window-colors/
│   │   ├── lesson-1-3-shapes-coordinates/
│   │   └── lesson-1-4-delta-time-smooth-movement/
│   └── block-2-player-controls-animations/
│       ├── lesson-2-1-keyboard-events/
│       ├── lesson-2-2-images-sprites/
│       ├── lesson-2-3-score-text-rendering/
│       └── lesson-2-4-game-states/
└── .venv/                           ← YOU create (or reuse Course 2 .venv)
```

---

## Path B — no full repo?

| Lesson | Instead of long `cd`… |
|--------|------------------------|
| 1.1–2.4 | Copy the lesson `starter/` folder anywhere; activate a venv with Pygame; `cd` there before running |

---

## Virtual environment reminder

From Course 2 onward, install packages **inside** `.venv`, never globally.

```text
python -m venv .venv
.venv\Scripts\Activate.ps1          # Windows PowerShell
pip install pygame
```

**Mac/Linux:** `source .venv/bin/activate` then `pip install pygame`.

You may reuse a Course 2 `.venv` and just `pip install pygame` into it.

---

## Progress tick list

- [ ] 1.1 — Pygame installed; window opens and closes with the X button
- [ ] 1.2 — Background color fills; color changes each frame
- [ ] 1.3 — A rectangle moves across the window using `x` / `y`
- [ ] 1.4 — Motion uses `dt = clock.tick(60) / 1000` (smooth on any machine)
- [ ] 2.1 — Arrow keys move the player with `get_pressed`
- [ ] 2.2 — PNG sprite loads with `pygame.image.load` and `blit`
- [ ] 2.3 — Score text renders with `font.render` + `blit`
- [ ] 2.4 — Game has start → playing → game over; SPACE restarts
- [ ] 3.1–3.3 — *(coming later)*

---

## Course 3 graduation checklist (full course)

1. [ ] All Block 1–3 lessons ticked  
2. [ ] Capstone **Catch the Falling Stars** runs end-to-end  
3. [ ] A parent or teacher played one round of your game  

→ [Course 3 index](README.md)

---

[← Course 2](../course-2-web-apps/README.md)
