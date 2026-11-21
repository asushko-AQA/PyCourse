# game.py — Lesson 4.6: Prism Dash — complete (starter)
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prism Dash")

clock = pygame.time.Clock()
running = True

font_big = pygame.font.Font(None, 64)
font_small = pygame.font.Font(None, 32)

START = "start"
PLAYING = "playing"
GAME_OVER = "game_over"
WIN = "win"
state = START  # TODO: wire KEYDOWN like Lesson 4.3

PLAYER_X = 140
CUBE_SIZE = 36
GROUND_Y = 400
TILE_W = 48
BASE_SCROLL = 240
GRAVITY = 1400
JUMP_V = -520
ROT_SPEED = 300
PLATFORM_H = 44
SPIKE_H = 36

LEVEL = "____##__^^__####__^^__##__^^____####____"

world_x = 0.0
player_y = float(GROUND_Y - CUBE_SIZE)
vel_y = 0.0
angle = 0.0
grounded = True
attempts = 0
best_progress = 0  # TODO: update in die()


def level_length_px() -> int:
    return len(LEVEL) * TILE_W


def progress_pct() -> int:
    return min(100, int(world_x / level_length_px() * 100))


def draw_cube(surface: pygame.Surface, center_x: int, center_y: int, angle_deg: float) -> None:
    tile = pygame.Surface((CUBE_SIZE, CUBE_SIZE), pygame.SRCALPHA)
    pygame.draw.rect(tile, (255, 110, 210), tile.get_rect(), border_radius=6)
    rotated = pygame.transform.rotate(tile, -angle_deg)
    surface.blit(rotated, rotated.get_rect(center=(center_x, center_y)))


def player_rect() -> pygame.Rect:
    return pygame.Rect(PLAYER_X - CUBE_SIZE // 2, int(player_y), CUBE_SIZE, CUBE_SIZE)


def draw_ground(surface: pygame.Surface) -> None:
    pygame.draw.rect(surface, (45, 50, 70), (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))
    pygame.draw.line(surface, (120, 130, 180), (0, GROUND_Y), (WIDTH, GROUND_Y), 3)


def level_objects() -> tuple[list[pygame.Rect], list[pygame.Rect]]:
    """TODO: build platform + spike rects from LEVEL and world_x."""
    return [], []


def draw_level(surface: pygame.Surface) -> None:
    """TODO: draw # blocks and ^ triangles for each tile in LEVEL."""
    pass


def snap_platforms(platforms: list[pygame.Rect], dt: float) -> None:
    """TODO: land on platforms or GROUND_Y; set grounded."""
    global player_y, vel_y, grounded
    pass


def start_run() -> None:
    """TODO: reset run; state = PLAYING."""
    pass


def die() -> None:
    """TODO: attempts += 1; update best_progress; state = GAME_OVER."""
    pass


def draw_progress_bar(surface: pygame.Surface) -> None:
    """TODO: progress % bar + attempts + best %."""
    pass


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # TODO: state machine keys (start / jump / title)

    screen.fill((25, 18, 45))
    draw_ground(screen)

    if state == PLAYING:
        # TODO: scroll world_x, physics, draw_level, collisions, win at 100%
        pass
    elif state == START:
        title = font_big.render("Prism Dash", True, (255, 200, 245))
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

    pygame.display.flip()

pygame.quit()