from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# ✅ جلب رابط الاتصال من متغيرات البيئة
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("❌ DATABASE_URL is missing! Please check your Railway environment variables.")

# ✅ إعداد الاتصال بقاعدة البيانات
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ إنشاء قاعدة النماذج
Base = declarative_base()

# ✅ نموذج جدول صفقات الحيتان
class WhaleTrade(Base):
    __tablename__ = "whale_trades_v2"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)
    whale_wallet = Column(String, nullable=False)
    token_address = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    trade_type = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

# ✅ نموذج جدول طلبات الدفع
class PaymentRequest(Base):
    __tablename__ = "payment_requests"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)
    username = Column(String, nullable=True)
    wallet_address = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)

# ✅ دالة للحصول على جلسة قاعدة البيانات
def get_db_session():
    return SessionLocal()

# ✅ دالة التحقق من وجود طلب دفع معلّق
def has_pending_payment_request(user_id: int) -> bool:
    db = get_db_session()
    result = db.query(PaymentRequest).filter_by(user_id=user_id, status="pending").first()
    db.close()
    return result is not None
