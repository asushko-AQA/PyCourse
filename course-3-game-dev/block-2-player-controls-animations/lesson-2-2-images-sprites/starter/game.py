# game.py — Lesson 2.2: replace the square with a sprite image
import pygame
import os

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Summoner")

clock = pygame.time.Clock()
running = True

# Folder of this script — so player.png loads no matter where you cd from
HERE = os.path.dirname(os.path.abspath(__file__))

# TODO: Load the sprite image (player.png sits next to this file)
# player = pygame.image.load(os.path.join(HERE, "player.png")).convert_alpha()
# player_rect = player.get_rect()
# player_rect.center = (WIDTH // 2, HEIGHT // 2)

# Temporary stand-in until you load the image:
player = None
player_rect = pygame.Rect(0, 0, 48, 48)
player_rect.center = (WIDTH // 2, HEIGHT // 2)

speed = 250  # pixels per second

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= int(speed * dt)
    if keys[pygame.K_RIGHT]:
        player_rect.x += int(speed * dt)
    if keys[pygame.K_UP]:
        player_rect.y -= int(speed * dt)
    if keys[pygame.K_DOWN]:
        player_rect.y += int(speed * dt)

    player_rect.clamp_ip(screen.get_rect())

    screen.fill((15, 18, 32))

    # TODO: Blit the sprite instead of drawing a rect
    # screen.blit(player, player_rect)
    pygame.draw.rect(screen, (60, 200, 180), player_rect)  # remove after blit works

    pygame.display.flip()

pygame.quit()
