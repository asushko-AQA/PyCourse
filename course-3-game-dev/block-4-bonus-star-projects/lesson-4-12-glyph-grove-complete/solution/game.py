# game.py — Lesson 4.12: Glyph Grove — complete solitaire
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
selected: dict | None = None
moves = 0
elapsed = 0.0
best_time: float | None = None
tiles: list[dict] = []
hint_pair: tuple[dict, dict] | None = None


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


def tile_origin(tile: dict) -> tuple[int, int]:
    x = BOARD_X + tile["col"] * TILE_W + tile["layer"] * LAYER_DX
    y = BOARD_Y + tile["row"] * TILE_H + tile["layer"] * LAYER_DY
    return x, y


def tile_rect(tile: dict) -> pygame.Rect:
    x, y = tile_origin(tile)
    return pygame.Rect(x, y, TILE_W - 2, TILE_H - 2)


def is_covered(tile: dict, pool: list[dict]) -> bool:
    for other in pool:
        if other["id"] == tile["id"] or other["removed"]:
            continue
        if other["layer"] > tile["layer"] and other["col"] == tile["col"] and other["row"] == tile["row"]:
            return True
    return False


def has_open_side(tile: dict, pool: list[dict]) -> bool:
    for delta in (-1, 1):
        ncol = tile["col"] + delta
        blocked = any(
            not t["removed"]
            and t["layer"] == tile["layer"]
            and t["row"] == tile["row"]
            and t["col"] == ncol
            for t in pool
        )
        if not blocked:
            return True
    return False


def is_free(tile: dict, pool: list[dict]) -> bool:
    if tile["removed"]:
        return False
    return not is_covered(tile, pool) and has_open_side(tile, pool)


def remaining_count(pool: list[dict]) -> int:
    return sum(1 for t in pool if not t["removed"])


def any_moves_left(pool: list[dict]) -> bool:
    free = [t for t in pool if is_free(t, pool)]
    for i, a in enumerate(free):
        for b in free[i + 1 :]:
            if a["kind"] == b["kind"]:
                return True
    return False


def find_hint(pool: list[dict]) -> tuple[dict, dict] | None:
    free = [t for t in pool if is_free(t, pool)]
    for i, a in enumerate(free):
        for b in free[i + 1 :]:
            if a["kind"] == b["kind"]:
                return a, b
    return None


def reshuffle_kinds(pool: list[dict]) -> None:
    live = [t for t in pool if not t["removed"]]
    kinds = [t["kind"] for t in live]
    random.shuffle(kinds)
    for tile, kind in zip(live, kinds, strict=True):
        tile["kind"] = kind
        tile["kind_index"] = GLYPHS.index(kind)


def reset_play() -> None:
    global tiles, selected, moves, elapsed, hint_pair, state
    tiles = build_tiles()
    selected = None
    moves = 0
    elapsed = 0.0
    hint_pair = None
    state = PLAYING


def try_match(first: dict | None, second: dict, pool: list[dict]) -> dict | None:
    global hint_pair
    hint_pair = None
    if first is None:
        return second if is_free(second, pool) else None
    if first["id"] == second["id"]:
        return None
    if first["kind"] == second["kind"] and is_free(first, pool) and is_free(second, pool):
        first["removed"] = True
        second["removed"] = True
        return None
    return second if is_free(second, pool) else None


def tile_at_point(pos: tuple[int, int], pool: list[dict]) -> dict | None:
    for tile in sorted(pool, key=lambda t: t["layer"], reverse=True):
        if tile["removed"]:
            continue
        if tile_rect(tile).collidepoint(pos):
            return tile
    return None


HINT_RECT = pygame.Rect(16, 96, 96, 32)
SHUFFLE_RECT = pygame.Rect(120, 96, 110, 32)


def draw_tile(surface: pygame.Surface, tile: dict) -> None:
    if tile["removed"]:
        return
    rect = tile_rect(tile)
    base = GLYPH_COLORS[tile["kind_index"]]
    shade = tuple(max(0, c - 18 * tile["layer"]) for c in base)
    if not is_free(tile, tiles):
        shade = tuple(c // 2 for c in shade)
    if hint_pair and tile["id"] in (hint_pair[0]["id"], hint_pair[1]["id"]):
        shade = tuple(min(255, c + 50) for c in shade)
    pygame.draw.rect(surface, shade, rect, border_radius=8)
    border = (255, 245, 130) if selected and selected["id"] == tile["id"] else (240, 240, 255)
    pygame.draw.rect(surface, border, rect, 3 if selected and selected["id"] == tile["id"] else 2, border_radius=8)
    glyph = font_glyph.render(tile["kind"], True, (25, 28, 40))
    surface.blit(
        glyph,
        (rect.centerx - glyph.get_width() // 2, rect.centery - glyph.get_height() // 2),
    )


def draw_button(surface: pygame.Surface, rect: pygame.Rect, label: str) -> None:
    pygame.draw.rect(surface, (70, 78, 120), rect, border_radius=6)
    pygame.draw.rect(surface, (180, 190, 240), rect, 2, border_radius=6)
    text = font_small.render(label, True, (240, 240, 255))
    surface.blit(text, (rect.x + 10, rect.y + 6))


def draw_playing(surface: pygame.Surface) -> None:
    title = font_small.render("Glyph Grove — match free pairs", True, (210, 205, 255))
    surface.blit(title, (16, 14))
    time_text = font_small.render(f"Time: {elapsed:.1f}s", True, (180, 190, 230))
    surface.blit(time_text, (16, 38))
    move_text = font_small.render(f"Moves: {moves}", True, (180, 190, 230))
    surface.blit(move_text, (16, 62))
    draw_button(surface, HINT_RECT, "Hint H")
    draw_button(surface, SHUFFLE_RECT, "Shuffle R")

    for tile in sorted(tiles, key=lambda t: t["layer"]):
        draw_tile(surface, tile)


def draw_title(surface: pygame.Surface) -> None:
    surface.fill((18, 22, 38))
    head = font_big.render("Glyph Grove", True, (230, 220, 255))
    surface.blit(head, (WIDTH // 2 - head.get_width() // 2, 140))
    sub = font_small.render("Mahjong-style pairs with your own glyphs", True, (180, 185, 220))
    surface.blit(sub, (WIDTH // 2 - sub.get_width() // 2, 200))
    if best_time is not None:
        best = font_small.render(f"Session best: {best_time:.1f}s", True, (140, 255, 190))
        surface.blit(best, (WIDTH // 2 - best.get_width() // 2, 240))
    prompt = font_small.render("Click or press SPACE to play", True, (255, 245, 200))
    surface.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, 300))


def draw_end(surface: pygame.Surface, message: str) -> None:
    draw_playing(surface)
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((10, 12, 28, 170))
    surface.blit(overlay, (0, 0))
    box = font_big.render(message, True, (255, 230, 150))
    surface.blit(box, (WIDTH // 2 - box.get_width() // 2, HEIGHT // 2 - 40))
    again = font_small.render("SPACE = title screen", True, (220, 220, 255))
    surface.blit(again, (WIDTH // 2 - again.get_width() // 2, HEIGHT // 2 + 20))


def check_end_state() -> None:
    global state, best_time
    if remaining_count(tiles) == 0:
        if best_time is None or elapsed < best_time:
            best_time = elapsed
        state = WON
    elif not any_moves_left(tiles):
        state = STUCK


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if state == START:
                    reset_play()
                elif state in (WON, STUCK):
                    state = START
                    selected = None
            if state == PLAYING:
                if event.key == pygame.K_h:
                    hint_pair = find_hint(tiles)
                if event.key == pygame.K_r:
                    reshuffle_kinds(tiles)
                    if not any_moves_left(tiles):
                        state = STUCK
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if state == START:
                reset_play()
            elif state == PLAYING:
                if HINT_RECT.collidepoint(event.pos):
                    hint_pair = find_hint(tiles)
                elif SHUFFLE_RECT.collidepoint(event.pos):
                    reshuffle_kinds(tiles)
                    if not any_moves_left(tiles):
                        state = STUCK
                else:
                    hit = tile_at_point(event.pos, tiles)
                    if hit is not None:
                        selected = try_match(selected, hit, tiles)
                        moves += 1
                        check_end_state()

    if state == PLAYING:
        elapsed += dt

    screen.fill((22, 26, 42))
    if state == START:
        draw_title(screen)
    elif state == PLAYING:
        draw_playing(screen)
    elif state == WON:
        draw_end(screen, "Garden Clear!")
    elif state == STUCK:
        draw_end(screen, "No moves — try Shuffle!")

    pygame.display.flip()

pygame.quit()