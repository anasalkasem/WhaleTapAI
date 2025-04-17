# init_db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from models.models import Base
import os
from dotenv import load_dotenv

load_dotenv()

# تأكد أن متغير DATABASE_URL موجود في .env
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found in environment variables")

# إنشاء الاتصال بقاعدة البيانات
engine = create_engine(DATABASE_URL)

# حذف الجداول القديمة وإنشاء جديدة (اختياري)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

print("✅ تم تهيئة قاعدة البيانات بنجاح.")
