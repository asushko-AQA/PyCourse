# game.py — Lesson 5.36: Lane Rush — traffic spawns (starter)
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


def draw_player_car(surf: pygame.Surface, cx: float) -> None:
    body = pygame.Rect(0, 0, CAR_W, CAR_H)
    body.center = (int(cx), PLAYER_Y)
    pygame.draw.rect(surf, (80, 240, 255), body, border_radius=8)


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

    # TODO: lane keys, scroll_offset, lerp player_x (copy from 5.35)
    # TODO: spawn_timer — append traffic dict with random lane at top; move each car down with TRAFFIC_SPEED * dt
    # TODO: colliderect player vs traffic → game_over; distance_m += SCROLL_SPEED * dt * 0.12
    # TODO: remove off-screen traffic; R key restarts when game_over

    draw_road(screen, scroll_offset)
  # TODO: draw traffic shapes (see solution)
    draw_player_car(screen, player_x)
    hint = font.render("Finish TODOs — spawn, collide, distance!", True, (200, 210, 255))
    screen.blit(hint, (12, 12))
    pygame.display.flip()

pygame.quit()