from sqlalchemy import Column, Integer, String, Float, BigInteger, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class WhaleTrade(Base):
    __tablename__ = 'whale_trades_v2'  # اسم الجدول النهائي

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)
    whale_wallet = Column(String, nullable=False)
    token_address = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    trade_type = Column(String, nullable=False)  # buy أو sell
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
