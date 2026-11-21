# game.py — Lesson 5.21: Twin Cards — complete (starter)
from __future__ import annotations

import random

import pygame

pygame.init()

DIFFICULTIES = [("easy", 4, 3), ("medium", 4, 4), ("hard", 6, 4)]
CELL = 88
GAP = 8
BOARD_X = 40
BOARD_Y = 110
WAIT_SEC = 0.65

screen = pygame.display.set_mode((640, 620))
pygame.display.set_caption("Twin Cards — Cosmic Memory")
clock = pygame.time.Clock()
font_small = pygame.font.Font(None, 28)
font_big = pygame.font.Font(None, 46)

state = "START"
cols, rows = 4, 3
cards: list[dict] = []
moves = 0
elapsed = 0.0
session_best_moves: int | None = None

pick_phase = "idle"
first_pick: dict | None = None
wait_timer = 0.0

SYMBOL_COLORS = [(255, 210, 110), (160, 210, 255), (255, 150, 175), (140, 230, 170), (200, 170, 255), (255, 185, 120)]


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
            out.append({"col": col, "row": row, "symbol": deck[i], "face_up": False, "matched": False, "flip_t": 0.0})
            i += 1
    return out


def start_game(c: int, r: int) -> None:
    """TODO: reset cards, moves, elapsed, state=PLAYING."""
    pass


def stars_for_moves(move_count: int) -> int:
    """TODO: 3 / 2 / 1 stars based on moves vs pair count."""
    return 1


def card_rect(card: dict) -> pygame.Rect:
    x = BOARD_X + card["col"] * CELL
    y = BOARD_Y + card["row"] * CELL
    return pygame.Rect(x + GAP // 2, y + GAP // 2, CELL - GAP, CELL - GAP)


def draw_card(surface: pygame.Surface, card: dict) -> None:
    rect = card_rect(card)
    color = SYMBOL_COLORS[card["symbol"] % len(SYMBOL_COLORS)]
    if card["face_up"] or card["matched"]:
        pygame.draw.rect(surface, color, rect.inflate(-6, -6), border_radius=10)
    else:
        pygame.draw.rect(surface, (40, 34, 70), rect, border_radius=10)


def handle_pick(card: dict) -> None:
    """TODO: from lesson 5.20 + bump moves + win detection + best moves."""
    pass


def update_wait(dt: float) -> None:
    pass


running = True

while running:
    dt = clock.tick(60) / 1000
    if state == "PLAYING":
        elapsed += dt
        update_wait(dt)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and state == "START" and event.key == pygame.K_SPACE:
            start_game(4, 3)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and state == "PLAYING":
            for card in cards:
                if card_rect(card).collidepoint(event.pos):
                    handle_pick(card)

    screen.fill((12, 10, 26))
    if state == "PLAYING":
        for card in cards:
            draw_card(screen, card)
    elif state == "START":
        t = font_big.render("Twin Cards — finish TODOs", True, (230, 210, 255))
        screen.blit(t, t.get_rect(center=(320, 300)))
    pygame.display.flip()

pygame.quit()