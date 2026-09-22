# game.py — Lesson 1.2: fill the window; change colors each frame
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Caster")

clock = pygame.time.Clock()
running = True

r = 40
g = 80
b = 160

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((r, g, b))

    # Cycle red so the sky slowly shifts every frame
    r = (r + 1) % 256

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
