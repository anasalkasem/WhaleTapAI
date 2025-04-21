from sqlalchemy import Column, BigInteger, String, DateTime
from models.database import Base
import datetime

class Subscription(Base):
    __tablename__ = 'subscriptions'

    user_id = Column(BigInteger, primary_key=True)
    plan_type = Column(String, nullable=False)  # 'free' أو 'pro'
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
