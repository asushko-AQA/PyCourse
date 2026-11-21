# game.py — Lesson 5.5: Bounce Forge — paddle (starter)
import math

import pygame

pygame.init()

WIDTH = 720
HEIGHT = 540
PLAY_TOP = 40
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounce Forge — Anvil Paddle")

clock = pygame.time.Clock()
running = True

font_small = pygame.font.Font(None, 28)

BALL_R = 11
PADDLE_W = 120
PADDLE_H = 14
PADDLE_Y = HEIGHT - 36
paddle_speed = 420.0

ball_x = WIDTH / 2
ball_y = HEIGHT / 2
ball_vx = 200.0
ball_vy = -220.0

paddle = pygame.Rect(WIDTH // 2 - PADDLE_W // 2, PADDLE_Y, PADDLE_W, PADDLE_H)
lives = 3


def draw_forge_bg(surface: pygame.Surface) -> None:
    surface.fill((14, 10, 18))


def draw_spark_ball(surface: pygame.Surface, x: float, y: float) -> None:
    pygame.draw.circle(surface, (255, 220, 120), (int(x), int(y)), BALL_R)


def draw_anvil(surface: pygame.Surface, rect: pygame.Rect) -> None:
    pygame.draw.rect(surface, (140, 150, 170), rect, border_radius=4)


def bounce_walls() -> None:
    global ball_x, ball_y, ball_vx, ball_vy
    if ball_x - BALL_R <= 0:
        ball_x = BALL_R
        ball_vx = abs(ball_vx)
    elif ball_x + BALL_R >= WIDTH:
        ball_x = WIDTH - BALL_R
        ball_vx = -abs(ball_vx)
    if ball_y - BALL_R <= PLAY_TOP:
        ball_y = PLAY_TOP + BALL_R
        ball_vy = abs(ball_vy)


def paddle_bounce() -> None:
    """TODO: on paddle hit while falling, set vx from hit_frac and vy upward."""
    pass


def check_miss() -> None:
    """TODO: if ball falls below window, subtract a life and reset ball center."""
    pass


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO: move paddle with A/D or arrows; clamp to screen width

    if lives > 0:
        ball_x += ball_vx * dt
        ball_y += ball_vy * dt
        bounce_walls()
        paddle_bounce()
        check_miss()

    draw_forge_bg(screen)
    draw_anvil(screen, paddle)
    if lives > 0:
        draw_spark_ball(screen, ball_x, ball_y)
    hud = font_small.render(f"Lives {lives}", True, (220, 200, 170))
    screen.blit(hud, (12, 10))
    pygame.display.flip()

pygame.quit()