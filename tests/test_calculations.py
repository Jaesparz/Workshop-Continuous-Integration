"""Tests of R3 (subtotal) and R7 (rounding). Owner: Developer A."""

from decimal import Decimal

import pytest

from gym_quote.calculations import is_valid_members, round_half_up, subtotal


def test_r3_subtotal_plan_only():
    """R3: one member, no extras, is the plan price."""
    assert subtotal("BASIC", [], 1) == Decimal("30")


def test_r3_subtotal_with_extras_and_members():
    """R3: (45 + 15 + 25) x 4 = 340."""
    assert subtotal("STANDARD", ["GROUP_CLASSES", "PERSONAL_TRAINING"], 4) == Decimal("340")


def test_r3_members_must_be_at_least_one():
    """R3: zero or negative members are invalid."""
    assert not is_valid_members(0)
    assert not is_valid_members(-2)
    assert is_valid_members(1)
    with pytest.raises(ValueError):
        subtotal("BASIC", [], 0)


def test_r7_round_half_up():
    """R7: .5 rounds up, not to the even number."""
    assert round_half_up(Decimal("121.5")) == 122
    assert round_half_up(Decimal("2.5")) == 3
    assert round_half_up(Decimal("411.7")) == 412
    assert round_half_up(Decimal("215.05")) == 215
