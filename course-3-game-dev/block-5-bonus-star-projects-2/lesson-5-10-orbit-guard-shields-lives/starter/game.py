# game.py — Lesson 5.10: Orbit Guard — shields & score (starter)
import random

import pygame

pygame.init()

WIDTH = 720
HEIGHT = 560
PLAY_TOP = 56
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Orbit Guard — Shields & Score")

clock = pygame.time.Clock()
running = True

font_small = pygame.font.Font(None, 28)

SHIP_W = 44
SHIP_Y = HEIGHT - 52
ship_x = WIDTH / 2
ship_speed = 360.0

lives = 3
score = 0

formation_x = 100.0
formation_y = PLAY_TOP + 30.0
march_dir = 1
march_speed = 55.0
COLS = 8
ROWS = 3
INV_W = 34
INV_GAP_X = 12
INV_H = 26
INV_GAP_Y = 10

player_bolts: list[dict[str, float]] = []
enemy_bolts: list[dict[str, float]] = []
invaders: list[pygame.Rect] = []
shields: list[dict[str, object]] = []


def build_invaders() -> list[pygame.Rect]:
    rects: list[pygame.Rect] = []
    for row in range(ROWS):
        for col in range(COLS):
            x = int(formation_x + col * (INV_W + INV_GAP_X))
            y = int(formation_y + row * (INV_H + INV_GAP_Y))
            rects.append(pygame.Rect(x, y, INV_W, INV_H))
    return rects


invaders = build_invaders()


def draw_orbit_bg(surface: pygame.Surface) -> None:
    surface.fill((6, 8, 22))


def draw_patrol_ship(surface: pygame.Surface, x: float, y: float) -> None:
    pygame.draw.polygon(
        surface,
        (70, 220, 255),
        [(int(x), int(y) - 12), (int(x) - 20, int(y) + 10), (int(x) + 20, int(y) + 10)],
    )


def update_bolts(dt: float) -> None:
    """TODO: move bolts; remove on invader hit (+score); enemy bolts damage ship (-life) or shields."""
    pass


def maybe_enemy_shot(dt: float) -> None:
    """TODO: timer — pick random invader and append downward enemy_bolts."""
    pass


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO: ship move, fire player_bolts, march formation from 5.9

    maybe_enemy_shot(dt)
    update_bolts(dt)

    draw_orbit_bg(screen)
    for inv in invaders:
        pygame.draw.ellipse(screen, (255, 120, 170), inv)
    draw_patrol_ship(screen, ship_x, SHIP_Y)

    hud = font_small.render(f"Score {score}  Lives {lives}", True, (190, 210, 245))
    screen.blit(hud, (12, 12))
    pygame.display.flip()

pygame.quit()