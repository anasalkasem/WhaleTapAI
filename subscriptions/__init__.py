from models.models import Base
from models.database import engine

def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ تمت إعادة إنشاء جدول whale_trades_v2 بنجاح.")
