# game.py — Lesson 5.13: Mine Whisper — mines (starter)
import random

import pygame

pygame.init()

WIDTH = 580
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mine Whisper — Hidden Mines")

clock = pygame.time.Clock()
running = True
font_small = pygame.font.Font(None, 28)
font_num = pygame.font.Font(None, 26)

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
        [{"mine": False, "revealed": False, "neighbors": 0} for _ in range(COLS)]
        for _ in range(ROWS)
    ]


def in_bounds(col: int, row: int) -> bool:
    return 0 <= col < COLS and 0 <= row < ROWS


def count_neighbor_mines(board: list[list[dict]], col: int, row: int) -> int:
    """TODO: count mine=True neighbors in the 8 directions."""
    return 0


def place_mines(board: list[list[dict]], safe_col: int, safe_row: int) -> None:
    """TODO: shuffle random cells (skip safe_col, safe_row); set mine=True; fill neighbors."""
    pass


def mouse_to_cell(pos: tuple[int, int]) -> tuple[int, int] | None:
    """TODO: return (col, row) from a click."""
    return None


def reveal_at(board: list[list[dict]], col: int, row: int) -> bool:
    """TODO: set revealed=True; return True if this cell was a mine."""
    return False


def draw_board(surface: pygame.Surface) -> None:
    """TODO: hidden tiles vs revealed numbers (see solution)."""
    pass


grid = make_board()

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # TODO: first click → place_mines; then reveal_at
            pass

    screen.fill((10, 8, 22))
    draw_board(screen)
    hud = font_small.render("Finish mine TODOs!", True, (200, 185, 240))
    screen.blit(hud, (BOARD_X, 16))
    pygame.display.flip()

pygame.quit()