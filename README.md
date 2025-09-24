# Finance Tracker

A simple Python + SQLite project for tracking recurring expenses and subscriptions.

## Features
- Add subscriptions with name, amount, and billing period
- Store start date and calculate next payment date
- Track upcoming expenses

## Project Structure
- `tracker.py` — main script for adding subscriptions
- `db.py` — handles database connection (`get_connection()`)
- `recurring.py` — (planned) script to handle recurring payment updates
- `finance.db` — SQLite database (auto-created on first run)

## Getting Started

1. **Clone this repository**
   ```bash
   git clone <repository-url>
   cd finance-tracker
   ```
   > Replace `<repository-url>` with your actual repo link.

2. **(Optional) Create a virtual environment**
   ```bash
   python -m venv venv
   ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the tracker**
   ```bash
   python tracker.py
   ```

## TODO
- [ ] Implement recurring payment updater
- [ ] Add email field for account references
- [ ] Create a `payments` table to log history
- [ ] Add CLI/GUI for easier use

## License
This project is licensed under the MIT License (see `LICENSE` for details).
