# game.py — Lesson 1.3: draw a rectangle and move it with x/y
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Box Voyager")

clock = pygame.time.Clock()
running = True

x = 100
y = 200
box_w = 50
box_h = 50
speed = 3

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x = x + speed
    # Wrap: when the box leaves the right edge, restart on the left
    if x > WIDTH:
        x = -box_w

    screen.fill((20, 24, 40))
    pygame.draw.rect(screen, (255, 200, 50), (x, y, box_w, box_h))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
