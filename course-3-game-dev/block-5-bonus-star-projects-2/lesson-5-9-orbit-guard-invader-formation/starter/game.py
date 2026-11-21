# game.py — Lesson 5.9: Orbit Guard — invader grid (starter)
import pygame

pygame.init()

WIDTH = 720
HEIGHT = 560
PLAY_TOP = 56
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Orbit Guard — Invader Grid")

clock = pygame.time.Clock()
running = True

font_small = pygame.font.Font(None, 28)

SHIP_W = 44
SHIP_Y = HEIGHT - 52
ship_x = WIDTH / 2
ship_speed = 360.0

INV_W = 34
INV_H = 26
INV_GAP_X = 12
INV_GAP_Y = 10
COLS = 9
ROWS = 4

formation_x = 80.0
formation_y = PLAY_TOP + 24.0
march_dir = 1
march_speed = 62.0
step_down = 18.0

player_bolts: list[dict[str, float]] = []


def build_invaders() -> list[pygame.Rect]:
    rects: list[pygame.Rect] = []
    for row in range(ROWS):
        for col in range(COLS):
            x = int(formation_x + col * (INV_W + INV_GAP_X))
            y = int(formation_y + row * (INV_H + INV_GAP_Y))
            rects.append(pygame.Rect(x, y, INV_W, INV_H))
    return rects


invaders: list[pygame.Rect] = build_invaders()


def formation_width() -> float:
    return COLS * INV_W + (COLS - 1) * INV_GAP_X


def draw_orbit_bg(surface: pygame.Surface, tick: int) -> None:
    surface.fill((6, 8, 22))


def draw_patrol_ship(surface: pygame.Surface, x: float, y: float) -> None:
    pygame.draw.polygon(
        surface,
        (70, 210, 255),
        [(int(x), int(y) - 10), (int(x) - 20, int(y) + 10), (int(x) + 20, int(y) + 10)],
    )


def draw_invader(surface: pygame.Surface, rect: pygame.Rect) -> None:
    pygame.draw.ellipse(surface, (255, 120, 160), rect)


def march_formation(dt: float) -> None:
    """TODO: move formation_x by march_dir * march_speed * dt.
    When the grid hits left/right margin, flip march_dir and add step_down to formation_y.
    Rebuild invaders with build_invaders()."""
    pass


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO: ship left/right + bolts from lesson 5.8 (optional)

    march_formation(dt)

    draw_orbit_bg(screen, 0)
    for inv in invaders:
        draw_invader(screen, inv)
    draw_patrol_ship(screen, ship_x, SHIP_Y)

    hud = font_small.render(f"dir={march_dir}", True, (180, 200, 240))
    screen.blit(hud, (12, 12))
    pygame.display.flip()

pygame.quit()