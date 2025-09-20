import argparse
import sqlite3
from pathlib import Path

# Database file lives in the same folder as this script
db_path = Path(__file__).resolve().parent / "finance.db"


# ----------------------
# Database helpers
# ----------------------
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


def add_subscription(name, amount, period):
    """Insert a new subscription into the database"""
    # TODO
    pass


def list_subscriptions():
    """List all subscriptions"""
    "will use cur"
    # TODO
    pass


def monthly_total():
    """Calculate monthly equivalent sum of all subscriptions"""
    # TODO
    pass


def due_charges(days):
    """Show subscriptions due in the next N days"""
    # TODO
    pass


def cancel_subscription(sub_id):
    """Mark a subscription as inactive"""
    # TODO
    pass


# ----------------------
# CLI
# ----------------------
def main():
    parser = argparse.ArgumentParser(description="Simple subscription tracker")
    subparsers = parser.add_subparsers(dest="command")

    # TODO: add subcommands here (add, list, monthly, due, cancel)

    args = parser.parse_args()

    # TODO: handle args.command and call functions above
    pass


if __name__ == "__main__":
    main()