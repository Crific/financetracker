
from db import get_connection 


"""
Helpers for working with recurring expenses.

Covers:
- Normalizing period values (daily, weekly, monthly, yearly, one-time)
- Doing date math for next payments
- Updating the DB with the right next_payment values

"""

# ----------------------
# Period utilities
# ----------------------
def normalize_period(period: str) -> str:
    """Make period strings consistent.

    Examples:
    - "Monthly" -> "monthly"
    - "mo" -> "monthly"
    - "1m" -> "monthly"

    TODO: add alias mapping + validation.
    """
    pass


def is_recurring(period: str) -> bool:
    """Return True if the period repeats.

    Tip: "one-time" should be treated as non-recurring.
    """
    pass


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