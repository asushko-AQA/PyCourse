# game.py — Lesson 5.12: Mine Whisper — crystal grid (solution)
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

# Each cell is a dict — we add mines in lesson 5.13
grid: list[list[dict[str, bool]]] = [
    [{"revealed": False, "peek": False} for _ in range(COLS)] for _ in range(ROWS)
]
picked: tuple[int, int] | None = None


def in_bounds(col: int, row: int) -> bool:
    return 0 <= col < COLS and 0 <= row < ROWS


def mouse_to_cell(pos: tuple[int, int]) -> tuple[int, int] | None:
    mx, my = pos
    if mx < BOARD_X or my < BOARD_Y:
        return None
    col = (mx - BOARD_X) // CELL
    row = (my - BOARD_Y) // CELL
    if not in_bounds(col, row):
        return None
    return col, row


def draw_crystal_tile(surface: pygame.Surface, x: int, y: int, *, peek: bool) -> None:
    rect = pygame.Rect(x + 2, y + 2, CELL - 4, CELL - 4)
    base = (70, 55, 105) if peek else (46, 38, 72)
    edge = (140, 110, 200) if peek else (88, 70, 128)
    pygame.draw.rect(surface, base, rect, border_radius=6)
    pygame.draw.rect(surface, edge, rect, width=2, border_radius=6)
    pygame.draw.rect(surface, (110, 90, 160), (x + 7, y + 7, 10, 8), border_radius=2)


def draw_board(surface: pygame.Surface) -> None:
    frame = pygame.Rect(BOARD_X - 8, BOARD_Y - 8, COLS * CELL + 16, ROWS * CELL + 16)
    pygame.draw.rect(surface, (26, 20, 40), frame, border_radius=10)
    for row in range(ROWS):
        for col in range(COLS):
            x = BOARD_X + col * CELL
            y = BOARD_Y + row * CELL
            cell = grid[row][col]
            draw_crystal_tile(surface, x, y, peek=cell["peek"] or cell["revealed"])


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            picked = mouse_to_cell(event.pos)
            if picked:
                for row in range(ROWS):
                    for col in range(COLS):
                        grid[row][col]["peek"] = False
                c, r = picked
                grid[r][c]["peek"] = True

    screen.fill((10, 8, 22))
    draw_board(screen)
    hud = font_small.render("Mine Whisper — click a crystal cell", True, (200, 185, 240))
    screen.blit(hud, (BOARD_X, 16))
    if picked:
        col, row = picked
        info = font_small.render(f"Cell ({col}, {row})", True, (160, 255, 210))
        screen.blit(info, (BOARD_X, BOARD_Y + ROWS * CELL + 16))
    pygame.display.flip()

pygame.quit()