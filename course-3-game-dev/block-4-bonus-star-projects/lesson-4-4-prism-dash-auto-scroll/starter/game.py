# game.py — Lesson 4.4: Prism Dash — auto scroll world (starter)
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
    """TODO: draw '#' blocks using screen x = tile_index * TILE_W - int(world_x)."""
    for i, ch in enumerate(DECOR * 8):
        if ch != "#":
            continue
        # TODO: compute sx and pygame.draw.rect when block is on screen
        pass


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO: grow world_x each frame: world_x += SCROLL * dt

    screen.fill((25, 18, 45))
    for stripe in range(0, WIDTH, 80):
        pygame.draw.rect(screen, (35, 28, 58), (stripe, 0, 40, GROUND_Y))

    # TODO: call draw_decor(screen) after you implement it
    draw_ground(screen)
    draw_cube(screen, PLAYER_X, int(player_y))

    hud = font_small.render(f"world_x: {int(world_x)}", True, (240, 220, 255))
    screen.blit(hud, (16, 12))

    pygame.display.flip()

pygame.quit()