# game.py — Lesson 4.1: Sky Hopper — gravity + flap (starter)
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sky Hopper — Practice")

clock = pygame.time.Clock()
running = True

font_small = pygame.font.Font(None, 32)

BIRD_X = 160
GRAVITY = 720
FLAP_STRENGTH = -280

bird_y = HEIGHT // 2
vel_y = 0.0
bird_size = 28
bird = pygame.Rect(0, 0, bird_size, bird_size)
bird.center = (BIRD_X, int(bird_y))


def draw_bird(surface: pygame.Surface, rect: pygame.Rect) -> None:
    """Procedural bird — no image files."""
    cx, cy = rect.center
    pygame.draw.circle(surface, (255, 210, 70), (cx, cy), 14)
    pygame.draw.circle(surface, (30, 30, 40), (cx + 5, cy - 4), 3)
    pygame.draw.circle(surface, (250, 250, 255), (cx + 6, cy - 5), 1)
    pygame.draw.polygon(surface, (255, 130, 50), [(cx + 12, cy), (cx + 22, cy + 3), (cx + 12, cy + 7)])
    wing = pygame.Rect(cx - 18, cy + 2, 14, 9)
    pygame.draw.ellipse(surface, (255, 190, 90), wing)


def draw_cloud(surface: pygame.Surface, x: int, y: int) -> None:
    pygame.draw.circle(surface, (240, 245, 255), (x, y), 22)
    pygame.draw.circle(surface, (240, 245, 255), (x + 28, y + 4), 18)
    pygame.draw.circle(surface, (240, 245, 255), (x - 22, y + 6), 16)


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # TODO 1: On KEYDOWN + SPACE, set vel_y = FLAP_STRENGTH

    # TODO 2: Apply gravity each frame: vel_y += GRAVITY * dt
    # TODO 3: Move bird: bird_y += vel_y * dt
    # TODO 4: Clamp bird_y between bird_size and HEIGHT - bird_size (bounce on floor/ceiling)

    bird.center = (BIRD_X, int(bird_y))

    screen.fill((120, 190, 255))
    draw_cloud(screen, 80, 90)
    draw_cloud(screen, 360, 140)
    draw_cloud(screen, 500, 60)
    draw_bird(screen, bird)
    hint = font_small.render("SPACE to flap — stay in the sky!", True, (20, 50, 90))
    screen.blit(hint, (16, 12))
    vel_hud = font_small.render(f"vel_y: {vel_y:.0f}", True, (20, 50, 90))
    screen.blit(vel_hud, (16, 44))

    pygame.display.flip()

pygame.quit()