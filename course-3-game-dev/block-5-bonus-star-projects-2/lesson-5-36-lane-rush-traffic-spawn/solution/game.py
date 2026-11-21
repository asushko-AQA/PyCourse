# game.py — Lesson 5.36: Lane Rush — traffic spawns (solution)
from __future__ import annotations

import random

import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
ROAD_LEFT = 140
ROAD_WIDTH = 360
NUM_LANES = 4
LANE_W = ROAD_WIDTH // NUM_LANES
STRIPE_H = 44
SCROLL_SPEED = 190.0
TRAFFIC_SPEED = 240.0
SPAWN_EVERY = 1.05
PLAYER_Y = HEIGHT - 78
CAR_W, CAR_H = 42, 68
TRAFFIC_W, TRAFFIC_H = 40, 62
LANE_LERP = 14.0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lane Rush — Traffic Tide")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

player_lane = 1
player_x = 0.0
scroll_offset = 0.0
distance_m = 0.0
spawn_timer = 0.4
traffic: list[dict] = []
game_over = False
rng = random.Random()
running = True


def lane_center(lane: int) -> float:
    return ROAD_LEFT + lane * LANE_W + LANE_W / 2


def draw_road(surf: pygame.Surface, offset: float) -> None:
    surf.fill((18, 12, 32))
    pygame.draw.rect(surf, (32, 34, 52), (ROAD_LEFT, 0, ROAD_WIDTH, HEIGHT))
    y = -STRIPE_H + (offset % STRIPE_H)
    while y < HEIGHT:
        stripe = pygame.Rect(ROAD_LEFT + 12, int(y), ROAD_WIDTH - 24, STRIPE_H // 2)
        pygame.draw.rect(surf, (240, 230, 90), stripe, border_radius=3)
        y += STRIPE_H
    for i in range(1, NUM_LANES):
        lx = ROAD_LEFT + i * LANE_W
        pygame.draw.line(surf, (55, 58, 78), (lx, 0), (lx, HEIGHT), 1)


def draw_player_car(surf: pygame.Surface, cx: float) -> None:
    body = pygame.Rect(0, 0, CAR_W, CAR_H)
    body.center = (int(cx), PLAYER_Y)
    pygame.draw.rect(surf, (80, 240, 255), body, border_radius=8)
    pygame.draw.rect(surf, (180, 255, 255), (body.x + 6, body.y + 10, body.w - 12, 18), border_radius=4)


def draw_traffic_car(surf: pygame.Surface, cx: float, cy: float) -> None:
    body = pygame.Rect(0, 0, TRAFFIC_W, TRAFFIC_H)
    body.center = (int(cx), int(cy))
    pygame.draw.rect(surf, (255, 110, 150), body, border_radius=6)
    pygame.draw.rect(surf, (255, 180, 200), (body.x + 5, body.y + 8, body.w - 10, 14), border_radius=3)


def player_rect() -> pygame.Rect:
    r = pygame.Rect(0, 0, CAR_W - 4, CAR_H - 4)
    r.center = (int(player_x), PLAYER_Y)
    return r


player_x = lane_center(player_lane)

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key in (pygame.K_LEFT, pygame.K_a) and player_lane > 0:
                player_lane -= 1
            if event.key in (pygame.K_RIGHT, pygame.K_d) and player_lane < NUM_LANES - 1:
                player_lane += 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r and game_over:
            game_over = False
            traffic.clear()
            distance_m = 0.0
            spawn_timer = 0.3
            player_lane = 1
            player_x = lane_center(player_lane)

    if not game_over:
        scroll_offset = (scroll_offset + SCROLL_SPEED * dt) % STRIPE_H
        distance_m += SCROLL_SPEED * dt * 0.12
        target_x = lane_center(player_lane)
        player_x += (target_x - player_x) * min(1.0, LANE_LERP * dt)

        spawn_timer -= dt
        if spawn_timer <= 0:
            spawn_timer = SPAWN_EVERY
            lane = rng.randint(0, NUM_LANES - 1)
            traffic.append({"lane": lane, "y": -TRAFFIC_H, "cy": float(-TRAFFIC_H)})

        pr = player_rect()
        for car in traffic:
            car["cy"] += TRAFFIC_SPEED * dt
            cx = lane_center(car["lane"])
            tr = pygame.Rect(0, 0, TRAFFIC_W - 4, TRAFFIC_H - 4)
            tr.center = (int(cx), int(car["cy"]))
            if pr.colliderect(tr):
                game_over = True
        traffic = [c for c in traffic if c["cy"] < HEIGHT + TRAFFIC_H]

    draw_road(screen, scroll_offset)
    for car in traffic:
        draw_traffic_car(screen, lane_center(car["lane"]), car["cy"])
    draw_player_car(screen, player_x)
    hud = font.render(f"Distance {distance_m:.0f} m", True, (210, 220, 255))
    screen.blit(hud, (12, 12))
    if game_over:
        over = font.render("CRASH — press R", True, (255, 120, 140))
        screen.blit(over, (WIDTH // 2 - 90, HEIGHT // 2))
    pygame.display.flip()

pygame.quit()