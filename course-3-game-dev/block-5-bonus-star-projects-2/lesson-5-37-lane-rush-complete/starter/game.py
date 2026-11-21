# game.py — Lesson 5.37: Lane Rush — complete (starter)
from __future__ import annotations

import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lane Rush — Pro")
clock = pygame.time.Clock()
font_big = pygame.font.Font(None, 52)
font = pygame.font.Font(None, 28)

state = "MENU"
running = True

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # TODO: MENU → PLAY on ENTER; PLAY lane keys; GAME_OVER/GRADUATE → MENU on R

    screen.fill((14, 10, 28))
    if state == "MENU":
        t1 = font_big.render("Lane Rush", True, (90, 250, 255))
        screen.blit(t1, (WIDTH // 2 - t1.get_width() // 2, 140))
        hint = font.render("Finish TODOs — full game in solution/game.py", True, (200, 210, 255))
        screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, 210))
        # TODO: speed ramp, fuel drain, coin/fuel pickups, near-miss bonus +25
        # TODO: session best in ~/.lane_rush_best.json
        # TODO: GRADUATE screen when distance >= 1200 m — celebrate Block 5 complete

    pygame.display.flip()

pygame.quit()