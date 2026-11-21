# game.py — Lesson 5.13: Mine Whisper — mines & numbers (solution)
from __future__ import annotations

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

NUMBER_COLORS = [
    (0, 0, 0),
    (80, 140, 255),
    (90, 220, 150),
    (255, 120, 140),
    (160, 100, 220),
    (255, 180, 90),
    (120, 230, 230),
    (200, 200, 200),
    (255, 255, 255),
]

grid: list[list[dict[str, int | bool]]] = []
mines_placed = False
lost = False


def make_board() -> list[list[dict[str, int | bool]]]:
    return [
        [{"mine": False, "revealed": False, "flagged": False, "neighbors": 0} for _ in range(COLS)]
        for _ in range(ROWS)
    ]


def in_bounds(col: int, row: int) -> bool:
    return 0 <= col < COLS and 0 <= row < ROWS


def count_neighbor_mines(board: list[list[dict]], col: int, row: int) -> int:
    total = 0
    for dc in (-1, 0, 1):
        for dr in (-1, 0, 1):
            if dc == 0 and dr == 0:
                continue
            nc, nr = col + dc, row + dr
            if in_bounds(nc, nr) and board[nr][nc]["mine"]:
                total += 1
    return total


def safe_zone(col: int, row: int) -> set[tuple[int, int]]:
    zone = {(col, row)}
    for dc in (-1, 0, 1):
        for dr in (-1, 0, 1):
            nc, nr = col + dc, row + dr
            if in_bounds(nc, nr):
                zone.add((nc, nr))
    return zone


def place_mines(board: list[list[dict]], safe_col: int, safe_row: int) -> None:
    forbidden = safe_zone(safe_col, safe_row)
    spots = [(c, r) for r in range(ROWS) for c in range(COLS) if (c, r) not in forbidden]
    random.shuffle(spots)
    for c, r in spots[:MINE_COUNT]:
        board[r][c]["mine"] = True
    for r in range(ROWS):
        for c in range(COLS):
            board[r][c]["neighbors"] = count_neighbor_mines(board, c, r)


def mouse_to_cell(pos: tuple[int, int]) -> tuple[int, int] | None:
    mx, my = pos
    if mx < BOARD_X or my < BOARD_Y:
        return None
    col = (mx - BOARD_X) // CELL
    row = (my - BOARD_Y) // CELL
    if not in_bounds(col, row):
        return None
    return col, row


def reveal_at(board: list[list[dict]], col: int, row: int) -> bool:
    cell = board[row][col]
    if cell["revealed"] or cell["flagged"]:
        return False
    cell["revealed"] = True
    return bool(cell["mine"])


def draw_board(surface: pygame.Surface) -> None:
    for row in range(ROWS):
        for col in range(COLS):
            x = BOARD_X + col * CELL
            y = BOARD_Y + row * CELL
            cell = grid[row][col]
            rect = pygame.Rect(x + 2, y + 2, CELL - 4, CELL - 4)
            if not cell["revealed"]:
                pygame.draw.rect(surface, (46, 38, 72), rect, border_radius=6)
                pygame.draw.rect(surface, (88, 70, 128), rect, width=2, border_radius=6)
            else:
                pygame.draw.rect(surface, (30, 26, 44), rect, border_radius=4)
                if cell["mine"]:
                    cx, cy = x + CELL // 2, y + CELL // 2
                    pts = [(cx, cy - 10), (cx + 9, cy), (cx, cy + 10), (cx - 9, cy)]
                    pygame.draw.polygon(surface, (240, 80, 100), pts)
                elif cell["neighbors"]:
                    n = int(cell["neighbors"])
                    txt = font_num.render(str(n), True, NUMBER_COLORS[n])
                    surface.blit(txt, (x + CELL // 2 - 6, y + CELL // 2 - 10))


grid = make_board()

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not lost:
            picked = mouse_to_cell(event.pos)
            if not picked:
                continue
            col, row = picked
            if not mines_placed:
                place_mines(grid, col, row)
                mines_placed = True
            if reveal_at(grid, col, row):
                lost = True

    screen.fill((10, 8, 22))
    draw_board(screen)
    status = "Boom!" if lost else "First click is always safe — reveal numbers"
    hud = font_small.render(status, True, (200, 185, 240))
    screen.blit(hud, (BOARD_X, 16))
    pygame.display.flip()

pygame.quit()