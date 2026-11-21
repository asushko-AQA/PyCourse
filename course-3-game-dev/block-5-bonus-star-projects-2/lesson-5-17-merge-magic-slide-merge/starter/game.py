# game.py — Lesson 5.17: Merge Magic — slide & merge (starter)
from __future__ import annotations

import random

import pygame

pygame.init()

WIDTH = 520
HEIGHT = 580
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Merge Magic — Slide & Merge")

clock = pygame.time.Clock()
running = True
font_small = pygame.font.Font(None, 28)
font_rune = pygame.font.Font(None, 36)

SIZE = 4
CELL = 100
GAP = 8
BOARD_X = 60
BOARD_Y = 80

board: list[list[int]] = [[0] * SIZE for _ in range(SIZE)]
score = 0

RUNE_COLORS: dict[int, tuple[int, int, int]] = {
    0: (35, 28, 52),
    2: (75, 65, 115),
    4: (95, 80, 145),
    8: (130, 95, 175),
    16: (165, 110, 200),
}


def compress(row: list[int]) -> list[int]:
    """TODO: slide non-zero values to the left, pad with zeros."""
    return row


def merge_row(row: list[int]) -> tuple[list[int], int]:
    """TODO: compress, merge equal neighbors once each, compress again."""
    return row, 0


def move_left(b: list[list[int]]) -> tuple[list[list[int]], int, bool]:
    """TODO: merge_row on every row; return new board, score gain, changed flag."""
    return b, 0, False


def reverse_rows(b: list[list[int]]) -> list[list[int]]:
    return [list(reversed(row)) for row in b]


def transpose(b: list[list[int]]) -> list[list[int]]:
    return [[b[r][c] for r in range(SIZE)] for c in range(SIZE)]


def move_right(b: list[list[int]]) -> tuple[list[list[int]], int, bool]:
    """TODO: reverse → move_left → reverse."""
    return b, 0, False


def move_up(b: list[list[int]]) -> tuple[list[list[int]], int, bool]:
    """TODO: transpose → move_left → transpose."""
    return b, 0, False


def move_down(b: list[list[int]]) -> tuple[list[list[int]], int, bool]:
    """TODO: transpose → reverse → move_left → reverse → transpose."""
    return b, 0, False


def try_move(direction: str) -> None:
    """TODO: if board changed, update score and spawn_rune()."""
    pass


def spawn_rune() -> bool:
    spots = [(c, r) for r in range(SIZE) for c in range(SIZE) if board[r][c] == 0]
    if not spots:
        return False
    c, r = random.choice(spots)
    board[r][c] = 2 if random.random() < 0.9 else 4
    return True


def draw_rune_tile(surface: pygame.Surface, x: int, y: int, value: int) -> None:
    color = RUNE_COLORS.get(value, (200, 200, 200))
    inner = pygame.Rect(x + GAP // 2, y + GAP // 2, CELL - GAP, CELL - GAP)
    pygame.draw.rect(surface, color, inner, border_radius=10)
    if value:
        label = font_rune.render(str(value), True, (255, 255, 255))
        surface.blit(label, label.get_rect(center=(x + CELL // 2, y + CELL // 2)))


def draw_board(surface: pygame.Surface) -> None:
    for row in range(SIZE):
        for col in range(SIZE):
            x = BOARD_X + col * CELL
            y = BOARD_Y + row * CELL
            draw_rune_tile(surface, x, y, board[row][col])


spawn_rune()
spawn_rune()

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            try_move("left")

    screen.fill((12, 9, 22))
    draw_board(screen)
    hud = font_small.render("Finish merge_row TODOs!", True, (200, 185, 255))
    screen.blit(hud, (BOARD_X, 24))
    pygame.display.flip()

pygame.quit()