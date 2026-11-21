# game.py — Lesson 5.30: Night Swarm — lantern movement (solution)
import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
MARGIN = 22
PLAYER_SPEED = 185
PLAYER_RADIUS = 14

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Night Swarm — Lantern Step")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

player_pos = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
running = True


def clamp_player(pos: pygame.Vector2) -> None:
    pos.x = max(MARGIN + PLAYER_RADIUS, min(WIDTH - MARGIN - PLAYER_RADIUS, pos.x))
    pos.y = max(MARGIN + PLAYER_RADIUS, min(HEIGHT - MARGIN - PLAYER_RADIUS, pos.y))


def draw_lantern(surf: pygame.Surface, pos: pygame.Vector2) -> None:
    pygame.draw.circle(surf, (255, 230, 140), (int(pos.x), int(pos.y)), PLAYER_RADIUS + 6, 2)
    pygame.draw.circle(surf, (255, 210, 80), (int(pos.x), int(pos.y)), PLAYER_RADIUS)
    pygame.draw.circle(surf, (255, 255, 210), (int(pos.x), int(pos.y)), 5)


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    move = pygame.Vector2(0, 0)
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        move.y -= 1
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        move.y += 1
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        move.x -= 1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        move.x += 1
    if move.length_squared() > 0:
        move = move.normalize()

    player_pos += move * PLAYER_SPEED * dt
    clamp_player(player_pos)

    screen.fill((12, 14, 28))
    for gx in range(MARGIN, WIDTH - MARGIN, 40):
        pygame.draw.line(screen, (22, 26, 44), (gx, MARGIN), (gx, HEIGHT - MARGIN))
    for gy in range(MARGIN, HEIGHT - MARGIN, 40):
        pygame.draw.line(screen, (22, 26, 44), (MARGIN, gy), (WIDTH - MARGIN, gy))
    pygame.draw.rect(screen, (30, 36, 58), (MARGIN, MARGIN, WIDTH - 2 * MARGIN, HEIGHT - 2 * MARGIN), 2)

    draw_lantern(screen, player_pos)
    hint = font.render("8-way move · normalized vector · dt", True, (180, 190, 230))
    screen.blit(hint, (12, 12))

    pygame.display.flip()

pygame.quit()