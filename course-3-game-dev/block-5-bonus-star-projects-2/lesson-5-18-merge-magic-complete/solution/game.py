# game.py — Lesson 5.18: Merge Magic — full rune forge (solution)
from __future__ import annotations

import copy
import random

import pygame

pygame.init()

WIDTH = 520
HEIGHT = 620
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Merge Magic")

clock = pygame.time.Clock()
running = True

font_big = pygame.font.Font(None, 52)
font_small = pygame.font.Font(None, 28)
font_rune = pygame.font.Font(None, 36)

SIZE = 4
CELL = 100
GAP = 8
BOARD_X = 60
BOARD_Y = 100
WIN_VALUE = 2048

START = "start"
PLAYING = "playing"
WON = "won"
OVER = "over"
state = START

board: list[list[int]] = [[0] * SIZE for _ in range(SIZE)]
display_board: list[list[int]] = [[0] * SIZE for _ in range(SIZE)]
score = 0
best_score = 0
undo_snapshot: tuple[list[list[int]], int] | None = None
won_acknowledged = False
anim_t = 0.0

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


def apply_move_dir(
    b: list[list[int]], direction: str
) -> tuple[list[list[int]], int, bool]:
    if direction == "left":
        return move_left(b)
    if direction == "right":
        flipped = reverse_rows(b)
        moved, pts, changed = move_left(flipped)
        return reverse_rows(moved), pts, changed
    if direction == "up":
        t = transpose(b)
        moved, pts, changed = move_left(t)
        return transpose(moved), pts, changed
    t = transpose(b)
    flipped = reverse_rows(t)
    moved, pts, changed = move_left(flipped)
    back = reverse_rows(moved)
    return transpose(back), pts, changed


def empty_cells(b: list[list[int]]) -> list[tuple[int, int]]:
    return [(c, r) for r in range(SIZE) for c in range(SIZE) if b[r][c] == 0]


def spawn_rune(b: list[list[int]]) -> None:
    spots = empty_cells(b)
    if not spots:
        return
    c, r = random.choice(spots)
    b[r][c] = 2 if random.random() < 0.9 else 4


def can_move(b: list[list[int]]) -> bool:
    for direction in ("left", "right", "up", "down"):
        _, _, changed = apply_move_dir(b, direction)
        if changed:
            return True
    return False


def has_win_tile(b: list[list[int]]) -> bool:
    return any(b[r][c] >= WIN_VALUE for r in range(SIZE) for c in range(SIZE))


def draw_rune_tile(surface: pygame.Surface, x: int, y: int, value: int) -> None:
    color = RUNE_COLORS.get(value, (255, 255, 255))
    inner = pygame.Rect(x + GAP // 2, y + GAP // 2, CELL - GAP, CELL - GAP)
    pygame.draw.rect(surface, color, inner, border_radius=10)
    pygame.draw.rect(surface, (160, 140, 220), inner, width=2, border_radius=10)
    if value:
        text_col = (25, 18, 40) if value <= 4 else (255, 255, 255)
        label = font_rune.render(str(value), True, text_col)
        surface.blit(label, label.get_rect(center=(x + CELL // 2, y + CELL // 2)))


def draw_board(surface: pygame.Surface, b: list[list[int]]) -> None:
    frame = pygame.Rect(BOARD_X - 8, BOARD_Y - 8, SIZE * CELL + 16, SIZE * CELL + 16)
    pygame.draw.rect(surface, (22, 16, 38), frame, border_radius=12)
    for row in range(SIZE):
        for col in range(SIZE):
            x = BOARD_X + col * CELL
            y = BOARD_Y + row * CELL
            draw_rune_tile(surface, x, y, b[row][col])


def new_game() -> None:
    global board, display_board, score, state, undo_snapshot, won_acknowledged, anim_t
    board = [[0] * SIZE for _ in range(SIZE)]
    display_board = copy.deepcopy(board)
    score = 0
    undo_snapshot = None
    won_acknowledged = False
    anim_t = 0.0
    spawn_rune(board)
    spawn_rune(board)
    state = PLAYING


def start_play() -> None:
    global state
    if state == START:
        new_game()


def try_move(direction: str) -> None:
    global board, display_board, score, best_score, state, undo_snapshot, won_acknowledged, anim_t
    if state not in (PLAYING, WON):
        return
    new, pts, changed = apply_move_dir(board, direction)
    if not changed:
        return
    undo_snapshot = (copy.deepcopy(board), score)
    board = new
    score += pts
    if score > best_score:
        best_score = score
    spawn_rune(board)
    display_board = copy.deepcopy(board)
    anim_t = 0.12
    if has_win_tile(board) and not won_acknowledged:
        state = WON
    elif not can_move(board) and not empty_cells(board):
        state = OVER


def undo_once() -> None:
    global board, display_board, score, state, undo_snapshot
    if undo_snapshot is None or state == OVER:
        return
    prev_board, prev_score = undo_snapshot
    board = copy.deepcopy(prev_board)
    display_board = copy.deepcopy(board)
    score = prev_score
    undo_snapshot = None
    if state == WON and not has_win_tile(board):
        state = PLAYING


new_game()
state = START

while running:
    dt = clock.tick(60) / 1000
    anim_t = max(0.0, anim_t - dt)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and state == START:
                start_play()
            if event.key == pygame.K_SPACE and state in (OVER, WON):
                new_game()
            if event.key == pygame.K_c and state == WON:
                won_acknowledged = True
                state = PLAYING
            if event.key == pygame.K_u:
                undo_once()
            if event.key in (pygame.K_LEFT, pygame.K_a):
                try_move("left")
            if event.key in (pygame.K_RIGHT, pygame.K_d):
                try_move("right")
            if event.key in (pygame.K_UP, pygame.K_w):
                try_move("up")
            if event.key in (pygame.K_DOWN, pygame.K_s):
                try_move("down")

    screen.fill((12, 9, 22))

    if state == START:
        title = font_big.render("Merge Magic", True, (230, 210, 255))
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50)))
        sub = font_small.render("SPACE — begin the rune forge", True, (170, 160, 220))
        screen.blit(sub, sub.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10)))
    else:
        draw_board(screen, display_board)
        if anim_t > 0:
            glow = pygame.Rect(BOARD_X - 4, BOARD_Y - 4, SIZE * CELL + 8, SIZE * CELL + 8)
            pygame.draw.rect(screen, (120, 80, 180), glow, width=2, border_radius=14)
        hud = font_small.render(f"Score: {score}   Best: {best_score}", True, (160, 255, 210))
        screen.blit(hud, (BOARD_X, 56))
        hint = font_small.render("Arrows move · U undo · C continue after 2048", True, (150, 140, 200))
        screen.blit(hint, (BOARD_X, BOARD_Y + SIZE * CELL + 24))
        if state == WON:
            banner = font_small.render("Rune 2048 forged! C continue · SPACE restart", True, (255, 220, 140))
            screen.blit(banner, (BOARD_X, BOARD_Y + SIZE * CELL + 48))
        if state == OVER:
            banner = font_small.render("No moves left — SPACE to restart", True, (255, 130, 130))
            screen.blit(banner, (BOARD_X, BOARD_Y + SIZE * CELL + 48))

    pygame.display.flip()

pygame.quit()