from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
import datetime

Base = declarative_base()

class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, unique=True, nullable=False)
    plan_type = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
