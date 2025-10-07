import sqlite3
from pathlib import Path

# ----------------------
# Database helpers
# ----------------------
# Database file lives in the same folder as this script
db_path = Path(__file__).resolve().parent / "finance.db"

def get_connection():
    """Return a SQLite connection to finance.db"""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Create subscriptions table if it does not exist"""
    # TODO
    # Open a connection to finance.db
    with get_connection() as conn:  
        # Create a cursor object to execute SQL commands
        cur = conn.cursor()
        # Run SQL to create the 'expenses' table if it doesn't already exist
        cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT,
            amount REAL,
            period TEXT NOT NULL,
            start DATE,
            next_payment DATE,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)

        # Save changes to the database
        conn.commit()

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