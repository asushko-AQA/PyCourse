# game.py — Lesson 4.10: Glyph Grove — tiles & layout
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

# (layer, row, col) — our own garden layout (24 cells = 12 pairs)
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
    kinds = GLYPHS * 2
    random.shuffle(kinds)
    tiles: list[dict] = []
    for i, (layer, row, col) in enumerate(LAYOUT):
        kind_index = GLYPHS.index(kinds[i])
        tiles.append(
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
    tiles.sort(key=lambda t: t["layer"])
    return tiles


def tile_origin(tile: dict) -> tuple[int, int]:
    x = BOARD_X + tile["col"] * TILE_W + tile["layer"] * LAYER_DX
    y = BOARD_Y + tile["row"] * TILE_H + tile["layer"] * LAYER_DY
    return x, y


def draw_tile(surface: pygame.Surface, tile: dict) -> None:
    if tile["removed"]:
        return
    x, y = tile_origin(tile)
    rect = pygame.Rect(x, y, TILE_W - 2, TILE_H - 2)
    base = GLYPH_COLORS[tile["kind_index"]]
    shade = tuple(max(0, c - 18 * tile["layer"]) for c in base)
    pygame.draw.rect(surface, shade, rect, border_radius=8)
    pygame.draw.rect(surface, (240, 240, 255), rect, 2, border_radius=8)
    glyph = font_glyph.render(tile["kind"], True, (25, 28, 40))
    gx = x + (TILE_W - glyph.get_width()) // 2
    gy = y + (TILE_H - glyph.get_height()) // 2
    surface.blit(glyph, (gx, gy))


tiles = build_tiles()

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((22, 26, 42))
    title = font_small.render("Glyph Grove — layered tiles (lesson 4.10)", True, (210, 205, 255))
    screen.blit(title, (16, 14))

    for tile in tiles:
        draw_tile(screen, tile)

    hint = font_small.render("Next lesson: mouse pick + free tile rule", True, (170, 175, 210))
    screen.blit(hint, (16, HEIGHT - 32))

    pygame.display.flip()

pygame.quit()