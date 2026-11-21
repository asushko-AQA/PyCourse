# game.py — Lesson 4.7: Shard Stack — grid and cells
import pygame

pygame.init()

WIDTH = 420
HEIGHT = 560
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shard Stack — Grid")

clock = pygame.time.Clock()
running = True

font_small = pygame.font.Font(None, 28)

COLS = 10
ROWS = 20
CELL = 24
BOARD_X = 48
BOARD_Y = 48

# A 2D list: each row is a list of cells; 0 means empty
grid: list[list[int]] = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# Demo: pre-lock a few cells so you see colors in the well
grid[18][4] = 1
grid[18][5] = 1
grid[18][6] = 1
grid[17][5] = 1

LOCKED_COLOR = (120, 130, 200)
EMPTY_COLOR = (32, 36, 52)

# One T-shaped shard shown as offsets (lesson 4.8 will move this)
DEMO_OFFSETS = [(0, 1), (1, 0), (1, 1), (1, 2)]
DEMO_ANCHOR = (2, 4)
DEMO_COLOR = (180, 120, 255)


def draw_cell(surface: pygame.Surface, row: int, col: int, color: tuple[int, int, int]) -> None:
    x = BOARD_X + col * CELL
    y = BOARD_Y + row * CELL
    rect = pygame.Rect(x, y, CELL - 1, CELL - 1)
    pygame.draw.rect(surface, color, rect, border_radius=4)


def draw_grid(surface: pygame.Surface) -> None:
    frame = pygame.Rect(BOARD_X - 4, BOARD_Y - 4, COLS * CELL + 8, ROWS * CELL + 8)
    pygame.draw.rect(surface, (55, 60, 90), frame, border_radius=6)
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col]:
                draw_cell(surface, row, col, LOCKED_COLOR)
            else:
                x = BOARD_X + col * CELL
                y = BOARD_Y + row * CELL
                pygame.draw.rect(surface, EMPTY_COLOR, (x, y, CELL - 1, CELL - 1))


def draw_demo_piece(surface: pygame.Surface) -> None:
    base_r, base_c = DEMO_ANCHOR
    for dr, dc in DEMO_OFFSETS:
        draw_cell(surface, base_r + dr, base_c + dc, DEMO_COLOR)


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((18, 20, 32))
    draw_grid(screen)
    draw_demo_piece(screen)

    title = font_small.render("Shard Stack — grid[ row ][ col ]", True, (220, 210, 255))
    tip = font_small.render(
        f"grid is {ROWS} rows x {COLS} cols  |  dt={dt:.3f}s",
        True,
        (150, 145, 180),
    )
    screen.blit(title, (BOARD_X, 12))
    screen.blit(tip, (BOARD_X, BOARD_Y + ROWS * CELL + 16))

    pygame.display.flip()

pygame.quit()