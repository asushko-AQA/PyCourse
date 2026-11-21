# game.py — Lesson 5.30: Night Swarm — lantern movement (starter)
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
    # TODO: keep pos inside the arena (use MARGIN + PLAYER_RADIUS)
    pass


def draw_lantern(surf: pygame.Surface, pos: pygame.Vector2) -> None:
    pygame.draw.circle(surf, (255, 210, 80), (int(pos.x), int(pos.y)), PLAYER_RADIUS)


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    move = pygame.Vector2(0, 0)
    # TODO: WASD + arrow keys fill move.x / move.y for all 8 directions
    # TODO: if move.length_squared() > 0: move = move.normalize()
    # TODO: player_pos += move * PLAYER_SPEED * dt
    # TODO: call clamp_player(player_pos)

    screen.fill((12, 14, 28))
    pygame.draw.rect(screen, (30, 36, 58), (MARGIN, MARGIN, WIDTH - 2 * MARGIN, HEIGHT - 2 * MARGIN), 2)

    draw_lantern(screen, player_pos)
    hint = font.render("Finish TODOs — 8-dir movement with dt!", True, (180, 190, 230))
    screen.blit(hint, (12, 12))

    pygame.display.flip()

pygame.quit()