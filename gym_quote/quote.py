"""Quote calculation: joins R1-R7. Does no input or output (R8)."""

from dataclasses import dataclass
from decimal import Decimal

from gym_quote.adjustments import (
    apply_group_discount,
    apply_premium_surcharge,
    apply_special_offer,
)
from gym_quote.calculations import is_valid_members, round_half_up, subtotal
from gym_quote.catalog import has_premium_extra, is_valid_selection

INVALID = -1


@dataclass(frozen=True)
class QuoteBreakdown:
    """Every step of the quote, so the command line can show it."""

    subtotal: Decimal
    group_discount: Decimal
    special_offer: Decimal
    premium_surcharge: Decimal
    total: int


def build_quote(plan, extras, members):
    """Return the breakdown of a valid selection, or None if it is invalid."""
    extras = list(extras)
    if not is_valid_selection(plan, extras) or not is_valid_members(members):
        return None
    base = subtotal(plan, extras, members)
    after_group = apply_group_discount(base, members)
    after_offer = apply_special_offer(after_group)
    after_surcharge = apply_premium_surcharge(after_offer, has_premium_extra(extras))
    return QuoteBreakdown(
        subtotal=base,
        group_discount=base - after_group,
        special_offer=after_group - after_offer,
        premium_surcharge=after_surcharge - after_offer,
        total=round_half_up(after_surcharge),
    )


def calculate_total(plan, extras, members):
    """R7: the rounded total, or -1 if the selection is invalid."""
    breakdown = build_quote(plan, extras, members)
    return INVALID if breakdown is None else breakdown.total
