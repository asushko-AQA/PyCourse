# game.py — Lesson 4.10: Glyph Grove — tiles & layout (starter)
import random

import pygame

pygame.init()

WIDTH = 620
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Glyph Grove — Tiles")

clock = pygame.time.Clock()
running = True

font_glyph = pygame.font.Font(None, 52)
font_small = pygame.font.Font(None, 26)

TILE_W = 54
TILE_H = 66
BOARD_X = 150
BOARD_Y = 120
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


def build_tiles() -> list[dict]:
    """TODO: shuffle GLYPHS*2 kinds, zip with LAYOUT into tile dicts."""
    return []


def tile_origin(tile: dict) -> tuple[int, int]:
    """TODO: pixel x/y from col, row, layer offsets."""
    return BOARD_X, BOARD_Y


def draw_tile(surface: pygame.Surface, tile: dict) -> None:
    """TODO: draw rounded rect + font_glyph.render(kind)."""
    pass


tiles = build_tiles()

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((22, 26, 42))
    hud = font_small.render("Finish build_tiles + draw_tile TODOs", True, (220, 210, 255))
    screen.blit(hud, (16, 14))

    for tile in tiles:
        draw_tile(screen, tile)

    pygame.display.flip()

pygame.quit()