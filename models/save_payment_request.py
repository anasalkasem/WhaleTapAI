# utils/save_payment_request.py

from models.database import get_db
from models.payment_requests import PaymentRequest
from datetime import datetime

async def save_payment_request(user_id: int, username: str, wallet_address: str):
    db = get_db()
    new_request = PaymentRequest(
        user_id=user_id,
        username=username,
        wallet_address=wallet_address,
        amount=20.0,
        status="pending",
        created_at=datetime.utcnow()
    )
    db.add(new_request)
    db.commit()
    db.close()
