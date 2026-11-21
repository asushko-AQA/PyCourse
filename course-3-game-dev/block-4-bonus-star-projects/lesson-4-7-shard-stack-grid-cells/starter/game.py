# game.py — Lesson 4.7: Shard Stack — grid (starter)
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

# TODO: build the 2D list — outer list = rows, inner list = columns
grid = None  # [[0 for _ in range(COLS)] for _ in range(ROWS)]

LOCKED_COLOR = (120, 130, 200)
EMPTY_COLOR = (32, 36, 52)


def draw_cell(surface: pygame.Surface, row: int, col: int, color: tuple[int, int, int]) -> None:
    x = BOARD_X + col * CELL
    y = BOARD_Y + row * CELL
    rect = pygame.Rect(x, y, CELL - 1, CELL - 1)
    pygame.draw.rect(surface, color, rect, border_radius=4)


def draw_grid(surface: pygame.Surface) -> None:
    """TODO: loop row in range(ROWS), col in range(COLS); draw empty or locked cell."""
    pass


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((18, 20, 32))
    if grid is not None:
        draw_grid(screen)

    hud = font_small.render("Finish the grid TODOs!", True, (220, 210, 255))
    screen.blit(hud, (BOARD_X, 12))

    pygame.display.flip()

pygame.quit()