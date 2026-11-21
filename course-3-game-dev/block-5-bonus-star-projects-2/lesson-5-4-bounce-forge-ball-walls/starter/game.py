# game.py — Lesson 5.4: Bounce Forge — spark ball (starter)
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
# TODO: position and velocity as floats; velocity is a 2D vector (vx, vy)
ball_x = WIDTH / 2
ball_y = HEIGHT / 2
ball_vx = 240.0
ball_vy = -190.0


def draw_forge_bg(surface: pygame.Surface) -> None:
    surface.fill((14, 10, 18))
    for row in range(0, HEIGHT, 40):
        pygame.draw.line(surface, (28, 22, 32), (0, row), (WIDTH, row), 1)


def draw_spark_ball(surface: pygame.Surface, x: float, y: float) -> None:
    cx, cy = int(x), int(y)
    pygame.draw.circle(surface, (255, 120, 40), (cx, cy), BALL_R + 6)
    pygame.draw.circle(surface, (255, 220, 120), (cx, cy), BALL_R)


def bounce_walls() -> None:
    """TODO: flip vx when touching left/right; flip vy on top/bottom; clamp position."""
    pass


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO: move ball with ball_vx * dt and ball_vy * dt, then bounce_walls()

    draw_forge_bg(screen)
    draw_spark_ball(screen, ball_x, ball_y)
    hud = font_small.render("Finish bounce_walls() + motion!", True, (220, 200, 170))
    screen.blit(hud, (12, 10))
    pygame.display.flip()

pygame.quit()