# game.py — Lesson 5.23: Tic-Tac-Bot — win & score (starter)
from __future__ import annotations

import pygame

pygame.init()

WIDTH, HEIGHT = 520, 640
GRID_SIZE = 3
CELL = 120
GAP = 14
BOARD_X = (WIDTH - GRID_SIZE * CELL) // 2
BOARD_Y = 165

# TODO: fill WIN_LINES with the 8 winning triples of indices 0–8
WIN_LINES: list[tuple[int, int, int]] = []

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Bot — Circuit Win")
clock = pygame.time.Clock()
font_big = pygame.font.Font(None, 44)
font_small = pygame.font.Font(None, 28)

board: list[str | None] = [None] * 9
current = "X"
state = "PLAYING"
win_line: tuple[int, int, int] | None = None
scores = {"X": 0, "O": 0, "draws": 0}


def cell_rect(index: int) -> pygame.Rect:
    row, col = divmod(index, GRID_SIZE)
    x = BOARD_X + col * CELL
    y = BOARD_Y + row * CELL
    return pygame.Rect(x + GAP // 2, y + GAP // 2, CELL - GAP, CELL - GAP)


def mouse_to_cell(pos: tuple[int, int]) -> int | None:
    for idx in range(9):
        if cell_rect(idx).collidepoint(pos):
            return idx
    return None


def find_winner() -> tuple[str | None, tuple[int, int, int] | None]:
    """TODO: loop WIN_LINES; return (mark, line) or (None, None)."""
    return None, None


def board_full() -> bool:
    return all(cell is not None for cell in board)


def reset_round() -> None:
    global board, current, state, win_line
    board = [None] * 9
    current = "X"
    state = "PLAYING"
    win_line = None


def apply_move(idx: int) -> None:
    """TODO: place mark, detect win/draw, bump scores, swap turn."""
    pass


def draw_grid(surface: pygame.Surface) -> None:
    for idx in range(9):
        rect = cell_rect(idx)
        fill = (28, 36, 58)
        if win_line and idx in win_line:
            fill = (55, 70, 120)
        pygame.draw.rect(surface, fill, rect, border_radius=14)
        pygame.draw.rect(surface, (90, 140, 220), rect, width=2, border_radius=14)


def draw_x(surface: pygame.Surface, rect: pygame.Rect) -> None:
    inner = rect.inflate(-28, -28)
    pygame.draw.line(surface, (255, 210, 90), inner.topleft, inner.bottomright, 8)
    pygame.draw.line(surface, (255, 210, 90), inner.topright, inner.bottomleft, 8)


def draw_o(surface: pygame.Surface, rect: pygame.Rect) -> None:
    pygame.draw.circle(
        surface, (120, 220, 255), rect.center, rect.width // 2 - 18, width=8
    )
    pygame.draw.circle(surface, (60, 120, 180), rect.center, 10)


def draw_mark(surface: pygame.Surface, idx: int) -> None:
    mark = board[idx]
    if mark == "X":
        draw_x(surface, cell_rect(idx))
    elif mark == "O":
        draw_o(surface, cell_rect(idx))


def draw_win_line(surface: pygame.Surface) -> None:
    """TODO: draw a pink line across the three winning cell centers."""
    pass


running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset_round()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            idx = mouse_to_cell(event.pos)
            if idx is not None:
                apply_move(idx)

    screen.fill((16, 20, 34))
    title = font_big.render("Tic-Tac-Bot — Score", True, (230, 240, 255))
    screen.blit(title, title.get_rect(midtop=(WIDTH // 2, 18)))
    hud = font_small.render(
        f"X {scores['X']}  ·  O {scores['O']}  ·  draws {scores['draws']}",
        True,
        (170, 190, 230),
    )
    screen.blit(hud, hud.get_rect(midtop=(WIDTH // 2, 62)))
    status = font_small.render("TODO: show turn / win / draw", True, (200, 215, 255))
    screen.blit(status, status.get_rect(midtop=(WIDTH // 2, 98)))
    draw_grid(screen)
    draw_win_line(screen)
    for i in range(9):
        draw_mark(screen, i)

    pygame.display.flip()

pygame.quit()