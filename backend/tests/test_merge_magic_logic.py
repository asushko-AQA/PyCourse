"""Pure-Python checks for Merge Magic slide, merge, and game-over rules."""

from __future__ import annotations

SIZE = 4


def compress(row: list[int]) -> list[int]:
    values = [v for v in row if v != 0]
    values.extend([0] * (SIZE - len(values)))
    return values


def merge_row(row: list[int]) -> tuple[list[int], int]:
    row = compress(row[:])
    gained = 0
    i = 0
    while i < SIZE - 1:
        if row[i] != 0 and row[i] == row[i + 1]:
            row[i] *= 2
            gained += row[i]
            row[i + 1] = 0
            i += 2
        else:
            i += 1
    row = compress(row)
    return row, gained


def move_left(board: list[list[int]]) -> tuple[list[list[int]], int, bool]:
    new_board: list[list[int]] = []
    total = 0
    changed = False
    for r in range(SIZE):
        merged, pts = merge_row(board[r])
        total += pts
        if merged != board[r]:
            changed = True
        new_board.append(merged)
    return new_board, total, changed


def reverse_rows(board: list[list[int]]) -> list[list[int]]:
    return [list(reversed(row)) for row in board]


def transpose(board: list[list[int]]) -> list[list[int]]:
    return [[board[r][c] for r in range(SIZE)] for c in range(SIZE)]


def move_right(board: list[list[int]]) -> tuple[list[list[int]], int, bool]:
    flipped = reverse_rows(board)
    moved, pts, changed = move_left(flipped)
    return reverse_rows(moved), pts, changed


def move_up(board: list[list[int]]) -> tuple[list[list[int]], int, bool]:
    t = transpose(board)
    moved, pts, changed = move_left(t)
    return transpose(moved), pts, changed


def move_down(board: list[list[int]]) -> tuple[list[list[int]], int, bool]:
    t = transpose(board)
    flipped = reverse_rows(t)
    moved, pts, changed = move_left(flipped)
    back = reverse_rows(moved)
    return transpose(back), pts, changed


def apply_move(
    board: list[list[int]], direction: str
) -> tuple[list[list[int]], int, bool]:
    if direction == "left":
        return move_left(board)
    if direction == "right":
        return move_right(board)
    if direction == "up":
        return move_up(board)
    if direction == "down":
        return move_down(board)
    raise ValueError(f"unknown direction: {direction}")


def has_empty(board: list[list[int]]) -> bool:
    return any(board[r][c] == 0 for r in range(SIZE) for c in range(SIZE))


def can_move(board: list[list[int]]) -> bool:
    for direction in ("left", "right", "up", "down"):
        _, _, changed = apply_move(board, direction)
        if changed:
            return True
    return False


def test_merge_row_combines_once() -> None:
    row, score = merge_row([2, 2, 2, 0])
    assert row == [4, 2, 0, 0]
    assert score == 4


def test_merge_row_no_double_merge_in_one_slide() -> None:
    row, score = merge_row([2, 2, 4, 4])
    assert row == [4, 8, 0, 0]
    assert score == 12


def test_move_left_unchanged_when_blocked() -> None:
    board = [
        [2, 4, 8, 16],
        [4, 8, 16, 32],
        [8, 16, 32, 64],
        [16, 32, 64, 128],
    ]
    moved, score, changed = move_left(board)
    assert moved == board
    assert score == 0
    assert changed is False


def test_move_up_uses_transpose() -> None:
    board = [
        [2, 0, 0, 0],
        [2, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    moved, score, changed = move_up(board)
    assert moved[0][0] == 4
    assert score == 4
    assert changed is True


def test_game_over_full_board() -> None:
    board = [
        [2, 4, 2, 4],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2],
    ]
    assert not has_empty(board)
    assert can_move(board) is False