from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

Base = declarative_base()

class WhaleTrade(Base):
    __tablename__ = "whale_trades"

    id = Column(Integer, primary_key=True, index=True)
    wallet_address = Column(String, index=True)
    token = Column(String)
    amount = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
