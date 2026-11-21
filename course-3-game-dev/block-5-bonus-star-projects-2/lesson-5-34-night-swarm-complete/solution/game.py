# game.py — Lesson 5.34: Night Swarm — complete (solution)
from __future__ import annotations

import json
import math
import random
from pathlib import Path

import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
MARGIN = 22
WIN_SURVIVE = 180.0
MAX_ENEMIES = 72
MAX_GEMS = 120
MAX_ORBS = 90

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Night Swarm — Pro")
clock = pygame.time.Clock()
font_big = pygame.font.Font(None, 52)
font = pygame.font.Font(None, 28)

SESSION_FILE = Path.home() / ".night_swarm_best.json"

UPGRADE_POOL = {
    "damage": {"label": "Bright Pulse", "damage_add": 4},
    "fire_rate": {"label": "Quick Glow", "cooldown_mul": 0.82},
    "speed": {"label": "Swift Steps", "speed_mul": 1.14},
    "extra_orb": {"label": "Twin Lantern", "extra_shots": 1},
    "orbit": {"label": "Halo Guard", "orbit_add": 1},
}


def load_best() -> float:
    if SESSION_FILE.is_file():
        try:
            data = json.loads(SESSION_FILE.read_text())
            return float(data.get("best_time", 0.0))
        except (json.JSONDecodeError, OSError, TypeError, ValueError):
            pass
    return 0.0


def save_best(seconds: float) -> None:
    prev = load_best()
    if seconds > prev:
        SESSION_FILE.write_text(json.dumps({"best_time": round(seconds, 1)}))


def direction_toward(ax: float, ay: float, bx: float, by: float) -> pygame.Vector2:
    d = pygame.Vector2(bx - ax, by - ay)
    if d.length_squared() > 0:
        d = d.normalize()
    return d


def nearest_enemy_index(px: float, py: float, enemies: list[dict]) -> int | None:
    best_i: int | None = None
    best_d2 = math.inf
    for i, e in enumerate(enemies):
        if e["hp"] <= 0:
            continue
        dx = e["pos"].x - px
        dy = e["pos"].y - py
        d2 = dx * dx + dy * dy
        if d2 < best_d2:
            best_d2 = d2
            best_i = i
    return best_i


def pick_level_up_choices(
    pool: dict[str, dict],
    n: int,
    rng: random.Random,
) -> list[str]:
    keys = list(pool.keys())
    rng.shuffle(keys)
    return keys[: min(n, len(keys))]


def spawn_at_edge(rng: random.Random, radius: float) -> pygame.Vector2:
    side = rng.randint(0, 3)
    if side == 0:
        return pygame.Vector2(rng.uniform(MARGIN, WIDTH - MARGIN), -radius)
    if side == 1:
        return pygame.Vector2(WIDTH + radius, rng.uniform(MARGIN, HEIGHT - MARGIN))
    if side == 2:
        return pygame.Vector2(rng.uniform(MARGIN, WIDTH - MARGIN), HEIGHT + radius)
    return pygame.Vector2(-radius, rng.uniform(MARGIN, HEIGHT - MARGIN))


def clamp_player(pos: pygame.Vector2, radius: float) -> None:
    pos.x = max(MARGIN + radius, min(WIDTH - MARGIN - radius, pos.x))
    pos.y = max(MARGIN + radius, min(HEIGHT - MARGIN - radius, pos.y))


def draw_lantern(surf: pygame.Surface, pos: pygame.Vector2, radius: int) -> None:
    pygame.draw.circle(surf, (255, 230, 140), (int(pos.x), int(pos.y)), radius + 6, 2)
    pygame.draw.circle(surf, (255, 210, 80), (int(pos.x), int(pos.y)), radius)
    pygame.draw.circle(surf, (255, 255, 210), (int(pos.x), int(pos.y)), max(4, radius // 3))


def draw_hp_bar(surf: pygame.Surface, hp: float, max_hp: float) -> None:
    w, h = 200, 14
    x, y = 12, 12
    pygame.draw.rect(surf, (40, 44, 70), (x, y, w, h), border_radius=4)
    fill = int(w * max(0.0, min(1.0, hp / max_hp)))
    pygame.draw.rect(surf, (120, 220, 255), (x, y, fill, h), border_radius=4)
    pygame.draw.rect(surf, (160, 170, 220), (x, y, w, h), width=2, border_radius=4)


def reset_run(rng: random.Random) -> dict:
    return {
        "player_pos": pygame.Vector2(WIDTH / 2, HEIGHT / 2),
        "player_hp": 100.0,
        "player_max_hp": 100.0,
        "player_speed": 185.0,
        "player_radius": 14,
        "damage": 12,
        "fire_cooldown": 0.55,
        "fire_timer": 0.0,
        "extra_shots": 0,
        "orbit_count": 0,
        "orbit_angle": 0.0,
        "enemies": [],
        "orbs": [],
        "gems": [],
        "spawn_timer": 0.4,
        "spawn_every": 1.6,
        "hurt_cd": 0.0,
        "elapsed": 0.0,
        "xp": 0,
        "level": 1,
        "xp_need": 12,
        "level_choices": [],
        "rng": rng,
    }


rng = random.Random()
state = "MENU"
paused = False
best_time = load_best()
world = reset_run(rng)
running = True

while running:
    dt = min(clock.tick(60) / 1000, 0.05)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if state == "PLAY":
                    paused = not paused
                elif state in ("MENU", "GAME_OVER", "WIN"):
                    running = False
            if state == "MENU" and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                world = reset_run(random.Random())
                state = "PLAY"
                paused = False
            if state == "GAME_OVER" and event.key == pygame.K_r:
                state = "MENU"
            if state == "WIN" and event.key == pygame.K_r:
                state = "MENU"
            if state == "LEVEL_UP" and event.key in (pygame.K_1, pygame.K_2, pygame.K_3):
                idx = event.key - pygame.K_1
                choices = world["level_choices"]
                if idx < len(choices):
                    key = choices[idx]
                    up = UPGRADE_POOL[key]
                    if key == "damage":
                        world["damage"] += up["damage_add"]
                    elif key == "fire_rate":
                        world["fire_cooldown"] *= up["cooldown_mul"]
                    elif key == "speed":
                        world["player_speed"] *= up["speed_mul"]
                    elif key == "extra_orb":
                        world["extra_shots"] += up["extra_shots"]
                    elif key == "orbit":
                        world["orbit_count"] += up["orbit_add"]
                    world["level_choices"] = []
                    state = "PLAY"

    if state == "PLAY" and not paused:
        world["elapsed"] += dt
        world["hurt_cd"] = max(0.0, world["hurt_cd"] - dt)
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
        world["player_pos"] += move * world["player_speed"] * dt
        clamp_player(world["player_pos"], world["player_radius"])

        ramp = world["elapsed"] / WIN_SURVIVE
        world["spawn_every"] = max(0.45, 1.65 - ramp * 1.1)
        world["spawn_timer"] -= dt
        if world["spawn_timer"] <= 0 and len(world["enemies"]) < MAX_ENEMIES:
            world["spawn_timer"] = world["spawn_every"]
            spd = 55 + ramp * 65
            world["enemies"].append({
                "pos": spawn_at_edge(world["rng"], 12),
                "hp": 20 + int(ramp * 25),
                "max_hp": 20 + int(ramp * 25),
                "speed": spd,
                "radius": 11,
            })

        px, py = world["player_pos"].x, world["player_pos"].y
        for e in world["enemies"]:
            if e["hp"] <= 0:
                continue
            d = direction_toward(e["pos"].x, e["pos"].y, px, py)
            e["pos"] += d * e["speed"] * dt
            dist = e["pos"].distance_to(world["player_pos"])
            if dist < world["player_radius"] + e["radius"] and world["hurt_cd"] <= 0:
                world["player_hp"] -= 14
                world["hurt_cd"] = 0.45
                if world["player_hp"] <= 0:
                    state = "GAME_OVER"

        world["fire_timer"] -= dt
        if world["fire_timer"] <= 0:
            target = nearest_enemy_index(px, py, world["enemies"])
            if target is not None:
                te = world["enemies"][target]
                base_dir = direction_toward(px, py, te["pos"].x, te["pos"].y)
                shots = 1 + world["extra_shots"]
                for s in range(shots):
                    ang = (s - (shots - 1) / 2) * 0.15
                    dir_v = base_dir.rotate_rad(ang)
                    world["orbs"].append({
                        "pos": pygame.Vector2(px, py),
                        "vel": dir_v * 320,
                        "life": 2.0,
                    })
                world["fire_timer"] = world["fire_cooldown"]

        world["orbit_angle"] += dt * 2.2
        if world["orbit_count"] > 0:
            for o in range(world["orbit_count"]):
                ang = world["orbit_angle"] + o * (6.283 / world["orbit_count"])
                ox = px + math.cos(ang) * 48
                oy = py + math.sin(ang) * 48
                for e in world["enemies"]:
                    if e["hp"] <= 0:
                        continue
                    if math.hypot(e["pos"].x - ox, e["pos"].y - oy) < e["radius"] + 8:
                        e["hp"] -= world["damage"] * 0.35 * dt

        for orb in world["orbs"]:
            orb["pos"] += orb["vel"] * dt
            orb["life"] -= dt
        world["orbs"] = [o for o in world["orbs"] if o["life"] > 0 and -20 < o["pos"].x < WIDTH + 20]
        if len(world["orbs"]) > MAX_ORBS:
            world["orbs"] = world["orbs"][-MAX_ORBS:]

        for orb in world["orbs"]:
            for e in world["enemies"]:
                if e["hp"] <= 0:
                    continue
                if orb["pos"].distance_to(e["pos"]) < e["radius"] + 6:
                    e["hp"] -= world["damage"]
                    orb["life"] = 0
                    break

        for e in world["enemies"]:
            if e["hp"] <= 0 and e.get("drop", True):
                e["drop"] = False
                if len(world["gems"]) < MAX_GEMS:
                    world["gems"].append({
                        "pos": pygame.Vector2(e["pos"].x, e["pos"].y),
                        "value": 3,
                    })
        world["enemies"] = [e for e in world["enemies"] if e["hp"] > 0]

        for gem in world["gems"]:
            if gem["pos"].distance_to(world["player_pos"]) < 70:
                gem["pos"] += direction_toward(
                    gem["pos"].x, gem["pos"].y, px, py
                ) * 220 * dt
            if gem["pos"].distance_to(world["player_pos"]) < world["player_radius"] + 8:
                world["xp"] += gem["value"]
                gem["value"] = 0
        world["gems"] = [g for g in world["gems"] if g["value"] > 0]

        while world["xp"] >= world["xp_need"]:
            world["xp"] -= world["xp_need"]
            world["level"] += 1
            world["xp_need"] = 10 + world["level"] * 4
            world["level_choices"] = pick_level_up_choices(UPGRADE_POOL, 3, world["rng"])
            state = "LEVEL_UP"
            break

        if world["elapsed"] >= WIN_SURVIVE and state == "PLAY":
            save_best(world["elapsed"])
            best_time = load_best()
            state = "WIN"

    screen.fill((12, 14, 28))
    for gx in range(MARGIN, WIDTH - MARGIN, 40):
        pygame.draw.line(screen, (22, 26, 44), (gx, MARGIN), (gx, HEIGHT - MARGIN))
    for gy in range(MARGIN, HEIGHT - MARGIN, 40):
        pygame.draw.line(screen, (22, 26, 44), (MARGIN, gy), (WIDTH - MARGIN, gy))
    pygame.draw.rect(screen, (30, 36, 58), (MARGIN, MARGIN, WIDTH - 2 * MARGIN, HEIGHT - 2 * MARGIN), 2)

    if state in ("PLAY", "LEVEL_UP", "PAUSE"):
        for gem in world["gems"]:
            pygame.draw.polygon(
                screen,
                (80, 230, 255),
                [
                    (gem["pos"].x, gem["pos"].y - 6),
                    (gem["pos"].x + 5, gem["pos"].y),
                    (gem["pos"].x, gem["pos"].y + 6),
                    (gem["pos"].x - 5, gem["pos"].y),
                ],
            )
        for orb in world["orbs"]:
            pygame.draw.circle(screen, (255, 255, 180), (int(orb["pos"].x), int(orb["pos"].y)), 5)
        for e in world["enemies"]:
            pygame.draw.circle(screen, (90, 70, 140), (int(e["pos"].x), int(e["pos"].y)), e["radius"])
            pygame.draw.circle(screen, (50, 40, 80), (int(e["pos"].x), int(e["pos"].y)), e["radius"], 2)
        if world["orbit_count"]:
            px, py = world["player_pos"].x, world["player_pos"].y
            for o in range(world["orbit_count"]):
                ang = world["orbit_angle"] + o * (6.283 / world["orbit_count"])
                ox, oy = int(px + math.cos(ang) * 48), int(py + math.sin(ang) * 48)
                pygame.draw.circle(screen, (255, 240, 160), (ox, oy), 7)
        draw_lantern(screen, world["player_pos"], world["player_radius"])
        draw_hp_bar(screen, world["player_hp"], world["player_max_hp"])
        hud = font.render(
            f"Time {world['elapsed']:.0f}/{WIN_SURVIVE:.0f}s  Lv{world['level']}  XP {world['xp']}/{world['xp_need']}",
            True,
            (200, 210, 255),
        )
        screen.blit(hud, (12, 32))
        if paused:
            overlay = font_big.render("PAUSED", True, (255, 255, 200))
            screen.blit(overlay, overlay.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

    if state == "MENU":
        t1 = font_big.render("Night Swarm", True, (255, 230, 150))
        t2 = font.render("Lantern keeper vs shadow creatures", True, (180, 190, 230))
        t3 = font.render(f"Survive {int(WIN_SURVIVE)}s · SPACE start · Best {best_time:.0f}s", True, (150, 160, 200))
        screen.blit(t1, t1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50)))
        screen.blit(t2, t2.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        screen.blit(t3, t3.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40)))

    if state == "LEVEL_UP":
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))
        title = font_big.render("Level up! Pick 1", True, (255, 240, 160))
        screen.blit(title, title.get_rect(center=(WIDTH // 2, 120)))
        for i, key in enumerate(world["level_choices"]):
            line = font.render(f"{i + 1} — {UPGRADE_POOL[key]['label']}", True, (220, 230, 255))
            screen.blit(line, line.get_rect(center=(WIDTH // 2, 200 + i * 36)))

    if state == "GAME_OVER":
        t1 = font_big.render("Lantern out", True, (255, 120, 120))
        t2 = font.render(f"Held {world['elapsed']:.1f}s · R menu", True, (200, 200, 230))
        screen.blit(t1, t1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20)))
        screen.blit(t2, t2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30)))

    if state == "WIN":
        save_best(world["elapsed"])
        best_time = load_best()
        t1 = font_big.render("Dawn!", True, (160, 255, 200))
        t2 = font.render(f"Survived {world['elapsed']:.1f}s · Best {best_time:.1f}s · R menu", True, (200, 230, 220))
        screen.blit(t1, t1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20)))
        screen.blit(t2, t2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30)))

    pygame.display.flip()

pygame.quit()