"""Catalog of plans and extras, and selection validation (R1, R2).

Owner: Developer A.
"""

PLANS = {
    "BASIC": 30,
    "STANDARD": 45,
    "PREMIUM": 70,
}

# name -> (price per member, is premium extra)
EXTRAS = {
    "GROUP_CLASSES": (15, False),
    "PERSONAL_TRAINING": (25, False),
    "SPA": (30, True),
    "SPECIALIZED_PROGRAM": (40, True),
}

PREMIUM_PLAN = "PREMIUM"


def normalize(name):
    """Return the name without surrounding spaces and in upper case."""
    return str(name).strip().upper()


def is_valid_plan(plan):
    """R1: the plan must be one of the plans in the catalog."""
    return normalize(plan) in PLANS


def is_premium_extra(extra):
    """Return True if the extra exists and is a premium extra."""
    entry = EXTRAS.get(normalize(extra))
    return entry is not None and entry[1]


def has_premium_extra(extras):
    """Return True if at least one extra of the list is premium."""
    return any(is_premium_extra(extra) for extra in extras)


def is_valid_selection(plan, extras):
    """R1 + R2: valid plan, known extras, no repeats, premium only with PREMIUM."""
    if not is_valid_plan(plan):
        return False
    names = [normalize(extra) for extra in extras]
    if len(names) != len(set(names)):
        return False
    if any(name not in EXTRAS for name in names):
        return False
    if has_premium_extra(names) and normalize(plan) != PREMIUM_PLAN:
        return False
    return True
