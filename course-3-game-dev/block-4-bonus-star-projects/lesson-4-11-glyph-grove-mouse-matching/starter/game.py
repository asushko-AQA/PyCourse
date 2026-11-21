# game.py — Lesson 4.11: Glyph Grove — mouse pick & matching (starter)
import random

import pygame

pygame.init()

WIDTH = 620
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Glyph Grove — Match")

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
    return tiles


def tile_origin(tile: dict) -> tuple[int, int]:
    x = BOARD_X + tile["col"] * TILE_W + tile["layer"] * LAYER_DX
    y = BOARD_Y + tile["row"] * TILE_H + tile["layer"] * LAYER_DY
    return x, y


def tile_rect(tile: dict) -> pygame.Rect:
    x, y = tile_origin(tile)
    return pygame.Rect(x, y, TILE_W - 2, TILE_H - 2)


def is_free(tile: dict, tiles: list[dict]) -> bool:
    """TODO: not covered + open left OR right on same layer."""
    return True


def draw_tile(surface: pygame.Surface, tile: dict, selected: bool) -> None:
    if tile["removed"]:
        return
    rect = tile_rect(tile)
    base = GLYPH_COLORS[tile["kind_index"]]
    pygame.draw.rect(surface, base, rect, border_radius=8)
    glyph = font_glyph.render(tile["kind"], True, (25, 28, 40))
    surface.blit(glyph, (rect.centerx - glyph.get_width() // 2, rect.centery - glyph.get_height() // 2))


tiles = build_tiles()
selected: dict | None = None

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # TODO: MOUSEBUTTONDOWN — tile_rect(tile).collidepoint(event.pos)
        # TODO: pick two; if same kind and both free, set removed=True

    screen.fill((22, 26, 42))
    hud = font_small.render("Wire mouse + is_free + matching", True, (220, 210, 255))
    screen.blit(hud, (16, 14))

    for tile in sorted(tiles, key=lambda t: t["layer"]):
        draw_tile(screen, tile, selected is not None and selected["id"] == tile["id"])

    pygame.display.flip()

pygame.quit()