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
START_LIVES = 3
SOLID = {"#", "="}


def build_level(rows: list[str]):
    """TODO: include E enemies with min_x/max_x patrol bounds (see solution)."""
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
            # TODO: elif ch == "E": append patrol enemy dict
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
lives = START_LIVES
coin_count = 0
camera_x = 0.0
running = True


def stomp_enemy(enemy: dict) -> bool:
    """TODO: return True when player stomps from above (see solution)."""
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

    # TODO: patrol each enemy; stomp vs side hit
    # TODO: coins, spikes, lives from 5.27
    # TODO: smooth camera_x toward player.centerx - VIEW_W//2, clamp 0..world_w-VIEW_W
    # TODO: draw world with .move(-int(camera_x), 0)

    screen.fill((14, 18, 40))
    pygame.draw.rect(screen, (90, 250, 200), player, border_radius=5)
    hint = font.render("Finish TODOs — patrol E enemies + camera scroll!", True, (220, 230, 255))
    screen.blit(hint, (8, 8))
    pygame.display.flip()

pygame.quit()