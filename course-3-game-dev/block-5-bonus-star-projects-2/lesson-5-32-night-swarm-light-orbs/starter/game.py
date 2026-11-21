# game.py — Lesson 5.32: Night Swarm — light orbs (starter)
from __future__ import annotations

import random

import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
MARGIN = 22
PLAYER_SPEED = 185
PLAYER_RADIUS = 14

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Night Swarm — Orb Sentinel")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

player_pos = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
enemies: list[dict] = []
orbs: list[dict] = []
gems: list[dict] = []
rng = random.Random()
running = True


def direction_toward(ax: float, ay: float, bx: float, by: float) -> pygame.Vector2:
    d = pygame.Vector2(bx - ax, by - ay)
    if d.length_squared() > 0:
        return d.normalize()
    return d


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    move = pygame.Vector2(0, 0)
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        move.x -= 1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        move.x += 1
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        move.y -= 1
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        move.y += 1
    if move.length_squared() > 0:
        move = move.normalize()
    player_pos += move * PLAYER_SPEED * dt

    # TODO: keep prior lesson spawns + chase + HP
    # TODO: nearest_enemy_index + auto fire orbs on cooldown
    # TODO: enemy hp; orb hits reduce hp; drop XP gems on defeat

    screen.fill((12, 14, 28))
    pygame.draw.circle(screen, (255, 210, 80), (int(player_pos.x), int(player_pos.y)), PLAYER_RADIUS)
    hint = font.render("TODO: auto light orbs, enemy HP, XP gems", True, (190, 200, 240))
    screen.blit(hint, (12, 12))

    pygame.display.flip()

pygame.quit()