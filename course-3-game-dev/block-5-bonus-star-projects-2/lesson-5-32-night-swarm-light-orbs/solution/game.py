# game.py — Lesson 5.32: Night Swarm — light orbs (solution)
from __future__ import annotations

import math
import random

import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
MARGIN = 22
PLAYER_SPEED = 185
PLAYER_RADIUS = 14
MAX_ENEMIES = 45
SPAWN_EVERY = 1.3
SHADOW_SPEED = 75

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Night Swarm — Orb Sentinel")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

player_pos = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
player_hp = 100.0
player_max_hp = 100.0
damage = 14
fire_cooldown = 0.6
fire_timer = 0.0
enemies: list[dict] = []
orbs: list[dict] = []
gems: list[dict] = []
spawn_timer = 0.4
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


def nearest_enemy_index(px: float, py: float, shadow_list: list[dict]) -> int | None:
    best_i = None
    best_d2 = math.inf
    for i, e in enumerate(shadow_list):
        if e["hp"] <= 0:
            continue
        dx = e["pos"].x - px
        dy = e["pos"].y - py
        d2 = dx * dx + dy * dy
        if d2 < best_d2:
            best_d2 = d2
            best_i = i
    return best_i


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
        enemies.append({"pos": spawn_at_edge(), "radius": 11, "hp": 24, "drop": True})

    px, py = player_pos.x, player_pos.y
    for e in enemies:
        if e["hp"] <= 0:
            continue
        d = direction_toward(e["pos"].x, e["pos"].y, px, py)
        e["pos"] += d * SHADOW_SPEED * dt
        if e["pos"].distance_to(player_pos) < PLAYER_RADIUS + e["radius"] and hurt_cd <= 0:
            player_hp -= 10
            hurt_cd = 0.45

    fire_timer -= dt
    if fire_timer <= 0:
        idx = nearest_enemy_index(px, py, enemies)
        if idx is not None:
            te = enemies[idx]
            vel = direction_toward(px, py, te["pos"].x, te["pos"].y) * 300
            orbs.append({"pos": pygame.Vector2(px, py), "vel": vel, "life": 1.8})
            fire_timer = fire_cooldown

    for orb in orbs:
        orb["pos"] += orb["vel"] * dt
        orb["life"] -= dt
    orbs = [o for o in orbs if o["life"] > 0]

    for orb in orbs:
        for e in enemies:
            if e["hp"] <= 0:
                continue
            if orb["pos"].distance_to(e["pos"]) < e["radius"] + 6:
                e["hp"] -= damage
                orb["life"] = 0
                break

    for e in enemies:
        if e["hp"] <= 0 and e.get("drop"):
            e["drop"] = False
            gems.append({"pos": pygame.Vector2(e["pos"]), "value": 3})
    enemies = [e for e in enemies if e["hp"] > 0]

    for gem in gems[:]:
        if gem["pos"].distance_to(player_pos) < PLAYER_RADIUS + 10:
            gems.remove(gem)

    screen.fill((12, 14, 28))
    pygame.draw.rect(screen, (30, 36, 58), (MARGIN, MARGIN, WIDTH - 2 * MARGIN, HEIGHT - 2 * MARGIN), 2)
    for gem in gems:
        pygame.draw.circle(screen, (80, 230, 255), (int(gem["pos"].x), int(gem["pos"].y)), 6)
    for orb in orbs:
        pygame.draw.circle(screen, (255, 255, 170), (int(orb["pos"].x), int(orb["pos"].y)), 5)
    for e in enemies:
        pygame.draw.circle(screen, (90, 70, 140), (int(e["pos"].x), int(e["pos"].y)), e["radius"])
    pygame.draw.circle(screen, (255, 210, 80), (int(px), int(py)), PLAYER_RADIUS)
    hud = font.render(f"Orbs auto-aim · Gems {len(gems)}", True, (190, 200, 240))
    screen.blit(hud, (12, 12))

    pygame.display.flip()

pygame.quit()