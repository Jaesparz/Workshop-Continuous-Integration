"""Tests of R1 (plans) and R2 (extras). Owner: Developer A."""

from gym_quote.catalog import has_premium_extra, is_valid_plan, is_valid_selection


def test_r1_known_plans_are_valid():
    """R1: every plan of the table is valid."""
    assert is_valid_plan("BASIC")
    assert is_valid_plan("STANDARD")
    assert is_valid_plan("PREMIUM")


def test_r1_plan_ignores_case_and_spaces():
    """R1 (assumption): ' basic ' is read as BASIC."""
    assert is_valid_plan(" basic ")


def test_r1_unknown_plan_is_invalid():
    """R1: any other plan is invalid."""
    assert not is_valid_plan("GOLD")
    assert not is_valid_plan("")


def test_r2_no_extras_is_valid():
    """R2: zero extras is a valid selection."""
    assert is_valid_selection("BASIC", [])


def test_r2_regular_extras_with_any_plan():
    """R2: non-premium extras can go with any plan."""
    assert is_valid_selection("BASIC", ["GROUP_CLASSES", "PERSONAL_TRAINING"])


def test_r2_unknown_extra_is_invalid():
    """R2: an unknown extra makes the selection invalid."""
    assert not is_valid_selection("PREMIUM", ["SAUNA"])


def test_r2_premium_extra_needs_premium_plan():
    """R2: a premium extra with another plan is invalid."""
    assert not is_valid_selection("BASIC", ["SPA"])
    assert not is_valid_selection("STANDARD", ["SPECIALIZED_PROGRAM"])
    assert is_valid_selection("PREMIUM", ["SPA", "SPECIALIZED_PROGRAM"])


def test_r2_repeated_extra_is_invalid():
    """R2 (assumption): the same extra cannot be chosen twice."""
    assert not is_valid_selection("BASIC", ["GROUP_CLASSES", "GROUP_CLASSES"])


def test_r2_detects_premium_extra():
    """R2: a selection with SPA has a premium extra."""
    assert has_premium_extra(["GROUP_CLASSES", "SPA"])
    assert not has_premium_extra(["GROUP_CLASSES"])
