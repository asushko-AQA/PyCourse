# game.py — Lesson 5.14: Mine Whisper — flood & flags (starter)
import random

import pygame

pygame.init()

WIDTH = 580
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mine Whisper — Whisper Flood")

clock = pygame.time.Clock()
running = True
font_small = pygame.font.Font(None, 28)

COLS = 14
ROWS = 10
CELL = 32
BOARD_X = 48
BOARD_Y = 56
MINE_COUNT = 18

grid: list[list[dict]] = []
mines_placed = False


def make_board() -> list[list[dict]]:
    return [
        [
            {"mine": False, "revealed": False, "flagged": False, "neighbors": 0}
            for _ in range(COLS)
        ]
        for _ in range(ROWS)
    ]


def flood_reveal_stack(board: list[list[dict]], col: int, row: int) -> None:
    """TODO: use a stack list; pop cells; reveal zeros and push neighbors."""
    pass


def toggle_flag(board: list[list[dict]], col: int, row: int) -> None:
    """TODO: flip flagged when cell is hidden."""
    pass


grid = make_board()

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # TODO: button 1 reveal (+ flood), button 3 toggle_flag
            pass

    screen.fill((10, 8, 22))
    hud = font_small.render("Finish flood + flag TODOs!", True, (200, 185, 240))
    screen.blit(hud, (BOARD_X, 16))
    pygame.display.flip()

pygame.quit()