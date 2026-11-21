# game.py — Lesson 5.28: Leap Lands — patrollers & camera (starter)
from __future__ import annotations

import pygame

pygame.init()

TILE = 32
VIEW_W, VIEW_H = 640, 480
screen = pygame.display.set_mode((VIEW_W, VIEW_H))
pygame.display.set_caption("Leap Lands — Scroll Patrol")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

LEVEL = [
    "################################",
    "#S    C      E        C       F#",
    "#  ========       ====          #",
    "#          ^                    ##",
    "################################",
]

PLAYER_W, PLAYER_H = 26, 34
ENEMY_W, ENEMY_H = 30, 24
MOVE_SPEED = 260
GRAVITY = 1150
JUMP_V = -400
PATROL_SPEED = 70

SOLID = {"#", "="}


def build_level(rows: list[str]):
    solids: list[pygame.Rect] = []
    coins: list[pygame.Rect] = []
    spikes: list[pygame.Rect] = []
    enemies: list[dict] = []
    spawn = pygame.Rect(64, 200, PLAYER_W, PLAYER_H)
    flag = pygame.Rect(0, 0, TILE, TILE * 2)
    world_w = max(len(r) for r in rows) * TILE

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
            elif ch == "E":
                pad = pygame.Rect(x, y - ENEMY_H + TILE, TILE * 3, TILE)
                enemies.append({
                    "rect": pygame.Rect(x, y - ENEMY_H + TILE, ENEMY_W, ENEMY_H),
                    "dir": 1,
                    "min_x": pad.left,
                    "max_x": pad.right - ENEMY_W,
                    "alive": True,
                })
    return solids, coins, spikes, enemies, spawn, flag, world_w


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


solids, coins, spikes, enemies, spawn_point, flag, world_w = build_level(LEVEL)
player = spawn_point.copy()
vel_y = 0.0
grounded = False
camera_x = 0.0
running = True


def stomp_enemy(enemy: dict) -> bool:
    """Return True if player stomps from above."""
    if not enemy["alive"]:
        return False
    er = enemy["rect"]
    if player.bottom <= er.top + 8 and player.right > er.left and player.left < er.right:
        if vel_y > 0:
            enemy["alive"] = False
            return True
    return False


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

    for enemy in enemies:
        if not enemy["alive"]:
            continue
        er = enemy["rect"]
        er.x += int(enemy["dir"] * PATROL_SPEED * dt)
        if er.left <= enemy["min_x"]:
            er.left = enemy["min_x"]
            enemy["dir"] = 1
        if er.right >= enemy["max_x"]:
            er.right = enemy["max_x"]
            enemy["dir"] = -1
        if player.colliderect(er):
            if stomp_enemy(enemy):
                vel_y = JUMP_V * 0.45
            else:
                player = spawn_point.copy()
                vel_y = 0.0

    for coin in coins[:]:
        if player.colliderect(coin):
            coins.remove(coin)

    target_cam = player.centerx - VIEW_W // 2
    camera_x += (target_cam - camera_x) * min(1.0, dt * 6)
    camera_x = max(0, min(world_w - VIEW_W, camera_x))

    screen.fill((14, 18, 40))
    cam = int(camera_x)

    for tile in solids:
        draw = tile.move(-cam, 0)
        if draw.right < 0 or draw.left > VIEW_W:
            continue
        ch = LEVEL[tile.y // TILE][tile.x // TILE]
        color = (70, 85, 130) if ch == "#" else (100, 180, 220)
        pygame.draw.rect(screen, color, draw)

    for coin in coins:
        dr = coin.move(-cam, 0)
        if 0 <= dr.centerx <= VIEW_W:
            pygame.draw.circle(screen, (255, 220, 80), dr.center, dr.width // 2)

    for enemy in enemies:
        if enemy["alive"]:
            dr = enemy["rect"].move(-cam, 0)
            pygame.draw.ellipse(screen, (255, 110, 170), dr)

    fr = flag.move(-cam, 0)
    pygame.draw.rect(screen, (80, 255, 160), fr)
    pygame.draw.rect(screen, (90, 250, 200), player.move(-cam, 0), border_radius=5)

    hud = font.render(f"camera_x={camera_x:.0f}  stomp enemies from above!", True, (220, 230, 255))
    screen.blit(hud, (8, 8))
    pygame.display.flip()

pygame.quit()