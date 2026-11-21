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
│   ├── block-2-player-controls-animations/
│   │   ├── lesson-2-1-keyboard-events/
│   │   ├── lesson-2-2-images-sprites/
│   │   ├── lesson-2-3-score-text-rendering/
│   │   └── lesson-2-4-game-states/
│   ├── block-3-physics-collisions-final-project/
│   │   ├── lesson-3-1-collision-detection/
│   │   ├── lesson-3-2-catch-the-falling-stars/
│   │   └── lesson-3-3-polish/
│   └── block-4-bonus-star-projects/  ← optional ★ bonus after Block 3
│       ├── lesson-4-1-sky-hopper-gravity-flap/
│       ├── lesson-4-2-scrolling-gateways/
│       ├── lesson-4-3-sky-hopper-complete/
│       ├── lesson-4-4-prism-dash-auto-scroll/
│       ├── lesson-4-5-prism-dash-jump-rotate/
│       ├── lesson-4-6-prism-dash-complete/
│       ├── lesson-4-7-shard-stack-grid-cells/
│       ├── lesson-4-8-shard-stack-falling-pieces/
│       ├── lesson-4-9-shard-stack-complete/
│       ├── lesson-4-10-glyph-grove-tiles-layout/
│       ├── lesson-4-11-glyph-grove-mouse-matching/
│       └── lesson-4-12-glyph-grove-complete/
│   └── block-5-bonus-star-projects-2/  ← optional ★ II after Block 4
│       ├── lesson-5-1-glow-worm-grid-segments/
│       ├── lesson-5-2-glow-worm-food-growth/
│       ├── lesson-5-3-glow-worm-complete/
│       ├── lesson-5-4-bounce-forge-ball-walls/
│       ├── lesson-5-5-bounce-forge-paddle-lives/
│       ├── lesson-5-6-bounce-forge-bricks-score/
│       ├── lesson-5-7-bounce-forge-complete/
│       ├── lesson-5-8-orbit-guard-patrol-ship/
│       ├── lesson-5-9-orbit-guard-invader-formation/
│       ├── lesson-5-10-orbit-guard-shields-lives/
│       ├── lesson-5-11-orbit-guard-complete/
│       ├── lesson-5-12-mine-whisper-crystal-grid/
│       ├── lesson-5-13-mine-whisper-mines-numbers/
│       ├── lesson-5-14-mine-whisper-flood-flags/
│       ├── lesson-5-15-mine-whisper-complete/
│       ├── lesson-5-16-merge-magic-rune-board/
│       ├── lesson-5-17-merge-magic-slide-merge/
│       ├── lesson-5-18-merge-magic-complete/
│       ├── lesson-5-19-twin-cards-symbol-deck/
│       ├── lesson-5-20-twin-cards-flip-match/
│       ├── lesson-5-21-twin-cards-complete/
│       ├── lesson-5-22-tic-tac-bot-grid-turns/
│       ├── lesson-5-23-tic-tac-bot-win-score/
│       ├── lesson-5-24-tic-tac-bot-complete/
│       ├── lesson-5-25-leap-lands-player-jump/
│       ├── lesson-5-26-leap-lands-text-map/
│       ├── lesson-5-27-leap-lands-coins-lives/
│       ├── lesson-5-28-leap-lands-enemies-camera/
│       ├── lesson-5-29-leap-lands-complete/
│       ├── lesson-5-30-night-swarm-lantern-move/
│       ├── lesson-5-31-night-swarm-shadow-spawns/
│       ├── lesson-5-32-night-swarm-light-orbs/
│       ├── lesson-5-33-night-swarm-level-up/
│       └── lesson-5-34-night-swarm-complete/
└── .venv/                           ← YOU create (or reuse Course 2 .venv)
```

---

## Path B — no full repo?

| Lesson | Instead of long `cd`… |
|--------|------------------------|
| 1.1–5.37 | Copy the lesson `starter/` folder anywhere; activate a venv with Pygame; `cd` there before running |

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
- [ ] 3.1 — `rect.colliderect()` collects a coin and relocates it
- [ ] 3.2 — Capstone: stars spawn, fall, get caught, score updates, restart works
- [ ] 3.3 — Polish: high score (session), difficulty ramp, optional catch/miss sounds

### Optional ★ Block 4 — Sky Hopper

- [ ] 4.1 — Gravity + flap with procedural bird
- [ ] 4.2 — Scrolling gateways, score, crash
- [ ] 4.3 — Full Sky Hopper: title / play / game over, high score, speed ramp

### Optional ★ Block 4 — Prism Dash

- [ ] 4.4 — `world_x` scroll; cube stays at fixed X
- [ ] 4.5 — Jump when grounded; cube spins in air
- [ ] 4.6 — Full Prism Dash: level string, spikes, progress %, attempts, best %

### Optional ★ Block 4 — Shard Stack

- [ ] 4.7 — 2D grid list; draw the well and offsets
- [ ] 4.8 — `can_move`, timer fall, lock piece
- [ ] 4.9 — Full Shard Stack: rotate, clear lines, score, high score

### Optional ★ Block 4 — Glyph Grove

- [ ] 4.10 — Tile dicts; layered layout; font glyph drawing
- [ ] 4.11 — Mouse pick; free-tile rule; matching pairs
- [ ] 4.12 — Full Glyph Grove: hint, shuffle, timer, best time, win/stuck

### Optional ★ Block 5 II — Glow Worm

- [ ] 5.1 — `segments` list; `(col, row)`; direction tuple; timed steps
- [ ] 5.2 — Food spawn; grow tail; wall + self crash
- [ ] 5.3 — Full Glow Worm: start / play / game over, score, speed ramp, session best

### Optional ★ Block 5 II — Bounce Forge

- [ ] 5.4 — `ball_vx` / `ball_vy` + wall bounces (forge spark)
- [ ] 5.5 — Anvil paddle, `hit_frac` angle, lives
- [ ] 5.6 — Brick `Rect` list, side bounce, score
- [ ] 5.7 — Full Bounce Forge: levels, high score, optional Pong (**P**)

### Optional ★ Block 5 II — Orbit Guard

- [ ] 5.8 — Patrol ship + `player_bolts` list, cooldown, off-screen cleanup
- [ ] 5.9 — Invader grid march + step down at screen edges
- [ ] 5.10 — Collisions, enemy bolts, shields with HP, lives & score
- [ ] 5.11 — Full Orbit Guard: waves, UFO bonus, states, session best

### Optional ★ Block 5 II — Mine Whisper

- [ ] 5.12 — 2D cell dict grid; draw crystals; mouse → `(col, row)`
- [ ] 5.13 — Mines after first click; neighbor counts; reveal numbers
- [ ] 5.14 — Flood-fill open zeros; right-click flags
- [ ] 5.15 — Full Mine Whisper: difficulties, timer, mine counter, win/lose, best time

### Optional ★ Block 5 II — Merge Magic

- [ ] 5.16 — 4×4 int `board`; `RUNE_COLORS`; spawn 2/4 in empty cells
- [ ] 5.17 — `merge_row` slide+merge; four directions; spawn on change only
- [ ] 5.18 — Full Merge Magic: score, 2048 win + continue, game over, undo, best score

### Optional ★ Block 5 II — Twin Cards

- [ ] 5.19 — Pair deck, shuffle, 4×3 grid, card backs vs shape symbols
- [ ] 5.20 — Click flips; idle/first/waiting; timer hides mismatches
- [ ] 5.21 — Full Twin Cards: moves, timer, 3 sizes, win stars, session best

### Optional ★ Block 5 II — Tic-Tac-Bot

- [ ] 5.22 — 9-cell list board; draw bolt X / gear O; hot-seat mouse turns
- [ ] 5.23 — `WIN_LINES`, highlight win, score table, round restart
- [ ] 5.24 — Full Tic-Tac-Bot: Easy/Medium/Hard bot, delay, who starts, session W/L/D

### Optional ★ Block 5 II — Leap Lands

- [ ] 5.25 — Player `Rect`, arrows + `dt`, gravity, jump when grounded
- [ ] 5.26 — Text map tiles; axis-separated collision
- [ ] 5.27 — Coins `C`, spikes `^`, lives, HUD, respawn at `S`
- [ ] 5.28 — Patrol enemies `E`, stomp, `camera_x` scroll
- [ ] 5.29 — Full Leap Lands: 3 levels, flag win, timer + session best

### Optional ★ Block 5 II — Night Swarm

- [ ] 5.30 — `Vector2` 8-way move, normalize, arena clamp + `dt`
- [ ] 5.31 — Edge spawns on timer, vector chase, contact damage, HP bar
- [ ] 5.32 — Nearest-target auto orbs, enemy HP, XP gem drops
- [ ] 5.33 — XP level-up pause; 3 random upgrades from dict
- [ ] 5.34 — Full Night Swarm: survive ~3 min, wave ramp, states, session best

---

## Course 3 graduation checklist (full course)

1. [ ] All Block 1–3 lessons ticked  
2. [ ] Capstone **Catch the Falling Stars** runs end-to-end  
3. [ ] A parent or teacher played one round of your game  

**★ Bonus:** finish Block 4 and demo **Sky Hopper**, **Prism Dash**, **Shard Stack**, and **Glyph Grove** — all four Block 4 ★ projects!

**★ II Bonus:** continue in Block 5 through **Night Swarm** (nine ★ games shipped); **Lane Rush** *coming soon* on the block README roadmap).

→ [Course 3 index](README.md)

---

[← Course 2](../course-2-web-apps/README.md)
