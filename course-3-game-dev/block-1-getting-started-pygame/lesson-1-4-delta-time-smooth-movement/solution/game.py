# game.py — Lesson 1.4: frame-rate independent motion with delta time
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Time Slider")

clock = pygame.time.Clock()
running = True

x = 50.0
y = 220.0
box_w = 50
box_h = 50
speed = 200  # pixels per second

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x = x + speed * dt

    if x > WIDTH:
        x = -box_w

    screen.fill((15, 18, 32))
    pygame.draw.rect(screen, (80, 220, 180), (int(x), int(y), box_w, box_h))
    pygame.display.flip()

pygame.quit()
