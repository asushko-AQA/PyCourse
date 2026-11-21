# game.py — Lesson 5.1: Glow Worm — grid (starter)
import pygame

pygame.init()

WIDTH = 620
HEIGHT = 560
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Glow Worm — Grid")

clock = pygame.time.Clock()
running = True

font_small = pygame.font.Font(None, 28)

COLS = 20
ROWS = 16
CELL = 26
BOARD_X = 36
BOARD_Y = 48
MOVE_INTERVAL = 0.2

# TODO: segments is a list of (col, row); index 0 = head
segments: list[tuple[int, int]] | None = None

direction = (1, 0)
pending_dir = (1, 0)
move_timer = 0.0


def is_opposite(new_dir: tuple[int, int], current: tuple[int, int]) -> bool:
    return new_dir[0] == -current[0] and new_dir[1] == -current[1]


def draw_cell_grid(surface: pygame.Surface) -> None:
    frame = pygame.Rect(BOARD_X - 6, BOARD_Y - 6, COLS * CELL + 12, ROWS * CELL + 12)
    pygame.draw.rect(surface, (40, 50, 70), frame, border_radius=8)
    for row in range(ROWS):
        for col in range(COLS):
            x = BOARD_X + col * CELL
            y = BOARD_Y + row * CELL
            pygame.draw.rect(surface, (18, 22, 34), (x, y, CELL - 1, CELL - 1))


def draw_glow_segment(surface: pygame.Surface, col: int, row: int, *, is_head: bool) -> None:
    cx = BOARD_X + col * CELL + CELL // 2
    cy = BOARD_Y + row * CELL + CELL // 2
    if is_head:
        pygame.draw.circle(surface, (60, 255, 170), (cx, cy), CELL // 2 + 6)
        pygame.draw.circle(surface, (140, 255, 210), (cx, cy), CELL // 2 - 2)
    else:
        pygame.draw.circle(surface, (50, 180, 255), (cx, cy), CELL // 2 + 4)
        pygame.draw.circle(surface, (90, 220, 255), (cx, cy), CELL // 2 - 2)


def step_worm() -> None:
    """TODO: read pending_dir into direction, compute new_head, slide body."""
    pass


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # TODO: set pending_dir from arrows; block 180° turns with is_opposite
            pass

    # TODO: move_timer += dt; when >= MOVE_INTERVAL, call step_worm()

    screen.fill((10, 12, 22))
    draw_cell_grid(screen)
    if segments:
        for i, (col, row) in enumerate(segments):
            draw_glow_segment(screen, col, row, is_head=(i == 0))

    hud = font_small.render("Finish the segment TODOs!", True, (220, 210, 255))
    screen.blit(hud, (BOARD_X, 12))
    pygame.display.flip()

pygame.quit()