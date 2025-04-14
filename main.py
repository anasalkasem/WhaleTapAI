
import os
import psycopg2

# الاتصال بقاعدة البيانات من متغير البيئة
DATABASE_URL = os.environ.get("DATABASE_URL")

# فتح الاتصال
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# إنشاء جدول للمحافظ إذا لم يكن موجود
cursor.execute("""
    CREATE TABLE IF NOT EXISTS whales (
        id SERIAL PRIMARY KEY,
        wallet_address TEXT UNIQUE,
        activity TEXT
    );
""")
conn.commit()

# إدخال محفظة تجريبية
try:
    cursor.execute("INSERT INTO whales (wallet_address, activity) VALUES (%s, %s)",
                   ("So1anaWhaleWalletTest123", "buy"))
    conn.commit()
except psycopg2.errors.UniqueViolation:
    conn.rollback()

# قراءة المحافظ من القاعدة
cursor.execute("SELECT * FROM whales;")
rows = cursor.fetchall()

for row in rows:
    print(f"Whale Wallet: {row[1]} | Activity: {row[2]}")

# إغلاق الاتصال
cursor.close()
conn.close()
