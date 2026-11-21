# game.py — Lesson 5.27: Leap Lands — coins, spikes & lives (starter)
import pygame

pygame.init()

TILE = 32
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Leap Lands — Hazard Bloom")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

LEVEL = [
    "################",
    "#S     C      ##",
    "#   ===   ^   ##",
    "#  C          F#",
    "################",
]

PLAYER_W, PLAYER_H = 26, 34
MOVE_SPEED = 260
GRAVITY = 1150
JUMP_V = -400
START_LIVES = 3

SOLID = {"#", "="}


def build_level(rows: list[str]) -> tuple[list[pygame.Rect], list[pygame.Rect], list[pygame.Rect], pygame.Rect, pygame.Rect]:
    """TODO: parse C coins, ^ spikes, S spawn, F flag like the solution."""
    solids: list[pygame.Rect] = []
    coins: list[pygame.Rect] = []
    spikes: list[pygame.Rect] = []
    spawn = pygame.Rect(64, 200, PLAYER_W, PLAYER_H)
    flag = pygame.Rect(0, 0, TILE, TILE * 2)
    for row_i, row in enumerate(rows):
        for col_i, ch in enumerate(row):
            x, y = col_i * TILE, row_i * TILE
            if ch in SOLID:
                solids.append(pygame.Rect(x, y, TILE, TILE))
            # TODO: elif branches for C, ^, S, F
    return solids, coins, spikes, spawn, flag


def move_and_resolve(rect: pygame.Rect, solids: list[pygame.Rect], dx: float, dy: float) -> tuple[pygame.Rect, bool]:
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


solids, coins, spikes, spawn_point, flag = build_level(LEVEL)
player = spawn_point.copy()
vel_y = 0.0
grounded = False
lives = START_LIVES
coin_count = 0
running = True


def respawn() -> None:
    global player, vel_y, grounded
    player = spawn_point.copy()
    vel_y = 0.0
    grounded = False


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
    player, grounded = move_and_resolve(player, solids, dx, vel_y * dt)

    # TODO: spike hit → lives -= 1, respawn()
    # TODO: coin colliderect → remove coin, coin_count += 1
    # TODO: optional early win message when touching flag (see solution)

    screen.fill((16, 20, 42))
    for tile in solids:
        pygame.draw.rect(screen, (70, 85, 130), tile, border_radius=2)

    # TODO: draw spikes, coins, flag, HUD (lives + coins)

    pygame.draw.rect(screen, (90, 250, 200), player, border_radius=5)
    hint = font.render("Finish TODOs — hazards, coins, lives!", True, (210, 220, 255))
    screen.blit(hint, (8, 8))
    pygame.display.flip()

pygame.quit()