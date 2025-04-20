from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import datetime

# جلب رابط الاتصال من متغير البيئة
DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise Exception("❌ DATABASE_URL is missing! Please check your Railway environment variables.")
# إنشاء الاتصال بقاعدة البيانات
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# تعريف القاعدة
Base = declarative_base()

# تعريف جدول صفقات الحيتان الجديد
class WhaleTrade(Base):
    __tablename__ = "whale_trades_v2"  # تأكد أنه نفس الاسم الموجود بقاعدة البيانات

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, nullable=False)
    whale_wallet = Column(String, nullable=False)
    token_address = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    trade_type = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# إرجاع جلسة قاعدة البيانات
def get_db():
    return Session()
