from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class WhaleTrade(Base):
    __tablename__ = "whale_trades"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    whale_wallet = Column(String, nullable=False)
    token_address = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    trade_type = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)

def get_db():
    return Session()
