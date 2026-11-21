# game.py — Lesson 4.5: Prism Dash — jump, gravity, spin (solution)
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prism Dash — Jump")

clock = pygame.time.Clock()
running = True

font_small = pygame.font.Font(None, 32)

PLAYER_X = 140
CUBE_SIZE = 36
GROUND_Y = 400
TILE_W = 48
SCROLL = 220
GRAVITY = 1400
JUMP_V = -520
ROT_SPEED = 300

world_x = 0.0
player_y = float(GROUND_Y - CUBE_SIZE)
vel_y = 0.0
angle = 0.0
grounded = True

DECOR = "##__..__##__..__##"


def draw_cube(surface: pygame.Surface, center_x: int, center_y: int, angle_deg: float) -> None:
    tile = pygame.Surface((CUBE_SIZE, CUBE_SIZE), pygame.SRCALPHA)
    pygame.draw.rect(tile, (255, 110, 210), tile.get_rect(), border_radius=6)
    pygame.draw.rect(tile, (255, 245, 255), tile.get_rect().inflate(-8, -8), width=2, border_radius=4)
    rotated = pygame.transform.rotate(tile, -angle_deg)
    rect = rotated.get_rect(center=(center_x, center_y))
    surface.blit(rotated, rect)


def player_rect() -> pygame.Rect:
    return pygame.Rect(PLAYER_X - CUBE_SIZE // 2, int(player_y), CUBE_SIZE, CUBE_SIZE)


def draw_ground(surface: pygame.Surface) -> None:
    pygame.draw.rect(surface, (45, 50, 70), (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))
    pygame.draw.line(surface, (120, 130, 180), (0, GROUND_Y), (WIDTH, GROUND_Y), 3)


def draw_decor(surface: pygame.Surface) -> None:
    pattern_len = len(DECOR) * TILE_W
    offset = int(world_x) % pattern_len
    for i, ch in enumerate(DECOR * 10):
        if ch != "#":
            continue
        sx = i * TILE_W - offset
        if -TILE_W < sx < WIDTH + TILE_W:
            block = pygame.Rect(sx, GROUND_Y - 56, TILE_W, 56)
            pygame.draw.rect(surface, (70, 120, 255), block, border_radius=4)


def snap_ground() -> None:
    global player_y, vel_y, grounded
    grounded = False
    if player_y + CUBE_SIZE >= GROUND_Y - 1:
        player_y = GROUND_Y - CUBE_SIZE
        vel_y = 0
        grounded = True


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and grounded:
            vel_y = JUMP_V
            grounded = False

    world_x += SCROLL * dt

    vel_y += GRAVITY * dt
    player_y += vel_y * dt
    snap_ground()

    center_y = int(player_y) + CUBE_SIZE // 2
    if grounded:
        angle = 0.0
    else:
        angle = (angle + ROT_SPEED * dt) % 360

    screen.fill((25, 18, 45))
    for stripe in range(0, WIDTH, 80):
        pygame.draw.rect(screen, (35, 28, 58), (stripe, 0, 40, GROUND_Y))

    draw_decor(screen)
    draw_ground(screen)
    draw_cube(screen, PLAYER_X, center_y, angle)

    status = "grounded" if grounded else "airborne"
    hud = font_small.render(f"vel_y: {vel_y:.0f}  ({status})", True, (240, 220, 255))
    hint = font_small.render("SPACE jump (only on ground)", True, (180, 160, 210))
    screen.blit(hud, (16, 12))
    screen.blit(hint, (16, 44))

    pygame.display.flip()

pygame.quit()