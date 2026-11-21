# game.py — Lesson 5.15: Mine Whisper — complete (starter)
from __future__ import annotations

import random

import pygame

pygame.init()

WIDTH = 620
HEIGHT = 520
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mine Whisper")

clock = pygame.time.Clock()
running = True
font_big = pygame.font.Font(None, 52)
font_small = pygame.font.Font(None, 28)

START = "start"
PLAYING = "playing"
WON = "won"
LOST = "lost"
state = START

DIFFICULTIES = {"easy": (9, 9, 10), "medium": (16, 12, 30), "hard": (22, 16, 55)}
difficulty = "medium"
COLS, ROWS, MINE_COUNT = DIFFICULTIES[difficulty]
CELL = 32
BOARD_X = 40
BOARD_Y = 56

grid: list[list[dict]] = []
mines_placed = False
elapsed = 0.0
best_times: dict[str, float | None] = {"easy": None, "medium": None, "hard": None}


def start_game(diff: str) -> None:
    """TODO: pick COLS/ROWS/MINE_COUNT from DIFFICULTIES; fresh grid; state=PLAYING."""
    pass


def player_won(board: list[list[dict]]) -> bool:
    """TODO: every safe cell revealed."""
    return False


def record_best() -> None:
    """TODO: save elapsed into best_times[difficulty] if faster."""
    pass


while running:
    dt = clock.tick(60) / 1000
    if state == PLAYING:
        elapsed += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # TODO: START → keys 1/2/3 call start_game; WON/LOST → SPACE → START
            pass
        if event.type == pygame.MOUSEBUTTONDOWN and state == PLAYING:
            # TODO: first click places mines; reveal / flag; win & lose checks
            pass

    screen.fill((10, 8, 22))
    # TODO: draw title overlay, HUD (mines left + timer), board, win/lose screens
    hint = font_small.render("Finish full Mine Whisper TODOs!", True, (200, 185, 240))
    screen.blit(hint, (BOARD_X, 16))
    pygame.display.flip()

pygame.quit()