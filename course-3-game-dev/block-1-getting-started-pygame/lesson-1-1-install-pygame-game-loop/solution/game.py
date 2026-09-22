# game.py — Lesson 1.1: open a window and quit cleanly
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My First Pygame Window")

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 80))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
