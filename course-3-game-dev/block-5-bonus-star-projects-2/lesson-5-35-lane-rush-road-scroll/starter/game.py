# game.py — Lesson 5.35: Lane Rush — road scroll & lanes (starter)
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
  # TODO: return center x for this lane index
    return ROAD_LEFT


def draw_road(surf: pygame.Surface, offset: float) -> None:
    surf.fill((18, 12, 32))
    road = pygame.Rect(ROAD_LEFT, 0, ROAD_WIDTH, HEIGHT)
    pygame.draw.rect(surf, (32, 34, 52), road)
    # TODO: draw repeating yellow stripes using offset and STRIPE_H (loop y down screen)
    # TODO: draw dashed lane dividers for NUM_LANES - 1 lines


def draw_player_car(surf: pygame.Surface, cx: float) -> None:
    body = pygame.Rect(0, 0, CAR_W, CAR_H)
    body.center = (int(cx), PLAYER_Y)
    pygame.draw.rect(surf, (80, 240, 255), body, border_radius=8)


player_x = lane_center(player_lane)

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # TODO: KEYDOWN LEFT/A and RIGHT/D change player_lane (clamp 0..NUM_LANES-1)

    # TODO: scroll_offset = (scroll_offset + SCROLL_SPEED * dt) % STRIPE_H
    # TODO: player_x += (lane_center(player_lane) - player_x) * min(1.0, LANE_LERP * dt)

    draw_road(screen, scroll_offset)
    draw_player_car(screen, player_x)
    hint = font.render("Finish TODOs — stripes scroll, lanes lerp!", True, (200, 210, 255))
    screen.blit(hint, (12, 12))
    pygame.display.flip()

pygame.quit()