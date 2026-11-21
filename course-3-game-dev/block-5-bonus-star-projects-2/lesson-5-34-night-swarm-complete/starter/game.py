# game.py — Lesson 5.34: Night Swarm — complete (starter)
"""Starter: combat from 5.33 is sketched; finish waves, states, win timer, session best."""
from __future__ import annotations

import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
WIN_SURVIVE = 180.0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Night Swarm — Pro")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

state = "MENU"
elapsed = 0.0
player_pos = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
running = True

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # TODO: SPACE starts PLAY from MENU; ESC toggles PAUSE
        # TODO: survive WIN_SURVIVE seconds → WIN; HP 0 → GAME_OVER; R → MENU

    if state == "PLAY":
        # TODO: ramp spawn rate over elapsed; cap enemy count for performance
        # TODO: orbit upgrade, gem magnet, session best JSON in ~/.night_swarm_best.json
        elapsed += dt

    screen.fill((12, 14, 28))
    if state == "MENU":
        msg = font.render("TODO: full Night Swarm — see solution/game.py", True, (200, 210, 255))
        screen.blit(msg, msg.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
    else:
        pygame.draw.circle(screen, (255, 210, 80), (int(player_pos.x), int(player_pos.y)), 14)
        hud = font.render(f"state={state} t={elapsed:.1f}", True, (180, 190, 230))
        screen.blit(hud, (12, 12))

    pygame.display.flip()

pygame.quit()