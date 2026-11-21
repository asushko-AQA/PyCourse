# game.py — Lesson 5.6: Bounce Forge — ember bricks + score
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

BRICK_COLORS = [
    (220, 80, 60),
    (240, 120, 50),
    (255, 170, 70),
    (255, 210, 100),
]


def make_brick_row(row: int, cols: int, pattern: str) -> list[pygame.Rect]:
    bricks: list[pygame.Rect] = []
    start_x = (WIDTH - cols * (BRICK_W + BRICK_GAP)) // 2
    y = PLAY_TOP + row * (BRICK_H + BRICK_GAP)
    for c, ch in enumerate(pattern):
        if ch == "1":
            bricks.append(pygame.Rect(start_x + c * (BRICK_W + BRICK_GAP), y, BRICK_W, BRICK_H))
    return bricks


bricks: list[pygame.Rect] = []
for i, row in enumerate(["111111111", "101010101", "111011111"]):
    bricks.extend(make_brick_row(i, 9, row))


def draw_forge_bg(surface: pygame.Surface) -> None:
    surface.fill((14, 10, 18))
    pygame.draw.rect(surface, (32, 24, 30), (0, PLAY_TOP - 8, WIDTH, HEIGHT - PLAY_TOP - 40))


def draw_brick(surface: pygame.Surface, rect: pygame.Rect, color: tuple[int, int, int]) -> None:
    pygame.draw.rect(surface, color, rect, border_radius=4)
    pygame.draw.rect(surface, (255, 240, 200), rect.inflate(-6, -8), border_radius=2)


def draw_spark_ball(surface: pygame.Surface, x: float, y: float) -> None:
    pygame.draw.circle(surface, (255, 120, 40), (int(x), int(y)), BALL_R + 4)
    pygame.draw.circle(surface, (255, 230, 140), (int(x), int(y)), BALL_R)


def draw_anvil(surface: pygame.Surface, rect: pygame.Rect) -> None:
    pygame.draw.rect(surface, (150, 155, 175), rect, border_radius=4)


def brick_hit_side(prev_x: float, prev_y: float, x: float, y: float, brick: pygame.Rect) -> str | None:
    if not brick.collidepoint(x, y):
        return None
    if brick.collidepoint(prev_x, prev_y):
        return "top"
    dx = min(abs(x - brick.left), abs(brick.right - x))
    dy = min(abs(y - brick.top), abs(brick.bottom - y))
    return "left" if dx < dy else "top"


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
    if ball_vy > 0 and ball_rect.colliderect(paddle) and ball_y < paddle.centery:
        hit_frac = (ball_x - paddle.centerx) / (paddle.width / 2)
        hit_frac = max(-1.0, min(1.0, hit_frac))
        speed = math.hypot(ball_vx, ball_vy)
        ball_vx = hit_frac * speed * 0.9
        ball_vy = -max(220.0, speed * 0.85)
        ball_y = paddle.top - BALL_R


def bricks_collision() -> None:
    global ball_vx, ball_vy, score
    for brick in bricks[:]:
        side = brick_hit_side(prev_ball_x, prev_ball_y, ball_x, ball_y, brick)
        if not side:
            continue
        if side in ("left", "right"):
            ball_vx = -ball_vx
        else:
            ball_vy = -ball_vy
        bricks.remove(brick)
        score += 10
        break


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

    if ball_y - BALL_R > HEIGHT:
        ball_x = WIDTH / 2
        ball_y = HEIGHT - 120
        ball_vx = 180.0
        ball_vy = -240.0

    draw_forge_bg(screen)
    for i, brick in enumerate(bricks):
        color = BRICK_COLORS[i % len(BRICK_COLORS)]
        draw_brick(screen, brick, color)
    draw_anvil(screen, paddle)
    draw_spark_ball(screen, ball_x, ball_y)
    hud = font_small.render(f"Score {score}  |  bricks {len(bricks)}", True, (220, 200, 170))
    screen.blit(hud, (12, 10))
    pygame.display.flip()

pygame.quit()