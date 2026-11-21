# game.py — Lesson 5.19: Twin Cards — symbol deck (solution)
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

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Twin Cards — Cosmic Deck")
clock = pygame.time.Clock()
font_small = pygame.font.Font(None, 28)

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
            cards.append(
                {
                    "col": col,
                    "row": row,
                    "symbol": deck[i],
                    "face_up": False,
                    "matched": False,
                }
            )
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
    pygame.draw.rect(surface, (120, 100, 190), rect, width=2, border_radius=12)
    cx, cy = rect.center
    for dx, dy in ((-14, -14), (14, -14), (14, 14), (-14, 14)):
        pygame.draw.circle(surface, (90, 75, 140), (cx + dx, cy + dy), 6)
    q = font_small.render("?", True, (200, 180, 255))
    surface.blit(q, q.get_rect(center=rect.center))


def draw_symbol(surface: pygame.Surface, rect: pygame.Rect, symbol_id: int) -> None:
    color = SYMBOL_COLORS[symbol_id % len(SYMBOL_COLORS)]
    pygame.draw.rect(surface, (32, 26, 52), rect, border_radius=12)
    pygame.draw.rect(surface, color, rect.inflate(-10, -10), border_radius=10)
    cx, cy = rect.center
    shape = symbol_id % 6
    if shape == 0:
        pts = [(cx, cy - 22), (cx + 20, cy + 14), (cx - 20, cy + 14)]
        pygame.draw.polygon(surface, (255, 255, 255), pts)
    elif shape == 1:
        pygame.draw.circle(surface, (255, 255, 255), (cx, cy), 22, width=4)
        pygame.draw.circle(surface, color, (cx + 10, cy - 8), 8)
    elif shape == 2:
        pts = [(cx, cy - 24), (cx + 22, cy + 18), (cx - 22, cy + 18)]
        pygame.draw.polygon(surface, (255, 255, 255), pts)
    elif shape == 3:
        pts = [(cx, cy - 20), (cx + 16, cy), (cx, cy + 20), (cx - 16, cy)]
        pygame.draw.polygon(surface, (255, 255, 255), pts)
    elif shape == 4:
        pygame.draw.line(surface, (255, 255, 255), (cx - 18, cy), (cx + 18, cy), 5)
        pygame.draw.line(surface, (255, 255, 255), (cx, cy - 18), (cx, cy + 18), 5)
    else:
        pygame.draw.circle(surface, (255, 255, 255), (cx, cy), 18, width=4)


def draw_card(surface: pygame.Surface, card: dict) -> None:
    rect = card_rect(card)
    if card["face_up"] or card["matched"]:
        draw_symbol(surface, rect, card["symbol"])
    else:
        draw_card_back(surface, rect)


cards = make_cards(COLS, ROWS)
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            cards = make_cards(COLS, ROWS)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            picked = mouse_to_card(event.pos, cards)
            if picked:
                picked["face_up"] = not picked["face_up"]

    screen.fill((12, 10, 26))
    frame = pygame.Rect(
        BOARD_X - 12,
        BOARD_Y - 12,
        COLS * CELL + 24,
        ROWS * CELL + 24,
    )
    pygame.draw.rect(screen, (22, 18, 40), frame, border_radius=14)
    for card in cards:
        draw_card(screen, card)
    hud = font_small.render("Twin Cards — click to peek, R = reshuffle", True, (200, 185, 255))
    screen.blit(hud, (BOARD_X, 24))
    pygame.display.flip()

pygame.quit()