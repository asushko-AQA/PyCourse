"""Pure-Python checks for Night Swarm vectors, targeting, and level-up picks."""

from __future__ import annotations

import math
import random


def direction_toward(ax: float, ay: float, bx: float, by: float) -> tuple[float, float]:
  """Unit vector from A toward B (0,0 if same point)."""
  dx, dy = bx - ax, by - ay
  length = math.hypot(dx, dy)
  if length == 0:
    return 0.0, 0.0
  return dx / length, dy / length


def nearest_enemy_index(
  px: float,
  py: float,
  enemies: list[dict],
) -> int | None:
  best_i: int | None = None
  best_d2 = math.inf
  for i, e in enumerate(enemies):
    if e.get("hp", 1) <= 0:
      continue
    ex, ey = e["x"], e["y"]
    d2 = (ex - px) ** 2 + (ey - py) ** 2
    if d2 < best_d2:
      best_d2 = d2
      best_i = i
  return best_i


def pick_level_up_choices(
  upgrade_keys: list[str],
  n: int,
  rng: random.Random,
) -> list[str]:
  pool = list(upgrade_keys)
  rng.shuffle(pool)
  return pool[: min(n, len(pool))]


def xp_after_pickups(current_xp: int, need: int, pickups: list[int]) -> tuple[int, int, int]:
  """Returns (xp, level, times_leveled) after collecting gem values."""
  level = 1
  xp = current_xp
  leveled = 0
  for value in pickups:
    xp += value
    while xp >= need:
      xp -= need
      level += 1
      need += 4
      leveled += 1
  return xp, level, leveled


def test_direction_toward_is_normalized() -> None:
  ux, uy = direction_toward(0.0, 0.0, 30.0, 40.0)
  assert math.isclose(math.hypot(ux, uy), 1.0)
  assert math.isclose(ux, 0.6)
  assert math.isclose(uy, 0.8)


def test_direction_toward_zero_when_same_point() -> None:
  assert direction_toward(5.0, 5.0, 5.0, 5.0) == (0.0, 0.0)


def test_nearest_enemy_picks_closest() -> None:
  enemies = [
    {"x": 100.0, "y": 0.0, "hp": 10},
    {"x": 12.0, "y": 0.0, "hp": 10},
    {"x": 200.0, "y": 0.0, "hp": 0},
  ]
  assert nearest_enemy_index(0.0, 0.0, enemies) == 1


def test_pick_level_up_three_unique() -> None:
  rng = random.Random(7)
  keys = ["damage", "fire_rate", "speed", "extra_orb", "orbit"]
  choices = pick_level_up_choices(keys, 3, rng)
  assert len(choices) == 3
  assert len(set(choices)) == 3
  assert set(choices).issubset(set(keys))


def test_xp_level_up_chain() -> None:
  xp, level, ups = xp_after_pickups(8, 10, [3, 3, 6])
  assert ups == 1
  assert level == 2
  assert xp == 10