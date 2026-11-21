# game.py — Lesson 5.21: Twin Cards — complete (solution)
from __future__ import annotations

import random

import pygame

pygame.init()

DIFFICULTIES: list[tuple[str, int, int]] = [
    ("easy", 4, 3),
    ("medium", 4, 4),
    ("hard", 6, 4),
]
CELL = 88
GAP = 8
BOARD_X = 40
BOARD_Y = 110
WAIT_SEC = 0.65
FLIP_ANIM = 0.18

screen = pygame.display.set_mode((640, 620))
pygame.display.set_caption("Twin Cards — Cosmic Memory")
clock = pygame.time.Clock()
font_small = pygame.font.Font(None, 28)
font_big = pygame.font.Font(None, 46)

SYMBOL_COLORS: list[tuple[int, int, int]] = [
    (255, 210, 110),
    (160, 210, 255),
    (255, 150, 175),
    (140, 230, 170),
    (200, 170, 255),
    (255, 185, 120),
    (120, 220, 230),
    (230, 200, 255),
    (255, 255, 150),
    (180, 255, 200),
    (255, 160, 140),
    (190, 190, 255),
]

state = "START"
cols, rows = 4, 3
cards: list[dict] = []
moves = 0
elapsed = 0.0
session_best_moves: int | None = None
pick_phase = "idle"
first_pick: dict | None = None
wait_timer = 0.0


def build_deck(c: int, r: int) -> list[int]:
    pair_count = (c * r) // 2
    deck = list(range(pair_count)) * 2
    random.shuffle(deck)
    return deck


def make_cards(c: int, r: int) -> list[dict]:
    deck = build_deck(c, r)
    out: list[dict] = []
    i = 0
    for row in range(r):
        for col in range(c):
            out.append(
                {
                    "col": col,
                    "row": row,
                    "symbol": deck[i],
                    "face_up": False,
                    "matched": False,
                    "flip_t": 0.0,
                }
            )
            i += 1
    return out


def reset_pick() -> None:
    global pick_phase, first_pick, wait_timer
    pick_phase = "idle"
    first_pick = None
    wait_timer = 0.0


def start_game(c: int, r: int) -> None:
    global state, cols, rows, cards, moves, elapsed
    cols, rows = c, r
    cards = make_cards(c, r)
    moves = 0
    elapsed = 0.0
    reset_pick()
    state = "PLAYING"


def pair_count() -> int:
    return (cols * rows) // 2


def stars_for_moves(move_count: int) -> int:
    perfect = pair_count() + 2
    good = pair_count() + 6
    if move_count <= perfect:
        return 3
    if move_count <= good:
        return 2
    return 1


def board_size() -> tuple[int, int]:
    return cols * CELL + 24, rows * CELL + 24


def card_rect(card: dict) -> pygame.Rect:
    x = BOARD_X + card["col"] * CELL
    y = BOARD_Y + card["row"] * CELL
    return pygame.Rect(x + GAP // 2, y + GAP // 2, CELL - GAP, CELL - GAP)


def mouse_to_card(pos: tuple[int, int]) -> dict | None:
    for card in reversed(cards):
        if card_rect(card).collidepoint(pos):
            return card
    return None


def draw_card_back(surface: pygame.Surface, rect: pygame.Rect, anim: float) -> None:
    wobble = int(4 * anim)
    rect = rect.inflate(wobble, wobble)
    pygame.draw.rect(surface, (38, 32, 68), rect, border_radius=12)
    pygame.draw.rect(surface, (120, 100, 190), rect, width=2, border_radius=12)
    q = font_small.render("?", True, (200, 180, 255))
    surface.blit(q, q.get_rect(center=rect.center))


def draw_symbol(surface: pygame.Surface, rect: pygame.Rect, symbol_id: int, anim: float) -> None:
    grow = int(6 * anim)
    rect = rect.inflate(grow, grow)
    color = SYMBOL_COLORS[symbol_id % len(SYMBOL_COLORS)]
    pygame.draw.rect(surface, (32, 26, 52), rect, border_radius=12)
    inner = rect.inflate(-10, -10)
    pygame.draw.rect(surface, color, inner, border_radius=10)
    cx, cy = rect.center
    shape = symbol_id % 6
    if shape == 0:
        pts = [(cx, cy - 20), (cx + 18, cy + 12), (cx - 18, cy + 12)]
        pygame.draw.polygon(surface, (255, 255, 255), pts)
    elif shape == 1:
        pygame.draw.circle(surface, (255, 255, 255), (cx, cy), 20, width=4)
    elif shape == 2:
        pts = [(cx, cy - 22), (cx + 20, cy + 16), (cx - 20, cy + 16)]
        pygame.draw.polygon(surface, (255, 255, 255), pts)
    elif shape == 3:
        pts = [(cx, cy - 18), (cx + 14, cy), (cx, cy + 18), (cx - 14, cy)]
        pygame.draw.polygon(surface, (255, 255, 255), pts)
    elif shape == 4:
        pygame.draw.line(surface, (255, 255, 255), (cx - 16, cy), (cx + 16, cy), 4)
        pygame.draw.line(surface, (255, 255, 255), (cx, cy - 16), (cx, cy + 16), 4)
    else:
        pygame.draw.circle(surface, (255, 255, 255), (cx, cy), 16, width=4)


def draw_card(surface: pygame.Surface, card: dict) -> None:
    rect = card_rect(card)
    anim = min(1.0, card["flip_t"])
    if card["face_up"] or card["matched"]:
        draw_symbol(surface, rect, card["symbol"], anim)
        if card["matched"]:
            pygame.draw.rect(surface, (100, 255, 180), rect.inflate(8, 8), width=2, border_radius=14)
    else:
        draw_card_back(surface, rect, anim)


def handle_pick(card: dict) -> None:
    global pick_phase, first_pick, wait_timer, moves, state, session_best_moves
    if state != "PLAYING" or pick_phase == "waiting":
        return
    if card["matched"] or card["face_up"]:
        return
    card["face_up"] = True
    card["flip_t"] = 0.0
    if pick_phase == "idle":
        first_pick = card
        pick_phase = "first"
        return
    if first_pick is None:
        return
    moves += 1
    if card["symbol"] == first_pick["symbol"] and card is not first_pick:
        card["matched"] = True
        first_pick["matched"] = True
        reset_pick()
        if all(c["matched"] for c in cards):
            state = "WON"
            if session_best_moves is None or moves < session_best_moves:
                session_best_moves = moves
    else:
        pick_phase = "waiting"
        wait_timer = WAIT_SEC


def update_wait(dt: float) -> None:
    global wait_timer, first_pick, pick_phase
    if pick_phase != "waiting":
        return
    wait_timer -= dt
    if wait_timer > 0:
        return
    if first_pick:
        first_pick["face_up"] = False
    for card in cards:
        if not card["matched"]:
            card["face_up"] = False
    reset_pick()


def update_flips(dt: float) -> None:
    for card in cards:
        if card["face_up"] or card["matched"]:
            card["flip_t"] = min(1.0, card["flip_t"] + dt / FLIP_ANIM)
        else:
            card["flip_t"] = max(0.0, card["flip_t"] - dt / FLIP_ANIM)


def draw_overlay(title: str, lines: list[str]) -> None:
    overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    overlay.fill((8, 6, 20, 210))
    screen.blit(overlay, (0, 0))
    t = font_big.render(title, True, (240, 220, 255))
    screen.blit(t, t.get_rect(midtop=(screen.get_width() // 2, 150)))
    y = 230
    for line in lines:
        surf = font_small.render(line, True, (200, 190, 230))
        screen.blit(surf, surf.get_rect(midtop=(screen.get_width() // 2, y)))
        y += 34


running = True

while running:
    dt = clock.tick(60) / 1000
    if state == "PLAYING":
        elapsed += dt
        update_wait(dt)
        update_flips(dt)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if state == "START":
                if event.key in (pygame.K_SPACE, pygame.K_1):
                    start_game(4, 3)
                elif event.key == pygame.K_2:
                    start_game(4, 4)
                elif event.key == pygame.K_3:
                    start_game(6, 4)
            elif state in ("WON", "PLAYING") and event.key == pygame.K_r:
                start_game(cols, rows)
            elif state == "WON" and event.key == pygame.K_SPACE:
                state = "START"
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and state == "PLAYING":
            picked = mouse_to_card(event.pos)
            if picked:
                handle_pick(picked)

    screen.fill((12, 10, 26))
    if state != "START":
        bw, bh = board_size()
        frame = pygame.Rect(BOARD_X - 12, BOARD_Y - 12, bw, bh)
        pygame.draw.rect(screen, (22, 18, 40), frame, border_radius=12)
        for card in cards:
            draw_card(screen, card)
        hud = font_small.render(
            f"Moves {moves}  Time {elapsed:0.1f}s  Best {session_best_moves if session_best_moves else '-'}",
            True,
            (200, 185, 255),
        )
        screen.blit(hud, (BOARD_X, 72))
        hint = font_small.render(f"{cols}×{rows} — R restart", True, (150, 140, 190))
        screen.blit(hint, (BOARD_X, BOARD_Y + rows * CELL + 16))

    if state == "START":
        draw_overlay(
            "Twin Cards",
            [
                "1 = easy 4×3",
                "2 = medium 4×4",
                "3 = hard 6×4",
                "SPACE also starts easy",
            ],
        )
    elif state == "WON":
        stars = stars_for_moves(moves)
        draw_overlay(
            "You found every pair!",
            [
                f"★" * stars + "☆" * (3 - stars),
                f"Moves: {moves}",
                f"Time: {elapsed:0.1f}s",
                "R = same size again",
                "SPACE = title",
            ],
        )

    pygame.display.flip()

pygame.quit()