# game.py — Lesson 5.12: Mine Whisper — crystal grid (starter)
import pygame

pygame.init()

WIDTH = 580
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mine Whisper — Crystal Grid")

clock = pygame.time.Clock()
running = True
font_small = pygame.font.Font(None, 28)

COLS = 14
ROWS = 10
CELL = 32
BOARD_X = 48
BOARD_Y = 56

# TODO: finish grid helpers — list of rows, each row a list of cell dicts
grid: list[list[dict[str, bool]]] = [
    [{"revealed": False, "peek": False} for _ in range(COLS)] for _ in range(ROWS)
]
picked: tuple[int, int] | None = None


def in_bounds(col: int, row: int) -> bool:
    return 0 <= col < COLS and 0 <= row < ROWS


def mouse_to_cell(pos: tuple[int, int]) -> tuple[int, int] | None:
    """TODO: convert event.pos to (col, row); return None if outside the board."""
    return None


def draw_crystal_tile(surface: pygame.Surface, x: int, y: int, *, peek: bool) -> None:
    rect = pygame.Rect(x + 2, y + 2, CELL - 4, CELL - 4)
    base = (70, 55, 105) if peek else (46, 38, 72)
    pygame.draw.rect(surface, base, rect, border_radius=6)
    pygame.draw.rect(surface, (88, 70, 128), rect, width=2, border_radius=6)


def draw_board(surface: pygame.Surface) -> None:
    """TODO: loop all cells and call draw_crystal_tile."""
    pass


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # TODO: mouse_to_cell → highlight that cell (peek=True)
            pass

    screen.fill((10, 8, 22))
    if grid:
        draw_board(screen)
    hud = font_small.render("Finish the grid TODOs!", True, (200, 185, 240))
    screen.blit(hud, (BOARD_X, 16))
    pygame.display.flip()

pygame.quit()