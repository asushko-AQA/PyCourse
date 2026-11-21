# game.py — Lesson 5.26: Leap Lands — text map & collision (starter)
import pygame

pygame.init()

TILE = 32
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Leap Lands — Map Mason")

clock = pygame.time.Clock()

LEVEL = [
    "################",
    "#S            ##",
    "#      ===    ##",
    "#             ##",
    "################",
]

PLAYER_W, PLAYER_H = 26, 34
MOVE_SPEED = 260
GRAVITY = 1150
JUMP_V = -400

SOLID = {"#", "="}


def build_solids(rows: list[str]) -> list[pygame.Rect]:
    rects: list[pygame.Rect] = []
    for row_i, row in enumerate(rows):
        for col_i, ch in enumerate(row):
            if ch in SOLID:
                rects.append(pygame.Rect(col_i * TILE, row_i * TILE, TILE, TILE))
    return rects


def find_spawn(rows: list[str]) -> tuple[float, float]:
    for row_i, row in enumerate(rows):
        for col_i, ch in enumerate(row):
            if ch == "S":
                return float(col_i * TILE), float(row_i * TILE - PLAYER_H)
    return 64.0, 200.0


def move_and_resolve(
    rect: pygame.Rect,
    solids: list[pygame.Rect],
    dx: float,
    dy: float,
) -> tuple[pygame.Rect, bool]:
    """TODO: move X, resolve collisions, move Y, resolve — return (rect, on_ground)."""
    on_ground = False
    return rect, on_ground


solids = build_solids(LEVEL)
spawn_x, spawn_y = find_spawn(LEVEL)
player = pygame.Rect(int(spawn_x), int(spawn_y), PLAYER_W, PLAYER_H)
vel_y = 0.0
grounded = False
running = True

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO: keyboard move, gravity, jump, call move_and_resolve

    screen.fill((16, 20, 42))
    for tile in solids:
        pygame.draw.rect(screen, (70, 85, 130), tile)

    pygame.draw.rect(screen, (90, 250, 200), player, border_radius=5)
    pygame.display.flip()

pygame.quit()