# game.py — Lesson 5.24: Tic-Tac-Bot — complete (starter)
from __future__ import annotations

import random

import pygame

pygame.init()

WIDTH, HEIGHT = 560, 680
GRID_SIZE = 3
CELL = 120
GAP = 14
BOARD_X = (WIDTH - GRID_SIZE * CELL) // 2
BOARD_Y = 200
BOT_DELAY = 0.55

WIN_LINES: list[tuple[int, int, int]] = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Bot — Pro")
clock = pygame.time.Clock()
font_big = pygame.font.Font(None, 46)
font_small = pygame.font.Font(None, 26)

HUMAN = "X"
BOT = "O"

board: list[str | None] = [None] * 9
current = HUMAN
state = "MENU"
mode = "pvp"
difficulty = "medium"
human_starts = True
win_line: tuple[int, int, int] | None = None
bot_timer = 0.0
session = {"wins": 0, "losses": 0, "draws": 0}


def cell_rect(index: int) -> pygame.Rect:
    row, col = divmod(index, GRID_SIZE)
    x = BOARD_X + col * CELL
    y = BOARD_Y + row * CELL
    return pygame.Rect(x + GAP // 2, y + GAP // 2, CELL - GAP, CELL - GAP)


def pick_easy(brd: list[str | None]) -> int:
    options = [i for i, c in enumerate(brd) if c is None]
    return random.choice(options)


def pick_medium(brd: list[str | None]) -> int:
    """TODO: win → block → centre → corner → any."""
    return pick_easy(brd)


def pick_hard(brd: list[str | None]) -> int:
    """TODO stretch: minimax — look ahead at all futures."""
    return pick_medium(brd)


def bot_move() -> None:
    """TODO: call pick_* then place bot mark."""
    pass


def apply_move_index(idx: int) -> None:
    """TODO: place mark, end round, session stats, schedule bot timer."""
    pass


def start_round() -> None:
    global board, current, state, win_line, bot_timer
    board = [None] * 9
    state = "PLAYING"
    win_line = None
    bot_timer = 0.0
    current = HUMAN if human_starts else BOT
    if mode == "bot" and current == BOT:
        bot_timer = BOT_DELAY


running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and state == "MENU":
            start_round()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and state == "PLAYING":
            # TODO: human clicks only on their turn in bot mode
            pass

    if state == "PLAYING" and mode == "bot" and current == BOT:
        bot_timer -= dt
        if bot_timer <= 0:
            bot_move()

    screen.fill((16, 20, 34))
    title = font_big.render("Tic-Tac-Bot", True, (235, 245, 255))
    screen.blit(title, title.get_rect(midtop=(WIDTH // 2, 24)))
    pygame.display.flip()

pygame.quit()