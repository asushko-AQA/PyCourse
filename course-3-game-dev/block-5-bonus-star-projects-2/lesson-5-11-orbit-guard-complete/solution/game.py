# game.py — Lesson 5.11: Orbit Guard — waves, UFO bonus, full states
from __future__ import annotations

import random

import pygame

pygame.init()

WIDTH = 720
HEIGHT = 560
PLAY_TOP = 64
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Orbit Guard")

clock = pygame.time.Clock()
running = True

font_big = pygame.font.Font(None, 52)
font_small = pygame.font.Font(None, 28)

START = "start"
PLAYING = "playing"
WAVE_CLEAR = "wave_clear"
GAME_OVER = "game_over"
VICTORY = "victory"
state = START

SHIP_W = 44
SHIP_H = 28
SHIP_Y = HEIGHT - 48
ship_x = WIDTH / 2
ship_speed = 380.0

INV_W = 34
INV_H = 26
INV_GAP_X = 11
INV_GAP_Y = 9

formation_x = 90.0
formation_y = PLAY_TOP + 28.0
march_dir = 1
base_march = 48.0

lives = 3
score = 0
high_score = 0
wave = 1
WAVE_ROWS = [3, 4, 4, 5]
WAVE_COLS = [7, 8, 9, 9]

player_bolts: list[dict[str, float]] = []
enemy_bolts: list[dict[str, float]] = []
invaders: list[pygame.Rect] = []

BOLT_SPEED = 520.0
COOLDOWN = 0.24
cooldown_left = 0.0
enemy_fire_timer = 0.0

ufo_x = -80.0
ufo_active = False
ufo_timer = 0.0
ufo_speed = 120.0

COLS = 8
ROWS = 3


def make_shields() -> list[dict[str, object]]:
    shields: list[dict[str, object]] = []
    for sx in (WIDTH // 2 - 210, WIDTH // 2 - 70, WIDTH // 2 + 70):
        blocks: list[pygame.Rect] = []
        hp: dict[tuple[int, int], int] = {}
        for row in range(4):
            for col in range(6):
                r = pygame.Rect(sx + col * 14, SHIP_Y - 118 + row * 12, 12, 10)
                blocks.append(r)
                hp[(r.x, r.y)] = 3
        shields.append({"blocks": blocks, "hp": hp})
    return shields


shields = make_shields()


def wave_size() -> tuple[int, int]:
    idx = min(wave - 1, len(WAVE_ROWS) - 1)
    return WAVE_COLS[idx], WAVE_ROWS[idx]


def build_invaders() -> list[pygame.Rect]:
    global COLS, ROWS
    COLS, ROWS = wave_size()
    rects: list[pygame.Rect] = []
    for row in range(ROWS):
        for col in range(COLS):
            x = int(formation_x + col * (INV_W + INV_GAP_X))
            y = int(formation_y + row * (INV_H + INV_GAP_Y))
            rects.append(pygame.Rect(x, y, INV_W, INV_H))
    return rects


def formation_width() -> float:
    return COLS * INV_W + max(0, COLS - 1) * INV_GAP_X


def march_speed() -> float:
    return base_march + wave * 6 + max(0, 8 - len(invaders)) * 2


def reset_wave() -> None:
    global formation_x, formation_y, march_dir, invaders, shields, enemy_bolts, player_bolts
    global enemy_fire_timer, ufo_active, ufo_x, ufo_timer
    formation_x = 90.0
    formation_y = PLAY_TOP + 28.0
    march_dir = 1
    invaders = build_invaders()
    shields = make_shields()
    enemy_bolts = []
    player_bolts = []
    enemy_fire_timer = 0.0
    ufo_active = False
    ufo_x = -80.0
    ufo_timer = random.uniform(8.0, 18.0)


def start_play() -> None:
    global state, lives, score, wave
    state = PLAYING
    lives = 3
    score = 0
    wave = 1
    reset_wave()


def draw_orbit_bg(surface: pygame.Surface, tick: int) -> None:
    surface.fill((5, 7, 20))
    for i in range(50):
        x = (i * 163 + tick // 12) % WIDTH
        y = (i * 89) % HEIGHT
        pygame.draw.circle(surface, (30, 40, 75), (x, y), 1)
    pygame.draw.rect(surface, (8, 12, 28), (0, PLAY_TOP, WIDTH, HEIGHT - PLAY_TOP))


def draw_patrol_ship(surface: pygame.Surface, x: float, y: float) -> None:
    cx = int(x)
    pygame.draw.polygon(
        surface,
        (60, 215, 255),
        [(cx, int(y) - 14), (cx - 24, int(y) + 12), (cx + 24, int(y) + 12)],
    )
    pygame.draw.circle(surface, (200, 250, 255), (cx, int(y)), 6)


def draw_invader(surface: pygame.Surface, rect: pygame.Rect, pulse: float) -> None:
    tint = int(100 + 50 * pulse)
    pygame.draw.ellipse(surface, (255, tint, 160), rect)
    pygame.draw.line(surface, (255, 220, 240), rect.midtop, rect.midbottom, 2)


def draw_ufo(surface: pygame.Surface) -> None:
    if not ufo_active:
        return
    body = pygame.Rect(int(ufo_x) - 28, PLAY_TOP + 6, 56, 18)
    pygame.draw.ellipse(surface, (180, 255, 200), body)
    pygame.draw.ellipse(surface, (120, 220, 255), body.inflate(-10, -8))
    pygame.draw.circle(surface, (255, 255, 220), (body.centerx, body.centery - 6), 8)


def draw_shields(surface: pygame.Surface) -> None:
    for shield in shields:
        hp_map: dict[tuple[int, int], int] = shield["hp"]  # type: ignore[assignment]
        for block in shield["blocks"]:  # type: ignore[union-attr]
            if hp_map.get((block.x, block.y), 0) > 0:
                pygame.draw.rect(surface, (70, 240, 150), block)


def march_formation(dt: float) -> None:
    global formation_x, formation_y, march_dir, invaders, state
    if not invaders:
        if state == PLAYING:
            state = WAVE_CLEAR
        return
    formation_x += march_dir * march_speed() * dt
    margin = 22
    if formation_x < margin or formation_x + formation_width() > WIDTH - margin:
        march_dir *= -1
        formation_x += march_dir * march_speed() * dt
        formation_y += 14
        if formation_y + ROWS * (INV_H + INV_GAP_Y) > SHIP_Y - 40:
            state = GAME_OVER
    invaders = build_invaders()


def fire_bolt() -> None:
    global cooldown_left
    if cooldown_left > 0 or state != PLAYING:
        return
    player_bolts.append({"x": ship_x, "y": SHIP_Y - SHIP_H, "vy": -BOLT_SPEED})
    cooldown_left = COOLDOWN


def damage_shields_at(x: float, y: float) -> bool:
    for shield in shields:
        hp_map: dict[tuple[int, int], int] = shield["hp"]  # type: ignore[assignment]
        for block in shield["blocks"]:  # type: ignore[union-attr]
            if block.collidepoint(x, y):
                key = (block.x, block.y)
                hp_map[key] = hp_map.get(key, 0) - 1
                return True
    return False


def update_ufo(dt: float) -> None:
    global ufo_active, ufo_x, ufo_timer, score, high_score
    if state != PLAYING:
        return
    ufo_timer -= dt
    if not ufo_active and ufo_timer <= 0:
        ufo_active = True
        ufo_x = -60.0
        ufo_timer = random.uniform(14.0, 26.0)
    if ufo_active:
        ufo_x += ufo_speed * dt
        body = pygame.Rect(int(ufo_x) - 28, PLAY_TOP + 6, 56, 18)
        for bolt in player_bolts:
            if body.collidepoint(bolt["x"], bolt["y"]):
                ufo_active = False
                score += 350
                high_score = max(high_score, score)
                player_bolts.remove(bolt)
                break
        if ufo_x > WIDTH + 60:
            ufo_active = False


def maybe_enemy_shot(dt: float) -> None:
    global enemy_fire_timer
    if not invaders or state != PLAYING:
        return
    enemy_fire_timer += dt
    interval = max(0.45, 1.1 - wave * 0.08)
    if enemy_fire_timer < interval:
        return
    enemy_fire_timer = 0.0
    shooter = random.choice(invaders)
    enemy_bolts.append(
        {"x": float(shooter.centerx), "y": float(shooter.bottom), "vy": 240.0 + wave * 12}
    )


def update_bolts(dt: float) -> None:
    global player_bolts, enemy_bolts, invaders, score, lives, high_score, state
    for bolt in player_bolts:
        bolt["y"] += bolt["vy"] * dt
    new_player: list[dict[str, float]] = []
    for bolt in player_bolts:
        if bolt["y"] < PLAY_TOP:
            continue
        if damage_shields_at(bolt["x"], bolt["y"]):
            continue
        hit = next((inv for inv in invaders if inv.collidepoint(bolt["x"], bolt["y"])), None)
        if hit:
            invaders.remove(hit)
            score += 100
            high_score = max(high_score, score)
            continue
        new_player.append(bolt)
    player_bolts = new_player

    ship_rect = pygame.Rect(0, 0, SHIP_W, SHIP_H)
    ship_rect.midbottom = (int(ship_x), int(SHIP_Y + 4))
    new_enemy: list[dict[str, float]] = []
    for bolt in enemy_bolts:
        bolt["y"] += bolt["vy"] * dt
        if bolt["y"] > HEIGHT:
            continue
        if damage_shields_at(bolt["x"], bolt["y"]):
            continue
        if ship_rect.collidepoint(bolt["x"], bolt["y"]):
            lives -= 1
            if lives <= 0:
                state = GAME_OVER
            continue
        new_enemy.append(bolt)
    enemy_bolts = new_enemy


def draw_hud(surface: pygame.Surface) -> None:
    text = font_small.render(
        f"Wave {wave}  Score {score}  Best {high_score}  Lives {lives}",
        True,
        (185, 205, 245),
    )
    surface.blit(text, (12, 10))


def draw_overlay(surface: pygame.Surface, title: str, hint: str) -> None:
    shade = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    shade.fill((0, 0, 0, 160))
    surface.blit(shade, (0, 0))
    t = font_big.render(title, True, (120, 240, 255))
    h = font_small.render(hint, True, (200, 215, 240))
    surface.blit(t, t.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 24)))
    surface.blit(h, h.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 28)))


reset_wave()

while running:
    dt = clock.tick(60) / 1000
    tick = pygame.time.get_ticks()
    pulse = (tick % 700) / 700
    cooldown_left = max(0.0, cooldown_left - dt)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if state == START:
                    start_play()
                elif state == PLAYING:
                    fire_bolt()
                elif state in (GAME_OVER, VICTORY, WAVE_CLEAR):
                    if state == WAVE_CLEAR and wave < len(WAVE_ROWS):
                        wave += 1
                        state = PLAYING
                        reset_wave()
                    elif state == WAVE_CLEAR and wave >= len(WAVE_ROWS):
                        state = VICTORY
                    else:
                        state = START
            if event.key in (pygame.K_UP,) and state == PLAYING:
                fire_bolt()

    if state == PLAYING and lives > 0:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            ship_x -= ship_speed * dt
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            ship_x += ship_speed * dt
        ship_x = max(28, min(WIDTH - 28, ship_x))
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            fire_bolt()
        march_formation(dt)
        maybe_enemy_shot(dt)
        update_bolts(dt)
        update_ufo(dt)

    draw_orbit_bg(screen, tick)
    if state != START:
        for inv in invaders:
            draw_invader(screen, inv, pulse)
        draw_shields(screen)
        draw_ufo(screen)
        draw_patrol_ship(screen, ship_x, SHIP_Y)
        for bolt in player_bolts:
            pygame.draw.rect(screen, (255, 250, 180), (int(bolt["x"]) - 2, int(bolt["y"]) - 8, 4, 12))
        for bolt in enemy_bolts:
            pygame.draw.rect(screen, (255, 90, 120), (int(bolt["x"]) - 2, int(bolt["y"]), 4, 12))
        draw_hud(screen)

    if state == START:
        draw_overlay(screen, "Orbit Guard", "SPACE — defend the orbit (4 waves)")
    elif state == WAVE_CLEAR:
        draw_overlay(screen, f"Wave {wave} cleared!", "SPACE — next wave")
    elif state == GAME_OVER:
        draw_overlay(screen, "Orbit breached", "SPACE — title")
    elif state == VICTORY:
        draw_overlay(screen, "Orbit secure!", f"Best {high_score} — SPACE title")

    pygame.display.flip()

pygame.quit()