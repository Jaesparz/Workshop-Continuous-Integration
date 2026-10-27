"""Tests of the whole quote with the table of the workshop (R9)."""

from decimal import Decimal

import pytest

from gym_quote.quote import build_quote, calculate_total

TABLE = [
    ("BASIC", [], 1, 30),
    ("STANDARD", ["PERSONAL_TRAINING"], 1, 70),
    ("BASIC", ["GROUP_CLASSES"], 2, 81),
    ("BASIC", ["GROUP_CLASSES"], 3, 122),
    ("STANDARD", ["GROUP_CLASSES", "PERSONAL_TRAINING"], 4, 286),
    ("PREMIUM", ["GROUP_CLASSES", "SPA"], 2, 215),
    ("PREMIUM", ["SPA", "SPECIALIZED_PROGRAM"], 3, 412),
    ("PREMIUM", ["SPA", "SPECIALIZED_PROGRAM", "PERSONAL_TRAINING"], 4, 626),
    ("BASIC", ["SPA"], 1, -1),
    ("GOLD", [], 1, -1),
    ("BASIC", [], 0, -1),
]


@pytest.mark.parametrize("plan, extras, members, expected", TABLE)
def test_r9_table_of_the_workshop(plan, extras, members, expected):
    """R9: every row of the table of the workshop."""
    assert calculate_total(plan, extras, members) == expected


def test_r7_invalid_members_type_returns_minus_one():
    """R7: a number of members that is not an integer is invalid."""
    assert calculate_total("BASIC", [], None) == -1
    assert calculate_total("BASIC", [], 1.5) == -1


def test_breakdown_shows_each_step():
    """R8 support: the breakdown keeps every discount and the surcharge."""
    breakdown = build_quote("PREMIUM", ["GROUP_CLASSES", "SPA"], 2)
    assert breakdown.subtotal == Decimal("230")
    assert breakdown.group_discount == Decimal("23")
    assert breakdown.special_offer == Decimal("20")
    assert breakdown.premium_surcharge == Decimal("28.05")
    assert breakdown.total == 215
