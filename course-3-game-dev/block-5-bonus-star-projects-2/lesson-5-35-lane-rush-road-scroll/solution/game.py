# game.py — Lesson 5.35: Lane Rush — road scroll & lanes (solution)
from __future__ import annotations

import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
ROAD_LEFT = 140
ROAD_WIDTH = 360
NUM_LANES = 4
LANE_W = ROAD_WIDTH // NUM_LANES
STRIPE_H = 44
SCROLL_SPEED = 180.0
PLAYER_Y = HEIGHT - 78
CAR_W, CAR_H = 42, 68
LANE_LERP = 14.0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lane Rush — Neon Stripes")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

player_lane = 1
player_x = 0.0
scroll_offset = 0.0
running = True


def lane_center(lane: int) -> float:
    return ROAD_LEFT + lane * LANE_W + LANE_W / 2


def draw_road(surf: pygame.Surface, offset: float) -> None:
    surf.fill((18, 12, 32))
    road = pygame.Rect(ROAD_LEFT, 0, ROAD_WIDTH, HEIGHT)
    pygame.draw.rect(surf, (32, 34, 52), road)
    pygame.draw.rect(surf, (90, 100, 150), road, 2)
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
    pygame.draw.circle(surf, (30, 40, 60), (body.left + 8, body.bottom - 6), 7)
    pygame.draw.circle(surf, (30, 40, 60), (body.right - 8, body.bottom - 6), 7)


player_x = lane_center(player_lane)

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_a) and player_lane > 0:
                player_lane -= 1
            if event.key in (pygame.K_RIGHT, pygame.K_d) and player_lane < NUM_LANES - 1:
                player_lane += 1

    scroll_offset = (scroll_offset + SCROLL_SPEED * dt) % STRIPE_H
    target_x = lane_center(player_lane)
    player_x += (target_x - player_x) * min(1.0, LANE_LERP * dt)

    draw_road(screen, scroll_offset)
    draw_player_car(screen, player_x)
    hint = font.render("Lanes ←/→ · smooth lerp · scrolling stripes", True, (200, 210, 255))
    screen.blit(hint, (12, 12))
    pygame.display.flip()

pygame.quit()