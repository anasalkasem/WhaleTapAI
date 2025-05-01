from sqlalchemy import Column, Integer, BigInteger, String, DateTime
from models.database import Base
import datetime

class UserSubscription(Base):
    __tablename__ = "user_subscriptions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)
    plan_type = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
