# game.py — Lesson 4.4: Prism Dash — auto scroll world (solution)
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prism Dash — Scroll")

clock = pygame.time.Clock()
running = True

font_small = pygame.font.Font(None, 32)

PLAYER_X = 140
CUBE_SIZE = 36
GROUND_Y = 400
TILE_W = 48
SCROLL = 220

world_x = 0.0
player_y = GROUND_Y - CUBE_SIZE

# Decorative skyline — same pattern repeats (procedural art)
DECOR = "##__..__##__..__##"


def draw_cube(surface: pygame.Surface, center_x: int, top_y: int) -> None:
    rect = pygame.Rect(0, 0, CUBE_SIZE, CUBE_SIZE)
    rect.center = (center_x, top_y + CUBE_SIZE // 2)
    pygame.draw.rect(surface, (255, 110, 210), rect, border_radius=6)
    pygame.draw.rect(surface, (255, 245, 255), rect.inflate(-8, -8), width=2, border_radius=4)


def draw_ground(surface: pygame.Surface) -> None:
    pygame.draw.rect(surface, (45, 50, 70), (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))
    pygame.draw.line(surface, (120, 130, 180), (0, GROUND_Y), (WIDTH, GROUND_Y), 3)


def draw_decor(surface: pygame.Surface) -> None:
    """Blocks slide left as world_x grows — the cube stays at PLAYER_X."""
    for i, ch in enumerate(DECOR * 12):
        if ch != "#":
            continue
        sx = i * TILE_W - int(world_x)
        if -TILE_W < sx < WIDTH + TILE_W:
            block = pygame.Rect(sx, GROUND_Y - 56, TILE_W, 56)
            pygame.draw.rect(surface, (70, 120, 255), block, border_radius=4)


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    world_x += SCROLL * dt

    screen.fill((25, 18, 45))
    for stripe in range(0, WIDTH, 80):
        pygame.draw.rect(screen, (35, 28, 58), (stripe, 0, 40, GROUND_Y))

    draw_decor(screen)
    draw_ground(screen)
    draw_cube(screen, PLAYER_X, int(player_y))

    hud = font_small.render(f"world_x: {int(world_x)}", True, (240, 220, 255))
    hint = font_small.render("Cube runs in place — world scrolls!", True, (200, 180, 230))
    screen.blit(hud, (16, 12))
    screen.blit(hint, (16, 44))

    pygame.display.flip()

pygame.quit()