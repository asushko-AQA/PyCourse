# game.py — Lesson 5.22: Tic-Tac-Bot — grid (starter)
from __future__ import annotations

import pygame

pygame.init()

WIDTH, HEIGHT = 520, 620
GRID_SIZE = 3
CELL = 120
GAP = 14
BOARD_X = (WIDTH - GRID_SIZE * CELL) // 2
BOARD_Y = 150

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Bot — Robot Grid")
clock = pygame.time.Clock()
font_big = pygame.font.Font(None, 46)
font_small = pygame.font.Font(None, 30)

# TODO: list of 9 cells — None means empty, "X" or "O" for marks
board: list[str | None] = [None] * 9
current = "X"


def cell_rect(index: int) -> pygame.Rect:
    """TODO: index 0–8 → pygame.Rect for that grid cell."""
    row, col = divmod(index, GRID_SIZE)
    x = BOARD_X + col * CELL
    y = BOARD_Y + row * CELL
    return pygame.Rect(x + GAP // 2, y + GAP // 2, CELL - GAP, CELL - GAP)


def mouse_to_cell(pos: tuple[int, int]) -> int | None:
    """TODO: return cell index if click hits a cell, else None."""
    return None


def draw_grid(surface: pygame.Surface) -> None:
    """TODO: draw 9 rounded blue-tinted cells."""
    pass


def draw_x(surface: pygame.Surface, rect: pygame.Rect) -> None:
    """TODO: golden bolt X with two thick lines."""
    pass


def draw_o(surface: pygame.Surface, rect: pygame.Rect) -> None:
    """TODO: cyan gear ring (circle) with a small hub dot."""
    pass


def draw_mark(surface: pygame.Surface, idx: int) -> None:
    mark = board[idx]
    if mark == "X":
        draw_x(surface, cell_rect(idx))
    elif mark == "O":
        draw_o(surface, cell_rect(idx))


def reset_board() -> None:
    global board, current
    board = [None] * 9
    current = "X"


running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset_board()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            idx = mouse_to_cell(event.pos)
            # TODO: if empty, place current mark and swap player X ↔ O
            pass

    screen.fill((16, 20, 34))
    title = font_big.render("Tic-Tac-Bot — Grid", True, (230, 240, 255))
    screen.blit(title, title.get_rect(midtop=(WIDTH // 2, 24)))
    turn = font_small.render(
        f"Turn: {'Bolt X' if current == 'X' else 'Gear O'}  |  R reset",
        True,
        (180, 200, 240),
    )
    screen.blit(turn, turn.get_rect(midtop=(WIDTH // 2, 78)))
    draw_grid(screen)
    for i in range(9):
        draw_mark(screen, i)

    pygame.display.flip()

pygame.quit()