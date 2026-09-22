# game.py — Lesson 3.1: rect.colliderect() — collect a coin
import pygame
import os
import random

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Collector")

clock = pygame.time.Clock()
running = True

HERE = os.path.dirname(os.path.abspath(__file__))

player = pygame.Rect(0, 0, 48, 48)
player.center = (WIDTH // 2, HEIGHT - 60)
speed = 280

coin_img = pygame.image.load(os.path.join(HERE, "coin.png")).convert_alpha()
coin = coin_img.get_rect()
coin.center = (random.randint(40, WIDTH - 40), random.randint(40, HEIGHT - 120))

score = 0
font = pygame.font.Font(None, 36)

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= int(speed * dt)
    if keys[pygame.K_RIGHT]:
        player.x += int(speed * dt)
    if keys[pygame.K_UP]:
        player.y -= int(speed * dt)
    if keys[pygame.K_DOWN]:
        player.y += int(speed * dt)

    player.clamp_ip(screen.get_rect())

    # TODO: If the player touches the coin, add 1 to score and move the coin
    # if player.colliderect(coin):
    #     score += 1
    #     coin.center = (
    #         random.randint(40, WIDTH - 40),
    #         random.randint(40, HEIGHT - 120),
    #     )

    screen.fill((18, 22, 40))
    pygame.draw.rect(screen, (80, 200, 255), player)
    screen.blit(coin_img, coin)
    score_surf = font.render(f"Coins: {score}", True, (255, 255, 255))
    screen.blit(score_surf, (16, 12))
    hint = font.render("Touch the coin!", True, (180, 190, 210))
    screen.blit(hint, (16, 48))

    pygame.display.flip()

pygame.quit()
