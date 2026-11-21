# game.py — Lesson 5.31: Night Swarm — shadow spawns (solution)
from __future__ import annotations

import random

import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
MARGIN = 22
PLAYER_SPEED = 185
PLAYER_RADIUS = 14
MAX_ENEMIES = 40
SPAWN_EVERY = 1.4
SHADOW_SPEED = 78

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Night Swarm — Shadow Tide")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

player_pos = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
player_hp = 100.0
player_max_hp = 100.0
enemies: list[dict] = []
spawn_timer = 0.5
hurt_cd = 0.0
rng = random.Random()
running = True


def clamp_player(pos: pygame.Vector2) -> None:
    pos.x = max(MARGIN + PLAYER_RADIUS, min(WIDTH - MARGIN - PLAYER_RADIUS, pos.x))
    pos.y = max(MARGIN + PLAYER_RADIUS, min(HEIGHT - MARGIN - PLAYER_RADIUS, pos.y))


def direction_toward(ax: float, ay: float, bx: float, by: float) -> pygame.Vector2:
    d = pygame.Vector2(bx - ax, by - ay)
    if d.length_squared() > 0:
        d = d.normalize()
    return d


def spawn_at_edge() -> pygame.Vector2:
    side = rng.randint(0, 3)
    r = 12
    if side == 0:
        return pygame.Vector2(rng.uniform(MARGIN, WIDTH - MARGIN), -r)
    if side == 1:
        return pygame.Vector2(WIDTH + r, rng.uniform(MARGIN, HEIGHT - MARGIN))
    if side == 2:
        return pygame.Vector2(rng.uniform(MARGIN, WIDTH - MARGIN), HEIGHT + r)
    return pygame.Vector2(-r, rng.uniform(MARGIN, HEIGHT - MARGIN))


def draw_hp_bar(surf: pygame.Surface, hp: float, max_hp: float) -> None:
    w, h = 200, 14
    x, y = 12, 12
    pygame.draw.rect(surf, (40, 44, 70), (x, y, w, h), border_radius=4)
    fill = int(w * max(0.0, min(1.0, hp / max_hp)))
    pygame.draw.rect(surf, (120, 220, 255), (x, y, fill, h), border_radius=4)
    pygame.draw.rect(surf, (160, 170, 220), (x, y, w, h), width=2, border_radius=4)


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    move = pygame.Vector2(0, 0)
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        move.y -= 1
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        move.y += 1
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        move.x -= 1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        move.x += 1
    if move.length_squared() > 0:
        move = move.normalize()
    player_pos += move * PLAYER_SPEED * dt
    clamp_player(player_pos)

    hurt_cd = max(0.0, hurt_cd - dt)
    spawn_timer -= dt
    if spawn_timer <= 0 and len(enemies) < MAX_ENEMIES:
        spawn_timer = SPAWN_EVERY
        enemies.append({"pos": spawn_at_edge(), "radius": 11})

    px, py = player_pos.x, player_pos.y
    for e in enemies:
        d = direction_toward(e["pos"].x, e["pos"].y, px, py)
        e["pos"] += d * SHADOW_SPEED * dt
        if e["pos"].distance_to(player_pos) < PLAYER_RADIUS + e["radius"] and hurt_cd <= 0:
            player_hp -= 12
            hurt_cd = 0.5

    screen.fill((12, 14, 28))
    pygame.draw.rect(screen, (30, 36, 58), (MARGIN, MARGIN, WIDTH - 2 * MARGIN, HEIGHT - 2 * MARGIN), 2)
    for e in enemies:
        pygame.draw.circle(screen, (90, 70, 140), (int(e["pos"].x), int(e["pos"].y)), e["radius"])
    pygame.draw.circle(screen, (255, 210, 80), (int(px), int(py)), PLAYER_RADIUS)
    draw_hp_bar(screen, player_hp, player_max_hp)
    hud = font.render(f"Shadows {len(enemies)} · HP {player_hp:.0f}", True, (190, 200, 240))
    screen.blit(hud, (12, 32))

    pygame.display.flip()

pygame.quit()