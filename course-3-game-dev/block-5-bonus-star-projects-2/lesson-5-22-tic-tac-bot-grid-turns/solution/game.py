# game.py — Lesson 5.22: Tic-Tac-Bot — grid & hot-seat turns (solution)
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

# 9 cells: None, "X" (player bolt), or "O" (gear ring)
board: list[str | None] = [None] * 9
current = "X"


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


def draw_grid(surface: pygame.Surface) -> None:
    for idx in range(9):
        rect = cell_rect(idx)
        pygame.draw.rect(surface, (28, 36, 58), rect, border_radius=14)
        pygame.draw.rect(surface, (90, 140, 220), rect, width=2, border_radius=14)


def draw_x(surface: pygame.Surface, rect: pygame.Rect) -> None:
    inner = rect.inflate(-28, -28)
    color = (255, 210, 90)
    pygame.draw.line(surface, color, inner.topleft, inner.bottomright, 8)
    pygame.draw.line(surface, color, inner.topright, inner.bottomleft, 8)


def draw_o(surface: pygame.Surface, rect: pygame.Rect) -> None:
    color = (120, 220, 255)
    pygame.draw.circle(surface, color, rect.center, rect.width // 2 - 18, width=8)
    pygame.draw.circle(surface, (60, 120, 180), rect.center, 10)


def draw_mark(surface: pygame.Surface, idx: int) -> None:
    rect = cell_rect(idx)
    mark = board[idx]
    if mark == "X":
        draw_x(surface, rect)
    elif mark == "O":
        draw_o(surface, rect)


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
            if idx is not None and board[idx] is None:
                board[idx] = current
                current = "O" if current == "X" else "X"

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