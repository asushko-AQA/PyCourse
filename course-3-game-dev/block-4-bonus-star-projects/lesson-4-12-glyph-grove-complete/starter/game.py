# game.py — Lesson 4.12: Glyph Grove — complete (starter)
# Copy your 4.11 solution here, then add game states, timer, hint, shuffle, best time.
import random

import pygame

pygame.init()

WIDTH = 640
HEIGHT = 540
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Glyph Grove")

clock = pygame.time.Clock()

font_big = pygame.font.Font(None, 56)
font_glyph = pygame.font.Font(None, 52)
font_small = pygame.font.Font(None, 26)

TILE_W = 54
TILE_H = 66
BOARD_X = 150
BOARD_Y = 150
LAYER_DX = 10
LAYER_DY = 10

GLYPHS = ["◆", "●", "▲", "★", "✚", "☘"]
GLYPH_COLORS = [
    (120, 200, 255),
    (255, 150, 160),
    (255, 210, 110),
    (200, 170, 255),
    (140, 230, 170),
    (255, 180, 120),
]

LAYOUT: list[tuple[int, int, int]] = [
    (0, 2, 0),
    (0, 2, 1),
    (0, 2, 2),
    (0, 2, 3),
    (0, 2, 4),
    (0, 2, 5),
    (0, 3, 0),
    (0, 3, 1),
    (0, 3, 2),
    (0, 3, 3),
    (0, 3, 4),
    (0, 3, 5),
    (1, 2, 1),
    (1, 2, 2),
    (1, 2, 3),
    (1, 2, 4),
    (1, 3, 1),
    (1, 3, 2),
    (1, 3, 3),
    (1, 3, 4),
    (2, 2, 2),
    (2, 2, 3),
    (2, 3, 2),
    (2, 3, 3),
]

START = "start"
PLAYING = "playing"
WON = "won"
STUCK = "stuck"

state = START
running = True
selected = None
moves = 0
elapsed = 0.0
best_time = None
tiles: list[dict] = []


def build_tiles() -> list[dict]:
    kinds = GLYPHS * 2
    random.shuffle(kinds)
    built: list[dict] = []
    for i, (layer, row, col) in enumerate(LAYOUT):
        kind_index = GLYPHS.index(kinds[i])
        built.append(
            {
                "id": i,
                "kind": kinds[i],
                "kind_index": kind_index,
                "layer": layer,
                "row": row,
                "col": col,
                "removed": False,
            }
        )
    return built


# TODO: paste is_free / matching from lesson 4.11, then add:
# - reset_play(), timer (elapsed += dt), hint (H key), reshuffle (R key)
# - win when no tiles left; STUCK when no_moves_left
# - title screen + session best_time


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # TODO: SPACE starts / returns to title; mouse matching from 4.11

    screen.fill((22, 26, 42))
    hud = font_small.render("Finish Glyph Grove Pro TODOs", True, (220, 210, 255))
    screen.blit(hud, (16, 14))

    pygame.display.flip()

pygame.quit()