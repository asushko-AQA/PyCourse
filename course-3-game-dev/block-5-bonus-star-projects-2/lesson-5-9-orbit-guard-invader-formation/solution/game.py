# game.py — Lesson 5.9: Orbit Guard — invader formation march
import pygame

pygame.init()

WIDTH = 720
HEIGHT = 560
PLAY_TOP = 56
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Orbit Guard — Invader Grid")

clock = pygame.time.Clock()
running = True

font_small = pygame.font.Font(None, 28)

SHIP_W = 44
SHIP_H = 28
SHIP_Y = HEIGHT - 52
ship_x = WIDTH / 2
ship_speed = 360.0

INV_W = 34
INV_H = 26
INV_GAP_X = 12
INV_GAP_Y = 10
COLS = 9
ROWS = 4

formation_x = 80.0
formation_y = PLAY_TOP + 24.0
march_dir = 1
march_speed = 62.0
step_down = 18.0

player_bolts: list[dict[str, float]] = []
BOLT_SPEED = 520.0
COOLDOWN = 0.28
cooldown_left = 0.0


def build_invaders() -> list[pygame.Rect]:
    rects: list[pygame.Rect] = []
    for row in range(ROWS):
        for col in range(COLS):
            x = int(formation_x + col * (INV_W + INV_GAP_X))
            y = int(formation_y + row * (INV_H + INV_GAP_Y))
            rects.append(pygame.Rect(x, y, INV_W, INV_H))
    return rects


invaders: list[pygame.Rect] = build_invaders()


def formation_width() -> float:
    return COLS * INV_W + (COLS - 1) * INV_GAP_X


def draw_orbit_bg(surface: pygame.Surface, tick: int) -> None:
    surface.fill((6, 8, 22))
    for i in range(35):
        x = (i * 151 + tick // 10) % WIDTH
        y = (i * 97) % (HEIGHT // 2)
        pygame.draw.circle(surface, (35, 45, 85), (x, y), 1)
    pygame.draw.rect(surface, (10, 14, 32), (0, PLAY_TOP, WIDTH, HEIGHT - PLAY_TOP - 6))


def draw_patrol_ship(surface: pygame.Surface, x: float, y: float) -> None:
    cx = int(x)
    base_y = int(y)
    points = [(cx, base_y - SHIP_H // 2), (cx - SHIP_W // 2, base_y + 8), (cx + SHIP_W // 2, base_y + 8)]
    pygame.draw.polygon(surface, (70, 210, 255), points)


def draw_invader(surface: pygame.Surface, rect: pygame.Rect, pulse: float) -> None:
    c1 = (255, int(90 + 40 * pulse), 140)
    pygame.draw.ellipse(surface, c1, rect)
    pygame.draw.circle(surface, (255, 200, 220), (rect.centerx - 8, rect.centery - 2), 4)
    pygame.draw.circle(surface, (255, 200, 220), (rect.centerx + 8, rect.centery - 2), 4)
    pygame.draw.rect(surface, (200, 60, 100), (rect.left + 6, rect.bottom - 6, rect.width - 12, 4))


def march_formation(dt: float) -> None:
    global formation_x, formation_y, march_dir, invaders
    formation_x += march_dir * march_speed * dt
    left = formation_x
    right = formation_x + formation_width()
    margin = 24
    if left <= margin or right >= WIDTH - margin:
        march_dir *= -1
        formation_x += march_dir * march_speed * dt
        formation_y += step_down
    invaders = build_invaders()


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
    pulse = (tick % 600) / 600
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
    ship_x = max(32, min(WIDTH - 32, ship_x))

    march_formation(dt)
    update_bolts(dt)

    draw_orbit_bg(screen, tick)
    for inv in invaders:
        draw_invader(screen, inv, pulse)
    draw_patrol_ship(screen, ship_x, SHIP_Y)
    for bolt in player_bolts:
        pygame.draw.rect(screen, (255, 240, 160), (int(bolt["x"]) - 2, int(bolt["y"]) - 10, 4, 12))

    hud = font_small.render(
        f"formation=({formation_x:.0f},{formation_y:.0f}) dir={march_dir:+d}",
        True,
        (170, 190, 230),
    )
    screen.blit(hud, (12, 12))
    tip = font_small.render("Bolts pass through — collisions in 5.10", True, (130, 150, 190))
    screen.blit(tip, (12, HEIGHT - 26))
    pygame.display.flip()

pygame.quit()