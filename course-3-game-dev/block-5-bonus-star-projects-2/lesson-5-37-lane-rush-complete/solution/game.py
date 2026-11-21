# game.py — Lesson 5.37: Lane Rush — complete (solution)
from __future__ import annotations

import json
import random
from pathlib import Path

import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
ROAD_LEFT = 140
ROAD_WIDTH = 360
NUM_LANES = 4
LANE_W = ROAD_WIDTH // NUM_LANES
STRIPE_H = 44
BASE_SCROLL = 175.0
TRAFFIC_BASE = 235.0
SPAWN_BASE = 1.15
PLAYER_Y = HEIGHT - 78
CAR_W, CAR_H = 42, 68
TRAFFIC_W, TRAFFIC_H = 40, 62
LANE_LERP = 14.0
NEAR_MISS = 22.0
MAX_TRAFFIC = 28

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lane Rush — Pro")
clock = pygame.time.Clock()
font_big = pygame.font.Font(None, 52)
font = pygame.font.Font(None, 28)

SESSION_FILE = Path.home() / ".lane_rush_best.json"


def load_best() -> float:
    if SESSION_FILE.is_file():
        try:
            data = json.loads(SESSION_FILE.read_text())
            return float(data.get("best_distance", 0.0))
        except (json.JSONDecodeError, OSError, TypeError, ValueError):
            pass
    return 0.0


def save_best(meters: float) -> None:
    prev = load_best()
    if meters > prev:
        SESSION_FILE.write_text(json.dumps({"best_distance": round(meters, 1)}))


def lane_center(lane: int) -> float:
    return ROAD_LEFT + lane * LANE_W + LANE_W / 2


def draw_road(surf: pygame.Surface, offset: float) -> None:
    surf.fill((14, 10, 28))
    pygame.draw.rect(surf, (30, 32, 50), (ROAD_LEFT, 0, ROAD_WIDTH, HEIGHT))
    y = -STRIPE_H + (offset % STRIPE_H)
    while y < HEIGHT:
        stripe = pygame.Rect(ROAD_LEFT + 12, int(y), ROAD_WIDTH - 24, STRIPE_H // 2)
        pygame.draw.rect(surf, (250, 235, 100), stripe, border_radius=3)
        y += STRIPE_H
    for i in range(1, NUM_LANES):
        lx = ROAD_LEFT + i * LANE_W
        pygame.draw.line(surf, (50, 54, 74), (lx, 0), (lx, HEIGHT), 1)


def draw_player(surf: pygame.Surface, cx: float) -> None:
    body = pygame.Rect(0, 0, CAR_W, CAR_H)
    body.center = (int(cx), PLAYER_Y)
    pygame.draw.rect(surf, (70, 230, 255), body, border_radius=8)
    pygame.draw.rect(surf, (170, 255, 255), (body.x + 6, body.y + 10, body.w - 12, 18), border_radius=4)


def draw_traffic(surf: pygame.Surface, cx: float, cy: float) -> None:
    body = pygame.Rect(0, 0, TRAFFIC_W, TRAFFIC_H)
    body.center = (int(cx), int(cy))
    pygame.draw.rect(surf, (255, 105, 145), body, border_radius=6)


def draw_pickup(surf: pygame.Surface, cx: float, cy: float, kind: str) -> None:
    if kind == "coin":
        pygame.draw.circle(surf, (255, 220, 90), (int(cx), int(cy)), 10)
        pygame.draw.circle(surf, (255, 250, 180), (int(cx), int(cy)), 6)
    else:
        pygame.draw.circle(surf, (120, 200, 255), (int(cx), int(cy)), 10, 2)
        pygame.draw.rect(surf, (140, 220, 255), (int(cx) - 5, int(cy) - 7, 10, 14), border_radius=2)


def edge_gap(a: pygame.Rect, b: pygame.Rect) -> float:
    if a.colliderect(b):
        return 0.0
    dx = max(b.left - a.right, a.left - b.right, 0)
    dy = max(b.top - a.bottom, a.top - b.bottom, 0)
    return (dx * dx + dy * dy) ** 0.5


def reset_run(rng: random.Random) -> dict:
    return {
        "player_lane": 1,
        "player_x": lane_center(1),
        "scroll_offset": 0.0,
        "distance_m": 0.0,
        "bonus_score": 0,
        "fuel": 100.0,
        "elapsed": 0.0,
        "spawn_timer": 0.35,
        "pickup_timer": 2.2,
        "traffic": [],
        "pickups": [],
        "rng": rng,
    }


state = "MENU"
best_distance = load_best()
rng = random.Random()
world = reset_run(rng)
running = True

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if state == "MENU" and event.key in (pygame.K_RETURN, pygame.K_SPACE):
                world = reset_run(rng)
                state = "PLAY"
            elif state == "PLAY":
                if event.key in (pygame.K_LEFT, pygame.K_a) and world["player_lane"] > 0:
                    world["player_lane"] -= 1
                if event.key in (pygame.K_RIGHT, pygame.K_d) and world["player_lane"] < NUM_LANES - 1:
                    world["player_lane"] += 1
            elif state in ("GAME_OVER", "GRADUATE") and event.key == pygame.K_r:
                world = reset_run(rng)
                state = "MENU"

    scroll_speed = BASE_SCROLL + world["elapsed"] * 6.5 if state == "PLAY" else BASE_SCROLL
    traffic_speed = TRAFFIC_BASE + world["elapsed"] * 4.0 if state == "PLAY" else TRAFFIC_BASE
    spawn_every = max(0.42, SPAWN_BASE - world["elapsed"] * 0.015) if state == "PLAY" else SPAWN_BASE

    if state == "PLAY":
        world["elapsed"] += dt
        world["fuel"] = max(0.0, world["fuel"] - dt * 3.2)
        if world["fuel"] <= 0:
            state = "GAME_OVER"
            save_best(world["distance_m"])

        world["scroll_offset"] = (world["scroll_offset"] + scroll_speed * dt) % STRIPE_H
        world["distance_m"] += scroll_speed * dt * 0.12
        tx = lane_center(world["player_lane"])
        world["player_x"] += (tx - world["player_x"]) * min(1.0, LANE_LERP * dt)

        world["spawn_timer"] -= dt
        if world["spawn_timer"] <= 0 and len(world["traffic"]) < MAX_TRAFFIC:
            world["spawn_timer"] = spawn_every
            lane = world["rng"].randint(0, NUM_LANES - 1)
            world["traffic"].append({"lane": lane, "cy": float(-TRAFFIC_H), "near": False})

        world["pickup_timer"] -= dt
        if world["pickup_timer"] <= 0:
            world["pickup_timer"] = world["rng"].uniform(1.4, 2.8)
            lane = world["rng"].randint(0, NUM_LANES - 1)
            kind = "fuel" if world["rng"].random() < 0.35 else "coin"
            world["pickups"].append({"lane": lane, "cy": -20.0, "kind": kind})

        pr = pygame.Rect(0, 0, CAR_W - 6, CAR_H - 6)
        pr.center = (int(world["player_x"]), PLAYER_Y)

        for car in world["traffic"]:
            car["cy"] += traffic_speed * dt
            tr = pygame.Rect(0, 0, TRAFFIC_W - 4, TRAFFIC_H - 4)
            tr.center = (int(lane_center(car["lane"])), int(car["cy"]))
            if pr.colliderect(tr):
                state = "GAME_OVER"
                save_best(world["distance_m"])
            gap = edge_gap(pr, tr)
            if not car["near"] and 0 < gap < NEAR_MISS:
                car["near"] = True
                world["bonus_score"] += 25

        world["traffic"] = [c for c in world["traffic"] if c["cy"] < HEIGHT + 80]

        for pk in world["pickups"][:]:
            pk["cy"] += scroll_speed * dt
            pick = pygame.Rect(0, 0, 20, 20)
            pick.center = (int(lane_center(pk["lane"])), int(pk["cy"]))
            if pr.colliderect(pick):
                if pk["kind"] == "coin":
                    world["bonus_score"] += 40
                else:
                    world["fuel"] = min(100.0, world["fuel"] + 22.0)
                world["pickups"].remove(pk)
        world["pickups"] = [p for p in world["pickups"] if p["cy"] < HEIGHT + 40]

        if world["distance_m"] >= 1200 and state == "PLAY":
            state = "GRADUATE"
            save_best(world["distance_m"])
            best_distance = load_best()

    draw_road(screen, world["scroll_offset"])
    if state == "PLAY":
        for car in world["traffic"]:
            draw_traffic(screen, lane_center(car["lane"]), car["cy"])
        for pk in world["pickups"]:
            draw_pickup(screen, lane_center(pk["lane"]), pk["cy"], pk["kind"])
        draw_player(screen, world["player_x"])
        fuel_w = int(160 * world["fuel"] / 100)
        pygame.draw.rect(screen, (40, 44, 70), (12, 12, 160, 12), border_radius=4)
        pygame.draw.rect(screen, (100, 220, 255), (12, 12, fuel_w, 12), border_radius=4)
        hud = font.render(
            f"{world['distance_m']:.0f} m  bonus {world['bonus_score']}  best {best_distance:.0f}",
            True,
            (210, 220, 255),
        )
        screen.blit(hud, (12, 30))

    if state == "MENU":
        t1 = font_big.render("Lane Rush", True, (90, 250, 255))
        t2 = font.render("ENTER start · dodge traffic · grab fuel", True, (190, 200, 240))
        screen.blit(t1, (WIDTH // 2 - t1.get_width() // 2, 120))
        screen.blit(t2, (WIDTH // 2 - t2.get_width() // 2, 190))
        best = font.render(f"Best distance: {best_distance:.0f} m", True, (200, 210, 255))
        screen.blit(best, (WIDTH // 2 - best.get_width() // 2, 230))
    elif state == "GAME_OVER":
        over = font_big.render("Game Over", True, (255, 120, 150))
        screen.blit(over, (WIDTH // 2 - over.get_width() // 2, 160))
        msg = font.render("R — menu", True, (210, 220, 255))
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, 230))
    elif state == "GRADUATE":
        g1 = font_big.render("Block 5 ★ Complete!", True, (255, 230, 120))
        g2 = font.render("All ten bonus games shipped — you rock!", True, (200, 240, 255))
        screen.blit(g1, (WIDTH // 2 - g1.get_width() // 2, 130))
        screen.blit(g2, (WIDTH // 2 - g2.get_width() // 2, 200))
        map_hint = font.render("See STUDENT-MAP for graduation checklist", True, (180, 200, 255))
        screen.blit(map_hint, (WIDTH // 2 - map_hint.get_width() // 2, 250))

    pygame.display.flip()

pygame.quit()