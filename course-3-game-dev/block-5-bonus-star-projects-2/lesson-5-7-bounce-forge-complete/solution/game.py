# game.py — Lesson 5.7: Bounce Forge — complete Breakout + optional Pong
from __future__ import annotations

import math

import pygame

pygame.init()

WIDTH = 720
HEIGHT = 560
PLAY_TOP = 72
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounce Forge")

clock = pygame.time.Clock()
running = True

font_big = pygame.font.Font(None, 56)
font_small = pygame.font.Font(None, 28)

START = "start"
PLAYING = "playing"
WIN = "win"
GAME_OVER = "game_over"
PONG = "pong"
state = START

BALL_R = 11
PADDLE_W = 120
PADDLE_H = 14
PADDLE_Y = HEIGHT - 42
BRICK_W = 64
BRICK_H = 22
BRICK_GAP = 6

paddle_speed = 420.0
lives = 3
score = 0
high_score = 0
level_index = 0
pong_mode = False
pong_score_p1 = 0
pong_score_p2 = 0

ball_x = WIDTH / 2
ball_y = HEIGHT - 140
ball_vx = 0.0
ball_vy = 0.0
prev_ball_x = ball_x
prev_ball_y = ball_y
base_speed = 280.0

paddle = pygame.Rect(WIDTH // 2 - PADDLE_W // 2, PADDLE_Y, PADDLE_W, PADDLE_H)
paddle_top = pygame.Rect(WIDTH // 2 - PADDLE_W // 2, PLAY_TOP + 8, PADDLE_W, PADDLE_H)

BRICK_COLORS = [
    (220, 80, 60),
    (240, 120, 50),
    (255, 170, 70),
    (255, 210, 100),
]

LEVEL_PATTERNS = [
    ["111111111", "111111111", "111111111"],
    ["101010101", "010101010", "101010101", "011111110"],
    ["001111100", "011111110", "111111111", "011111110", "001111100"],
]


def make_level(patterns: list[str]) -> list[pygame.Rect]:
    bricks: list[pygame.Rect] = []
    cols = max(len(p) for p in patterns)
    for row, pattern in enumerate(patterns):
        start_x = (WIDTH - cols * (BRICK_W + BRICK_GAP)) // 2
        y = PLAY_TOP + row * (BRICK_H + BRICK_GAP)
        for c, ch in enumerate(pattern):
            if ch == "1":
                bricks.append(
                    pygame.Rect(start_x + c * (BRICK_W + BRICK_GAP), y, BRICK_W, BRICK_H)
                )
    return bricks


bricks: list[pygame.Rect] = []


def speed_for_level() -> float:
    return base_speed + level_index * 25 + score * 0.15


def draw_forge_bg(surface: pygame.Surface) -> None:
    surface.fill((14, 10, 18))
    pygame.draw.rect(surface, (35, 26, 32), (0, PLAY_TOP - 8, WIDTH, HEIGHT - PLAY_TOP - 50))
    for row in range(PLAY_TOP, HEIGHT - 60, 36):
        pygame.draw.line(surface, (50, 40, 52), (0, row), (WIDTH, row), 1)


def draw_brick(surface: pygame.Surface, rect: pygame.Rect, color: tuple[int, int, int]) -> None:
    pygame.draw.rect(surface, color, rect, border_radius=4)
    pygame.draw.rect(surface, (255, 235, 200), rect.inflate(-8, -10), border_radius=2)


def draw_spark_ball(surface: pygame.Surface, x: float, y: float, pulse: float) -> None:
    glow = int(5 + 3 * pulse)
    cx, cy = int(x), int(y)
    pygame.draw.circle(surface, (255, 110, 40), (cx, cy), BALL_R + glow)
    pygame.draw.circle(surface, (255, 230, 140), (cx, cy), BALL_R)


def draw_anvil(surface: pygame.Surface, rect: pygame.Rect) -> None:
    pygame.draw.rect(surface, (90, 95, 115), rect, border_radius=4)
    pygame.draw.rect(surface, (170, 175, 195), rect.inflate(-6, -8), border_radius=3)


def brick_hit_side(prev_x: float, prev_y: float, x: float, y: float, brick: pygame.Rect) -> str | None:
    if not brick.collidepoint(x, y):
        return None
    if brick.collidepoint(prev_x, prev_y):
        return "top"
    dx = min(abs(x - brick.left), abs(brick.right - x))
    dy = min(abs(y - brick.top), abs(brick.bottom - y))
    return "left" if dx < dy else "top"


def bounce_walls_breakout() -> None:
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


def bounce_walls_pong() -> None:
    global ball_x, ball_vx
    if ball_x - BALL_R <= 0:
        ball_x = BALL_R
        ball_vx = abs(ball_vx)
    elif ball_x + BALL_R >= WIDTH:
        ball_x = WIDTH - BALL_R
        ball_vx = -abs(ball_vx)


def paddle_bounce(rect: pygame.Rect, upward: bool) -> None:
    global ball_vx, ball_vy, ball_y
    ball_rect = pygame.Rect(0, 0, BALL_R * 2, BALL_R * 2)
    ball_rect.center = (int(ball_x), int(ball_y))
    if not ball_rect.colliderect(rect):
        return
    hit_frac = (ball_x - rect.centerx) / (rect.width / 2)
    hit_frac = max(-1.0, min(1.0, hit_frac))
    spd = speed_for_level()
    ball_vx = hit_frac * spd * 0.95
    if upward:
        if ball_vy > 0:
            ball_vy = -max(220.0, spd * 0.85)
            ball_y = rect.top - BALL_R - 1
    else:
        if ball_vy < 0:
            ball_vy = max(220.0, spd * 0.85)
            ball_y = rect.bottom + BALL_R + 1


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


def reset_ball_serve() -> None:
    global ball_x, ball_y, ball_vx, ball_vy
    ball_x = WIDTH / 2
    ball_y = HEIGHT / 2
    ball_vx = 160.0
    ball_vy = -speed_for_level() if not pong_mode else -240.0


def load_level(index: int) -> None:
    global bricks, level_index
    level_index = index % len(LEVEL_PATTERNS)
    bricks = make_level(LEVEL_PATTERNS[level_index])


def start_breakout() -> None:
    global state, lives, score, pong_mode
    pong_mode = False
    lives = 3
    score = 0
    load_level(0)
    reset_ball_serve()
    state = PLAYING


def start_pong() -> None:
    global state, pong_mode, pong_score_p1, pong_score_p2, bricks
    pong_mode = True
    pong_score_p1 = pong_score_p2 = 0
    bricks = []
    paddle.centery = HEIGHT // 2 + 120
    paddle_top.centery = HEIGHT // 2 - 120
    reset_ball_serve()
    state = PONG


def crash_life() -> None:
    global lives, state
    lives -= 1
    if lives <= 0:
        state = GAME_OVER
    else:
        reset_ball_serve()


def step_breakout(dt: float) -> None:
    global ball_x, ball_y, prev_ball_x, prev_ball_y, state, level_index, high_score
    prev_ball_x, prev_ball_y = ball_x, ball_y
    ball_x += ball_vx * dt
    ball_y += ball_vy * dt
    bounce_walls_breakout()
    paddle_bounce(paddle, upward=True)
    bricks_collision()
    if ball_y - BALL_R > HEIGHT:
        crash_life()
    if score > high_score:
        high_score = score
    if not bricks and state == PLAYING:
        if level_index + 1 < len(LEVEL_PATTERNS):
            load_level(level_index + 1)
            reset_ball_serve()
        else:
            state = WIN


def step_pong(dt: float) -> None:
    global ball_x, ball_y, ball_vx, ball_vy, pong_score_p1, pong_score_p2, state
    ball_x += ball_vx * dt
    ball_y += ball_vy * dt
    bounce_walls_pong()
    paddle_bounce(paddle, upward=False)
    paddle_bounce(paddle_top, upward=True)
    if ball_y - BALL_R < 0:
        pong_score_p2 += 1
        reset_ball_serve()
    elif ball_y + BALL_R > HEIGHT:
        pong_score_p1 += 1
        reset_ball_serve()
    if pong_score_p1 >= 5 or pong_score_p2 >= 5:
        state = WIN


while running:
    dt = clock.tick(60) / 1000
    pulse = (pygame.time.get_ticks() % 900) / 900

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if state == START:
                if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                    start_breakout()
                elif event.key == pygame.K_p:
                    start_pong()
            elif state in (GAME_OVER, WIN) and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                state = START
            elif event.key == pygame.K_p and state == START:
                start_pong()

    keys = pygame.key.get_pressed()
    if state == PLAYING:
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            paddle.x -= int(paddle_speed * dt)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            paddle.x += int(paddle_speed * dt)
        paddle.clamp_ip(screen.get_rect().inflate(0, -80))
        step_breakout(dt)
    elif state == PONG:
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            paddle.x -= int(paddle_speed * dt)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            paddle.x += int(paddle_speed * dt)
        if keys[pygame.K_q]:
            paddle_top.x -= int(paddle_speed * dt)
        if keys[pygame.K_e]:
            paddle_top.x += int(paddle_speed * dt)
        paddle.clamp_ip(screen.get_rect().inflate(0, -40))
        paddle_top.clamp_ip(screen.get_rect().inflate(0, -40))
        step_pong(dt)

    draw_forge_bg(screen)
    for i, brick in enumerate(bricks):
        draw_brick(screen, brick, BRICK_COLORS[i % len(BRICK_COLORS)])
    if state in (PLAYING, PONG):
        draw_anvil(screen, paddle)
    if state == PONG:
        draw_anvil(screen, paddle_top)
    if state in (PLAYING, PONG):
        draw_spark_ball(screen, ball_x, ball_y, pulse)

    if state == PLAYING:
        hud = font_small.render(
            f"Score {score}  |  Best {high_score}  |  Lv {level_index + 1}  |  Lives {lives}",
            True,
            (220, 200, 170),
        )
        screen.blit(hud, (12, 10))
    elif state == PONG:
        hud = font_small.render(
            f"Pong — You {pong_score_p1}  :  Forge {pong_score_p2}  (Q/E top paddle)",
            True,
            (220, 200, 170),
        )
        screen.blit(hud, (12, 10))
    elif state == START:
        title = font_big.render("Bounce Forge", True, (255, 180, 90))
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50)))
        sub = font_small.render(
            "SPACE — Breakout   |   P — 2-player Pong",
            True,
            (190, 180, 200),
        )
        screen.blit(sub, sub.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        best = font_small.render(f"Session best score: {high_score}", True, (255, 220, 150))
        screen.blit(best, best.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40)))
    elif state == WIN:
        msg = "Forge cleared!" if not pong_mode else "Pong champion!"
        won = font_big.render(msg, True, (140, 255, 180))
        screen.blit(won, won.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20)))
        sub = font_small.render("SPACE — back to title", True, (200, 190, 210))
        screen.blit(sub, sub.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30)))
    elif state == GAME_OVER:
        over = font_big.render("Sparks out!", True, (255, 120, 100))
        screen.blit(over, over.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20)))
        final = font_small.render(f"Score {score}  |  Best {high_score}", True, (220, 200, 170))
        screen.blit(final, final.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))
        sub = font_small.render("SPACE — title", True, (180, 170, 190))
        screen.blit(sub, sub.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50)))

    pygame.display.flip()

pygame.quit()