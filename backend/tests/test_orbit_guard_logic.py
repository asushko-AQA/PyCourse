"""Pure-Python checks for Orbit Guard ★ formation march and bullet hits."""

from __future__ import annotations


def step_formation(
    offset_x: float,
    offset_y: float,
    direction: int,
    *,
    speed: float,
    dt: float,
    margin: float,
    formation_width: float,
    screen_width: float,
    step_down: float,
) -> tuple[float, float, int, bool]:
    """March sideways; at edges flip direction and step down once."""
    new_x = offset_x + direction * speed * dt
    left = new_x
    right = new_x + formation_width
    stepped_down = False
    if left <= margin or right >= screen_width - margin:
        direction *= -1
        new_x = offset_x + direction * speed * dt
        offset_y += step_down
        stepped_down = True
    return new_x, offset_y, direction, stepped_down


def bullet_hits_rect(bx: float, by: float, rect: tuple[float, float, float, float]) -> bool:
    """Axis-aligned hit test (bullet as a point)."""
    left, top, w, h = rect
    return left <= bx <= left + w and top <= by <= top + h


def prune_bolts(bolts: list[dict[str, float]], *, top: float, bottom: float) -> list[dict[str, float]]:
    """Drop bolts that scrolled off the playfield."""
    return [b for b in bolts if top < b["y"] < bottom]


def test_formation_bounces_and_steps_down() -> None:
    x, y, d, stepped = step_formation(
        95.0,
        40.0,
        1,
        speed=120.0,
        dt=1.0,
        margin=20.0,
        formation_width=600.0,
        screen_width=720.0,
        step_down=14.0,
    )
    assert stepped is True
    assert d == -1
    assert y == 54.0


def test_bullet_hits_invader_rect() -> None:
    inv = (100.0, 80.0, 34.0, 26.0)
    assert bullet_hits_rect(117.0, 93.0, inv)
    assert not bullet_hits_rect(50.0, 93.0, inv)


def test_prune_bolts_off_screen() -> None:
    bolts = [{"x": 10.0, "y": 5.0, "vy": -200.0}, {"x": 20.0, "y": 200.0, "vy": -200.0}]
    kept = prune_bolts(bolts, top=50.0, bottom=500.0)
    assert len(kept) == 1
    assert kept[0]["y"] == 200.0