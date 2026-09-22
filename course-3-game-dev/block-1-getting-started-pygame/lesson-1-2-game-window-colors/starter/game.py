# game.py — Lesson 1.2: fill the window; change colors each frame
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Caster")

clock = pygame.time.Clock()
running = True

# Start RGB values (red, green, blue) — each 0–255
r = 40
g = 80
b = 160

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO: Fill the whole screen with the current (r, g, b) color
    # screen.fill((r, g, b))

    # TODO: Nudge the color each frame (try +1 on r, or cycle another channel)
    # Hint: keep values in 0–255, e.g. r = (r + 1) % 256

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
