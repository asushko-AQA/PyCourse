# game.py — Lesson 5.29: Leap Lands — complete (solution)
from __future__ import annotations

import json
import time
from pathlib import Path

import pygame

pygame.init()

TILE = 32
VIEW_W, VIEW_H = 640, 480
screen = pygame.display.set_mode((VIEW_W, VIEW_H))
pygame.display.set_caption("Leap Lands — Pro")

clock = pygame.time.Clock()
font_big = pygame.font.Font(None, 46)
font_small = pygame.font.Font(None, 28)

LEVELS = [
    [
        "################",
        "#S  C           #",
        "#  ===    ^     #",
        "#     C         F#",
        "################",
    ],
    [
        "########################",
        "#S    C    E     C      #",
        "#  =======      ====    #",
        "#        ^              #",
        "#  C              E     F#",
        "########################",
    ],
    [
        "################################",
        "#S  C   E    ====   C     ^    F#",
        "################################",
    ],
]

PLAYER_W, PLAYER_H = 26, 34
ENEMY_W, ENEMY_H = 30, 24
MOVE_SPEED = 265
GRAVITY = 1180
JUMP_V = -405
PATROL_SPEED = 75
START_LIVES = 3
SOLID = {"#", "="}
SESSION_FILE = Path.home() / ".leap_lands_best.json"


def load_best() -> dict:
    if SESSION_FILE.is_file():
        try:
            return json.loads(SESSION_FILE.read_text())
        except (json.JSONDecodeError, OSError):
            pass
    return {"coins": 0, "time": 9999.0}


def save_best(coins: int, elapsed: float) -> None:
    best = load_best()
    if coins > best["coins"] or (coins == best["coins"] and elapsed < best["time"]):
        SESSION_FILE.write_text(json.dumps({"coins": coins, "time": round(elapsed, 1)}))


def build_level(rows: list[str]):
    solids: list[pygame.Rect] = []
    coins: list[pygame.Rect] = []
    spikes: list[pygame.Rect] = []
    enemies: list[dict] = []
    spawn = pygame.Rect(64, 200, PLAYER_W, PLAYER_H)
    flag = pygame.Rect(0, 0, TILE, TILE * 2)
    world_w = max(len(r) for r in rows) * TILE
    for row_i, row in enumerate(rows):
        for col_i, ch in enumerate(row):
            x, y = col_i * TILE, row_i * TILE
            if ch in SOLID:
                solids.append(pygame.Rect(x, y, TILE, TILE))
            elif ch == "C":
                coins.append(pygame.Rect(x + 8, y + 8, TILE - 16, TILE - 16))
            elif ch == "^":
                spikes.append(pygame.Rect(x + 4, y + TILE // 2, TILE - 8, TILE // 2))
            elif ch == "S":
                spawn = pygame.Rect(x, y - PLAYER_H + TILE, PLAYER_W, PLAYER_H)
            elif ch == "F":
                flag = pygame.Rect(x, y - TILE, TILE, TILE * 2)
            elif ch == "E":
                pad = pygame.Rect(x, y - ENEMY_H + TILE, TILE * 4, TILE)
                enemies.append({
                    "rect": pygame.Rect(x, y - ENEMY_H + TILE, ENEMY_W, ENEMY_H),
                    "dir": 1,
                    "min_x": pad.left,
                    "max_x": pad.right - ENEMY_W,
                    "alive": True,
                })
    return solids, coins, spikes, enemies, spawn, flag, world_w


def move_and_resolve(rect: pygame.Rect, solids: list[pygame.Rect], dx: float, dy: float) -> tuple[pygame.Rect, bool]:
    on_ground = False
    rect.x += int(dx)
    for tile in solids:
        if rect.colliderect(tile):
            if dx > 0:
                rect.right = tile.left
            elif dx < 0:
                rect.left = tile.right
    rect.y += int(dy)
    for tile in solids:
        if rect.colliderect(tile):
            if dy > 0:
                rect.bottom = tile.top
                on_ground = True
            elif dy < 0:
                rect.top = tile.bottom
    return rect, on_ground


def load_level(index: int):
    return build_level(LEVELS[index])


state = "MENU"
level_index = 0
lives = START_LIVES
total_coins = 0
level_coins = 0
elapsed = 0.0
level_start = 0.0
camera_x = 0.0
vel_y = 0.0
grounded = False
player = pygame.Rect(0, 0, PLAYER_W, PLAYER_H)
solids: list[pygame.Rect] = []
coins: list[pygame.Rect] = []
spikes: list[pygame.Rect] = []
enemies: list[dict] = []
spawn_point = pygame.Rect(0, 0, 0, 0)
flag = pygame.Rect(0, 0, 0, 0)
world_w = VIEW_W
level_rows: list[str] = []
running = True


def reset_level(idx: int) -> None:
    global player, vel_y, grounded, camera_x, level_coins, level_start
    global solids, coins, spikes, enemies, spawn_point, flag, world_w, level_rows
    level_rows = LEVELS[idx]
    solids, coins, spikes, enemies, spawn_point, flag, world_w = load_level(idx)
    player = spawn_point.copy()
    vel_y = 0.0
    grounded = False
    camera_x = 0.0
    level_coins = 0
    level_start = time.time()


def start_game() -> None:
    global state, level_index, lives, total_coins, elapsed
    state = "PLAY"
    level_index = 0
    lives = START_LIVES
    total_coins = 0
    elapsed = 0.0
    reset_level(0)


def respawn() -> None:
    global player, vel_y, grounded, lives
    lives -= 1
    player = spawn_point.copy()
    vel_y = 0.0
    grounded = False
    if lives <= 0:
        state = "GAME_OVER"


def stomp(enemy: dict) -> bool:
    if not enemy["alive"]:
        return False
    er = enemy["rect"]
    if player.bottom <= er.top + 10 and vel_y > 0:
        if player.colliderect(er):
            enemy["alive"] = False
            return True
    return False


def draw_world() -> None:
    cam = int(camera_x)
    screen.fill((12, 16, 38))
    for tile in solids:
        dr = tile.move(-cam, 0)
        if dr.right < 0 or dr.left > VIEW_W:
            continue
        ch = level_rows[tile.y // TILE][tile.x // TILE]
        color = (68, 82, 128) if ch == "#" else (95, 175, 215)
        pygame.draw.rect(screen, color, dr)
    for spike in spikes:
        dr = spike.move(-cam, 0)
        pygame.draw.polygon(
            screen,
            (255, 85, 115),
            [(dr.centerx, dr.top), (dr.right, dr.bottom), (dr.left, dr.bottom)],
        )
    for coin in coins:
        dr = coin.move(-cam, 0)
        if 0 <= dr.centerx <= VIEW_W:
            pygame.draw.circle(screen, (255, 215, 75), dr.center, dr.width // 2)
    for enemy in enemies:
        if enemy["alive"]:
            dr = enemy["rect"].move(-cam, 0)
            pygame.draw.ellipse(screen, (255, 105, 175), dr)
    fr = flag.move(-cam, 0)
    pygame.draw.rect(screen, (75, 250, 155), fr)
    pygame.draw.rect(screen, (88, 248, 205), player.move(-cam, 0), border_radius=5)
    t = time.time() - level_start
    hud = font_small.render(
        f"Lvl {level_index + 1}/{len(LEVELS)}  Lives {lives}  Coins {total_coins}+{level_coins}  {t:.1f}s",
        True,
        (225, 230, 255),
    )
    screen.blit(hud, (8, 8))


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if state == "MENU" and event.key in (pygame.K_RETURN, pygame.K_SPACE):
                start_game()
            elif state == "PLAY" and event.key == pygame.K_SPACE and grounded:
                vel_y = JUMP_V
                grounded = False
            elif state == "GAME_OVER" and event.key == pygame.K_r:
                state = "MENU"
            elif state == "WIN" and event.key == pygame.K_r:
                state = "MENU"

    if state == "MENU":
        screen.fill((18, 22, 50))
        title = font_big.render("Leap Lands", True, (120, 255, 210))
        sub = font_small.render("ENTER/SPACE start · 3 levels · collect coins", True, (190, 200, 240))
        best = load_best()
        rec = font_small.render(f"Session best: {best['coins']} coins in {best['time']:.1f}s", True, (160, 170, 210))
        screen.blit(title, (VIEW_W // 2 - title.get_width() // 2, 140))
        screen.blit(sub, (VIEW_W // 2 - sub.get_width() // 2, 200))
        screen.blit(rec, (VIEW_W // 2 - rec.get_width() // 2, 240))

    elif state == "PLAY":
        keys = pygame.key.get_pressed()
        dx = 0.0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= MOVE_SPEED * dt
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += MOVE_SPEED * dt

        vel_y += GRAVITY * dt
        player, grounded = move_and_resolve(player, solids, dx, vel_y * dt)

        for spike in spikes:
            if player.colliderect(spike):
                respawn()
                break

        for enemy in enemies:
            if not enemy["alive"]:
                continue
            er = enemy["rect"]
            er.x += int(enemy["dir"] * PATROL_SPEED * dt)
            if er.left <= enemy["min_x"]:
                er.left = enemy["min_x"]
                enemy["dir"] = 1
            if er.right >= enemy["max_x"]:
                er.right = enemy["max_x"]
                enemy["dir"] = -1
            if player.colliderect(er):
                if stomp(enemy):
                    vel_y = JUMP_V * 0.4
                else:
                    respawn()
                    break

        for coin in coins[:]:
            if player.colliderect(coin):
                coins.remove(coin)
                level_coins += 1

        if player.colliderect(flag):
            total_coins += level_coins
            if level_index + 1 >= len(LEVELS):
                elapsed = time.time() - level_start + level_index * 30
                save_best(total_coins, elapsed)
                state = "WIN"
            else:
                state = "LEVEL_CLEAR"
                level_index += 1

        target = player.centerx - VIEW_W // 2
        camera_x += (target - camera_x) * min(1.0, dt * 5)
        camera_x = max(0, min(world_w - VIEW_W, camera_x))

        if state == "LEVEL_CLEAR":
            reset_level(level_index)
            state = "PLAY"
        else:
            draw_world()

    elif state == "LEVEL_CLEAR":
        draw_world()

    elif state == "GAME_OVER":
        screen.fill((40, 18, 28))
        msg = font_big.render("Game Over", True, (255, 120, 140))
        hint = font_small.render("R = menu", True, (220, 200, 210))
        screen.blit(msg, (VIEW_W // 2 - msg.get_width() // 2, 200))
        screen.blit(hint, (VIEW_W // 2 - hint.get_width() // 2, 260))

    elif state == "WIN":
        screen.fill((20, 50, 40))
        msg = font_big.render("You Win!", True, (140, 255, 200))
        stats = font_small.render(f"Coins {total_coins}  Time {elapsed:.1f}s", True, (220, 255, 230))
        screen.blit(msg, (VIEW_W // 2 - msg.get_width() // 2, 180))
        screen.blit(stats, (VIEW_W // 2 - stats.get_width() // 2, 240))

    pygame.display.flip()

pygame.quit()