# game.py — Lesson 5.33: Night Swarm — level up (solution)
from __future__ import annotations

import math
import random

import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
MARGIN = 22
PLAYER_SPEED = 185
PLAYER_RADIUS = 14

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Night Swarm — Bright Choice")
clock = pygame.time.Clock()
font_big = pygame.font.Font(None, 46)
font = pygame.font.Font(None, 28)

UPGRADE_POOL = {
    "damage": {"label": "Bright Pulse", "damage_add": 5},
    "fire_rate": {"label": "Quick Glow", "cooldown_mul": 0.85},
    "speed": {"label": "Swift Steps", "speed_mul": 1.12},
    "extra_orb": {"label": "Twin Lantern", "extra_shots": 1},
    "orbit": {"label": "Halo Guard", "orbit_add": 1},
}

state = "PLAY"
player_pos = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
damage = 12
fire_cooldown = 0.55
fire_timer = 0.0
extra_shots = 0
player_speed = PLAYER_SPEED
xp = 0
level = 1
xp_need = 10
level_choices: list[str] = []
enemies: list[dict] = []
orbs: list[dict] = []
gems: list[dict] = []
spawn_timer = 0.3
rng = random.Random()
running = True


def direction_toward(ax: float, ay: float, bx: float, by: float) -> pygame.Vector2:
    d = pygame.Vector2(bx - ax, by - ay)
    if d.length_squared() > 0:
        d = d.normalize()
    return d


def nearest_enemy_index(px: float, py: float, shadow_list: list[dict]) -> int | None:
    best_i = None
    best_d2 = math.inf
    for i, e in enumerate(shadow_list):
        if e["hp"] <= 0:
            continue
        dx = e["pos"].x - px
        dy = e["pos"].y - py
        if dx * dx + dy * dy < best_d2:
            best_d2 = dx * dx + dy * dy
            best_i = i
    return best_i


def pick_level_up_choices(pool: dict, n: int, r: random.Random) -> list[str]:
    keys = list(pool.keys())
    r.shuffle(keys)
    return keys[: min(n, len(keys))]


def spawn_edge() -> pygame.Vector2:
    return pygame.Vector2(rng.uniform(0, WIDTH), -12)


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if state == "LEVEL_UP" and event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_1, pygame.K_2, pygame.K_3):
                idx = event.key - pygame.K_1
                if idx < len(level_choices):
                    key = level_choices[idx]
                    up = UPGRADE_POOL[key]
                    if key == "damage":
                        damage += up["damage_add"]
                    elif key == "fire_rate":
                        fire_cooldown *= up["cooldown_mul"]
                    elif key == "speed":
                        player_speed *= up["speed_mul"]
                    elif key == "extra_orb":
                        extra_shots += up["extra_shots"]
                    state = "PLAY"
                    level_choices = []

    if state == "PLAY":
        keys = pygame.key.get_pressed()
        move = pygame.Vector2(0, 0)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            move.x -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            move.x += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            move.y -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            move.y += 1
        if move.length_squared() > 0:
            move = move.normalize()
        player_pos += move * player_speed * dt

        spawn_timer -= dt
        if spawn_timer <= 0 and len(enemies) < 35:
            spawn_timer = 1.2
            enemies.append({"pos": spawn_edge(), "hp": 22, "radius": 11, "drop": True})

        px, py = player_pos.x, player_pos.y
        for e in enemies:
            if e["hp"] <= 0:
                continue
            e["pos"] += direction_toward(e["pos"].x, e["pos"].y, px, py) * 70 * dt

        fire_timer -= dt
        if fire_timer <= 0 and nearest_enemy_index(px, py, enemies) is not None:
            te = enemies[nearest_enemy_index(px, py, enemies)]  # type: ignore[index]
            vel = direction_toward(px, py, te["pos"].x, te["pos"].y) * 280
            orbs.append({"pos": pygame.Vector2(px, py), "vel": vel, "life": 1.5})
            fire_timer = fire_cooldown

        for orb in orbs:
            orb["pos"] += orb["vel"] * dt
            orb["life"] -= dt
        orbs = [o for o in orbs if o["life"] > 0]
        for orb in orbs:
            for e in enemies:
                if e["hp"] > 0 and orb["pos"].distance_to(e["pos"]) < e["radius"] + 5:
                    e["hp"] -= damage
                    orb["life"] = 0
                    break
        for e in enemies:
            if e["hp"] <= 0 and e.get("drop"):
                e["drop"] = False
                gems.append({"pos": pygame.Vector2(e["pos"]), "value": 4})
        enemies = [e for e in enemies if e["hp"] > 0]
        for gem in gems[:]:
            if gem["pos"].distance_to(player_pos) < 20:
                xp += gem["value"]
                gems.remove(gem)
        while xp >= xp_need:
            xp -= xp_need
            level += 1
            xp_need = 8 + level * 3
            level_choices = pick_level_up_choices(UPGRADE_POOL, 3, rng)
            state = "LEVEL_UP"
            break

    screen.fill((12, 14, 28))
    for gem in gems:
        pygame.draw.circle(screen, (80, 230, 255), (int(gem["pos"].x), int(gem["pos"].y)), 6)
    for orb in orbs:
        pygame.draw.circle(screen, (255, 255, 170), (int(orb["pos"].x), int(orb["pos"].y)), 5)
    for e in enemies:
        pygame.draw.circle(screen, (90, 70, 140), (int(e["pos"].x), int(e["pos"].y)), e["radius"])
    pygame.draw.circle(screen, (255, 210, 80), (int(player_pos.x), int(player_pos.y)), PLAYER_RADIUS)
    hud = font.render(f"Lv {level} XP {xp}/{xp_need}", True, (200, 210, 255))
    screen.blit(hud, (12, 12))

    if state == "LEVEL_UP":
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 140))
        screen.blit(overlay, (0, 0))
        title = font_big.render("Pick upgrade 1-3", True, (255, 240, 160))
        screen.blit(title, title.get_rect(center=(WIDTH // 2, 100)))
        for i, key in enumerate(level_choices):
            txt = font.render(f"{i+1}: {UPGRADE_POOL[key]['label']}", True, (220, 230, 255))
            screen.blit(txt, txt.get_rect(center=(WIDTH // 2, 170 + i * 34)))

    pygame.display.flip()

pygame.quit()