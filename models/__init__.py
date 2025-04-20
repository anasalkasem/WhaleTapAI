from sqlalchemy import Column, Integer, String, Float, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class WhaleTrade(Base):
    __tablename__ = "whale_trades_v2"  # اسم الجدول الرسمي المتّبع

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)  # المستخدم الذي نسخ الصفقة
    whale_wallet = Column(String, nullable=False)  # محفظة الحوت
    token_address = Column(String, nullable=False)  # عنوان العملة
    amount = Column(Float, nullable=False)  # الكمية
    trade_type = Column(String, nullable=False)  # شراء أو بيع
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<WhaleTrade(whale_wallet='{self.whale_wallet}', token='{self.token_address}', amount={self.amount}, type='{self.trade_type}', time='{self.timestamp}')>"
