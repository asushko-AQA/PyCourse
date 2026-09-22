# game.py — Lesson 2.1: move a player square with arrow keys
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Key Captain")

clock = pygame.time.Clock()
running = True

x = 295.0
y = 215.0
box_w = 50
box_h = 50
speed = 250  # pixels per second

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x = x - speed * dt
    if keys[pygame.K_RIGHT]:
        x = x + speed * dt
    if keys[pygame.K_UP]:
        y = y - speed * dt
    if keys[pygame.K_DOWN]:
        y = y + speed * dt

    # Clamp so the box stays on screen
    x = max(0, min(x, WIDTH - box_w))
    y = max(0, min(y, HEIGHT - box_h))

    screen.fill((20, 24, 40))
    pygame.draw.rect(screen, (255, 200, 50), (int(x), int(y), box_w, box_h))
    pygame.display.flip()

pygame.quit()
