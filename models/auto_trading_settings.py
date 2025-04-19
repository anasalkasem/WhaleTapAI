from sqlalchemy import Column, Integer, Float, String, Boolean, BigInteger
from models.database import Base

class AutoTradingSettings(Base):
    __tablename__ = "auto_trading_settings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(BigInteger, nullable=False, unique=True)  # ID مستخدم تيليجرام

    amount_per_trade = Column(Float, default=0.0)
    total_amount = Column(Float, default=0.0)

    gas_fee_buy = Column(Float, default=0.0)
    gas_fee_sell = Column(Float, default=0.0)

    tip_buy = Column(Float, default=0.0)
    tip_sell = Column(Float, default=0.0)

    mev_protection = Column(Boolean, default=False)

    slippage_buy = Column(Float, default=20.0)
    slippage_sell = Column(Float, default=20.0)

    # شروط الشراء
    buy_condition_volume_min = Column(Float, default=0.0)
    buy_condition_volume_max = Column(Float, default=0.0)
    buy_condition_change_1m = Column(Float, default=0.0)
    buy_condition_change_5m = Column(Float, default=0.0)
    buy_condition_transactions_5s = Column(Integer, default=0)
    buy_condition_transactions_1m = Column(Integer, default=0)

    # شروط البيع
    sell_condition_change_1m = Column(Float, default=0.0)
    sell_condition_last_blocks_volume = Column(Float, default=0.0)
