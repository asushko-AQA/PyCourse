# game.py — Lesson 4.9: Shard Stack — complete falling-block puzzle
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
state = START

# shape_name -> list of (row, col) offsets from anchor
SHAPES: dict[str, list[tuple[int, int]]] = {
    "I": [(0, 0), (0, 1), (0, 2), (0, 3)],
    "O": [(0, 0), (0, 1), (1, 0), (1, 1)],
    "T": [(0, 1), (1, 0), (1, 1), (1, 2)],
    "S": [(0, 1), (0, 2), (1, 0), (1, 1)],
    "Z": [(0, 0), (0, 1), (1, 1), (1, 2)],
    "J": [(0, 0), (1, 0), (1, 1), (1, 2)],
    "L": [(0, 2), (1, 0), (1, 1), (1, 2)],
}

COLORS: dict[str, tuple[int, int, int]] = {
    "I": (90, 220, 255),
    "O": (255, 210, 90),
    "T": (180, 120, 255),
    "S": (110, 230, 140),
    "Z": (255, 110, 120),
    "J": (100, 140, 255),
    "L": (255, 150, 80),
}

BASE_FALL = 0.55
score = 0
level = 1
lines_cleared = 0
high_score = 0
fall_timer = 0.0

# 0 = empty; else stores color tuple of locked shard
grid: list[list[tuple[int, int, int] | int]] = [
    [0 for _ in range(COLS)] for _ in range(ROWS)
]

piece_name = "T"
piece_row = 0
piece_col = 3
piece_cells: list[tuple[int, int]] = list(SHAPES["T"])
next_name = "I"


def fall_interval() -> float:
    return max(0.12, BASE_FALL - (level - 1) * 0.045)


def rotate_cells(cells: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Turn offsets 90° clockwise: (row, col) -> (col, -row)."""
    return [(c, -r) for r, c in cells]


def can_move(cells: list[tuple[int, int]], anchor_r: int, anchor_c: int) -> bool:
    for dr, dc in cells:
        r, c = anchor_r + dr, anchor_c + dc
        if c < 0 or c >= COLS or r >= ROWS:
            return False
        if r >= 0 and grid[r][c]:
            return False
    return True


def clear_lines() -> int:
    global grid
    cleared = 0
    kept: list[list[tuple[int, int, int] | int]] = []
    for row in grid:
        if all(row):
            cleared += 1
        else:
            kept.append(row)
    while len(kept) < ROWS:
        kept.insert(0, [0] * COLS)
    grid[:] = kept
    return cleared


def lock_piece() -> None:
    global score, level, lines_cleared
    color = COLORS[piece_name]
    for dr, dc in piece_cells:
        r, c = piece_row + dr, piece_col + dc
        if r >= 0:
            grid[r][c] = color
    cleared = clear_lines()
    if cleared:
        lines_cleared += cleared
        score += cleared * 100 * level
        level = lines_cleared // 10 + 1
    spawn_piece()


def spawn_piece() -> None:
    global piece_name, piece_row, piece_col, piece_cells, next_name, state
    piece_name = next_name
    piece_cells = list(SHAPES[piece_name])
    piece_row = 0
    piece_col = COLS // 2 - 2
    next_name = random.choice(list(SHAPES.keys()))
    if not can_move(piece_cells, piece_row, piece_col):
        state = GAME_OVER


def draw_cell(surface: pygame.Surface, r: int, c: int, color: tuple[int, int, int]) -> None:
    x = BOARD_X + c * CELL
    y = BOARD_Y + r * CELL
    rect = pygame.Rect(x, y, CELL - 1, CELL - 1)
    pygame.draw.rect(surface, color, rect, border_radius=4)
    pygame.draw.rect(surface, (30, 30, 45), rect, width=1, border_radius=4)


def draw_grid(surface: pygame.Surface) -> None:
    frame = pygame.Rect(BOARD_X - 4, BOARD_Y - 4, COLS * CELL + 8, ROWS * CELL + 8)
    pygame.draw.rect(surface, (50, 55, 80), frame, border_radius=6)
    for r in range(ROWS):
        for c in range(COLS):
            x = BOARD_X + c * CELL
            y = BOARD_Y + r * CELL
            pygame.draw.rect(surface, (32, 36, 52), (x, y, CELL - 1, CELL - 1))
            val = grid[r][c]
            if val:
                draw_cell(surface, r, c, val)  # type: ignore[arg-type]


def draw_piece(surface: pygame.Surface) -> None:
    color = COLORS[piece_name]
    for dr, dc in piece_cells:
        draw_cell(surface, piece_row + dr, piece_col + dc, color)


def draw_preview(surface: pygame.Surface) -> None:
    px, py = BOARD_X + COLS * CELL + 36, BOARD_Y + 12
    label = font_small.render("Next", True, (220, 210, 255))
    surface.blit(label, (px, py))
    color = COLORS[next_name]
    for dr, dc in SHAPES[next_name]:
        rect = pygame.Rect(px + dc * 20, py + 36 + dr * 20, 18, 18)
        pygame.draw.rect(surface, color, rect, border_radius=3)


def try_move(dr: int, dc: int) -> bool:
    global piece_row, piece_col
    if can_move(piece_cells, piece_row + dr, piece_col + dc):
        piece_row += dr
        piece_col += dc
        return True
    return False


def try_rotate() -> None:
    global piece_cells
    rotated = rotate_cells(piece_cells)
    if can_move(rotated, piece_row, piece_col):
        piece_cells = rotated
    elif can_move(rotated, piece_row, piece_col - 1):
        piece_cells = rotated
        try_move(0, -1)
    elif can_move(rotated, piece_row, piece_col + 1):
        piece_cells = rotated
        try_move(0, 1)


def soft_drop_step() -> None:
    if not try_move(1, 0):
        lock_piece()


def start_game() -> None:
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
        title = font_big.render("Shard Stack", True, (200, 240, 255))
        sub = font_small.render("Bonus ★ Project #3", True, (180, 170, 220))
        hint = font_small.render("SPACE to play", True, (160, 150, 200))
        best = font_small.render(f"Session best: {high_score}", True, (160, 150, 200))
        draw_grid(screen)
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 70)))
        screen.blit(sub, sub.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30)))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10)))
        screen.blit(best, best.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 45)))

    elif state == PLAYING:
        fall_timer += dt
        if fall_timer >= fall_interval():
            fall_timer = 0.0
            soft_drop_step()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            fall_timer += dt * 0.5

        draw_grid(screen)
        draw_piece(screen)
        draw_preview(screen)
        hud = font_small.render(
            f"Score: {score}  Level: {level}  Lines: {lines_cleared}",
            True,
            (230, 225, 255),
        )
        screen.blit(hud, (BOARD_X, BOARD_Y + ROWS * CELL + 16))
        ctrl = font_small.render("← → move  ↑ rotate  ↓ soft drop", True, (150, 145, 180))
        screen.blit(ctrl, (BOARD_X, BOARD_Y + ROWS * CELL + 42))

    elif state == GAME_OVER:
        if score > high_score:
            high_score = score
        draw_grid(screen)
        over = font_big.render("Grid Full!", True, (255, 130, 150))
        lines = font_small.render(f"Score: {score}  Best: {high_score}", True, (255, 255, 255))
        hint = font_small.render("SPACE for title", True, (200, 190, 230))
        screen.blit(over, over.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)))
        screen.blit(lines, lines.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 5)))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 45)))

    pygame.display.flip()

pygame.quit()