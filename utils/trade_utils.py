from models.database import WhaleTrade, SessionLocal
from datetime import datetime

def save_fake_trade(user_id: int, wallet: str):
    db = SessionLocal()
    try:
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
    except Exception as e:
        db.rollback()
        print(f"Error saving trade: {e}")
    finally:
        db.close()
