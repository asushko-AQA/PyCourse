# game.py — Lesson 5.17: Merge Magic — slide & merge (solution)
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
    32: (200, 130, 210),
    64: (230, 150, 160),
    128: (255, 180, 120),
    256: (255, 210, 100),
    512: (255, 235, 130),
    1024: (255, 255, 200),
    2048: (255, 255, 255),
}


def compress(row: list[int]) -> list[int]:
    values = [v for v in row if v != 0]
    values.extend([0] * (SIZE - len(values)))
    return values


def merge_row(row: list[int]) -> tuple[list[int], int]:
  row = compress(row[:])
  gained = 0
  i = 0
  while i < SIZE - 1:
    if row[i] != 0 and row[i] == row[i + 1]:
      row[i] *= 2
      gained += row[i]
      row[i + 1] = 0
      i += 2
    else:
      i += 1
  return compress(row), gained


def move_left(b: list[list[int]]) -> tuple[list[list[int]], int, bool]:
    new: list[list[int]] = []
    total = 0
    changed = False
    for r in range(SIZE):
        merged, pts = merge_row(b[r])
        total += pts
        if merged != b[r]:
            changed = True
        new.append(merged)
    return new, total, changed


def reverse_rows(b: list[list[int]]) -> list[list[int]]:
    return [list(reversed(row)) for row in b]


def transpose(b: list[list[int]]) -> list[list[int]]:
    return [[b[r][c] for r in range(SIZE)] for c in range(SIZE)]


def move_right(b: list[list[int]]) -> tuple[list[list[int]], int, bool]:
    flipped = reverse_rows(b)
    moved, pts, changed = move_left(flipped)
    return reverse_rows(moved), pts, changed


def move_up(b: list[list[int]]) -> tuple[list[list[int]], int, bool]:
    t = transpose(b)
    moved, pts, changed = move_left(t)
    return transpose(moved), pts, changed


def move_down(b: list[list[int]]) -> tuple[list[list[int]], int, bool]:
    t = transpose(b)
    flipped = reverse_rows(t)
    moved, pts, changed = move_left(flipped)
    back = reverse_rows(moved)
    return transpose(back), pts, changed


def try_move(direction: str) -> None:
    global board, score
    if direction == "left":
        new, pts, changed = move_left(board)
    elif direction == "right":
        new, pts, changed = move_right(board)
    elif direction == "up":
        new, pts, changed = move_up(board)
    else:
        new, pts, changed = move_down(board)
    if not changed:
        return
    board = new
    score += pts
    spawn_rune()


def empty_cells() -> list[tuple[int, int]]:
    return [(c, r) for r in range(SIZE) for c in range(SIZE) if board[r][c] == 0]


def spawn_rune() -> bool:
    spots = empty_cells()
    if not spots:
        return False
    c, r = random.choice(spots)
    board[r][c] = 2 if random.random() < 0.9 else 4
    return True


def draw_rune_tile(surface: pygame.Surface, x: int, y: int, value: int) -> None:
    color = RUNE_COLORS.get(value, (255, 255, 255))
    inner = pygame.Rect(x + GAP // 2, y + GAP // 2, CELL - GAP, CELL - GAP)
    pygame.draw.rect(surface, color, inner, border_radius=10)
    pygame.draw.rect(surface, (160, 140, 220), inner, width=2, border_radius=10)
    if value:
        text_col = (25, 18, 40) if value <= 4 else (255, 255, 255)
        label = font_rune.render(str(value), True, text_col)
        surface.blit(label, label.get_rect(center=(x + CELL // 2, y + CELL // 2)))


def draw_board(surface: pygame.Surface) -> None:
    for row in range(SIZE):
        for col in range(SIZE):
            x = BOARD_X + col * CELL
            y = BOARD_Y + row * CELL
            draw_rune_tile(surface, x, y, board[row][col])


def fresh_board() -> None:
    global board, score
    board = [[0] * SIZE for _ in range(SIZE)]
    score = 0
    spawn_rune()
    spawn_rune()


fresh_board()

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_a):
                try_move("left")
            if event.key in (pygame.K_RIGHT, pygame.K_d):
                try_move("right")
            if event.key in (pygame.K_UP, pygame.K_w):
                try_move("up")
            if event.key in (pygame.K_DOWN, pygame.K_s):
                try_move("down")
            if event.key == pygame.K_r:
                fresh_board()

    screen.fill((12, 9, 22))
    draw_board(screen)
    title = font_small.render("Merge Magic — arrow keys slide runes", True, (210, 195, 255))
    screen.blit(title, (BOARD_X, 24))
    score_s = font_small.render(f"Score: {score}", True, (160, 255, 210))
    screen.blit(score_s, (BOARD_X + 260, 24))
    pygame.display.flip()

pygame.quit()