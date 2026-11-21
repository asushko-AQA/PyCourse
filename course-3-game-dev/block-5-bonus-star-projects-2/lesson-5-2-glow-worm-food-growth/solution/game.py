# game.py — Lesson 5.2: Glow Worm — food + growth + crash
import random

import pygame

pygame.init()

WIDTH = 620
HEIGHT = 560
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Glow Worm — Eat")

clock = pygame.time.Clock()
running = True

font_big = pygame.font.Font(None, 48)
font_small = pygame.font.Font(None, 28)

COLS = 20
ROWS = 16
CELL = 26
BOARD_X = 36
BOARD_Y = 48
MOVE_INTERVAL = 0.2

segments: list[tuple[int, int]] = [(8, 8), (7, 8), (6, 8)]
direction = (1, 0)
pending_dir = (1, 0)
food = (12, 8)
score = 0
move_timer = 0.0
alive = True


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


def draw_glow_segment(surface: pygame.Surface, col: int, row: int, *, is_head: bool) -> None:
    cx = BOARD_X + col * CELL + CELL // 2
    cy = BOARD_Y + row * CELL + CELL // 2
    if is_head:
        pygame.draw.circle(surface, (60, 255, 170), (cx, cy), CELL // 2 + 6)
        pygame.draw.circle(surface, (140, 255, 210), (cx, cy), CELL // 2 - 2)
    else:
        pygame.draw.circle(surface, (50, 180, 255), (cx, cy), CELL // 2 + 4)
        pygame.draw.circle(surface, (90, 220, 255), (cx, cy), CELL // 2 - 2)


def draw_food(surface: pygame.Surface, pos: tuple[int, int]) -> None:
    fc, fr = pos
    cx = BOARD_X + fc * CELL + CELL // 2
    cy = BOARD_Y + fr * CELL + CELL // 2
    pygame.draw.circle(surface, (255, 100, 190), (cx, cy), CELL // 3 + 4)
    pygame.draw.circle(surface, (255, 220, 240), (cx, cy), CELL // 3)


def step_worm() -> None:
    global segments, food, score, alive, direction
    if not alive:
        return
    direction = pending_dir
    hc, hr = segments[0]
    dc, dr = direction
    new_head = (hc + dc, hr + dr)
    if new_head[0] < 0 or new_head[0] >= COLS or new_head[1] < 0 or new_head[1] >= ROWS:
        alive = False
        return
    grow = new_head == food
    segments = [new_head] + segments
    if not grow:
        segments.pop()
    if segments[0] in segments[1:]:
        alive = False
        return
    if grow:
        score += 1
        food = spawn_food()


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and alive:
            if event.key == pygame.K_UP and not is_opposite((0, -1), direction):
                pending_dir = (0, -1)
            elif event.key == pygame.K_DOWN and not is_opposite((0, 1), direction):
                pending_dir = (0, 1)
            elif event.key == pygame.K_LEFT and not is_opposite((-1, 0), direction):
                pending_dir = (-1, 0)
            elif event.key == pygame.K_RIGHT and not is_opposite((1, 0), direction):
                pending_dir = (1, 0)
        elif event.type == pygame.KEYDOWN and not alive and event.key == pygame.K_SPACE:
            segments = [(8, 8), (7, 8), (6, 8)]
            direction = (1, 0)
            pending_dir = (1, 0)
            food = spawn_food()
            score = 0
            alive = True

    if alive:
        move_timer += dt
        if move_timer >= MOVE_INTERVAL:
            move_timer = 0.0
            step_worm()

    screen.fill((10, 12, 22))
    draw_cell_grid(screen)
    draw_food(screen, food)
    for i, (col, row) in enumerate(segments):
        draw_glow_segment(screen, col, row, is_head=(i == 0))

    if alive:
        hud = font_small.render(f"Score {score}", True, (200, 230, 255))
        screen.blit(hud, (BOARD_X, 12))
    else:
        over = font_big.render("Bonk!", True, (255, 120, 140))
        screen.blit(over, over.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        tip = font_small.render("SPACE to try again", True, (180, 200, 230))
        screen.blit(tip, tip.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40)))

    pygame.display.flip()

pygame.quit()