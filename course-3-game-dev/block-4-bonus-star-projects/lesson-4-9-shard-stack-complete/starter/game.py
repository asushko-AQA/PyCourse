# game.py — Lesson 4.9: Shard Stack — complete (starter)
import random

import pygame

pygame.init()

WIDTH = 520
HEIGHT = 560
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shard Stack")

clock = pygame.time.Clock()
running = True

font_big = pygame.font.Font(None, 56)
font_small = pygame.font.Font(None, 28)

COLS = 10
ROWS = 20
CELL = 24
BOARD_X = 28
BOARD_Y = 36

START = "start"
PLAYING = "playing"
GAME_OVER = "game_over"
state = START  # TODO: wire like Lessons 2.4 and 4.3

SHAPES = {
    "T": [(0, 1), (1, 0), (1, 1), (1, 2)],
    "I": [(0, 0), (0, 1), (0, 2), (0, 3)],
    "O": [(0, 0), (0, 1), (1, 0), (1, 1)],
}
COLORS = {"T": (180, 120, 255), "I": (90, 220, 255), "O": (255, 210, 90)}

BASE_FALL = 0.55
score = 0
level = 1
lines_cleared = 0
high_score = 0
fall_timer = 0.0

grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

piece_name = "T"
piece_row = 0
piece_col = 3
piece_cells = list(SHAPES["T"])
next_name = "I"


def fall_interval() -> float:
    return max(0.12, BASE_FALL - (level - 1) * 0.045)


def can_move(cells, anchor_r, anchor_c):
  # TODO: copy from lesson 4.8 — walls + locked cells
    return False


def clear_lines() -> int:
    """TODO: remove full rows, slide rows down, return count cleared."""
    return 0


def lock_piece() -> None:
    """TODO: write colors into grid, clear_lines(), update score, spawn_piece()."""
    pass


def spawn_piece() -> None:
    """TODO: copy next shape, pick new random next_name, game over if blocked."""
    pass


def try_rotate() -> None:
    """TODO: rotate offsets (col, -row); wall-kick ±1 if needed."""
    pass


def draw_cell(surface, row, col, color):
    x = BOARD_X + col * CELL
    y = BOARD_Y + row * CELL
    rect = pygame.Rect(x, y, CELL - 1, CELL - 1)
    pygame.draw.rect(surface, color, rect, border_radius=4)


def draw_grid(surface):
    for row in range(ROWS):
        for col in range(COLS):
            x = BOARD_X + col * CELL
            y = BOARD_Y + row * CELL
            pygame.draw.rect(surface, (32, 36, 52), (x, y, CELL - 1, CELL - 1))
            if grid[row][col]:
                draw_cell(surface, row, col, grid[row][col])


def draw_piece(surface):
    color = COLORS[piece_name]
    for dr, dc in piece_cells:
        draw_cell(surface, piece_row + dr, piece_col + dc, color)


def draw_preview(surface):
    """TODO: draw next_name mini panel on the right."""
    pass


def try_move(dr, dc):
    global piece_row, piece_col
    if can_move(piece_cells, piece_row + dr, piece_col + dc):
        piece_row += dr
        piece_col += dc
        return True
    return False


def soft_drop_step():
    if not try_move(1, 0):
        lock_piece()


def start_game():
    global grid, score, level, lines_cleared, fall_timer, state, next_name
    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    score = 0
    level = 1
    lines_cleared = 0
    fall_timer = 0.0
    state = PLAYING
    next_name = random.choice(list(SHAPES.keys()))
    spawn_piece()


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if state == START and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                start_game()
            elif state == PLAYING:
                if event.key == pygame.K_LEFT:
                    try_move(0, -1)
                elif event.key == pygame.K_RIGHT:
                    try_move(0, 1)
                elif event.key == pygame.K_DOWN:
                    soft_drop_step()
                elif event.key in (pygame.K_UP, pygame.K_x):
                    try_rotate()
            elif state == GAME_OVER and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                state = START

    screen.fill((18, 20, 32))

    if state == START:
        draw_grid(screen)
        title = font_big.render("Shard Stack", True, (200, 240, 255))
        hint = font_small.render("SPACE to play — finish TODOs first!", True, (160, 150, 200))
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30)))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))

    elif state == PLAYING:
        # TODO: fall_timer tick + soft_drop_step
        draw_grid(screen)
        draw_piece(screen)
        draw_preview(screen)
        hud = font_small.render(f"Score: {score}  Level: {level}", True, (230, 225, 255))
        screen.blit(hud, (BOARD_X, BOARD_Y + ROWS * CELL + 16))

    elif state == GAME_OVER:
        # TODO: update high_score when score beats it
        draw_grid(screen)
        over = font_big.render("Grid Full!", True, (255, 130, 150))
        screen.blit(over, over.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

    pygame.display.flip()

pygame.quit()