"""Pure-Python checks for Twin Cards deck building and pair matching."""

from __future__ import annotations

import random


def build_deck(cols: int, rows: int, *, rng: random.Random | None = None) -> list[int]:
    """Return shuffled symbol ids — each id appears exactly twice."""
    if cols * rows % 2 != 0:
        raise ValueError("grid must have an even number of cells")
    pair_count = (cols * rows) // 2
    deck = list(range(pair_count)) * 2
    rng = rng or random.Random(0)
    rng.shuffle(deck)
    return deck


def cards_match(symbol_a: int, symbol_b: int) -> bool:
    return symbol_a == symbol_b


def all_matched(matched_flags: list[bool]) -> bool:
    return bool(matched_flags) and all(matched_flags)


def layout_deck(deck: list[int], cols: int, rows: int) -> list[dict]:
    if len(deck) != cols * rows:
        raise ValueError("deck length must match grid size")
    cards: list[dict] = []
    for row in range(rows):
        for col in range(cols):
            idx = row * cols + col
            cards.append({"col": col, "row": row, "symbol": deck[idx]})
    return cards


def test_build_deck_has_pairs_only() -> None:
    deck = build_deck(4, 3, rng=random.Random(42))
    assert len(deck) == 12
    counts: dict[int, int] = {}
    for sym in deck:
        counts[sym] = counts.get(sym, 0) + 1
    assert len(counts) == 6
    assert all(v == 2 for v in counts.values())


def test_build_deck_rejects_odd_grid() -> None:
    try:
        build_deck(3, 3)
    except ValueError:
        return
    raise AssertionError("expected ValueError for odd cell count")


def test_cards_match() -> None:
    assert cards_match(2, 2)
    assert not cards_match(1, 2)


def test_all_matched() -> None:
    assert not all_matched([True, False])
    assert all_matched([True, True, True])


def test_layout_deck_preserves_symbols() -> None:
    deck = build_deck(4, 4, rng=random.Random(1))
    cards = layout_deck(deck, 4, 4)
    assert [c["symbol"] for c in cards] == deck