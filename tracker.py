from db import init_db, get_connection  


def add_purchase(name, amount):
    """Insert a new one-time purchase into the database"""
    # TODO
    with get_connection() as conn:  
        # Create a cursor object to execute SQL commands
        cur = conn.cursor()
        # Makes new row and inserts it into the table 
        cur.execute("""
        INSERT INTO expenses (name, amount, period, start, next_payment)
        VALUES (?, ?, ?, DATE('now'), DATE('now'))
    """, (name, amount, "one-time")) # tuple for input values

        # Save changes to the database
        conn.commit()


def add_subscription(name, amount, period):
    """Insert a new subscription into the database"""
    # TODO
    # 1. add logic for calculating next_payment
    # importing date from datetime
    # setting up logic for reoccuring payments through a new script

    from datetime import date

    start_date = date.today()
    # placeholder - compute next_payment based on period
    # next_payment = 

    with get_connection() as conn:  
        # Create a cursor object to execute SQL commands
        cur = conn.cursor()
        # general parameters to insert new row 
        cur.execute("""
            INSERT INTO expenses (name, amount, period, start, next_payment)
            VALUES (?, ?, ?, ?, ?)
        """, ())        # allows inputs to the row
                        


        # Save changes to the database
        conn.commit()


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