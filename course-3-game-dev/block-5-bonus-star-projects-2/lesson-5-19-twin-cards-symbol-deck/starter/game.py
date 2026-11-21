# game.py — Lesson 5.19: Twin Cards — symbol deck (starter)
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
]


def build_deck(cols: int, rows: int) -> list[int]:
    """TODO: make pair_count symbols × 2, shuffle with random.shuffle, return list."""
    return [0] * (cols * rows)


def make_cards(cols: int, rows: int) -> list[dict]:
    """TODO: zip deck into card dicts with col, row, symbol, face_up=False, matched=False."""
    deck = build_deck(cols, rows)
    cards: list[dict] = []
    return cards


def card_rect(card: dict) -> pygame.Rect:
    x = BOARD_X + card["col"] * CELL
    y = BOARD_Y + card["row"] * CELL
    return pygame.Rect(x + GAP // 2, y + GAP // 2, CELL - GAP, CELL - GAP)


def draw_card_back(surface: pygame.Surface, rect: pygame.Rect) -> None:
    """TODO: rounded purple card back with little dots and a '?'."""
    pygame.draw.rect(surface, (50, 40, 80), rect, border_radius=12)


def draw_symbol(surface: pygame.Surface, rect: pygame.Rect, symbol_id: int) -> None:
    """TODO: tinted tile + one shape (star, circle, triangle, diamond, cross, ring)."""
    color = SYMBOL_COLORS[symbol_id % len(SYMBOL_COLORS)]
    pygame.draw.rect(surface, color, rect.inflate(-8, -8), border_radius=10)


def draw_card(surface: pygame.Surface, card: dict) -> None:
    rect = card_rect(card)
    if card.get("face_up"):
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

    screen.fill((12, 10, 26))
    for card in cards:
        draw_card(screen, card)
    hud = font_small.render("Twin Cards — finish TODOs, then press R", True, (200, 185, 255))
    screen.blit(hud, (BOARD_X, 24))
    pygame.display.flip()

pygame.quit()