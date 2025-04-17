from models.database import WhaleTrade, get_db
from datetime import datetime

def save_trade_data(user_id: int, wallet: str, token: str, amount: float, tx_type: str, timestamp: str):
    db = get_db()
    trade = WhaleTrade(
        user_id=user_id,
        whale_wallet=wallet,
        token_address=token,
        amount=amount,
        trade_type=tx_type,
        timestamp=timestamp
    )
    db.add(trade)
    db.commit()
    db.close()
