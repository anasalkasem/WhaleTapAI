from models.database import Base, engine
from sqlalchemy import text
from models.auto_trading_settings import AutoTradingSettings

def init_db():
    # حذف الجدول إذا كان موجود
    with engine.connect() as connection:
        connection.execute(text("DROP TABLE IF EXISTS whale_trades_v2"))
        connection.commit()

    # إعادة إنشاء الجداول
    Base.metadata.create_all(bind=engine)
    print("✅ تمت إعادة إنشاء جدول whale_trades_v2 بنجاح.")
