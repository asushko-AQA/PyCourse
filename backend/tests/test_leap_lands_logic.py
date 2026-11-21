"""Pure-Python checks for Leap Lands map parsing and axis-separated collision."""

from __future__ import annotations

SOLID_CHARS = {"#", "="}
COIN_CHAR = "C"
SPAWN_CHAR = "S"
FLAG_CHAR = "F"
SPIKE_CHAR = "^"
ENEMY_CHAR = "E"


def parse_map(rows: list[str], tile: int = 32) -> dict:
    """Turn ASCII map rows into world-space entities (tile-sized cells)."""
    solids: list[tuple[int, int, int, int]] = []
    coins: list[tuple[int, int]] = []
    spikes: list[tuple[int, int, int, int]] = []
    enemies: list[tuple[int, int]] = []
    spawn: tuple[int, int] | None = None
    flag: tuple[int, int, int, int] | None = None
    width = max(len(row) for row in rows) if rows else 0

    for row_i, row in enumerate(rows):
        for col_i, ch in enumerate(row):
            x, y = col_i * tile, row_i * tile
            if ch in SOLID_CHARS:
                solids.append((x, y, tile, tile))
            elif ch == COIN_CHAR:
                coins.append((x + tile // 4, y + tile // 4))
            elif ch == SPAWN_CHAR:
                spawn = (x, y)
            elif ch == FLAG_CHAR:
                flag = (x, y - tile // 2, tile, tile * 2)
            elif ch == SPIKE_CHAR:
                spikes.append((x, y + tile // 2, tile, tile // 2))
            elif ch == ENEMY_CHAR:
                enemies.append((x, y))

    return {
        "width_px": width * tile,
        "solids": solids,
        "coins": coins,
        "spikes": spikes,
        "enemies": enemies,
        "spawn": spawn or (0, 0),
        "flag": flag,
    }


def _overlap(
    ax: float, ay: float, aw: int, ah: int,
    bx: int, by: int, bw: int, bh: int,
) -> bool:
    return ax < bx + bw and ax + aw > bx and ay < by + bh and ay + ah > by


def move_and_resolve(
    x: float,
    y: float,
    w: int,
    h: int,
    solids: list[tuple[int, int, int, int]],
    dx: float,
    dy: float,
) -> tuple[float, float, bool]:
    """Axis-separated resolution: move X, resolve, move Y, resolve."""
    on_ground = False

    nx = x + dx
    for sx, sy, sw, sh in solids:
        if _overlap(nx, y, w, h, sx, sy, sw, sh):
            if dx > 0:
                nx = sx - w
            elif dx < 0:
                nx = sx + sw

    ny = y + dy
    for sx, sy, sw, sh in solids:
        if _overlap(nx, ny, w, h, sx, sy, sw, sh):
            if dy > 0:
                ny = sy - h
                on_ground = True
            elif dy < 0:
                ny = sy + sh

    return nx, ny, on_ground


SAMPLE_MAP = [
    "#######",
    "#S    #",
    "#  =  #",
    "#  C  #",
    "####F##",
]


def test_parse_map_solids_and_spawn() -> None:
    data = parse_map(SAMPLE_MAP, tile=32)
    assert len(data["solids"]) >= 10
    assert data["spawn"] == (32, 32)
    assert len(data["coins"]) == 1
    assert data["flag"] is not None


def test_move_and_resolve_lands_on_platform() -> None:
    solids = [(0, 96, 32, 32), (64, 96, 32, 32)]
    x, y, grounded = move_and_resolve(48.0, 80.0, 24, 24, solids, 0.0, 40.0)
    assert grounded
    assert abs(y - 72.0) < 0.01


def test_move_and_resolve_blocks_horizontal() -> None:
    solids = [(64, 64, 32, 32)]
    x, y, _ = move_and_resolve(50.0, 72.0, 24, 24, solids, 30.0, 0.0)
    assert x == 64 - 24


def test_parse_map_spikes_and_enemies() -> None:
    rows = ["#S#", "#^E", "###"]
    data = parse_map(rows, tile=32)
    assert len(data["spikes"]) == 1
    assert data["enemies"] == [(64, 32)]