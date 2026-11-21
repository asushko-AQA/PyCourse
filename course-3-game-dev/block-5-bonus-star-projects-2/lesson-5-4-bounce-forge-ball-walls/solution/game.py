# game.py — Lesson 5.4: Bounce Forge — spark ball + wall bounces
import math

import pygame

pygame.init()

WIDTH = 720
HEIGHT = 540
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounce Forge — Spark Ball")

clock = pygame.time.Clock()
running = True

font_small = pygame.font.Font(None, 28)

BALL_R = 11
ball_x = WIDTH / 2
ball_y = HEIGHT / 2
ball_vx = 240.0
ball_vy = -190.0

sparks: list[tuple[float, float, float]] = []


def draw_forge_bg(surface: pygame.Surface) -> None:
    surface.fill((14, 10, 18))
    for row in range(0, HEIGHT, 40):
        pygame.draw.line(surface, (28, 22, 32), (0, row), (WIDTH, row), 1)


def draw_spark_ball(surface: pygame.Surface, x: float, y: float, pulse: float) -> None:
    glow = int(6 + 4 * pulse)
    cx, cy = int(x), int(y)
    pygame.draw.circle(surface, (255, 120, 40), (cx, cy), BALL_R + glow)
    pygame.draw.circle(surface, (255, 220, 120), (cx, cy), BALL_R)
    pygame.draw.circle(surface, (255, 255, 200), (cx - 3, cy - 3), 3)


def burst_sparks(x: float, y: float) -> None:
    for i in range(6):
        angle = math.tau * i / 6
        sparks.append((x, y, angle))


def bounce_walls() -> None:
    global ball_x, ball_y, ball_vx, ball_vy
    if ball_x - BALL_R <= 0:
        ball_x = BALL_R
        ball_vx = abs(ball_vx)
        burst_sparks(ball_x, ball_y)
    elif ball_x + BALL_R >= WIDTH:
        ball_x = WIDTH - BALL_R
        ball_vx = -abs(ball_vx)
        burst_sparks(ball_x, ball_y)
    if ball_y - BALL_R <= 0:
        ball_y = BALL_R
        ball_vy = abs(ball_vy)
        burst_sparks(ball_x, ball_y)
    elif ball_y + BALL_R >= HEIGHT:
        ball_y = HEIGHT - BALL_R
        ball_vy = -abs(ball_vy)
        burst_sparks(ball_x, ball_y)


while running:
    dt = clock.tick(60) / 1000
    pulse = (pygame.time.get_ticks() % 800) / 800

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball_x += ball_vx * dt
    ball_y += ball_vy * dt
    bounce_walls()

    draw_forge_bg(screen)
    draw_spark_ball(screen, ball_x, ball_y, pulse)

    for i, (sx, sy, angle) in enumerate(sparks):
        life = 0.35
        px = sx + math.cos(angle) * 40 * life
        py = sy + math.sin(angle) * 40 * life
        pygame.draw.circle(screen, (255, 180, 60), (int(px), int(py)), 2)

    hud = font_small.render(f"vel=({ball_vx:.0f}, {ball_vy:.0f})", True, (220, 200, 170))
    screen.blit(hud, (12, 10))
    tip = font_small.render("Forge walls bounce the spark — no paddle yet", True, (140, 130, 150))
    screen.blit(tip, (12, HEIGHT - 28))
    pygame.display.flip()

pygame.quit()