# game.py — Lesson 5.26: Leap Lands — text map & collision (solution)
import pygame

pygame.init()

TILE = 32
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Leap Lands — Map Mason")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

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
    on_ground = False
    rect.x += int(dx)
    for tile in solids:
        if rect.colliderect(tile):
            if dx > 0:
                rect.right = tile.left
            elif dx < 0:
                rect.left = tile.right
    rect.y += int(dy)
    for tile in solids:
        if rect.colliderect(tile):
            if dy > 0:
                rect.bottom = tile.top
                on_ground = True
            elif dy < 0:
                rect.top = tile.bottom
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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and grounded:
            vel_y = JUMP_V
            grounded = False

    keys = pygame.key.get_pressed()
    dx = 0.0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dx -= MOVE_SPEED * dt
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dx += MOVE_SPEED * dt

    vel_y += GRAVITY * dt
    dy = vel_y * dt
    player, grounded = move_and_resolve(player, solids, dx, dy)

    screen.fill((16, 20, 42))
    for tile in solids:
        color = (70, 85, 130) if LEVEL[tile.y // TILE][tile.x // TILE] == "#" else (100, 180, 220)
        pygame.draw.rect(screen, color, tile)
        pygame.draw.rect(screen, (30, 35, 60), tile, 1)

    pygame.draw.rect(screen, (90, 250, 200), player, border_radius=5)

    tip = font.render("Map: # ground  = platform  S spawn", True, (180, 190, 230))
    screen.blit(tip, (8, 8))

    pygame.display.flip()

pygame.quit()