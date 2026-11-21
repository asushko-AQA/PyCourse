"""Pure-Python checks for Bounce Forge ★ ball, paddle, and brick helpers."""

from __future__ import annotations


def apply_wall_bounces(
    x: float,
    y: float,
    radius: float,
    vx: float,
    vy: float,
    width: int,
    height: int,
    *,
    bounce_floor: bool = True,
) -> tuple[float, float, float, float]:
    """Reflect velocity when the circle touches window edges."""
    if x - radius <= 0:
        x = radius
        vx = abs(vx)
    elif x + radius >= width:
        x = width - radius
        vx = -abs(vx)
    if y - radius <= 0:
        y = radius
        vy = abs(vy)
    elif bounce_floor and y + radius >= height:
        y = height - radius
        vy = -abs(vy)
    return x, y, vx, vy


def paddle_deflect(hit_frac: float, speed: float, min_vy: float = 180.0) -> tuple[float, float]:
    """Angle from where the ball hit the paddle (-1=left … 1=right)."""
    clamped = max(-1.0, min(1.0, hit_frac))
    vx = clamped * speed * 0.9
    vy = -max(min_vy, speed * 0.75)
    return vx, vy


def brick_hit_side(
    prev_x: float,
    prev_y: float,
    x: float,
    y: float,
    brick: tuple[int, int, int, int],
) -> str | None:
    """Return which brick face was entered: top, bottom, left, right."""
    bx, by, bw, bh = brick
    inside_now = bx <= x <= bx + bw and by <= y <= by + bh
    inside_prev = bx <= prev_x <= bx + bw and by <= prev_y <= by + bh
    if not inside_now:
        return None
    if inside_prev:
        return "top"
    dx_left = abs(x - bx)
    dx_right = abs((bx + bw) - x)
    dy_top = abs(y - by)
    dy_bottom = abs((by + bh) - y)
    side, _ = min(
        (("left", dx_left), ("right", dx_right), ("top", dy_top), ("bottom", dy_bottom)),
        key=lambda pair: pair[1],
    )
    return side


def reflect_brick(vx: float, vy: float, side: str) -> tuple[float, float]:
    if side in ("left", "right"):
        return -vx, vy
    return vx, -vy


def test_wall_bounce_left_and_top() -> None:
    x, y, vx, vy = apply_wall_bounces(-5, 50, 10, -200, -100, 400, 300)
    assert x == 10
    assert vx > 0
    assert vy < 0


def test_wall_bounce_right() -> None:
    x, y, vx, vy = apply_wall_bounces(395, 100, 10, 150, 50, 400, 300)
    assert x == 390
    assert vx < 0


def test_paddle_deflect_edges() -> None:
    left_vx, left_vy = paddle_deflect(-1.0, 300)
    right_vx, right_vy = paddle_deflect(1.0, 300)
    assert left_vx < 0 < right_vx
    assert left_vy < 0 and right_vy < 0


def test_brick_side_and_reflect() -> None:
    brick = (100, 50, 60, 20)
    side = brick_hit_side(130.0, 45.0, 130.0, 55.0, brick)
    assert side == "top"
    vx, vy = reflect_brick(120.0, 200.0, side)
    assert vy == -200.0
    assert vx == 120.0

    side_left = brick_hit_side(95.0, 60.0, 105.0, 60.0, brick)
    assert side_left == "left"
    vx2, vy2 = reflect_brick(100.0, 80.0, side_left)
    assert vx2 == -100.0