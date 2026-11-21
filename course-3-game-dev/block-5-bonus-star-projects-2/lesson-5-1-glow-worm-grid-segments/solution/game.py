# game.py — Lesson 5.1: Glow Worm — grid + segments
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

# Worm body: list of (col, row) — head is index 0
segments: list[tuple[int, int]] = [(8, 8), (7, 8), (6, 8)]
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
        pygame.draw.circle(surface, (25, 45, 35), (cx - 4, cy - 3), 3)
        pygame.draw.circle(surface, (25, 45, 35), (cx + 4, cy - 3), 3)
    else:
        pygame.draw.circle(surface, (50, 180, 255), (cx, cy), CELL // 2 + 4)
        pygame.draw.circle(surface, (90, 220, 255), (cx, cy), CELL // 2 - 2)


def step_worm() -> None:
    global segments, direction
    direction = pending_dir
    hc, hr = segments[0]
    dc, dr = direction
    new_head = (hc + dc, hr + dr)
    # Lesson 5.1: bounce at walls — no game over yet
    if new_head[0] < 0 or new_head[0] >= COLS or new_head[1] < 0 or new_head[1] >= ROWS:
        return
    segments = [new_head] + segments[:-1]


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not is_opposite((0, -1), direction):
                pending_dir = (0, -1)
            elif event.key == pygame.K_DOWN and not is_opposite((0, 1), direction):
                pending_dir = (0, 1)
            elif event.key == pygame.K_LEFT and not is_opposite((-1, 0), direction):
                pending_dir = (-1, 0)
            elif event.key == pygame.K_RIGHT and not is_opposite((1, 0), direction):
                pending_dir = (1, 0)

    move_timer += dt
    if move_timer >= MOVE_INTERVAL:
        move_timer = 0.0
        step_worm()

    screen.fill((10, 12, 22))
    draw_cell_grid(screen)
    for i, (col, row) in enumerate(segments):
        draw_glow_segment(screen, col, row, is_head=(i == 0))

    hud = font_small.render(f"dir={direction}  head={segments[0]}", True, (200, 230, 255))
    screen.blit(hud, (BOARD_X, 12))
    pygame.display.flip()

pygame.quit()