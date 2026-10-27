"""Subtotal and final rounding (R3, R7).

Owner: Developer A.
"""

from decimal import Decimal, ROUND_HALF_UP

from gym_quote.catalog import EXTRAS, PLANS, normalize


def is_valid_members(members):
    """R3: the number of members is an integer of at least 1."""
    return isinstance(members, int) and not isinstance(members, bool) and members >= 1


def subtotal(plan, extras, members):
    """R3: (plan price + price of the extras) x number of members."""
    if not is_valid_members(members):
        raise ValueError("The number of members must be at least 1")
    per_member = PLANS[normalize(plan)]
    per_member += sum(EXTRAS[normalize(extra)][0] for extra in extras)
    return Decimal(per_member * members)


def round_half_up(amount):
    """R7: round half up to a whole number (2.5 -> 3, 121.5 -> 122)."""
    return int(Decimal(str(amount)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
