"""Tests of R8 (command line). Owner: Repository lead."""

from gym_quote.cli import parse_extras, parse_members, run


def fake_session(answers):
    """Return a read function that gives the answers in order and a list of output lines."""
    pending = list(answers)
    lines = []

    def read(_prompt):
        return pending.pop(0)

    return read, lines.append, lines


def test_r8_confirmed_quote_returns_total():
    """R8: answering y returns the total and shows every step."""
    read, write, lines = fake_session(["PREMIUM", "GROUP_CLASSES, SPA", "2", "y"])
    assert run(read, write) == 215
    text = "\n".join(lines)
    assert "Subtotal" in text
    assert "Group discount" in text
    assert "Special offer" in text
    assert "Premium surcharge" in text
    assert "Total:             215" in text


def test_r8_cancelled_quote_returns_minus_one():
    """R8: answering n returns -1."""
    read, write, _ = fake_session(["BASIC", "none", "1", "n"])
    assert run(read, write) == -1


def test_r8_invalid_selection_returns_minus_one_without_confirmation():
    """R8: an invalid selection ends with -1 and does not ask for confirmation."""
    read, write, lines = fake_session(["GOLD", "", "1"])
    assert run(read, write) == -1
    assert "Invalid selection." in lines


def test_r8_parse_helpers():
    """R8: extras and members are parsed from text."""
    assert not parse_extras("none")
    assert parse_extras(" spa , group_classes ") == ["spa", "group_classes"]
    assert parse_members("3") == 3
    assert parse_members("three") is None
