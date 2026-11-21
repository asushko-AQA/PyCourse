# game.py — Lesson 5.31: Night Swarm — shadow spawns (starter)
import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
MARGIN = 22
PLAYER_SPEED = 185
PLAYER_RADIUS = 14

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Night Swarm — Shadow Tide")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

player_pos = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
player_hp = 100.0
player_max_hp = 100.0
enemies: list[dict] = []
running = True


def clamp_player(pos: pygame.Vector2) -> None:
    pos.x = max(MARGIN + PLAYER_RADIUS, min(WIDTH - MARGIN - PLAYER_RADIUS, pos.x))
    pos.y = max(MARGIN + PLAYER_RADIUS, min(HEIGHT - MARGIN - PLAYER_RADIUS, pos.y))


def direction_toward(ax: float, ay: float, bx: float, by: float) -> pygame.Vector2:
    d = pygame.Vector2(bx - ax, by - ay)
    if d.length_squared() > 0:
        return d.normalize()
    return d


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

    # TODO: spawn_timer — every ~1.4s append enemy at screen edge (cap ~40)
    # TODO: move each enemy toward player with direction_toward * speed * dt
    # TODO: contact damage with hurt_cd; draw HP bar at top

    screen.fill((12, 14, 28))
    pygame.draw.rect(screen, (30, 36, 58), (MARGIN, MARGIN, WIDTH - 2 * MARGIN, HEIGHT - 2 * MARGIN), 2)
    pygame.draw.circle(screen, (255, 210, 80), (int(player_pos.x), int(player_pos.y)), PLAYER_RADIUS)
    hint = font.render("TODO: edge spawns, chase, contact HP bar", True, (190, 200, 240))
    screen.blit(hint, (12, 12))

    pygame.display.flip()

pygame.quit()