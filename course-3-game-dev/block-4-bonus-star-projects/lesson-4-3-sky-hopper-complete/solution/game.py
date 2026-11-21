# game.py — Lesson 4.3: Sky Hopper — complete bonus mini-game
import pygame
import random

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sky Hopper")

clock = pygame.time.Clock()
running = True

font_big = pygame.font.Font(None, 64)
font_small = pygame.font.Font(None, 32)

START = "start"
PLAYING = "playing"
GAME_OVER = "game_over"
state = START

BIRD_X = 160
GRAVITY = 720
FLAP_STRENGTH = -280
PIPE_W = 72
GAP = 150
PIPE_SPACING = 220
BASE_SCROLL = 165

bird_y = HEIGHT // 2
vel_y = 0.0
bird_size = 28
bird = pygame.Rect(0, 0, bird_size, bird_size)
bird.center = (BIRD_X, int(bird_y))

score = 0
high_score = 0
scroll_speed = BASE_SCROLL

pipes: list[dict] = []


def draw_bird(surface: pygame.Surface, rect: pygame.Rect) -> None:
    cx, cy = rect.center
    pygame.draw.circle(surface, (255, 210, 70), (cx, cy), 14)
    pygame.draw.circle(surface, (30, 30, 40), (cx + 5, cy - 4), 3)
    pygame.draw.circle(surface, (250, 250, 255), (cx + 6, cy - 5), 1)
    pygame.draw.polygon(surface, (255, 130, 50), [(cx + 12, cy), (cx + 22, cy + 3), (cx + 12, cy + 7)])
    wing = pygame.Rect(cx - 18, cy + 2, 14, 9)
    pygame.draw.ellipse(surface, (255, 190, 90), wing)


def spawn_pipe() -> None:
    gap_y = random.randint(GAP // 2 + 40, HEIGHT - GAP // 2 - 40)
    pipes.append({"x": WIDTH + PIPE_W, "gap_y": gap_y, "scored": False})


def pipe_rects(pipe: dict) -> tuple[pygame.Rect, pygame.Rect]:
    top = pygame.Rect(pipe["x"], 0, PIPE_W, pipe["gap_y"] - GAP // 2)
    bottom = pygame.Rect(
        pipe["x"],
        pipe["gap_y"] + GAP // 2,
        PIPE_W,
        HEIGHT - (pipe["gap_y"] + GAP // 2),
    )
    return top, bottom


def draw_pipes(surface: pygame.Surface) -> None:
    for pipe in pipes:
        top, bottom = pipe_rects(pipe)
        pygame.draw.rect(surface, (60, 180, 90), top, border_radius=8)
        pygame.draw.rect(surface, (60, 180, 90), bottom, border_radius=8)
        cap_h = 16
        pygame.draw.rect(
            surface,
            (40, 140, 70),
            pygame.Rect(pipe["x"] - 4, top.bottom - cap_h, PIPE_W + 8, cap_h),
            border_radius=6,
        )
        pygame.draw.rect(
            surface,
            (40, 140, 70),
            pygame.Rect(pipe["x"] - 4, bottom.top, PIPE_W + 8, cap_h),
            border_radius=6,
        )


def start_round() -> None:
    global score, bird_y, vel_y, scroll_speed, state, pipes
    pipes.clear()
    spawn_pipe()
    score = 0
    bird_y = HEIGHT // 2
    vel_y = 0
    scroll_speed = BASE_SCROLL
    bird.center = (BIRD_X, int(bird_y))
    state = PLAYING


def crash() -> None:
    global state, high_score
    if score > high_score:
        high_score = score
    state = GAME_OVER


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if state == START and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                start_round()
            elif state == PLAYING and event.key == pygame.K_SPACE:
                vel_y = FLAP_STRENGTH
            elif state == GAME_OVER and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                state = START

    screen.fill((90, 165, 235))

    if state == START:
        title = font_big.render("Sky Hopper", True, (255, 235, 120))
        sub = font_small.render("Bonus ★ Project #1", True, (220, 235, 255))
        hint = font_small.render("SPACE to start", True, (30, 55, 95))
        best = font_small.render(f"Best: {high_score}", True, (30, 55, 95))
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 70)))
        screen.blit(sub, sub.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20)))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30)))
        screen.blit(best, best.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 70)))

    elif state == PLAYING:
        vel_y += GRAVITY * dt
        bird_y += vel_y * dt
        bird.center = (BIRD_X, int(bird_y))

        scroll_speed = BASE_SCROLL + score * 8

        for pipe in pipes:
            pipe["x"] -= int(scroll_speed * dt)
        pipes = [p for p in pipes if p["x"] > -PIPE_W]

        if not pipes or pipes[-1]["x"] < WIDTH - PIPE_SPACING:
            spawn_pipe()

        if bird.top < 0 or bird.bottom > HEIGHT:
            crash()
        else:
            for pipe in pipes:
                top, bottom = pipe_rects(pipe)
                if bird.colliderect(top) or bird.colliderect(bottom):
                    crash()
                    break
                if not pipe["scored"] and pipe["x"] + PIPE_W < bird.left:
                    pipe["scored"] = True
                    score += 1

        draw_pipes(screen)
        draw_bird(screen, bird)
        hud = font_small.render(
            f"Score: {score}  Best: {high_score}  Speed: {int(scroll_speed)}",
            True,
            (20, 50, 90),
        )
        screen.blit(hud, (16, 12))

    elif state == GAME_OVER:
        draw_pipes(screen)
        draw_bird(screen, bird)
        over = font_big.render("Game Over", True, (255, 120, 120))
        lines = font_small.render(f"Score: {score}   Best: {high_score}", True, (255, 255, 255))
        hint = font_small.render("SPACE for title", True, (220, 230, 250))
        screen.blit(over, over.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60)))
        screen.blit(lines, lines.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50)))

    pygame.display.flip()

pygame.quit()