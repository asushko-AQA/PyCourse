# game.py — Lesson 4.11: Glyph Grove — mouse pick & matching
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


def is_covered(tile: dict, tiles: list[dict]) -> bool:
    for other in tiles:
        if other["id"] == tile["id"] or other["removed"]:
            continue
        if other["layer"] > tile["layer"] and other["col"] == tile["col"] and other["row"] == tile["row"]:
            return True
    return False


def has_open_side(tile: dict, tiles: list[dict]) -> bool:
    for delta in (-1, 1):
        ncol = tile["col"] + delta
        blocked = any(
            not t["removed"]
            and t["layer"] == tile["layer"]
            and t["row"] == tile["row"]
            and t["col"] == ncol
            for t in tiles
        )
        if not blocked:
            return True
    return False


def is_free(tile: dict, tiles: list[dict]) -> bool:
    if tile["removed"]:
        return False
    return not is_covered(tile, tiles) and has_open_side(tile, tiles)


def try_match(first: dict | None, second: dict, tiles: list[dict]) -> dict | None:
    if first is None:
        return second
    if first["id"] == second["id"]:
        return None
    if (
        first["kind"] == second["kind"]
        and is_free(first, tiles)
        and is_free(second, tiles)
    ):
        first["removed"] = True
        second["removed"] = True
        return None
    return second


def draw_tile(surface: pygame.Surface, tile: dict, selected: bool) -> None:
    if tile["removed"]:
        return
    rect = tile_rect(tile)
    base = GLYPH_COLORS[tile["kind_index"]]
    shade = tuple(max(0, c - 18 * tile["layer"]) for c in base)
    if not is_free(tile, tiles):
        shade = tuple(c // 2 for c in shade)
    pygame.draw.rect(surface, shade, rect, border_radius=8)
    border = (255, 245, 130) if selected else (240, 240, 255)
    pygame.draw.rect(surface, border, rect, 3 if selected else 2, border_radius=8)
    glyph = font_glyph.render(tile["kind"], True, (25, 28, 40))
    gx = rect.x + (rect.width - glyph.get_width()) // 2
    gy = rect.y + (rect.height - glyph.get_height()) // 2
    surface.blit(glyph, (gx, gy))


def tile_at_point(pos: tuple[int, int], tiles: list[dict]) -> dict | None:
    """Topmost visible tile under the cursor."""
    for tile in sorted(tiles, key=lambda t: t["layer"], reverse=True):
        if tile["removed"]:
            continue
        if tile_rect(tile).collidepoint(pos):
            return tile
    return None


tiles = build_tiles()
selected: dict | None = None
moves = 0

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            hit = tile_at_point(event.pos, tiles)
            if hit is not None:
                selected = try_match(selected, hit, tiles)
                moves += 1

    screen.fill((22, 26, 42))
    title = font_small.render("Click free matching pairs — dim = blocked", True, (210, 205, 255))
    screen.blit(title, (16, 14))
    hud = font_small.render(f"Moves: {moves}", True, (180, 190, 230))
    screen.blit(hud, (16, 40))

    for tile in sorted(tiles, key=lambda t: t["layer"]):
        draw_tile(screen, tile, selected is not None and selected["id"] == tile["id"])

    left = sum(1 for t in tiles if not t["removed"])
    if left == 0:
        win = font_small.render("Cleared! Lesson 4.12 adds timer + title.", True, (140, 255, 190))
        screen.blit(win, (16, HEIGHT - 32))

    pygame.display.flip()

pygame.quit()