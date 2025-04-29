from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# ✅ جلب رابط الاتصال من متغير البيئة
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("❌ DATABASE_URL is missing! Please check your Railway environment variables.")

# ✅ إنشاء الاتصال والجلسة
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ تعريف قاعدة النماذج
Base = declarative_base()

# ✅ جدول صفقات الحيتان الرسمي
class WhaleTrade(Base):
    __tablename__ = "whale_trades_v2"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)
    whale_wallet = Column(String, nullable=False)
    token_address = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    trade_type = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<WhaleTrade(wallet='{self.whale_wallet}', token='{self.token_address}', amount={self.amount})>"

# ✅ جدول طلبات الدفع (استيراد النموذج من ملفه)
from models.payment_requests import PaymentRequest

# ✅ دالة التحقق من وجود طلب دفع معلّق للمستخدم
def has_pending_payment_request(user_id: int) -> bool:
    db = SessionLocal()
    try:
        result = db.query(PaymentRequest).filter_by(user_id=user_id, status="pending").first()
        return result is not None
    finally:
        db.close()
