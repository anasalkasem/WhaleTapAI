from models.database import Base, engine
from sqlalchemy import text

# حذف الجدول إذا كان موجود
with engine.connect() as connection:
    connection.execute(text("DROP TABLE IF EXISTS whale_trades_v2 CASCADE;"))
    connection.commit()

# إعادة إنشائه من جديد
Base.metadata.create_all(bind=engine)

print("✅ تمت إعادة إنشاء جدول whale_trades_v2 بنجاح.")
from models.auto_trading_settings import AutoTradingSettings
