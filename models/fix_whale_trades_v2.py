from sqlalchemy import create_engine, text
import os

# الاتصال بقاعدة البيانات
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    try:
        # حذف العمود إذا كان موجود
        connection.execute(text("ALTER TABLE whale_trades_v2 DROP COLUMN user_id"))
        print("تم حذف العمود user_id بنجاح.")
    except Exception as e:
        print("تخطي الحذف (العمود غير موجود أو تم حذفه مسبقًا):", e)

    try:
        # إضافة العمود بصيغة صحيحة
        connection.execute(text("ALTER TABLE whale_trades_v2 ADD COLUMN user_id BIGINT NOT NULL"))
        print("تمت إضافة العمود user_id بنجاح.")
    except Exception as e:
        print("خطأ أثناء إضافة العمود:", e)
