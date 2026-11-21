"""Pure-Python checks for Shard Stack ★ lesson helpers (rotation + line clear)."""


def rotate_cells(cells: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return [(c, -r) for r, c in cells]


def clear_lines_logic(grid_rows: list[list[int]]) -> tuple[list[list[int]], int]:
    kept: list[list[int]] = []
    cleared = 0
    for row in grid_rows:
        if row and all(row):
            cleared += 1
        else:
            kept.append(list(row))
    while len(kept) < len(grid_rows):
        kept.insert(0, [0] * len(grid_rows[0]))
    return kept, cleared


def test_rotate_cells_quarter_turn() -> None:
    assert rotate_cells([(0, 0), (0, 1), (1, 0)]) == [(0, 0), (1, 0), (0, -1)]
    assert rotate_cells([(1, 0)]) == [(0, -1)]
    turned = rotate_cells([(2, 3)])
    for _ in range(3):
        turned = rotate_cells(turned)
    assert turned == [(2, 3)]


def test_clear_lines_removes_full_rows() -> None:
    grid = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 1, 0],
        [1, 1, 1],
    ]
    new_grid, cleared = clear_lines_logic(grid)
    assert cleared == 2
    assert new_grid == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 1, 0],
    ]