# game.py — Lesson 4.5: Prism Dash — jump, gravity, spin (starter)
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
    # TODO: build a small Surface, draw the cube, rotate with pygame.transform.rotate, blit centered
    rect = pygame.Rect(0, 0, CUBE_SIZE, CUBE_SIZE)
    rect.center = (center_x, center_y)
    pygame.draw.rect(surface, (255, 110, 210), rect, border_radius=6)


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
    """TODO: if feet reach GROUND_Y, snap player_y, zero vel_y, grounded = True."""
    global player_y, vel_y, grounded
    grounded = False
    pass


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # TODO: SPACE + grounded → vel_y = JUMP_V, grounded = False

    world_x += SCROLL * dt

    # TODO: vel_y += GRAVITY * dt; player_y += vel_y * dt; call snap_ground()
    center_y = int(player_y) + CUBE_SIZE // 2

    # TODO: spin angle with ROT_SPEED * dt while airborne; reset angle on ground

    screen.fill((25, 18, 45))
    draw_decor(screen)
    draw_ground(screen)
    draw_cube(screen, PLAYER_X, center_y, angle)

    hud = font_small.render("Complete jump + spin TODOs", True, (240, 220, 255))
    screen.blit(hud, (16, 12))

    pygame.display.flip()

pygame.quit()