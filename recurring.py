
from db import get_connection 


"""
Helpers for working with recurring expenses.

Covers:
- Normalizing period values (daily, weekly, monthly, yearly, one-time)
- Doing date math for next payments
- Updating the DB with the right next_payment values

"""
# ----------------------
# Constants
# ----------------------
PERIOD_OPTIONS = ("weekly", "bi-weekly", "monthly", "yearly")
NON_RECURRING = ("one-time",)

# ----------------------
# Period utilities
# ----------------------
def validate_period(period: str) -> str:
    """Ensure period is one of the allowed options."""
    if period not in PERIOD_OPTIONS + NON_RECURRING:
        # Raise an error if the string is valid Python type (str)
        # but the *value* is not one of the allowed PERIOD_OPTIONS.
        # Example: validate_period("random") -> ValueError


        # Raise an exception instead of silently failing.
        raise ValueError(f"Invalid period: {period}. Must be one of {PERIOD_OPTIONS + NON_RECURRING}")
    return period


def is_recurring(period: str) -> bool:
    """Return True if the period repeats.

    "one-time" should be treated as non-recurring.
    """
    # if in PERIOD_OPTIONS then mark it as true since its recurring
    if period in PERIOD_OPTIONS:
        return True
    elif period in NON_RECURRING: # one-time = non-recurring
        return False
    else:
        raise ValueError(f"Unknown period: {period}") # not an option


# ----------------------
# Date helpers
# ----------------------
def calculate_next_payment(start_date, period: str, from_date=None):
    """Figure out the next payment date.

    Args:
        start_date: first charge date (datetime.date)
        period: normalized period string
        from_date: what date to calculate from (defaults to today)

    Rules:
    - one-time: return start_date if it hasn’t passed yet, else None
    - recurring: return the first date after `from_date`

    TODO: implement actual math (daily/weekly/monthly/yearly).
    """
    pass


def advance_until_after(current_next_date, period: str, after_date):
    """Keep moving `current_next_date` forward until it’s past `after_date`.

    Useful when the app hasn’t run for a while and you want to 
    “catch up” the schedule.
    """
    pass


# ----------------------
# Database operations
# ----------------------
def update_next_payments(days_ahead: int = 0) -> int:
    """Bump `next_payment` for anything that’s due or overdue.

    Plan:
    - Pull rows from `expenses` where next_payment is <= today (+ days_ahead).
    - Skip one-time entries.
    - Recalculate next_payment and save back to DB.

    Returns:
        int: number of rows updated
    """
    pass


def due_within(days: int):
    """Get rows due in the next N days.

    Plan:
    - Query `expenses` for next_payment within the given window.
    - Probably skip one-time entries that are already past due.
    """
    pass