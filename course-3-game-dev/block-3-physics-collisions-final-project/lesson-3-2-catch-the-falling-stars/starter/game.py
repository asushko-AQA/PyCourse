# game.py — Lesson 3.2: Catch the Falling Stars (capstone)
import pygame
import os
import random

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Star Catcher")

clock = pygame.time.Clock()
running = True

HERE = os.path.dirname(os.path.abspath(__file__))
star_img = pygame.image.load(os.path.join(HERE, "star.png")).convert_alpha()

font_big = pygame.font.Font(None, 64)
font_small = pygame.font.Font(None, 32)

START = "start"
PLAYING = "playing"
GAME_OVER = "game_over"
# TODO: Begin on the title screen
# state = START
state = PLAYING  # temporary — change to START when screens are wired

paddle_w, paddle_h = 100, 18
paddle = pygame.Rect(0, 0, paddle_w, paddle_h)
paddle.midbottom = (WIDTH // 2, HEIGHT - 24)
paddle_speed = 360

star = star_img.get_rect()
fall_speed = 180

score = 0
misses = 0
MAX_MISSES = 3


def reset_star():
    star.size = star_img.get_size()
    star.midtop = (random.randint(20, WIDTH - 20), -40)


def start_round():
    global score, misses, fall_speed, state
    score = 0
    misses = 0
    fall_speed = 180
    paddle.midbottom = (WIDTH // 2, HEIGHT - 24)
    reset_star()
    state = PLAYING


reset_star()

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # TODO: SPACE / RETURN — start round from START; return to START from GAME_OVER
        # if event.type == pygame.KEYDOWN:
        #     if state == START and event.key in (pygame.K_SPACE, pygame.K_RETURN):
        #         start_round()
        #     elif state == GAME_OVER and event.key in (pygame.K_SPACE, pygame.K_RETURN):
        #         state = START

    screen.fill((10, 12, 28))

    if state == START:
        title = font_big.render("Catch the Stars!", True, (255, 220, 80))
        hint = font_small.render("Press SPACE to start", True, (200, 200, 220))
        tip = font_small.render("LEFT / RIGHT to catch — 3 misses = game over", True, (160, 170, 200))
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50)))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))
        screen.blit(tip, tip.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60)))

    elif state == PLAYING:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.x -= int(paddle_speed * dt)
        if keys[pygame.K_RIGHT]:
            paddle.x += int(paddle_speed * dt)
        paddle.clamp_ip(screen.get_rect())

        # TODO: Move the star downward using fall_speed * dt
        # star.y += int(fall_speed * dt)

        # TODO: Catch → score += 1 and reset_star()
        #       Miss (star.top > HEIGHT) → misses += 1; if misses >= MAX_MISSES → GAME_OVER
        # if paddle.colliderect(star):
        #     score += 1
        #     reset_star()
        # elif star.top > HEIGHT:
        #     misses += 1
        #     reset_star()
        #     if misses >= MAX_MISSES:
        #         state = GAME_OVER

        pygame.draw.rect(screen, (90, 210, 255), paddle, border_radius=6)
        screen.blit(star_img, star)
        hud = font_small.render(
            f"Score: {score}   Misses: {misses}/{MAX_MISSES}",
            True,
            (255, 255, 255),
        )
        screen.blit(hud, (16, 12))

    elif state == GAME_OVER:
        over = font_big.render("Game Over", True, (255, 100, 100))
        final = font_small.render(f"Stars caught: {score}", True, (255, 255, 255))
        hint = font_small.render("Press SPACE for title", True, (200, 200, 220))
        screen.blit(over, over.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50)))
        screen.blit(final, final.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10)))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50)))

    pygame.display.flip()

pygame.quit()
