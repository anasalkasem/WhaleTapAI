import sqlite3
from datetime import datetime, timedelta

def init_db():
    conn = sqlite3.connect('subscriptions.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            user_id INTEGER PRIMARY KEY,
            plan TEXT,
            currency TEXT,
            amount REAL,
            tx_hash TEXT,
            status TEXT DEFAULT 'pending',
            expiry_date DATETIME
        )
    ''')
    conn.commit()
    conn.close()

def save_payment(user_id: int, plan: str, currency: str, amount: float):
    expiry = datetime.now() + timedelta(days=30)
    conn = sqlite3.connect('subscriptions.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO payments 
        (user_id, plan, currency, amount, expiry_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, plan, currency, amount, expiry))
    conn.commit()
    conn.close()
    def activate_subscription(user_id: int):
    conn = sqlite3.connect('subscriptions.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE payments SET status = 'active' WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()
from sqlalchemy import insert, select, update
from models import user_settings
from db import session

def set_user_language(user_id: int, language: str):
    stmt = insert(user_settings).values(user_id=user_id, language=language).on_conflict_do_update(
        index_elements=[user_settings.c.user_id],
        set_={"language": language}
    )
    session.execute(stmt)
    session.commit()

def get_user_language(user_id: int) -> str:
    stmt = select(user_settings.c.language).where(user_settings.c.user_id == user_id)
    result = session.execute(stmt).scalar()
    return result or "ar"
