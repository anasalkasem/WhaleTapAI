from models.database import WhaleTrade
from models.database import get_db
from datetime import datetime

def save_fake_trade(user_id: int, wallet: str):
    db = get_db()
    trade = WhaleTrade(
        user_id=user_id,
        whale_wallet=wallet,
        token_address="FakeToken123",
        amount=1000.0,
        trade_type="buy",
        timestamp=datetime.utcnow()
    )
    db.add(trade)
    db.commit()
    db.close()
