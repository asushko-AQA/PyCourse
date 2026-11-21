# game.py — Lesson 5.15: Mine Whisper — full crystal field (solution)
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
font_num = pygame.font.Font(None, 26)

START = "start"
PLAYING = "playing"
WON = "won"
LOST = "lost"
state = START

DIFFICULTIES: dict[str, tuple[int, int, int]] = {
    "easy": (9, 9, 10),
    "medium": (16, 12, 30),
    "hard": (22, 16, 55),
}
difficulty = "medium"
COLS, ROWS, MINE_COUNT = DIFFICULTIES[difficulty]
CELL = 32
BOARD_X = 40
BOARD_Y = 56
HUD_Y = 14

NUMBER_COLORS = [
    (0, 0, 0),
    (80, 140, 255),
    (90, 220, 150),
    (255, 120, 140),
    (160, 100, 220),
    (255, 180, 90),
    (120, 230, 230),
    (200, 200, 200),
    (255, 255, 255),
]

grid: list[list[dict[str, int | bool]]] = []
mines_placed = False
elapsed = 0.0
best_times: dict[str, float | None] = {"easy": None, "medium": None, "hard": None}


def make_board() -> list[list[dict[str, int | bool]]]:
    return [
        [{"mine": False, "revealed": False, "flagged": False, "neighbors": 0} for _ in range(COLS)]
        for _ in range(ROWS)
    ]


def in_bounds(col: int, row: int) -> bool:
    return 0 <= col < COLS and 0 <= row < ROWS


def count_neighbor_mines(board: list[list[dict]], col: int, row: int) -> int:
    total = 0
    for dc in (-1, 0, 1):
        for dr in (-1, 0, 1):
            if dc == 0 and dr == 0:
                continue
            nc, nr = col + dc, row + dr
            if in_bounds(nc, nr) and board[nr][nc]["mine"]:
                total += 1
    return total


def safe_zone(col: int, row: int) -> set[tuple[int, int]]:
    zone: set[tuple[int, int]] = {(col, row)}
    for dc in (-1, 0, 1):
        for dr in (-1, 0, 1):
            nc, nr = col + dc, row + dr
            if in_bounds(nc, nr):
                zone.add((nc, nr))
    return zone


def place_mines(board: list[list[dict]], safe_col: int, safe_row: int) -> None:
    forbidden = safe_zone(safe_col, safe_row)
    spots: list[tuple[int, int]] = [
        (c, r) for r in range(ROWS) for c in range(COLS) if (c, r) not in forbidden
    ]
    random.shuffle(spots)
    for c, r in spots[:MINE_COUNT]:
        board[r][c]["mine"] = True
    for r in range(ROWS):
        for c in range(COLS):
            board[r][c]["neighbors"] = count_neighbor_mines(board, c, r)


def flood_reveal_stack(board: list[list[dict]], col: int, row: int) -> None:
  stack: list[tuple[int, int]] = [(col, row)]
  while stack:
      c, r = stack.pop()
      if not in_bounds(c, r):
          continue
      cell = board[r][c]
      if cell["revealed"] or cell["flagged"]:
          continue
      cell["revealed"] = True
      if cell["neighbors"] == 0 and not cell["mine"]:
          for dc in (-1, 0, 1):
              for dr in (-1, 0, 1):
                  if dc == 0 and dr == 0:
                      continue
                  stack.append((c + dc, r + dr))


def reveal_at(board: list[list[dict]], col: int, row: int) -> str:
    cell = board[row][col]
    if cell["flagged"] or cell["revealed"]:
        return "noop"
    if cell["mine"]:
        cell["revealed"] = True
        return "mine"
    cell["revealed"] = True
    if cell["neighbors"] == 0:
        flood_reveal_stack(board, col, row)
    return "ok"


def toggle_flag(board: list[list[dict]], col: int, row: int) -> None:
    cell = board[row][col]
    if cell["revealed"]:
        return
    cell["flagged"] = not cell["flagged"]


def flags_count(board: list[list[dict]]) -> int:
    return sum(1 for r in range(ROWS) for c in range(COLS) if board[r][c]["flagged"])


def count_revealed_safe(board: list[list[dict]]) -> int:
    return sum(
        1
        for r in range(ROWS)
        for c in range(COLS)
        if board[r][c]["revealed"] and not board[r][c]["mine"]
    )


def player_won(board: list[list[dict]]) -> bool:
    safe_cells = COLS * ROWS - MINE_COUNT
    return count_revealed_safe(board) == safe_cells


def mouse_to_cell(pos: tuple[int, int]) -> tuple[int, int] | None:
    mx, my = pos
    if mx < BOARD_X or my < BOARD_Y:
        return None
    col = (mx - BOARD_X) // CELL
    row = (my - BOARD_Y) // CELL
    if not in_bounds(col, row):
        return None
    return col, row


def draw_crystal_cell(
    surface: pygame.Surface, x: int, y: int, *, revealed: bool, mine: bool, flash: bool
) -> None:
    rect = pygame.Rect(x + 2, y + 2, CELL - 4, CELL - 4)
    if not revealed:
        pygame.draw.rect(surface, (48, 38, 72), rect, border_radius=6)
        pygame.draw.rect(surface, (90, 70, 130), rect, width=2, border_radius=6)
        shine = pygame.Rect(x + 6, y + 6, CELL // 3, CELL // 4)
        pygame.draw.rect(surface, (120, 100, 170), shine, border_radius=3)
        return
    pygame.draw.rect(surface, (28, 24, 42), rect, border_radius=4)
    if mine:
        color = (255, 90, 110) if flash else (200, 60, 80)
        cx, cy = x + CELL // 2, y + CELL // 2
        pts = [(cx, cy - 10), (cx + 9, cy), (cx, cy + 10), (cx - 9, cy)]
        pygame.draw.polygon(surface, color, pts)


def draw_board(surface: pygame.Surface, *, show_mines: bool = False) -> None:
    frame = pygame.Rect(BOARD_X - 8, BOARD_Y - 8, COLS * CELL + 16, ROWS * CELL + 16)
    pygame.draw.rect(surface, (30, 22, 48), frame, border_radius=10)
    for row in range(ROWS):
        for col in range(COLS):
            x = BOARD_X + col * CELL
            y = BOARD_Y + row * CELL
            cell = grid[row][col]
            revealed = cell["revealed"] or (show_mines and cell["mine"])
            draw_crystal_cell(
                surface,
                x,
                y,
                revealed=revealed,
                mine=bool(cell["mine"]),
                flash=state == LOST,
            )
            if cell["flagged"] and not cell["revealed"]:
                fx, fy = x + CELL // 2, y + CELL // 2 + 4
                pygame.draw.polygon(
                    surface,
                    (255, 210, 90),
                    [(fx, fy - 12), (fx + 10, fy + 8), (fx - 10, fy + 8)],
                )
            if cell["revealed"] and not cell["mine"] and cell["neighbors"] > 0:
                n = int(cell["neighbors"])
                tint = NUMBER_COLORS[n]
                txt = font_num.render(str(n), True, tint)
                surface.blit(txt, (x + CELL // 2 - 6, y + CELL // 2 - 10))


def apply_difficulty(name: str) -> None:
    global COLS, ROWS, MINE_COUNT, CELL, BOARD_X, BOARD_Y
    COLS, ROWS, MINE_COUNT = DIFFICULTIES[name]
    CELL = 28 if name == "hard" else 32
    BOARD_X = max(24, (WIDTH - COLS * CELL) // 2)
    BOARD_Y = 56


def start_game(diff: str) -> None:
    global grid, mines_placed, state, elapsed, difficulty, COLS, ROWS, MINE_COUNT
    difficulty = diff
    apply_difficulty(diff)
    grid = make_board()
    mines_placed = False
    elapsed = 0.0
    state = PLAYING


def record_best() -> None:
    prev = best_times.get(difficulty)
    if prev is None or elapsed < prev:
        best_times[difficulty] = elapsed


grid = make_board()

while running:
    dt = clock.tick(60) / 1000
    if state == PLAYING:
        elapsed += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if state == START:
                if event.key == pygame.K_1:
                    start_game("easy")
                elif event.key == pygame.K_2:
                    start_game("medium")
                elif event.key == pygame.K_3:
                    start_game("hard")
            elif event.key == pygame.K_SPACE and state in (WON, LOST):
                state = START
        if event.type == pygame.MOUSEBUTTONDOWN and state == PLAYING:
            picked = mouse_to_cell(event.pos)
            if not picked:
                continue
            col, row = picked
            if event.button == 1:
                if not mines_placed:
                    place_mines(grid, col, row)
                    mines_placed = True
                result = reveal_at(grid, col, row)
                if result == "mine":
                    state = LOST
                elif player_won(grid):
                    state = WON
                    record_best()
            elif event.button == 3:
                toggle_flag(grid, col, row)

    screen.fill((10, 8, 22))
    title = font_small.render("Mine Whisper — crystal cavern", True, (200, 180, 255))
    screen.blit(title, (BOARD_X, HUD_Y))

    if state == START:
        draw_board(screen)
        hints = [
            "1 = Easy   2 = Medium   3 = Hard",
            "Left click reveal · Right click flag",
        ]
        for i, line in enumerate(hints):
            t = font_small.render(line, True, (180, 170, 220))
            screen.blit(t, (BOARD_X, HEIGHT - 80 + i * 28))
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((8, 6, 18, 170))
        screen.blit(overlay, (0, 0))
        big = font_big.render("Mine Whisper", True, (220, 200, 255))
        screen.blit(big, (WIDTH // 2 - big.get_width() // 2, HEIGHT // 2 - 60))
        menu_y = HEIGHT // 2 + 12
        for key, diff_key, label in (("1", "easy", "Easy"), ("2", "medium", "Med"), ("3", "hard", "Hard")):
            best = best_times[diff_key]
            bs = f" — best {best:.1f}s" if best is not None else ""
            row = font_small.render(f"[{key}] {label}{bs}", True, (200, 190, 230))
            screen.blit(row, (WIDTH // 2 - row.get_width() // 2, menu_y))
            menu_y += 26
    elif state == PLAYING:
        mines_left = MINE_COUNT - flags_count(grid)
        hud = font_small.render(
            f"Mines: {mines_left}   Time: {elapsed:.1f}s   ({difficulty})",
            True,
            (190, 175, 230),
        )
        screen.blit(hud, (BOARD_X, HUD_Y + 22))
        draw_board(screen)
    elif state == WON:
        draw_board(screen)
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((20, 40, 30, 160))
        screen.blit(overlay, (0, 0))
        msg = font_big.render("Cavern cleared!", True, (140, 255, 180))
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - 40))
        sub = font_small.render(f"Time {elapsed:.1f}s — SPACE menu", True, (220, 240, 220))
        screen.blit(sub, (WIDTH // 2 - sub.get_width() // 2, HEIGHT // 2 + 20))
    elif state == LOST:
        draw_board(screen, show_mines=True)
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((50, 10, 20, 150))
        screen.blit(overlay, (0, 0))
        msg = font_big.render("Crystal cracked!", True, (255, 140, 150))
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - 30))
        sub = font_small.render("SPACE to try again", True, (240, 200, 210))
        screen.blit(sub, (WIDTH // 2 - sub.get_width() // 2, HEIGHT // 2 + 24))

    pygame.display.flip()

pygame.quit()