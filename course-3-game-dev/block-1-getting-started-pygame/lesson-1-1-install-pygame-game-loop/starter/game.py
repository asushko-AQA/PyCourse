# game.py — Lesson 1.1: open a window and quit cleanly
import pygame

pygame.init()

# TODO: Confirm size (640, 480) — try (800, 600) after it works
screen = pygame.display.set_mode((640, 480))

# TODO: Change the caption to your own game title
pygame.display.set_caption("My First Pygame Window")

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        # TODO: Understand this — QUIT means the player clicked the window X
        if event.type == pygame.QUIT:
            running = False

    # Deep blue fill so you see a real window (not a flash)
    screen.fill((30, 30, 80))

    # TODO: Without flip(), the window never shows your fill — keep this line!
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
