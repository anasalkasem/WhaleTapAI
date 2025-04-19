# utils/delete_table_whale_trades_v2.py

from sqlalchemy import create_engine, MetaData, Table
import os

# الاتصال بقاعدة البيانات عبر DATABASE_URL من متغيرات البيئة
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise Exception("❌ تأكد من ضبط متغير البيئة DATABASE_URL")

# إعداد الاتصال
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# جلب كل الجداول من القاعدة
metadata.reflect(bind=engine)

# حذف الجدول إذا كان موجود
table_name = "whale_trades_v2"
if table_name in metadata.tables:
    table = Table(table_name, metadata, autoload_with=engine)
    table.drop(engine)
    print(f"✅ تم حذف الجدول {table_name} بنجاح.")
else:
    print(f"⚠️ الجدول {table_name} غير موجود أصلاً.")
