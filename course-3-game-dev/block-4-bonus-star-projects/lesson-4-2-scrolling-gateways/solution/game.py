# game.py — Lesson 4.2: Sky Hopper — scrolling gateways + score
import pygame
import random

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sky Hopper — Gateways")

clock = pygame.time.Clock()
running = True

font_small = pygame.font.Font(None, 32)

BIRD_X = 160
GRAVITY = 720
FLAP_STRENGTH = -280
PIPE_W = 72
GAP = 150
PIPE_SPACING = 240
SCROLL = 180

bird_y = HEIGHT // 2
vel_y = 0.0
bird_size = 28
bird = pygame.Rect(0, 0, bird_size, bird_size)
bird.center = (BIRD_X, int(bird_y))

score = 0
crashed = False

pipes: list[dict] = []


def draw_bird(surface: pygame.Surface, rect: pygame.Rect) -> None:
    cx, cy = rect.center
    pygame.draw.circle(surface, (255, 210, 70), (cx, cy), 14)
    pygame.draw.circle(surface, (30, 30, 40), (cx + 5, cy - 4), 3)
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


spawn_pipe()

while running:
    dt = clock.tick(60) / 1000
    want_reset = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if not crashed and event.key == pygame.K_SPACE:
                vel_y = FLAP_STRENGTH
            if crashed and event.key == pygame.K_r:
                want_reset = True

    if want_reset:
        pipes.clear()
        spawn_pipe()
        bird_y = HEIGHT // 2
        vel_y = 0
        score = 0
        crashed = False

    if not crashed:
        vel_y += GRAVITY * dt
        bird_y += vel_y * dt
        bird.center = (BIRD_X, int(bird_y))

        if bird.top < 0 or bird.bottom > HEIGHT:
            crashed = True

        for pipe in pipes:
            pipe["x"] -= int(SCROLL * dt)
        pipes = [p for p in pipes if p["x"] > -PIPE_W]

        if not pipes or pipes[-1]["x"] < WIDTH - PIPE_SPACING:
            spawn_pipe()

        for pipe in pipes:
            top, bottom = pipe_rects(pipe)
            if bird.colliderect(top) or bird.colliderect(bottom):
                crashed = True
            if not pipe["scored"] and pipe["x"] + PIPE_W < bird.left:
                pipe["scored"] = True
                score += 1

    screen.fill((100, 175, 245))
    draw_pipes(screen)
    draw_bird(screen, bird)
    hud = font_small.render(f"Score: {score}", True, (20, 50, 90))
    screen.blit(hud, (16, 12))
    if crashed:
        over = font_small.render("Bump! Press R to reset (full screens in 4.3)", True, (120, 30, 30))
        screen.blit(over, over.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

    pygame.display.flip()

pygame.quit()