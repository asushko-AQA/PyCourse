# game.py — Lesson 2.3: score counter with font.render()
import pygame
import os

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Score Scribbler")

clock = pygame.time.Clock()
running = True

HERE = os.path.dirname(os.path.abspath(__file__))

# Fallback: draw a rect if no sprite (works without Lesson 2.2 asset)
player_rect = pygame.Rect(0, 0, 48, 48)
player_rect.center = (WIDTH // 2, HEIGHT // 2)
player_img = None
sprite_path = os.path.join(HERE, "player.png")
# Optional: if you copy player.png here from Lesson 2.2, it will load
if os.path.isfile(sprite_path):
    player_img = pygame.image.load(sprite_path).convert_alpha()
    player_rect = player_img.get_rect(center=player_rect.center)

speed = 250
score = 0
# Points grow while you hold RIGHT — a simple "score engine" for practice
score_rate = 10  # points per second while moving right

# TODO: Create a Font (default system font is fine for now)
# font = pygame.font.Font(None, 36)

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= int(speed * dt)
    if keys[pygame.K_RIGHT]:
        player_rect.x += int(speed * dt)
        # Earn points while holding RIGHT
        score = score + score_rate * dt
    if keys[pygame.K_UP]:
        player_rect.y -= int(speed * dt)
    if keys[pygame.K_DOWN]:
        player_rect.y += int(speed * dt)

    player_rect.clamp_ip(screen.get_rect())

    screen.fill((18, 22, 38))

    if player_img is not None:
        screen.blit(player_img, player_rect)
    else:
        pygame.draw.rect(screen, (255, 200, 50), player_rect)

    # TODO: Render score text and blit it near the top-left
    # score_surf = font.render(f"Score: {int(score)}", True, (255, 255, 255))
    # screen.blit(score_surf, (16, 12))

    pygame.display.flip()

pygame.quit()
