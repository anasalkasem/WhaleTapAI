from models.database import WhaleTrade, get_db
from datetime import datetime
def copy_whale_trade(user_id: int, wallet_address: str, token: str, amount: float, tx_hash: str):
    db = get_db()
    trade = WhaleTrade(
        user_id=user_id,
        wallet_address=wallet_address,
        token=token,
        amount=amount,
        tx_hash=tx_hash,
        copied_at=datetime.utcnow()
    )
    db.add(trade)
    db.commit()
    db.close()
    return trade
