# game.py — Lesson 5.25: Leap Lands — player & jump (starter)
import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Leap Lands — Crystal Hop")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 32)

PLAYER_W, PLAYER_H = 28, 36
GROUND_Y = 400
MOVE_SPEED = 280
GRAVITY = 1200
JUMP_V = -420

player_x = 120.0
player_y = float(GROUND_Y - PLAYER_H)
vel_x = 0.0
vel_y = 0.0
grounded = False
running = True

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # TODO: on KEYDOWN SPACE, set vel_y = JUMP_V only when grounded

    keys = pygame.key.get_pressed()
    vel_x = 0.0
    # TODO: LEFT/RIGHT (or A/D) set vel_x using MOVE_SPEED and dt in the update below

    player_x += vel_x * dt
    player_x = max(0, min(WIDTH - PLAYER_W, player_x))

    # TODO: apply gravity (vel_y += GRAVITY * dt) and move player_y
    # TODO: snap to GROUND_Y when falling; set grounded True and vel_y = 0

    screen.fill((18, 22, 48))
    for stripe in range(0, WIDTH, 60):
        pygame.draw.rect(screen, (28, 34, 68), (stripe, 0, 30, GROUND_Y))

    pygame.draw.rect(screen, (55, 62, 95), (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))
    pygame.draw.line(screen, (120, 200, 255), (0, GROUND_Y), (WIDTH, GROUND_Y), 3)

    body = pygame.Rect(int(player_x), int(player_y), PLAYER_W, PLAYER_H)
    pygame.draw.rect(screen, (80, 240, 210), body, border_radius=6)

    hud = font.render("Finish TODOs — jump only on ground!", True, (210, 220, 255))
    screen.blit(hud, (12, 12))

    pygame.display.flip()

pygame.quit()