# game.py — Lesson 5.8: Orbit Guard — patrol ship + blaster bolts
import pygame

pygame.init()

WIDTH = 720
HEIGHT = 560
PLAY_TOP = 56
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Orbit Guard — Patrol Ship")

clock = pygame.time.Clock()
running = True

font_small = pygame.font.Font(None, 28)

SHIP_W = 44
SHIP_H = 28
SHIP_Y = HEIGHT - 52
ship_x = WIDTH / 2
ship_speed = 360.0

BOLT_SPEED = 520.0
COOLDOWN = 0.28
cooldown_left = 0.0

# Each bolt: {"x": float, "y": float, "vy": float}
player_bolts: list[dict[str, float]] = []


def draw_orbit_bg(surface: pygame.Surface, tick: int) -> None:
    surface.fill((6, 8, 22))
    for i in range(40):
        x = (i * 137 + tick // 8) % WIDTH
        y = (i * 93) % HEIGHT
        pygame.draw.circle(surface, (40, 50, 90), (x, y), 1)
    pygame.draw.rect(surface, (12, 18, 38), (0, PLAY_TOP, WIDTH, HEIGHT - PLAY_TOP - 8))


def draw_patrol_ship(surface: pygame.Surface, x: float, y: float) -> None:
    cx = int(x)
    base_y = int(y)
    nose = (cx, base_y - SHIP_H // 2)
    left = (cx - SHIP_W // 2, base_y + SHIP_H // 2)
    right = (cx + SHIP_W // 2, base_y + SHIP_H // 2)
    pygame.draw.polygon(surface, (80, 220, 255), [nose, left, right])
    pygame.draw.polygon(surface, (200, 250, 255), [nose, (cx - 8, base_y + 6), (cx + 8, base_y + 6)])


def fire_bolt() -> None:
    global cooldown_left
    if cooldown_left > 0:
        return
    player_bolts.append({"x": ship_x, "y": SHIP_Y - SHIP_H // 2, "vy": -BOLT_SPEED})
    cooldown_left = COOLDOWN


def update_bolts(dt: float) -> None:
    global player_bolts
    for bolt in player_bolts:
        bolt["y"] += bolt["vy"] * dt
    player_bolts = [b for b in player_bolts if PLAY_TOP < b["y"] < HEIGHT]


while running:
    dt = clock.tick(60) / 1000
    tick = pygame.time.get_ticks()
    cooldown_left = max(0.0, cooldown_left - dt)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, pygame.K_UP):
            fire_bolt()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        ship_x -= ship_speed * dt
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        ship_x += ship_speed * dt
    margin = SHIP_W // 2 + 8
    ship_x = max(margin, min(WIDTH - margin, ship_x))

    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        fire_bolt()

    update_bolts(dt)

    draw_orbit_bg(screen, tick)
    draw_patrol_ship(screen, ship_x, SHIP_Y)
    for bolt in player_bolts:
        bx, by = int(bolt["x"]), int(bolt["y"])
        pygame.draw.rect(screen, (255, 230, 120), (bx - 2, by - 8, 4, 14), border_radius=2)
        pygame.draw.circle(screen, (255, 255, 200), (bx, by - 10), 3)

    hud = font_small.render(
        f"Bolts: {len(player_bolts)}  |  SPACE fires (cooldown {COOLDOWN:.2f}s)",
        True,
        (180, 200, 240),
    )
    screen.blit(hud, (12, 12))
    tip = font_small.render("Patrol the orbit — invaders arrive in lesson 5.9", True, (120, 140, 180))
    screen.blit(tip, (12, HEIGHT - 28))
    pygame.display.flip()

pygame.quit()