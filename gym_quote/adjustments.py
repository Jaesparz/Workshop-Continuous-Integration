"""Owner: Developer B. Every function receives an amount and returns an amount.
"""

from decimal import Decimal

GROUP_MIN_MEMBERS = 2
GROUP_DISCOUNT_RATE = Decimal("0.10")
HIGH_OFFER_LIMIT = Decimal("400")
HIGH_OFFER_VALUE = Decimal("50")
LOW_OFFER_LIMIT = Decimal("200")
LOW_OFFER_VALUE = Decimal("20")
PREMIUM_SURCHARGE_RATE = Decimal("0.15")


def apply_group_discount(amount, members):
    """R4: with 2 or more members the amount gets a 10% discount."""
    amount = Decimal(str(amount))
    if members >= GROUP_MIN_MEMBERS:
        return amount - amount * GROUP_DISCOUNT_RATE
    return amount


def apply_special_offer(amount):
    """R5: more than 400 -> minus 50; else more than 200 -> minus 20. Never both."""
    amount = Decimal(str(amount))
    if amount > HIGH_OFFER_LIMIT:
        return amount - HIGH_OFFER_VALUE
    if amount > LOW_OFFER_LIMIT:
        return amount - LOW_OFFER_VALUE
    return amount


def apply_premium_surcharge(amount, has_premium):
    """R6: add 15% when the selection has at least one premium extra."""
    amount = Decimal(str(amount))
    if has_premium:
        return amount + amount * PREMIUM_SURCHARGE_RATE
    return amount
