# game.py — Lesson 4.6: Prism Dash — complete bonus auto-runner
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prism Dash")

clock = pygame.time.Clock()
running = True

font_big = pygame.font.Font(None, 64)
font_small = pygame.font.Font(None, 32)

START = "start"
PLAYING = "playing"
GAME_OVER = "game_over"
WIN = "win"
state = START

PLAYER_X = 140
CUBE_SIZE = 36
GROUND_Y = 400
TILE_W = 48
BASE_SCROLL = 240
GRAVITY = 1400
JUMP_V = -520
ROT_SPEED = 300
PLATFORM_H = 44
SPIKE_H = 36

# Level string: _ = flat ground, # = platform block, ^ = floor spike
LEVEL = "____##__^^__####__^^__##__^^____####____"

world_x = 0.0
player_y = float(GROUND_Y - CUBE_SIZE)
vel_y = 0.0
angle = 0.0
grounded = True
attempts = 0
best_progress = 0


def level_length_px() -> int:
    return len(LEVEL) * TILE_W


def progress_pct() -> int:
    if level_length_px() == 0:
        return 0
    return min(100, int(world_x / level_length_px() * 100))


def draw_cube(surface: pygame.Surface, center_x: int, center_y: int, angle_deg: float) -> None:
    tile = pygame.Surface((CUBE_SIZE, CUBE_SIZE), pygame.SRCALPHA)
    pygame.draw.rect(tile, (255, 110, 210), tile.get_rect(), border_radius=6)
    pygame.draw.rect(tile, (255, 245, 255), tile.get_rect().inflate(-8, -8), width=2, border_radius=4)
    rotated = pygame.transform.rotate(tile, -angle_deg)
    rect = rotated.get_rect(center=(center_x, center_y))
    surface.blit(rotated, rect)


def player_rect() -> pygame.Rect:
    return pygame.Rect(PLAYER_X - CUBE_SIZE // 2, int(player_y), CUBE_SIZE, CUBE_SIZE)


def draw_ground(surface: pygame.Surface) -> None:
    pygame.draw.rect(surface, (45, 50, 70), (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))
    pygame.draw.line(surface, (120, 130, 180), (0, GROUND_Y), (WIDTH, GROUND_Y), 3)


def level_objects() -> tuple[list[pygame.Rect], list[pygame.Rect]]:
    """Platforms you can land on + spike hitboxes."""
    platforms: list[pygame.Rect] = []
    spikes: list[pygame.Rect] = []
    for i, ch in enumerate(LEVEL):
        sx = i * TILE_W - int(world_x)
        if sx < -TILE_W or sx > WIDTH + TILE_W:
            continue
        if ch == "#":
            platforms.append(pygame.Rect(sx, GROUND_Y - PLATFORM_H, TILE_W, PLATFORM_H))
        elif ch == "^":
            spikes.append(pygame.Rect(sx + 6, GROUND_Y - SPIKE_H + 6, TILE_W - 12, SPIKE_H - 10))
    return platforms, spikes


def draw_level(surface: pygame.Surface) -> None:
    for i, ch in enumerate(LEVEL):
        sx = i * TILE_W - int(world_x)
        if sx < -TILE_W or sx > WIDTH + TILE_W:
            continue
        if ch == "#":
            block = pygame.Rect(sx, GROUND_Y - PLATFORM_H, TILE_W, PLATFORM_H)
            pygame.draw.rect(surface, (70, 200, 255), block, border_radius=4)
        elif ch == "^":
            tip = (sx + TILE_W // 2, GROUND_Y - SPIKE_H)
            base_l = (sx + 4, GROUND_Y)
            base_r = (sx + TILE_W - 4, GROUND_Y)
            pygame.draw.polygon(surface, (255, 80, 100), [tip, base_l, base_r])


def snap_platforms(platforms: list[pygame.Rect], dt: float) -> None:
    global player_y, vel_y, grounded
    grounded = False
    feet_prev = player_y + CUBE_SIZE - vel_y * dt
    for plat in platforms:
        if player_rect().colliderect(plat) and vel_y >= 0:
            if feet_prev <= plat.top + 10:
                player_y = plat.top - CUBE_SIZE
                vel_y = 0
                grounded = True
                return
    if player_y + CUBE_SIZE >= GROUND_Y - 1:
        player_y = GROUND_Y - CUBE_SIZE
        vel_y = 0
        grounded = True


def start_run() -> None:
    global world_x, player_y, vel_y, angle, state, grounded
    world_x = 0.0
    player_y = float(GROUND_Y - CUBE_SIZE)
    vel_y = 0.0
    angle = 0.0
    grounded = True
    state = PLAYING


def die() -> None:
    global state, attempts, best_progress
    attempts += 1
    pct = progress_pct()
    if pct > best_progress:
        best_progress = pct
    state = GAME_OVER


def draw_progress_bar(surface: pygame.Surface) -> None:
    pct = progress_pct()
    bar = pygame.Rect(16, HEIGHT - 36, WIDTH - 32, 16)
    fill = pygame.Rect(bar.x, bar.y, int(bar.width * pct / 100), bar.height)
    pygame.draw.rect(surface, (50, 50, 70), bar, border_radius=8)
    pygame.draw.rect(surface, (255, 140, 230), fill, border_radius=8)
    label = font_small.render(f"Progress: {pct}%  Attempts: {attempts}  Best: {best_progress}%", True, (240, 230, 255))
    surface.blit(label, (16, HEIGHT - 62))


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if state == START and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                start_run()
            elif state == PLAYING and event.key == pygame.K_SPACE and grounded:
                vel_y = JUMP_V
                grounded = False
            elif state in (GAME_OVER, WIN) and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                state = START

    screen.fill((25, 18, 45))
    for stripe in range(0, WIDTH, 80):
        pygame.draw.rect(screen, (35, 28, 58), (stripe, 0, 40, GROUND_Y))

    if state == START:
        title = font_big.render("Prism Dash", True, (255, 200, 245))
        sub = font_small.render("Bonus ★ Project #2", True, (220, 200, 240))
        hint = font_small.render("SPACE to run", True, (180, 170, 210))
        best = font_small.render(f"Best run: {best_progress}%", True, (180, 170, 210))
        draw_ground(screen)
        draw_cube(screen, PLAYER_X, GROUND_Y - CUBE_SIZE // 2, 0)
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 80)))
        screen.blit(sub, sub.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30)))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))
        screen.blit(best, best.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 55)))

    elif state == PLAYING:
        scroll = BASE_SCROLL + progress_pct() * 2
        world_x += scroll * dt

        vel_y += GRAVITY * dt
        player_y += vel_y * dt

        platforms, spikes = level_objects()
        snap_platforms(platforms, dt)

        center_y = int(player_y) + CUBE_SIZE // 2
        if grounded:
            angle = 0.0
        else:
            angle = (angle + ROT_SPEED * dt) % 360

        draw_level(screen)
        draw_ground(screen)
        draw_cube(screen, PLAYER_X, center_y, angle)
        draw_progress_bar(screen)

        rect = player_rect()
        for spike in spikes:
            if rect.colliderect(spike):
                die()
                break

        if world_x >= level_length_px():
            if progress_pct() > best_progress:
                best_progress = progress_pct()
            state = WIN

    elif state == GAME_OVER:
        draw_level(screen)
        draw_ground(screen)
        draw_cube(screen, PLAYER_X, int(player_y) + CUBE_SIZE // 2, angle)
        draw_progress_bar(screen)
        over = font_big.render("Try Again!", True, (255, 120, 140))
        lines = font_small.render(f"Reached {progress_pct()}%  Attempts: {attempts}", True, (255, 255, 255))
        hint = font_small.render("SPACE for title", True, (220, 210, 240))
        screen.blit(over, over.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50)))
        screen.blit(lines, lines.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50)))

    elif state == WIN:
        draw_level(screen)
        draw_ground(screen)
        draw_cube(screen, PLAYER_X, GROUND_Y - CUBE_SIZE // 2, 0)
        won = font_big.render("Level Clear!", True, (140, 255, 200))
        lines = font_small.render(f"100% in {attempts + 1} tries — Best: {best_progress}%", True, (255, 255, 255))
        hint = font_small.render("SPACE for title", True, (220, 210, 240))
        screen.blit(won, won.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50)))
        screen.blit(lines, lines.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50)))

    pygame.display.flip()

pygame.quit()