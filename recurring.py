
from db import get_connection 
from datetime import date
from dateutil.relativedelta import relativedelta

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
PERIOD_OPTIONS = ("daily", "weekly", "bi-weekly", "monthly", "yearly")
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
    - one-time: return None
    - recurring: return the first date after `from_date`

    TODO: implement actual math (daily/weekly/monthly/yearly).
    """
    period = validate_period(period) 

    # Handle default from_date
    if from_date is None:
        from_date = date.today()

    # One-time payments
    if period in NON_RECURRING:
        return None

    # Recurring payments
    # Start from the first payment date and move forward by period length
    # until we find a date that comes after from_date
    #
    # For example:
    #   - weekly     → +1 week
    #   - bi-weekly  → +2 weeks
    #   - monthly    → +1 month
    #   - yearly     → +1 year

    if period == "daily":
        next_payment = start_date + relativedelta(days=1)

    elif period == "weekly":
        next_payment = start_date + relativedelta(weeks=1)

    elif period == "bi-weekly":
        next_payment = start_date + relativedelta(weeks=2)

    elif period == "monthly":
        next_payment = start_date + relativedelta(months=1)

    elif period == "yearly":
        next_payment = start_date + relativedelta(years=1)

    else:
        # unknown period would result in an error
       raise ValueError(f"Unknown period: {period!r}")

    # TODO: ensure next_payment is actually after from_date

    next_payment = advance_until_after(next_payment, period, from_date)

    return next_payment


def advance_until_after(current_next_date, period: str, after_date):
    """Keep moving `current_next_date` forward until it’s past `after_date`.

    Useful when the app hasn’t run for a while and you want to 
    “catch up” the schedule.
    """
    while current_next_date <= after_date:
        if period == "daily":
            current_next_date += relativedelta(days=1)
        elif period == "weekly":
            current_next_date += relativedelta(weeks=1)
        elif period == "bi-weekly":
            current_next_date += relativedelta(weeks=2)
        elif period == "monthly":
            current_next_date += relativedelta(months=1)
        elif period == "yearly":
            current_next_date += relativedelta(years=1)
        else:
            raise ValueError(f"Unknown period: {period!r}")

    return current_next_date


