import sqlite3
from datetime import datetime, timedelta

def save_payment(user_id: int, plan: str, currency: str, amount: float):
    expiry = datetime.now() + timedelta(days=30)
    conn = sqlite3.connect('subscriptions.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            user_id INTEGER PRIMARY KEY,
            plan TEXT,
            currency TEXT,
            amount REAL,
            status TEXT DEFAULT 'pending',
            expiry_date DATETIME
        )
    """)
    cursor.execute("""
        INSERT INTO payments (user_id, plan, currency, amount, expiry_date)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, plan, currency, amount, expiry))
    conn.commit()
    conn.close()