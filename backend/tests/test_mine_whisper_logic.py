"""Pure-Python checks for Mine Whisper neighbour counts and flood reveal."""

from __future__ import annotations


def make_cell(*, mine: bool = False) -> dict[str, int | bool]:
    return {"mine": mine, "revealed": False, "flagged": False, "neighbors": 0}


def count_neighbor_mines(grid: list[list[dict]], col: int, row: int, cols: int, rows: int) -> int:
    total = 0
    for dc in (-1, 0, 1):
        for dr in (-1, 0, 1):
            if dc == 0 and dr == 0:
                continue
            nc, nr = col + dc, row + dr
            if 0 <= nc < cols and 0 <= nr < rows and grid[nr][nc]["mine"]:
                total += 1
    return total


def flood_reveal_stack(
    grid: list[list[dict]],
    col: int,
    row: int,
    cols: int,
    rows: int,
) -> None:
    stack: list[tuple[int, int]] = [(col, row)]
    while stack:
        c, r = stack.pop()
        if not (0 <= c < cols and 0 <= r < rows):
            continue
        cell = grid[r][c]
        if cell["revealed"] or cell["flagged"] or cell["mine"]:
            continue
        cell["revealed"] = True
        if cell["neighbors"] == 0:
            for dc in (-1, 0, 1):
                for dr in (-1, 0, 1):
                    if dc == 0 and dr == 0:
                        continue
                    stack.append((c + dc, r + dr))


def flood_reveal_recursive(
    grid: list[list[dict]],
    col: int,
    row: int,
    cols: int,
    rows: int,
) -> None:
    if not (0 <= col < cols and 0 <= row < rows):
        return
    cell = grid[row][col]
    if cell["revealed"] or cell["flagged"] or cell["mine"]:
        return
    cell["revealed"] = True
    if cell["neighbors"] != 0:
        return
    for dc in (-1, 0, 1):
        for dr in (-1, 0, 1):
            if dc == 0 and dr == 0:
                continue
            flood_reveal_recursive(grid, col + dc, row + dr, cols, rows)


def _tiny_board() -> tuple[list[list[dict]], int, int]:
    cols, rows = 5, 4
    grid = [[make_cell() for _ in range(cols)] for _ in range(rows)]
    grid[1][2]["mine"] = True
    grid[2][3]["mine"] = True
    for r in range(rows):
        for c in range(cols):
            grid[r][c]["neighbors"] = count_neighbor_mines(grid, c, r, cols, rows)
    return grid, cols, rows


def test_neighbor_mine_count() -> None:
    grid, cols, rows = _tiny_board()
    assert count_neighbor_mines(grid, 1, 1, cols, rows) == 1
    assert count_neighbor_mines(grid, 2, 2, cols, rows) == 2


def test_flood_stack_opens_zero_region() -> None:
    grid, cols, rows = _tiny_board()
    flood_reveal_stack(grid, 0, 0, cols, rows)
    revealed = sum(1 for r in range(rows) for c in range(cols) if grid[r][c]["revealed"])
    assert revealed >= 6
    assert not grid[1][2]["revealed"]


def test_flood_recursive_matches_stack() -> None:
    grid_a, cols, rows = _tiny_board()
    grid_b, _, _ = _tiny_board()
    flood_reveal_stack(grid_a, 0, 0, cols, rows)
    flood_reveal_recursive(grid_b, 0, 0, cols, rows)
    for r in range(rows):
        for c in range(cols):
            assert grid_a[r][c]["revealed"] == grid_b[r][c]["revealed"]