# game.py — Lesson 5.7: Bounce Forge — complete (starter)
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

# TODO: wire lives, score, high_score, level_index, LEVEL_PATTERNS from 5.6
lives = 3
score = 0
high_score = 0
bricks: list[pygame.Rect] = []

BALL_R = 11
PADDLE_W = 120
PADDLE_H = 14
paddle = pygame.Rect(WIDTH // 2 - PADDLE_W // 2, HEIGHT - 42, PADDLE_W, PADDLE_H)
paddle_speed = 420.0

ball_x = WIDTH / 2
ball_y = HEIGHT - 140
ball_vx = 200.0
ball_vy = -240.0
prev_ball_x = ball_x
prev_ball_y = ball_y


def start_breakout() -> None:
    """TODO: reset run vars, load level 0, state = PLAYING."""
    pass


def crash_life() -> None:
    """TODO: lives -= 1; game over or re-serve ball."""
    pass


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if state == START and event.key == pygame.K_SPACE:
                start_breakout()
            elif state in (GAME_OVER, WIN) and event.key == pygame.K_SPACE:
                state = START

    # TODO: paddle motion + breakout step when state == PLAYING
    # TODO: optional PONG mode with key P on title (see solution)

    screen.fill((14, 10, 18))
    for brick in bricks:
        pygame.draw.rect(screen, (240, 120, 60), brick, border_radius=3)
    pygame.draw.rect(screen, (150, 160, 180), paddle, border_radius=4)
    if state == PLAYING:
        pygame.draw.circle(screen, (255, 220, 120), (int(ball_x), int(ball_y)), BALL_R)

    if state == START:
        title = font_big.render("Bounce Forge", True, (255, 180, 90))
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30)))
        hint = font_small.render("Finish TODOs — SPACE to play", True, (200, 190, 210))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))
    elif state == PLAYING:
        hud = font_small.render(f"Score {score}  Lives {lives}", True, (220, 200, 170))
        screen.blit(hud, (12, 10))

    pygame.display.flip()

pygame.quit()