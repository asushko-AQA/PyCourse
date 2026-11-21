"""Pure-Python checks for Glyph Grove ★ free-tile and match helpers."""


def is_covered(tile: dict, tiles: list[dict]) -> bool:
    for other in tiles:
        if other.get("removed") or other["id"] == tile["id"]:
            continue
        if other["layer"] <= tile["layer"]:
            continue
        if other["col"] == tile["col"] and other["row"] == tile["row"]:
            return True
    return False


def has_open_side(tile: dict, tiles: list[dict]) -> bool:
    for delta in (-1, 1):
        ncol = tile["col"] + delta
        blocked = any(
            not t.get("removed")
            and t["layer"] == tile["layer"]
            and t["row"] == tile["row"]
            and t["col"] == ncol
            for t in tiles
        )
        if not blocked:
            return True
    return False


def is_free(tile: dict, tiles: list[dict]) -> bool:
    if tile.get("removed"):
        return False
    return not is_covered(tile, tiles) and has_open_side(tile, tiles)


def can_match(a: dict, b: dict, tiles: list[dict]) -> bool:
    if a["id"] == b["id"]:
        return False
    if a.get("removed") or b.get("removed"):
        return False
    if a["kind"] != b["kind"]:
        return False
    return is_free(a, tiles) and is_free(b, tiles)


def test_covered_by_higher_layer() -> None:
    bottom = {"id": 0, "kind": "A", "layer": 0, "row": 2, "col": 3, "removed": False}
    top = {"id": 1, "kind": "B", "layer": 1, "row": 2, "col": 3, "removed": False}
    tiles = [bottom, top]
    assert is_covered(bottom, tiles) is True
    assert is_covered(top, tiles) is False


def test_open_side_when_neighbor_missing() -> None:
    edge = {"id": 0, "kind": "A", "layer": 0, "row": 2, "col": 0, "removed": False}
    other = {"id": 1, "kind": "B", "layer": 0, "row": 2, "col": 2, "removed": False}
    tiles = [edge, other]
    assert has_open_side(edge, tiles) is True


def test_blocked_when_covered_and_walled() -> None:
    left = {"id": 0, "kind": "A", "layer": 0, "row": 1, "col": 1, "removed": False}
    mid = {"id": 1, "kind": "A", "layer": 0, "row": 1, "col": 2, "removed": False}
    right = {"id": 2, "kind": "B", "layer": 0, "row": 1, "col": 3, "removed": False}
    cover = {"id": 3, "kind": "C", "layer": 1, "row": 1, "col": 2, "removed": False}
    tiles = [left, mid, right, cover]
    assert is_free(mid, tiles) is False
    assert is_free(left, tiles) is True
    assert can_match(left, mid, tiles) is False


def test_can_match_free_pair() -> None:
    a = {"id": 0, "kind": "X", "layer": 0, "row": 0, "col": 0, "removed": False}
    b = {"id": 1, "kind": "X", "layer": 0, "row": 0, "col": 2, "removed": False}
    tiles = [a, b]
    assert can_match(a, b, tiles) is True
    b["kind"] = "Y"
    assert can_match(a, b, tiles) is False