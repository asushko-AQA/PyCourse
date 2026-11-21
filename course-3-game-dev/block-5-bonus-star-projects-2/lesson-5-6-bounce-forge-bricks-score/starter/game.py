# game.py — Lesson 5.6: Bounce Forge — bricks (starter)
import math

import pygame

pygame.init()

WIDTH = 720
HEIGHT = 540
PLAY_TOP = 72
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounce Forge — Ember Bricks")

clock = pygame.time.Clock()
running = True

font_small = pygame.font.Font(None, 28)

BALL_R = 11
PADDLE_W = 120
PADDLE_H = 14
PADDLE_Y = HEIGHT - 36
paddle_speed = 420.0
BRICK_W = 64
BRICK_H = 22
BRICK_GAP = 6

ball_x = WIDTH / 2
ball_y = HEIGHT - 120
ball_vx = 180.0
ball_vy = -240.0
prev_ball_x = ball_x
prev_ball_y = ball_y

paddle = pygame.Rect(WIDTH // 2 - PADDLE_W // 2, PADDLE_Y, PADDLE_W, PADDLE_H)
score = 0

# TODO: build bricks as a list of pygame.Rect rows (see solution pattern helper)
bricks: list[pygame.Rect] = []


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
    global ball_vx, ball_vy, ball_y
    ball_rect = pygame.Rect(0, 0, BALL_R * 2, BALL_R * 2)
    ball_rect.center = (int(ball_x), int(ball_y))
    if ball_vy > 0 and ball_rect.colliderect(paddle):
        ball_vy = -abs(ball_vy)
        ball_y = paddle.top - BALL_R


def bricks_collision() -> None:
    """TODO: detect side, flip vx or vy, remove brick, score += 10."""
    pass


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        paddle.x -= int(paddle_speed * dt)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        paddle.x += int(paddle_speed * dt)
    paddle.clamp_ip(screen.get_rect().inflate(0, -60))

    prev_ball_x, prev_ball_y = ball_x, ball_y
    ball_x += ball_vx * dt
    ball_y += ball_vy * dt
    bounce_walls()
    paddle_bounce()
    bricks_collision()

    screen.fill((14, 10, 18))
    for brick in bricks:
        pygame.draw.rect(screen, (240, 120, 60), brick, border_radius=3)
    pygame.draw.rect(screen, (150, 155, 175), paddle, border_radius=4)
    pygame.draw.circle(screen, (255, 220, 120), (int(ball_x), int(ball_y)), BALL_R)
    hud = font_small.render(f"Score {score}", True, (220, 200, 170))
    screen.blit(hud, (12, 10))
    pygame.display.flip()

pygame.quit()