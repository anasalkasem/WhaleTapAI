from sqlalchemy import Column, Integer, String
from models.database import Base

class UserLanguage(Base):
    __tablename__ = "user_languages"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True, nullable=False)
    language = Column(String, default="en")
