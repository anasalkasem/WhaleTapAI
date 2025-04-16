from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class WhaleTrade(Base):
    __tablename__ = "whale_trades"

    id = Column(Integer, primary_key=True, autoincrement=True)
    wallet = Column(String, nullable=False)
    token = Column(String, nullable=False)
    amount = Column(String, nullable=False)
    price = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<WhaleTrade(wallet='{self.wallet}', token='{self.token}', amount='{self.amount}', timestamp='{self.timestamp}')>"
