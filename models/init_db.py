# models/init_db.py

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base
import os

# إعداد قاعدة البيانات
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
metadata = MetaData()
Base = declarative_base()

def init_db():
    # إنشاء الجداول (لو في موديلات لاحقًا)
    Base.metadata.create_all(engine)
