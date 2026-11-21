# game.py — Lesson 5.3: Glow Worm — complete grid snake
import random

import pygame

pygame.init()

WIDTH = 620
HEIGHT = 560
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Glow Worm")

clock = pygame.time.Clock()
running = True

font_big = pygame.font.Font(None, 56)
font_small = pygame.font.Font(None, 28)

COLS = 20
ROWS = 16
CELL = 26
BOARD_X = 36
BOARD_Y = 48

START = "start"
PLAYING = "playing"
GAME_OVER = "game_over"
state = START

BASE_INTERVAL = 0.22
MIN_INTERVAL = 0.08

segments: list[tuple[int, int]] = [(8, 8), (7, 8), (6, 8)]
direction = (1, 0)
pending_dir = (1, 0)
food = (12, 8)
score = 0
high_score = 0
move_timer = 0.0
move_interval = BASE_INTERVAL


def move_interval_for_score() -> float:
    speedup = min(12, score // 3)
    return max(MIN_INTERVAL, BASE_INTERVAL - speedup * 0.012)


def is_opposite(new_dir: tuple[int, int], current: tuple[int, int]) -> bool:
    return new_dir[0] == -current[0] and new_dir[1] == -current[1]


def spawn_food() -> tuple[int, int]:
    occupied = set(segments)
    for _ in range(COLS * ROWS):
        pos = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
        if pos not in occupied:
            return pos
    return (-1, -1)


def draw_cell_grid(surface: pygame.Surface) -> None:
    frame = pygame.Rect(BOARD_X - 6, BOARD_Y - 6, COLS * CELL + 12, ROWS * CELL + 12)
    pygame.draw.rect(surface, (40, 50, 70), frame, border_radius=8)
    for row in range(ROWS):
        for col in range(COLS):
            x = BOARD_X + col * CELL
            y = BOARD_Y + row * CELL
            pygame.draw.rect(surface, (18, 22, 34), (x, y, CELL - 1, CELL - 1))


def draw_glow_segment(
    surface: pygame.Surface,
    col: int,
    row: int,
    *,
    is_head: bool,
    pulse: float,
) -> None:
    cx = BOARD_X + col * CELL + CELL // 2
    cy = BOARD_Y + row * CELL + CELL // 2
    glow = int(8 + 4 * pulse)
    if is_head:
        outer = (60, 255, 170)
        inner = (140, 255, 210)
        eye = (25, 45, 35)
    else:
        outer = (50, 180, 255)
        inner = (90, 220, 255)
        eye = None
    pygame.draw.circle(surface, outer, (cx, cy), CELL // 2 + glow)
    pygame.draw.circle(surface, inner, (cx, cy), CELL // 2 - 2)
    if eye:
        pygame.draw.circle(surface, eye, (cx - 4, cy - 3), 3)
        pygame.draw.circle(surface, eye, (cx + 4, cy - 3), 3)


def draw_food(surface: pygame.Surface, pos: tuple[int, int], pulse: float) -> None:
    if pos[0] < 0:
        return
    fc, fr = pos
    cx = BOARD_X + fc * CELL + CELL // 2
    cy = BOARD_Y + fr * CELL + CELL // 2
    r = int(CELL // 3 + 2 * pulse)
    pygame.draw.circle(surface, (255, 100, 190), (cx, cy), r + 4)
    pygame.draw.circle(surface, (255, 220, 240), (cx, cy), r)


def step_worm() -> None:
    global segments, food, score, state, move_interval, direction
    direction = pending_dir
    hc, hr = segments[0]
    dc, dr = direction
    new_head = (hc + dc, hr + dr)
    if new_head[0] < 0 or new_head[0] >= COLS or new_head[1] < 0 or new_head[1] >= ROWS:
        crash()
        return
    grow = new_head == food
    segments = [new_head] + segments
    if not grow:
        segments.pop()
    if segments[0] in segments[1:]:
        crash()
        return
    if grow:
        score += 1
        move_interval = move_interval_for_score()
        food = spawn_food()
        if food[0] < 0:
            state = GAME_OVER


def crash() -> None:
    global state, high_score
    if score > high_score:
        high_score = score
    state = GAME_OVER


def start_game() -> None:
    global segments, direction, pending_dir, food, score, move_timer, move_interval, state
    segments = [(8, 8), (7, 8), (6, 8)]
    direction = (1, 0)
    pending_dir = (1, 0)
    food = spawn_food()
    score = 0
    move_timer = 0.0
    move_interval = BASE_INTERVAL
    state = PLAYING


while running:
    dt = clock.tick(60) / 1000
    pulse = (pygame.time.get_ticks() % 1000) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if state == START and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                start_game()
            elif state == GAME_OVER and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                state = START
            elif state == PLAYING:
                if event.key == pygame.K_UP and not is_opposite((0, -1), direction):
                    pending_dir = (0, -1)
                elif event.key == pygame.K_DOWN and not is_opposite((0, 1), direction):
                    pending_dir = (0, 1)
                elif event.key == pygame.K_LEFT and not is_opposite((-1, 0), direction):
                    pending_dir = (-1, 0)
                elif event.key == pygame.K_RIGHT and not is_opposite((1, 0), direction):
                    pending_dir = (1, 0)

    if state == PLAYING:
        move_timer += dt
        if move_timer >= move_interval:
            move_timer = 0.0
            step_worm()

    screen.fill((10, 12, 22))
    draw_cell_grid(screen)

    if state == PLAYING:
        draw_food(screen, food, pulse)
        for i, (col, row) in enumerate(segments):
            draw_glow_segment(screen, col, row, is_head=(i == 0), pulse=pulse)
        hud = font_small.render(f"Score {score}  |  Best {high_score}", True, (200, 230, 255))
        screen.blit(hud, (BOARD_X, 12))
        tip = font_small.render(
            f"Tick {move_interval:.2f}s — faster as you eat!",
            True,
            (130, 150, 190),
        )
        screen.blit(tip, (BOARD_X, BOARD_Y + ROWS * CELL + 16))
    elif state == START:
        title = font_big.render("Glow Worm", True, (120, 255, 200))
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)))
        sub = font_small.render("SPACE to crawl — arrow keys steer", True, (180, 200, 230))
        screen.blit(sub, sub.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        best = font_small.render(f"Session best: {high_score}", True, (255, 220, 160))
        screen.blit(best, best.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 36)))
    else:
        over = font_big.render("Game Over", True, (255, 120, 140))
        screen.blit(over, over.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30)))
        final = font_small.render(f"Score {score}  |  Best {high_score}", True, (220, 230, 255))
        screen.blit(final, final.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))
        again = font_small.render("SPACE — title", True, (160, 180, 210))
        screen.blit(again, again.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 52)))

    pygame.display.flip()

pygame.quit()