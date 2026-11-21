# game.py — Lesson 5.16: Merge Magic — rune board (starter)
from __future__ import annotations

import random

import pygame

pygame.init()

WIDTH = 520
HEIGHT = 580
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Merge Magic — Rune Lattice")

clock = pygame.time.Clock()
running = True
font_small = pygame.font.Font(None, 28)
font_rune = pygame.font.Font(None, 36)

SIZE = 4
CELL = 100
GAP = 8
BOARD_X = 60
BOARD_Y = 80

# TODO: 4×4 list of ints — 0 means empty
board: list[list[int]] = [[0] * SIZE for _ in range(SIZE)]

RUNE_COLORS: dict[int, tuple[int, int, int]] = {
    0: (35, 28, 52),
    2: (75, 65, 115),
    4: (95, 80, 145),
    8: (130, 95, 175),
    16: (165, 110, 200),
}


def empty_cells() -> list[tuple[int, int]]:
    """TODO: return (col, row) for every cell where board[row][col] == 0."""
    return []


def spawn_rune() -> bool:
    """TODO: pick random empty cell; place 2 (90%) or 4 (10%)."""
    return False


def draw_rune_tile(surface: pygame.Surface, x: int, y: int, value: int) -> None:
    """TODO: rounded rect from RUNE_COLORS; draw value if not zero."""
    pass


def draw_board(surface: pygame.Surface) -> None:
    """TODO: loop all cells and call draw_rune_tile."""
    pass


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            # TODO: call spawn_rune after you implement it
            pass

    screen.fill((12, 9, 22))
    if board:
        draw_board(screen)
    hud = font_small.render("Finish the rune board TODOs!", True, (200, 185, 255))
    screen.blit(hud, (BOARD_X, 24))
    pygame.display.flip()

pygame.quit()