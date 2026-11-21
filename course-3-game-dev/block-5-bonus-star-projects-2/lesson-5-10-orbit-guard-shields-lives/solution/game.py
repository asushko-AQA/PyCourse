# game.py — Lesson 5.10: Orbit Guard — collisions, shields, lives, score
import random

import pygame

pygame.init()

WIDTH = 720
HEIGHT = 560
PLAY_TOP = 56
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Orbit Guard — Shields & Score")

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
COLS = 8
ROWS = 3

formation_x = 100.0
formation_y = PLAY_TOP + 30.0
march_dir = 1
march_speed = 55.0
step_down = 16.0

lives = 3
score = 0

player_bolts: list[dict[str, float]] = []
enemy_bolts: list[dict[str, float]] = []
BOLT_SPEED = 500.0
ENEMY_BOLT_SPEED = 280.0
COOLDOWN = 0.26
cooldown_left = 0.0
enemy_fire_timer = 0.0

# Shield blocks: small rects with hp
SHIELD_W = 88
SHIELD_H = 48


def make_shields() -> list[dict[str, object]]:
    shields: list[dict[str, object]] = []
    xs = [WIDTH // 2 - 200, WIDTH // 2 - 60, WIDTH // 2 + 80]
    for sx in xs:
        blocks: list[pygame.Rect] = []
        hp: dict[tuple[int, int], int] = {}
        for row in range(4):
            for col in range(6):
                r = pygame.Rect(sx + col * 14, SHIP_Y - 120 + row * 12, 12, 10)
                blocks.append(r)
                hp[(r.x, r.y)] = 3
        shields.append({"blocks": blocks, "hp": hp})
    return shields


shields = make_shields()


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
    pygame.draw.rect(surface, (10, 14, 30), (0, PLAY_TOP, WIDTH, HEIGHT - PLAY_TOP - 4))


def draw_patrol_ship(surface: pygame.Surface, x: float, y: float) -> None:
    cx = int(x)
    pygame.draw.polygon(
        surface,
        (70, 220, 255),
        [(cx, int(y) - 14), (cx - 22, int(y) + 12), (cx + 22, int(y) + 12)],
    )


def draw_invader(surface: pygame.Surface, rect: pygame.Rect) -> None:
    pygame.draw.ellipse(surface, (255, 110, 170), rect)
    pygame.draw.rect(surface, (180, 50, 90), (rect.left + 8, rect.bottom - 5, rect.width - 16, 4))


def draw_shields(surface: pygame.Surface) -> None:
    for shield in shields:
        hp_map: dict[tuple[int, int], int] = shield["hp"]  # type: ignore[assignment]
        for block in shield["blocks"]:  # type: ignore[union-attr]
            key = (block.x, block.y)
            if hp_map.get(key, 0) > 0:
                pygame.draw.rect(surface, (80, 255, 160), block)


def march_formation(dt: float) -> None:
    global formation_x, formation_y, march_dir, invaders
    if not invaders:
        return
    formation_x += march_dir * march_speed * dt
    margin = 28
    if formation_x <= margin or formation_x + formation_width() >= WIDTH - margin:
        march_dir *= -1
        formation_x += march_dir * march_speed * dt
        formation_y += step_down
    invaders = build_invaders()


def fire_bolt() -> None:
    global cooldown_left
    if cooldown_left > 0:
        return
    player_bolts.append({"x": ship_x, "y": SHIP_Y - SHIP_H, "vy": -BOLT_SPEED})
    cooldown_left = COOLDOWN


def maybe_enemy_shot(dt: float) -> None:
    global enemy_fire_timer
    if not invaders:
        return
    enemy_fire_timer += dt
    if enemy_fire_timer < 0.9:
        return
    enemy_fire_timer = 0.0
    shooter = random.choice(invaders)
    enemy_bolts.append(
        {"x": float(shooter.centerx), "y": float(shooter.bottom), "vy": ENEMY_BOLT_SPEED}
    )


def damage_shields_at(x: float, y: float) -> bool:
    hit = False
    for shield in shields:
        hp_map: dict[tuple[int, int], int] = shield["hp"]  # type: ignore[assignment]
        for block in shield["blocks"]:  # type: ignore[union-attr]
            if block.collidepoint(x, y):
                key = (block.x, block.y)
                hp_map[key] = hp_map.get(key, 0) - 1
                hit = True
    return hit


def update_bolts(dt: float) -> None:
    global player_bolts, enemy_bolts, invaders, score, lives, ship_x
    # Player bolts
    for bolt in player_bolts:
        bolt["y"] += bolt["vy"] * dt
    keep_player: list[dict[str, float]] = []
    for bolt in player_bolts:
        if bolt["y"] < PLAY_TOP:
            continue
        bx, by = bolt["x"], bolt["y"]
        if damage_shields_at(bx, by):
            continue
        hit_inv = None
        for inv in invaders:
            if inv.collidepoint(bx, by):
                hit_inv = inv
                break
        if hit_inv:
            invaders.remove(hit_inv)
            score += 100
            continue
        keep_player.append(bolt)
    player_bolts = keep_player

    # Enemy bolts
    for bolt in enemy_bolts:
        bolt["y"] += bolt["vy"] * dt
    keep_enemy: list[dict[str, float]] = []
    ship_rect = pygame.Rect(0, 0, SHIP_W, SHIP_H)
    ship_rect.midbottom = (int(ship_x), int(SHIP_Y + 6))
    for bolt in enemy_bolts:
        if bolt["y"] > HEIGHT:
            continue
        bx, by = bolt["x"], bolt["y"]
        if damage_shields_at(bx, by):
            continue
        if ship_rect.collidepoint(bx, by):
            lives -= 1
            continue
        keep_enemy.append(bolt)
    enemy_bolts = keep_enemy


while running:
    dt = clock.tick(60) / 1000
    cooldown_left = max(0.0, cooldown_left - dt)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, pygame.K_UP):
            fire_bolt()

    if lives > 0:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            ship_x -= ship_speed * dt
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            ship_x += ship_speed * dt
        ship_x = max(30, min(WIDTH - 30, ship_x))

        march_formation(dt)
        maybe_enemy_shot(dt)
        update_bolts(dt)

    draw_orbit_bg(screen, pygame.time.get_ticks())
    for inv in invaders:
        draw_invader(screen, inv)
    draw_shields(screen)
    draw_patrol_ship(screen, ship_x, SHIP_Y)
    for bolt in player_bolts:
        pygame.draw.rect(screen, (255, 250, 180), (int(bolt["x"]) - 2, int(bolt["y"]) - 8, 4, 12))
    for bolt in enemy_bolts:
        pygame.draw.rect(screen, (255, 100, 120), (int(bolt["x"]) - 2, int(bolt["y"]), 4, 12))

    hud = font_small.render(f"Score {score}  Lives {lives}  Invaders {len(invaders)}", True, (190, 210, 245))
    screen.blit(hud, (12, 12))
    if lives <= 0:
        over = font_small.render("Ship lost — restart Python (full game in 5.11)", True, (255, 140, 160))
        screen.blit(over, over.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
    pygame.display.flip()

pygame.quit()