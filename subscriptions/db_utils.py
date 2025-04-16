import sqlite3
from datetime import datetime, timedelta

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            user_id INTEGER PRIMARY KEY,
            plan TEXT,
            expiry TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_payment(user_id: int, plan: str, currency: str):
    expiry = datetime.now() + timedelta(days=30)
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO subscriptions (user_id, plan, expiry)
        VALUES (?, ?, ?)
    """, (user_id, f"{plan}_{currency}", expiry))
    conn.commit()
    conn.close()

def activate_subscription(user_id: int, days: int = 30):
    expiry = datetime.now() + timedelta(days=days)
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO subscriptions (user_id, plan, expiry)
        VALUES (?, ?, ?)
    """, (user_id, "manual", expiry))
    conn.commit()
    conn.close()
