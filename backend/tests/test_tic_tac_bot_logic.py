"""Pure-Python checks for Tic-Tac-Bot board state, wins, and bot moves."""

from __future__ import annotations

import random

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

CORNER_CELLS = (0, 2, 6, 8)
CENTER_CELL = 4


def empty_cells(board: list[str | None]) -> list[int]:
    return [i for i, cell in enumerate(board) if cell is None]


def find_winner(board: list[str | None]) -> tuple[str | None, tuple[int, int, int] | None]:
    """Return winning mark and line indices, or (None, None)."""
    for a, b, c in WIN_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a], (a, b, c)
    return None, None


def is_draw(board: list[str | None]) -> bool:
    return find_winner(board)[0] is None and len(empty_cells(board)) == 0


def find_winning_move(board: list[str | None], mark: str) -> int | None:
    for idx in empty_cells(board):
        trial = board[:]
        trial[idx] = mark
        if find_winner(trial)[0] == mark:
            return idx
    return None


def pick_easy(board: list[str | None], *, rng: random.Random | None = None) -> int:
    options = empty_cells(board)
    if not options:
        raise ValueError("no empty cells")
    rng = rng or random.Random(0)
    return rng.choice(options)


def pick_medium(board: list[str | None], bot: str, human: str) -> int:
    win = find_winning_move(board, bot)
    if win is not None:
        return win
    block = find_winning_move(board, human)
    if block is not None:
        return block
    if board[CENTER_CELL] is None:
        return CENTER_CELL
    for corner in CORNER_CELLS:
        if board[corner] is None:
            return corner
    options = empty_cells(board)
    return options[0]


def _minimax_score(
    board: list[str | None],
    bot: str,
    human: str,
    bot_turn: bool,
) -> int:
    winner, _ = find_winner(board)
    if winner == bot:
        return 10
    if winner == human:
        return -10
    if not empty_cells(board):
        return 0

    if bot_turn:
        best = -100
        for idx in empty_cells(board):
            trial = board[:]
            trial[idx] = bot
            best = max(best, _minimax_score(trial, bot, human, False))
        return best

    best = 100
    for idx in empty_cells(board):
        trial = board[:]
        trial[idx] = human
        best = min(best, _minimax_score(trial, bot, human, True))
    return best


def pick_hard(board: list[str | None], bot: str, human: str) -> int:
    """Minimax — optimal play for 3×3 (never loses as bot)."""
    best_idx = empty_cells(board)[0]
    best_score = -100
    for idx in empty_cells(board):
        trial = board[:]
        trial[idx] = bot
        score = _minimax_score(trial, bot, human, False)
        if score > best_score:
            best_score = score
            best_idx = idx
    return best_idx


def test_find_winner_row() -> None:
    board: list[str | None] = ["X", "X", "X", None, "O", None, None, None, "O"]
    mark, line = find_winner(board)
    assert mark == "X"
    assert line == (0, 1, 2)


def test_find_winner_diagonal() -> None:
    board = ["O", "X", "X", None, "O", None, "X", None, "O"]
    mark, line = find_winner(board)
    assert mark == "O"
    assert line == (0, 4, 8)


def test_is_draw() -> None:
    board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
    assert is_draw(board)
    assert find_winner(board)[0] is None


def test_medium_takes_win() -> None:
    # Bot O can win on cell 2
    board: list[str | None] = ["O", "O", None, "X", "X", None, None, None, None]
    assert pick_medium(board, "O", "X") == 2


def test_medium_blocks_loss() -> None:
    # Human X threatens index 2
    board = ["X", "X", None, "O", None, None, None, None, None]
    assert pick_medium(board, "O", "X") == 2


def test_medium_prefers_center() -> None:
    board = [None] * 9
    assert pick_medium(board, "O", "X") == 4


def test_easy_is_valid_cell() -> None:
    board = [None] * 9
    idx = pick_easy(board, rng=random.Random(7))
    assert 0 <= idx < 9


def test_hard_never_loses_as_second_player() -> None:
    """If human opens corner, optimal bot should not lose in any human follow-up."""
    bot, human = "O", "X"
    opening = 0
    board: list[str | None] = [None] * 9
    board[opening] = human
    bot_move = pick_hard(board, bot, human)
    board[bot_move] = bot
    for human_reply in empty_cells(board):
        trial = board[:]
        trial[human_reply] = human
        bot_reply = pick_hard(trial, bot, human)
        trial[bot_reply] = bot
        winner, _ = find_winner(trial)
        assert winner != human