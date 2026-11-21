# game.py — Lesson 5.8: Orbit Guard — patrol ship (starter)
import pygame

pygame.init()

WIDTH = 720
HEIGHT = 560
PLAY_TOP = 56
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Orbit Guard — Patrol Ship")

clock = pygame.time.Clock()
running = True

font_small = pygame.font.Font(None, 28)

SHIP_W = 44
SHIP_H = 28
SHIP_Y = HEIGHT - 52
ship_x = WIDTH / 2
ship_speed = 360.0

BOLT_SPEED = 520.0
COOLDOWN = 0.28
cooldown_left = 0.0

player_bolts: list[dict[str, float]] = []


def draw_orbit_bg(surface: pygame.Surface, tick: int) -> None:
    surface.fill((6, 8, 22))


def draw_patrol_ship(surface: pygame.Surface, x: float, y: float) -> None:
    cx, cy = int(x), int(y)
    pygame.draw.rect(surface, (80, 200, 240), (cx - SHIP_W // 2, cy - SHIP_H // 2, SHIP_W, SHIP_H))


def fire_bolt() -> None:
    """TODO: respect cooldown_left; append a bolt dict with x, y, vy (negative = up)."""
    pass


def update_bolts(dt: float) -> None:
    """TODO: move each bolt by vy * dt; drop bolts that leave the screen."""
    pass


while running:
    dt = clock.tick(60) / 1000
    tick = pygame.time.get_ticks()
    cooldown_left = max(0.0, cooldown_left - dt)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, pygame.K_UP):
            fire_bolt()

    # TODO: left/right keys move ship_x; clamp between margins

    if keys := pygame.key.get_pressed():
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            fire_bolt()

    update_bolts(dt)

    draw_orbit_bg(screen, tick)
    draw_patrol_ship(screen, ship_x, SHIP_Y)
    for bolt in player_bolts:
        bx, by = int(bolt["x"]), int(bolt["y"])
        pygame.draw.rect(screen, (255, 230, 120), (bx - 2, by - 8, 4, 14))

    hud = font_small.render(f"Bolts: {len(player_bolts)}", True, (180, 200, 240))
    screen.blit(hud, (12, 12))
    pygame.display.flip()

pygame.quit()