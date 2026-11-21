# game.py — Lesson 5.24: Tic-Tac-Bot — complete (solution)
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


def mouse_to_cell(pos: tuple[int, int]) -> int | None:
    for idx in range(9):
        if cell_rect(idx).collidepoint(pos):
            return idx
    return None


def empty_cells(brd: list[str | None]) -> list[int]:
    return [i for i, c in enumerate(brd) if c is None]


def find_winner_on(brd: list[str | None]) -> tuple[str | None, tuple[int, int, int] | None]:
    for a, b, c in WIN_LINES:
        if brd[a] and brd[a] == brd[b] == brd[c]:
            return brd[a], (a, b, c)
    return None, None


def find_winning_move(brd: list[str | None], mark: str) -> int | None:
    for idx in empty_cells(brd):
        trial = brd[:]
        trial[idx] = mark
        if find_winner_on(trial)[0] == mark:
            return idx
    return None


def minimax_score(
    brd: list[str | None], bot_turn: bool, bot_mark: str, human_mark: str
) -> int:
    winner, _ = find_winner_on(brd)
    if winner == bot_mark:
        return 10
    if winner == human_mark:
        return -10
    if not empty_cells(brd):
        return 0
    if bot_turn:
        best = -100
        for idx in empty_cells(brd):
            trial = brd[:]
            trial[idx] = bot_mark
            best = max(best, minimax_score(trial, False, bot_mark, human_mark))
        return best
    best = 100
    for idx in empty_cells(brd):
        trial = brd[:]
        trial[idx] = human_mark
        best = min(best, minimax_score(trial, True, bot_mark, human_mark))
    return best


def pick_hard(brd: list[str | None]) -> int:
    best_idx = empty_cells(brd)[0]
    best_score = -100
    for idx in empty_cells(brd):
        trial = brd[:]
        trial[idx] = BOT
        score = minimax_score(trial, False, BOT, HUMAN)
        if score > best_score:
            best_score = score
            best_idx = idx
    return best_idx


def pick_medium(brd: list[str | None]) -> int:
    move = find_winning_move(brd, BOT)
    if move is not None:
        return move
    block = find_winning_move(brd, HUMAN)
    if block is not None:
        return block
    if brd[4] is None:
        return 4
    for corner in (0, 2, 6, 8):
        if brd[corner] is None:
            return corner
    return empty_cells(brd)[0]


def pick_easy(brd: list[str | None]) -> int:
    return random.choice(empty_cells(brd))


def bot_move() -> None:
    global board, current, state, win_line
    if difficulty == "easy":
        idx = pick_easy(board)
    elif difficulty == "hard":
        idx = pick_hard(board)
    else:
        idx = pick_medium(board)
    apply_move_index(idx)


def apply_move_index(idx: int) -> None:
    global board, current, state, win_line, bot_timer
    if state != "PLAYING" or board[idx] is not None:
        return
    board[idx] = current
    winner, line = find_winner_on(board)
    if winner:
        state = "WIN"
        win_line = line
        if mode == "bot":
            if winner == HUMAN:
                session["wins"] += 1
            else:
                session["losses"] += 1
        return
    if not empty_cells(board):
        state = "DRAW"
        if mode == "bot":
            session["draws"] += 1
        return
    current = BOT if current == HUMAN else HUMAN
    if mode == "bot" and current == BOT:
        bot_timer = BOT_DELAY


def start_round() -> None:
    global board, current, state, win_line, bot_timer
    board = [None] * 9
    state = "PLAYING"
    win_line = None
    bot_timer = 0.0
    if mode == "pvp":
        current = HUMAN if human_starts else BOT
    else:
        current = HUMAN if human_starts else BOT
        if current == BOT:
            bot_timer = BOT_DELAY


def draw_grid(surface: pygame.Surface) -> None:
    for idx in range(9):
        rect = cell_rect(idx)
        fill = (28, 36, 58)
        if win_line and idx in win_line:
            fill = (55, 70, 120)
        pygame.draw.rect(surface, fill, rect, border_radius=14)
        pygame.draw.rect(surface, (90, 140, 220), rect, width=2, border_radius=14)


def draw_x(surface: pygame.Surface, rect: pygame.Rect) -> None:
    inner = rect.inflate(-28, -28)
    pygame.draw.line(surface, (255, 210, 90), inner.topleft, inner.bottomright, 8)
    pygame.draw.line(surface, (255, 210, 90), inner.topright, inner.bottomleft, 8)


def draw_o(surface: pygame.Surface, rect: pygame.Rect) -> None:
    pygame.draw.circle(
        surface, (120, 220, 255), rect.center, rect.width // 2 - 18, width=8
    )
    pygame.draw.circle(surface, (60, 120, 180), rect.center, 10)


def draw_robot(surface: pygame.Surface) -> None:
    """Tiny factory robot beside the title — shapes only."""
    base = pygame.Rect(WIDTH // 2 - 70, 8, 140, 46)
    pygame.draw.rect(surface, (50, 58, 90), base, border_radius=10)
    eye_l = pygame.Rect(WIDTH // 2 - 42, 22, 16, 16)
    eye_r = pygame.Rect(WIDTH // 2 + 26, 22, 16, 16)
    pygame.draw.rect(surface, (180, 255, 200), eye_l, border_radius=4)
    pygame.draw.rect(surface, (180, 255, 200), eye_r, border_radius=4)
    ant = [(WIDTH // 2, 4), (WIDTH // 2 - 10, 18), (WIDTH // 2 + 10, 18)]
    pygame.draw.polygon(surface, (140, 160, 200), ant)


def draw_menu(surface: pygame.Surface) -> None:
    draw_robot(surface)
    title = font_big.render("Tic-Tac-Bot", True, (235, 245, 255))
    surface.blit(title, title.get_rect(midtop=(WIDTH // 2, 58)))
    lines = [
        f"Mode: {mode.upper()}  (M toggle)",
        f"Difficulty: {difficulty}  (1 easy 2 med 3 hard)",
        f"You start: {human_starts}  (S toggle)",
        "SPACE — start round",
        f"Session W {session['wins']} L {session['losses']} D {session['draws']}",
    ]
    y = 150
    for line in lines:
        t = font_small.render(line, True, (180, 200, 235))
        surface.blit(t, t.get_rect(midtop=(WIDTH // 2, y)))
        y += 32


running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m and state == "MENU":
                mode = "bot" if mode == "pvp" else "pvp"
            if event.key == pygame.K_1 and state == "MENU":
                difficulty = "easy"
            if event.key == pygame.K_2 and state == "MENU":
                difficulty = "medium"
            if event.key == pygame.K_3 and state == "MENU":
                difficulty = "hard"
            if event.key == pygame.K_s and state == "MENU":
                human_starts = not human_starts
            if event.key == pygame.K_SPACE:
                if state == "MENU":
                    start_round()
                elif state in ("WIN", "DRAW"):
                    state = "MENU"
            if event.key == pygame.K_r and state in ("WIN", "DRAW", "PLAYING"):
                start_round()
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and state == "PLAYING"
        ):
            idx = mouse_to_cell(event.pos)
            if idx is not None:
                if mode == "bot" and current != HUMAN:
                    pass
                else:
                    apply_move_index(idx)

    if state == "PLAYING" and mode == "bot" and current == BOT:
        bot_timer -= dt
        if bot_timer <= 0:
            bot_move()

    screen.fill((16, 20, 34))

    if state == "MENU":
        draw_menu(screen)
    else:
        draw_robot(screen)
        hud = font_small.render(
            f"Session W {session['wins']} · L {session['losses']} · D {session['draws']}",
            True,
            (170, 190, 230),
        )
        screen.blit(hud, hud.get_rect(midtop=(WIDTH // 2, 58)))
        if state == "PLAYING":
            if mode == "bot":
                who = "Your bolt" if current == HUMAN else "Bot thinking…"
            else:
                who = "Bolt X" if current == HUMAN else "Gear O"
            status = font_small.render(
                f"{who}  |  R restart  SPACE menu", True, (200, 215, 255)
            )
        elif state == "WIN":
            if mode == "bot":
                msg = "You win!" if board[win_line[0]] == HUMAN else "Bot wins!"
            else:
                msg = "Bolt X wins!" if board[win_line[0]] == HUMAN else "Gear O wins!"
            status = font_small.render(
                f"{msg}  SPACE menu", True, (255, 210, 140)
            )
        else:
            status = font_small.render("Draw!  SPACE menu", True, (200, 215, 255))
        screen.blit(status, status.get_rect(midtop=(WIDTH // 2, 92)))
        draw_grid(screen)
        if win_line:
            pts = [cell_rect(i).center for i in win_line]
            pygame.draw.lines(screen, (255, 120, 180), False, pts, 6)
        for i in range(9):
            mark = board[i]
            rect = cell_rect(i)
            if mark == HUMAN:
                draw_x(screen, rect)
            elif mark == BOT:
                draw_o(screen, rect)

    pygame.display.flip()

pygame.quit()