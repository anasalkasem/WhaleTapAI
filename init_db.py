from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, MetaData, Table
from datetime import datetime
import os

# إعداد الاتصال بقاعدة البيانات (استخدم env في Railway)
db_url = os.getenv("DATABASE_URL", "sqlite:///whaletap.db")
engine = create_engine(db_url)
metadata = MetaData()

# إنشاء جدول الاشتراكات
subscriptions = Table(
    'subscriptions',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, nullable=False),
    Column('plan', String, nullable=False),  # مثل: "PRO" أو "FREE"
    Column('is_active', Boolean, default=False),
    Column('created_at', DateTime, default=datetime.utcnow),
    Column('expires_at', DateTime, nullable=True),
)

# تنفيذ الإنشاء
metadata.create_all(engine)

print("تم إنشاء الجدول بنجاح.")
