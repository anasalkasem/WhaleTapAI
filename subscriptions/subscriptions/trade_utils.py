from models.database import session
from models.database import Trade
from datetime import datetime

def save_trade(wallet_address, token_symbol, token_amount, transaction_type):
    trade = Trade(
        wallet_address=wallet_address,
        token_symbol=token_symbol,
        token_amount=token_amount,
        transaction_type=transaction_type,
        timestamp=datetime.utcnow()
    )
    session.add(trade)
    session.commit()
