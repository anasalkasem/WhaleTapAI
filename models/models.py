from sqlalchemy import Column, Integer, String, Float, BigInteger, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class WhaleTrade(Base):
    __tablename__ = 'whale_trades_v2'  # اسم الجدول الجديد

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger)
    whale_wallet = Column(String)
    token_address = Column(String)
    amount = Column(Float)
    trade_type = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class WhaleTrade(Base):
    __tablename__ = "whale_trades_v2"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    wallet_address = Column(String, nullable=False)
    token_symbol = Column(String, nullable=False)
    amount = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
