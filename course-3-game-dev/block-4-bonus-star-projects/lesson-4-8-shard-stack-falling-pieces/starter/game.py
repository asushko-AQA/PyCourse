# game.py — Lesson 4.8: Shard Stack — falling piece (starter)
import pygame

pygame.init()

WIDTH = 420
HEIGHT = 560
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shard Stack — Fall")

clock = pygame.time.Clock()
running = True

font_small = pygame.font.Font(None, 28)

COLS = 10
ROWS = 20
CELL = 24
BOARD_X = 48
BOARD_Y = 48
FALL_INTERVAL = 0.45

grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

PIECE_OFFSETS = [(0, 1), (1, 0), (1, 1), (1, 2)]
PIECE_COLOR = (180, 120, 255)
piece_row = 0
piece_col = 3
fall_timer = 0.0


def can_move(dr: int, dc: int) -> bool:
    """TODO: check walls, floor, and locked cells for every offset."""
    return False


def try_move(dr: int, dc: int) -> bool:
    global piece_row, piece_col
    # TODO: if can_move, update anchor and return True
    return False


def lock_piece() -> None:
    """TODO: copy piece color into grid, respawn at top center."""
    pass


def draw_cell(surface: pygame.Surface, row: int, col: int, color: tuple[int, int, int]) -> None:
    x = BOARD_X + col * CELL
    y = BOARD_Y + row * CELL
    rect = pygame.Rect(x, y, CELL - 1, CELL - 1)
    pygame.draw.rect(surface, color, rect, border_radius=4)


def draw_grid(surface: pygame.Surface) -> None:
    for row in range(ROWS):
        for col in range(COLS):
            x = BOARD_X + col * CELL
            y = BOARD_Y + row * CELL
            pygame.draw.rect(surface, (32, 36, 52), (x, y, CELL - 1, CELL - 1))
            if grid[row][col]:
                draw_cell(surface, row, col, grid[row][col])  # type: ignore[arg-type]


def draw_piece(surface: pygame.Surface) -> None:
    for dr, dc in PIECE_OFFSETS:
        draw_cell(surface, piece_row + dr, piece_col + dc, PIECE_COLOR)


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                try_move(0, -1)
            elif event.key == pygame.K_RIGHT:
                try_move(0, 1)
            elif event.key == pygame.K_DOWN:
                if not try_move(1, 0):
                    lock_piece()

    # TODO: fall_timer += dt; when timer hits FALL_INTERVAL, try_move(1, 0) or lock_piece()

    screen.fill((18, 20, 32))
    draw_grid(screen)
    draw_piece(screen)
    hud = font_small.render("Wire can_move + fall timer", True, (220, 210, 255))
    screen.blit(hud, (BOARD_X, 12))

    pygame.display.flip()

pygame.quit()