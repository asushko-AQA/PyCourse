# game.py — Lesson 5.5: Bounce Forge — anvil paddle + lives
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
    pygame.draw.rect(surface, (35, 28, 38), (0, PLAY_TOP, WIDTH, HEIGHT - PLAY_TOP - 50))
    for row in range(PLAY_TOP, HEIGHT - 50, 36):
        pygame.draw.line(surface, (45, 36, 50), (0, row), (WIDTH, row), 1)


def draw_spark_ball(surface: pygame.Surface, x: float, y: float) -> None:
    cx, cy = int(x), int(y)
    pygame.draw.circle(surface, (255, 120, 40), (cx, cy), BALL_R + 5)
    pygame.draw.circle(surface, (255, 230, 130), (cx, cy), BALL_R)


def draw_anvil(surface: pygame.Surface, rect: pygame.Rect) -> None:
    pygame.draw.rect(surface, (90, 95, 110), rect, border_radius=4)
    pygame.draw.rect(surface, (160, 165, 180), rect.inflate(-4, -6), border_radius=3)
    notch = pygame.Rect(rect.centerx - 8, rect.top - 6, 16, 8)
    pygame.draw.rect(surface, (70, 75, 90), notch, border_radius=2)


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
    global ball_vx, ball_vy, ball_y, lives
    ball_rect = pygame.Rect(0, 0, BALL_R * 2, BALL_R * 2)
    ball_rect.center = (int(ball_x), int(ball_y))
    if ball_vy > 0 and ball_rect.colliderect(paddle) and ball_y < paddle.centery:
        hit_frac = (ball_x - paddle.centerx) / (paddle.width / 2)
        hit_frac = max(-1.0, min(1.0, hit_frac))
        speed = math.hypot(ball_vx, ball_vy)
        ball_vx = hit_frac * speed * 0.9
        ball_vy = -max(200.0, speed * 0.85)
        ball_y = paddle.top - BALL_R - 1


def check_miss() -> None:
    global lives, ball_x, ball_y, ball_vx, ball_vy
    if ball_y - BALL_R > HEIGHT:
        lives -= 1
        ball_x = WIDTH / 2
        ball_y = HEIGHT / 2
        ball_vx = 200.0
        ball_vy = -220.0


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
    paddle.bottom = PADDLE_Y + PADDLE_H

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

    hud = font_small.render(f"Lives {lives}  |  hit angle from paddle center", True, (220, 200, 170))
    screen.blit(hud, (12, 10))
    if lives <= 0:
        over = font_small.render("Out of sparks — close window or restart Python", True, (255, 140, 120))
        screen.blit(over, over.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
    pygame.display.flip()

pygame.quit()