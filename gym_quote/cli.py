"""Command-line interface (R8).

Owner: Repository lead. Input and output are injected so the CLI can be tested.
"""

from gym_quote.catalog import EXTRAS, PLANS
from gym_quote.quote import INVALID, build_quote


def parse_extras(text):
    """Split a comma-separated list of extras. Empty text or 'none' means no extras."""
    text = text.strip()
    if text == "" or text.lower() == "none":
        return []
    return [part.strip() for part in text.split(",") if part.strip()]


def parse_members(text):
    """Return the number of members, or None if the text is not an integer."""
    try:
        return int(text.strip())
    except ValueError:
        return None


def run(read=input, write=print):
    """Ask for plan, extras and members, show the breakdown and ask for confirmation."""
    write("=== Gym Membership Quote ===")
    plan = read(f"Plan ({', '.join(PLANS)}): ")
    extras = parse_extras(read(f"Extras, comma separated ({', '.join(EXTRAS)}) or none: "))
    members = parse_members(read("Number of members: "))

    breakdown = build_quote(plan, extras, members)
    if breakdown is None:
        write("Invalid selection.")
        write(f"Result: {INVALID}")
        return INVALID

    write(f"Subtotal:          {breakdown.subtotal:.2f}")
    write(f"Group discount:   -{breakdown.group_discount:.2f}")
    write(f"Special offer:    -{breakdown.special_offer:.2f}")
    write(f"Premium surcharge: +{breakdown.premium_surcharge:.2f}")
    write(f"Total:             {breakdown.total}")

    answer = read("Confirm the quote? (y/n): ").strip().lower()
    result = breakdown.total if answer == "y" else INVALID
    write(f"Result: {result}")
    return result
