from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import datetime

# ✅ تأكد من وجود رابط الاتصال
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise Exception("❌ DATABASE_URL is missing! Please check your Railway environment variables.")

# إنشاء الاتصال بقاعدة البيانات
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# تعريف القاعدة
Base = declarative_base()

# جدول صفقات الحيتان
class WhaleTrade(Base):
    __tablename__ = "whale_trades_v2"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, nullable=False)
    whale_wallet = Column(String, nullable=False)
    token_address = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    trade_type = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# إرجاع جلسة
def get_db():
    return Session()
