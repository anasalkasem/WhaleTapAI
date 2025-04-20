from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# ✅ تأكد من وجود رابط الاتصال بقاعدة البيانات
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

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)
    whale_wallet = Column(String, nullable=False)
    token_address = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    trade_type = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<WhaleTrade(whale_wallet='{self.whale_wallet}', token='{self.token_address}', amount={self.amount}, type='{self.trade_type}', time='{self.timestamp}')>"

# إرجاع جلسة قاعدة البيانات
def get_db():
    return Session()
