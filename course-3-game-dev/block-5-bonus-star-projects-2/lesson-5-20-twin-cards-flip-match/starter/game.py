# game.py — Lesson 5.20: Twin Cards — flip & match (starter)
from __future__ import annotations

import random

import pygame

pygame.init()

COLS = 4
ROWS = 3
CELL = 96
GAP = 10
BOARD_X = 56
BOARD_Y = 90
WIDTH = BOARD_X * 2 + COLS * CELL
HEIGHT = 580
WAIT_SEC = 0.7

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Twin Cards — Flip & Match")
clock = pygame.time.Clock()
font_small = pygame.font.Font(None, 28)

SYMBOL_COLORS = [(255, 210, 110), (160, 210, 255), (255, 150, 175), (140, 230, 170), (200, 170, 255), (255, 185, 120)]

pick_phase = "idle"
first_pick: dict | None = None
wait_timer = 0.0


def build_deck(cols: int, rows: int) -> list[int]:
    pair_count = (cols * rows) // 2
    deck = list(range(pair_count)) * 2
    random.shuffle(deck)
    return deck


def make_cards(cols: int, rows: int) -> list[dict]:
    deck = build_deck(cols, rows)
    cards: list[dict] = []
    i = 0
    for row in range(rows):
        for col in range(cols):
            cards.append({"col": col, "row": row, "symbol": deck[i], "face_up": False, "matched": False})
            i += 1
    return cards


def card_rect(card: dict) -> pygame.Rect:
    x = BOARD_X + card["col"] * CELL
    y = BOARD_Y + card["row"] * CELL
    return pygame.Rect(x + GAP // 2, y + GAP // 2, CELL - GAP, CELL - GAP)


def mouse_to_card(pos: tuple[int, int], cards: list[dict]) -> dict | None:
    for card in reversed(cards):
        if card_rect(card).collidepoint(pos):
            return card
    return None


def draw_card_back(surface: pygame.Surface, rect: pygame.Rect) -> None:
    pygame.draw.rect(surface, (38, 32, 68), rect, border_radius=12)
    q = font_small.render("?", True, (200, 180, 255))
    surface.blit(q, q.get_rect(center=rect.center))


def draw_symbol(surface: pygame.Surface, rect: pygame.Rect, symbol_id: int) -> None:
    color = SYMBOL_COLORS[symbol_id % len(SYMBOL_COLORS)]
    pygame.draw.rect(surface, color, rect.inflate(-8, -8), border_radius=10)


def draw_card(surface: pygame.Surface, card: dict) -> None:
    rect = card_rect(card)
    if card["face_up"] or card["matched"]:
        draw_symbol(surface, rect, card["symbol"])
    else:
        draw_card_back(surface, rect)


def handle_pick(card: dict) -> None:
    """TODO: state machine idle → first → waiting; flip faces; keep matched open."""
    pass


def update_wait(cards: list[dict], dt: float) -> None:
    """TODO: count down wait_timer; flip both back if no match (no time.sleep!)."""
    pass


cards = make_cards(COLS, ROWS)
running = True

while running:
    dt = clock.tick(60) / 1000
    update_wait(cards, dt)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            picked = mouse_to_card(event.pos, cards)
            if picked:
                handle_pick(picked)

    screen.fill((12, 10, 26))
    for card in cards:
        draw_card(screen, card)
    hud = font_small.render("Twin Cards — wire handle_pick + update_wait", True, (200, 185, 255))
    screen.blit(hud, (BOARD_X, 24))
    pygame.display.flip()

pygame.quit()