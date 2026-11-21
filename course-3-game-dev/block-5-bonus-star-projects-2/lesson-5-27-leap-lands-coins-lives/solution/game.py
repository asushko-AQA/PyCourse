# game.py — Lesson 5.27: Leap Lands — coins, spikes & lives (solution)
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
            elif ch == "C":
                coins.append(pygame.Rect(x + 8, y + 8, TILE - 16, TILE - 16))
            elif ch == "^":
                spikes.append(pygame.Rect(x + 4, y + TILE // 2, TILE - 8, TILE // 2))
            elif ch == "S":
                spawn = pygame.Rect(x, y - PLAYER_H + TILE, PLAYER_W, PLAYER_H)
            elif ch == "F":
                flag = pygame.Rect(x, y - TILE, TILE, TILE * 2)
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

    for spike in spikes:
        if player.colliderect(spike):
            lives -= 1
            respawn()
            break

    for coin in coins[:]:
        if player.colliderect(coin):
            coins.remove(coin)
            coin_count += 1

    if player.colliderect(flag):
        pygame.draw.rect(screen, (40, 180, 120), (0, 0, WIDTH, HEIGHT))
        msg = font.render("Flag touched! (full game in 5.29)", True, (255, 255, 255))
        screen.blit(msg, (120, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(800)
        running = False
        continue

    screen.fill((16, 20, 42))
    for tile in solids:
        ch = LEVEL[tile.y // TILE][tile.x // TILE]
        color = (70, 85, 130) if ch == "#" else (100, 180, 220)
        pygame.draw.rect(screen, color, tile, border_radius=2)

    for spike in spikes:
        points = [
            (spike.centerx, spike.top),
            (spike.right, spike.bottom),
            (spike.left, spike.bottom),
        ]
        pygame.draw.polygon(screen, (255, 90, 120), points)

    for coin in coins:
        pygame.draw.circle(screen, (255, 220, 80), coin.center, coin.width // 2)

    pygame.draw.rect(screen, (80, 255, 160), flag, border_radius=4)
    pygame.draw.polygon(screen, (255, 240, 200), [
        (flag.right, flag.centery),
        (flag.right + 14, flag.centery - 10),
        (flag.right + 14, flag.centery + 10),
    ])

    pygame.draw.rect(screen, (90, 250, 200), player, border_radius=5)

    hud = font.render(f"Lives: {lives}   Coins: {coin_count}", True, (230, 235, 255))
    screen.blit(hud, (8, 8))

    if lives <= 0:
        over = font.render("Game Over — close window", True, (255, 120, 120))
        screen.blit(over, (WIDTH // 2 - 140, HEIGHT // 2))
        pygame.display.flip()
        continue

    pygame.display.flip()

pygame.quit()