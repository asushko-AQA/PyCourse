"""Pure-Python checks for Glow Worm ★ grid snake helpers."""


def advance_snake(
    segments: list[tuple[int, int]],
    direction: tuple[int, int],
    grow: bool,
) -> list[tuple[int, int]]:
    """Move head one cell; optionally keep the tail (growth)."""
    hc, hr = segments[0]
    dc, dr = direction
    new_head = (hc + dc, hr + dr)
    body = [new_head] + segments
    if not grow:
        body.pop()
    return body


def is_opposite_direction(
    new_dir: tuple[int, int],
    current: tuple[int, int],
) -> bool:
    return new_dir[0] == -current[0] and new_dir[1] == -current[1]


def hits_wall(cell: tuple[int, int], cols: int, rows: int) -> bool:
    c, r = cell
    return c < 0 or c >= cols or r < 0 or r >= rows


def hits_self(segments: list[tuple[int, int]]) -> bool:
    return segments[0] in segments[1:]


def spawn_food(
    cols: int,
    rows: int,
    occupied: set[tuple[int, int]],
    rng,
) -> tuple[int, int]:
    for _ in range(cols * rows):
        pos = (rng.randint(0, cols - 1), rng.randint(0, rows - 1))
        if pos not in occupied:
            return pos
    raise RuntimeError("grid full")


def test_advance_snake_moves_head() -> None:
    segs = [(5, 5), (4, 5), (3, 5)]
    moved = advance_snake(segs, (1, 0), grow=False)
    assert moved == [(6, 5), (5, 5), (4, 5)]


def test_advance_snake_grows_tail() -> None:
    segs = [(2, 2), (1, 2)]
    grown = advance_snake(segs, (0, 1), grow=True)
    assert grown == [(2, 3), (2, 2), (1, 2)]
    assert len(grown) == len(segs) + 1


def test_opposite_direction_blocks_u_turn() -> None:
    assert is_opposite_direction((-1, 0), (1, 0)) is True
    assert is_opposite_direction((0, -1), (0, 1)) is True
    assert is_opposite_direction((1, 0), (0, 1)) is False


def test_wall_and_self_collision() -> None:
    assert hits_wall((0, 0), 10, 10) is False
    assert hits_wall((-1, 0), 10, 10) is True
    assert hits_wall((10, 0), 10, 10) is True
    assert hits_self([(3, 3), (2, 3), (1, 3)]) is False
    segs = [(1, 1), (2, 1), (1, 1)]
    assert hits_self(segs) is True


def test_spawn_food_skips_body() -> None:
    import random

    rng = random.Random(0)
    body = {(0, 0), (1, 0)}
    food = spawn_food(3, 2, body, rng)
    assert food not in body