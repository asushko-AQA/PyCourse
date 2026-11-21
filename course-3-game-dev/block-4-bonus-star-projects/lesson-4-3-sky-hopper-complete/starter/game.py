# game.py — Lesson 4.3: Sky Hopper — complete (starter)
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
state = START  # TODO: wire KEYDOWN to switch states like Lesson 2.4

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
high_score = 0  # TODO: update when a round ends
scroll_speed = BASE_SCROLL

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


def start_round() -> None:
    """TODO: reset score, bird, pipes, scroll_speed; state = PLAYING."""
    pass


def crash() -> None:
    """TODO: update high_score; state = GAME_OVER."""
    pass


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # TODO: START + SPACE → start_round()
        # TODO: PLAYING + SPACE → flap
        # TODO: GAME_OVER + SPACE → state = START

    screen.fill((90, 165, 235))

    if state == START:
        title = font_big.render("Sky Hopper", True, (255, 235, 120))
        hint = font_small.render("Press SPACE to start", True, (30, 55, 95))
        best = font_small.render(f"Best: {high_score}", True, (30, 55, 95))
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10)))
        screen.blit(best, best.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50)))

    elif state == PLAYING:
        vel_y += GRAVITY * dt
        bird_y += vel_y * dt
        bird.center = (BIRD_X, int(bird_y))

        # TODO: scroll_speed = BASE_SCROLL + score * 8
        # TODO: move pipes, spawn, score, collide → crash() on hit

        draw_pipes(screen)
        draw_bird(screen, bird)
        hud = font_small.render(f"Score: {score}  Best: {high_score}", True, (20, 50, 90))
        screen.blit(hud, (16, 12))

    elif state == GAME_OVER:
        draw_pipes(screen)
        draw_bird(screen, bird)
        over = font_big.render("Game Over", True, (255, 120, 120))
        hint = font_small.render("SPACE for title", True, (220, 230, 250))
        screen.blit(over, over.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20)))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40)))

    pygame.display.flip()

pygame.quit()