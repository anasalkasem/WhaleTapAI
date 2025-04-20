import sqlite3
from datetime import datetime, timedelta

DB_NAME = 'subscriptions.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # جدول الاشتراكات
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
    
    # جدول إعدادات المستخدم (اللغة)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_settings (
            user_id INTEGER PRIMARY KEY,
            language TEXT DEFAULT 'ar'
        )
    ''')

    conn.commit()
    conn.close()

def save_payment(user_id: int, plan: str, currency: str, amount: float):
    expiry = datetime.now() + timedelta(days=30)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO payments 
        (user_id, plan, currency, amount, expiry_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, plan, currency, amount, expiry))
    conn.commit()
    conn.close()

def activate_subscription(user_id: int):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE payments SET status = 'active' WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()

def set_user_language(user_id: int, language: str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO user_settings (user_id, language)
        VALUES (?, ?)
        ON CONFLICT(user_id) DO UPDATE SET language = excluded.language
    ''', (user_id, language))
    conn.commit()
    conn.close()

def get_user_language(user_id: int) -> str:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT language FROM user_settings WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "ar"
