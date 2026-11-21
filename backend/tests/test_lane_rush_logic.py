"""Pure-Python checks for Lane Rush lanes, scroll, spawns, and collision."""

from __future__ import annotations

import math
import random


def lane_center_x(lane: int, road_left: int, lane_width: int) -> float:
    return road_left + lane * lane_width + lane_width / 2


def advance_scroll_offset(offset: float, speed: float, dt: float, stripe_h: float) -> float:
    return (offset + speed * dt) % stripe_h


def pick_spawn_lane(rng: random.Random, num_lanes: int) -> int:
    return rng.randint(0, num_lanes - 1)


def rects_overlap(
    ax: float,
    ay: float,
    aw: float,
    ah: float,
    bx: float,
    by: float,
    bw: float,
    bh: float,
) -> bool:
    return ax < bx + bw and ax + aw > bx and ay < by + bh and ay + ah > by


def distance_meters(elapsed: float, scroll_speed: float) -> float:
    return elapsed * scroll_speed * 0.12


def edge_gap(
    ax: float,
    ay: float,
    aw: float,
    ah: float,
    bx: float,
    by: float,
    bw: float,
    bh: float,
) -> float:
    """Positive gap between axis-aligned rects; 0 if overlapping."""
    if rects_overlap(ax, ay, aw, ah, bx, by, bw, bh):
        return 0.0
    dx = max(bx - (ax + aw), ax - (bx + bw), 0.0)
    dy = max(by - (ay + ah), ay - (by + bh), 0.0)
    return math.hypot(dx, dy)


def near_miss_bonus(collided: bool, gap: float, threshold: float = 22.0) -> int:
    if collided or gap <= 0 or gap > threshold:
        return 0
    return 25


def ramp_scroll_speed(base: float, elapsed: float, add_per_sec: float = 6.5) -> float:
    return base + elapsed * add_per_sec


def test_lane_center_x() -> None:
    assert lane_center_x(0, 100, 80) == 140.0
    assert lane_center_x(2, 100, 80) == 300.0


def test_advance_scroll_wraps() -> None:
    assert advance_scroll_offset(30.0, 100.0, 0.2, 40.0) == 10.0
    assert advance_scroll_offset(38.0, 50.0, 0.1, 40.0) == 3.0


def test_spawn_lane_range() -> None:
    rng = random.Random(3)
    lanes = {pick_spawn_lane(rng, 4) for _ in range(50)}
    assert lanes.issubset({0, 1, 2, 3})
    assert len(lanes) > 1


def test_rects_overlap_and_gap() -> None:
    assert rects_overlap(0, 0, 10, 10, 5, 5, 10, 10)
    assert not rects_overlap(0, 0, 10, 10, 20, 0, 10, 10)
    gap = edge_gap(0, 0, 10, 10, 12, 0, 10, 10)
    assert math.isclose(gap, 2.0)


def test_near_miss_only_when_close() -> None:
    assert near_miss_bonus(False, 8.0) == 25
    assert near_miss_bonus(True, 8.0) == 0
    assert near_miss_bonus(False, 40.0) == 0


def test_ramp_scroll_speed() -> None:
    assert math.isclose(ramp_scroll_speed(120.0, 10.0), 185.0)
    assert math.isclose(distance_meters(5.0, 200.0), 120.0)