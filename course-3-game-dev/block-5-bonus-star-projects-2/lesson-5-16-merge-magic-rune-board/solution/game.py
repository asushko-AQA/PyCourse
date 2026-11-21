# game.py — Lesson 5.16: Merge Magic — rune board (solution)
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

# 0 = empty slot; other values are rune power numbers
board: list[list[int]] = [[0] * SIZE for _ in range(SIZE)]

RUNE_COLORS: dict[int, tuple[int, int, int]] = {
    0: (35, 28, 52),
    2: (75, 65, 115),
    4: (95, 80, 145),
    8: (130, 95, 175),
    16: (165, 110, 200),
    32: (200, 130, 210),
    64: (230, 150, 160),
    128: (255, 180, 120),
    256: (255, 210, 100),
    512: (255, 235, 130),
    1024: (255, 255, 200),
    2048: (255, 255, 255),
}


def empty_cells() -> list[tuple[int, int]]:
    spots: list[tuple[int, int]] = []
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == 0:
                spots.append((col, row))
    return spots


def spawn_rune() -> bool:
    """Place 2 (90%) or 4 (10%) in a random empty cell. Returns False if board full."""
    spots = empty_cells()
    if not spots:
        return False
    col, row = random.choice(spots)
    board[row][col] = 2 if random.random() < 0.9 else 4
    return True


def rune_text_color(value: int) -> tuple[int, int, int]:
    return (25, 18, 40) if value <= 4 else (255, 255, 255)


def draw_rune_tile(surface: pygame.Surface, x: int, y: int, value: int) -> None:
    color = RUNE_COLORS.get(value, (255, 255, 255))
    inner = pygame.Rect(x + GAP // 2, y + GAP // 2, CELL - GAP, CELL - GAP)
    pygame.draw.rect(surface, color, inner, border_radius=10)
    pygame.draw.rect(surface, (160, 140, 220), inner, width=2, border_radius=10)
    if value:
        # Tiny diamond “rune” accent
        cx, cy = x + CELL // 2, y + CELL // 2 - 8
        pts = [(cx, cy - 10), (cx + 8, cy), (cx, cy + 10), (cx - 8, cy)]
        pygame.draw.polygon(surface, (220, 210, 255), pts)
        label = font_rune.render(str(value), True, rune_text_color(value))
        surface.blit(label, label.get_rect(center=(x + CELL // 2, y + CELL // 2 + 8)))


def draw_board(surface: pygame.Surface) -> None:
    frame_w = SIZE * CELL + 16
    frame = pygame.Rect(BOARD_X - 8, BOARD_Y - 8, frame_w, frame_w)
    pygame.draw.rect(surface, (22, 16, 38), frame, border_radius=12)
    for row in range(SIZE):
        for col in range(SIZE):
            x = BOARD_X + col * CELL
            y = BOARD_Y + row * CELL
            draw_rune_tile(surface, x, y, board[row][col])


def fresh_board() -> None:
    global board
    board = [[0] * SIZE for _ in range(SIZE)]
    spawn_rune()
    spawn_rune()


fresh_board()

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                fresh_board()
            if event.key == pygame.K_s:
                spawn_rune()

    screen.fill((12, 9, 22))
    draw_board(screen)
    title = font_small.render("Merge Magic — rune lattice", True, (210, 195, 255))
    screen.blit(title, (BOARD_X, 24))
    hint = font_small.render("R = reset board   S = spawn rune", True, (150, 140, 200))
    screen.blit(hint, (BOARD_X, BOARD_Y + SIZE * CELL + 20))
    pygame.display.flip()

pygame.quit()