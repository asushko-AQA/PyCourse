# game.py — Lesson 5.18: Merge Magic — complete (starter)
from __future__ import annotations

import random

import pygame

pygame.init()

WIDTH = 520
HEIGHT = 620
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Merge Magic")

clock = pygame.time.Clock()
running = True
font_big = pygame.font.Font(None, 52)
font_small = pygame.font.Font(None, 28)
font_rune = pygame.font.Font(None, 36)

SIZE = 4
CELL = 100
BOARD_X = 60
BOARD_Y = 100
WIN_VALUE = 2048

START = "start"
PLAYING = "playing"
WON = "won"
OVER = "over"
state = START

board: list[list[int]] = [[0] * SIZE for _ in range(SIZE)]
score = 0
best_score = 0

# TODO: undo_snapshot stores (board copy, score) for one undo step


def draw_board(surface: pygame.Surface) -> None:
    """TODO: draw 4×4 rune tiles."""
    pass


def try_move(direction: str) -> None:
    """TODO: move, score, spawn, win/over checks from lesson 5.17."""
    pass


def new_game() -> None:
    """TODO: reset board, score, spawn two runes, state = PLAYING."""
    pass


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # TODO: start or restart
            pass

    screen.fill((12, 9, 22))
    if state == START:
        title = font_big.render("Merge Magic", True, (230, 210, 255))
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
    else:
        draw_board(screen)
    hud = font_small.render("Finish full Merge Magic TODOs!", True, (200, 185, 255))
    screen.blit(hud, (BOARD_X, 40))
    pygame.display.flip()

pygame.quit()