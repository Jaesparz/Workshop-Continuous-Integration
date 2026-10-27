"""Tests of R4, R5 and R6. Owner: Developer B."""

from decimal import Decimal

from gym_quote.adjustments import (
    apply_group_discount,
    apply_premium_surcharge,
    apply_special_offer,
)


def test_r4_no_discount_for_one_member():
    """R4: one member pays the full subtotal."""
    assert apply_group_discount(Decimal("100"), 1) == Decimal("100")


def test_r4_ten_percent_from_two_members():
    """R4: two or more members get 10% off."""
    assert apply_group_discount(Decimal("90"), 2) == Decimal("81")
    assert apply_group_discount(Decimal("340"), 4) == Decimal("306")


def test_r5_no_offer_up_to_200():
    """R5: 200 is not greater than 200, so there is no offer."""
    assert apply_special_offer(Decimal("200")) == Decimal("200")


def test_r5_minus_20_above_200():
    """R5: more than 200 and up to 400 subtracts 20."""
    assert apply_special_offer(Decimal("207")) == Decimal("187")
    assert apply_special_offer(Decimal("400")) == Decimal("380")


def test_r5_minus_50_above_400_and_never_both():
    """R5: more than 400 subtracts only 50, not 70."""
    assert apply_special_offer(Decimal("594")) == Decimal("544")


def test_r6_surcharge_with_premium_extra():
    """R6: 15% is added when there is a premium extra."""
    assert apply_premium_surcharge(Decimal("100"), True) == Decimal("115")


def test_r6_no_surcharge_without_premium_extra():
    """R6: no premium extra, no surcharge."""
    assert apply_premium_surcharge(Decimal("100"), False) == Decimal("100")
