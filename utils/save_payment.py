# utils/save_payment.py

from models.payment_requests import PaymentRequest
from models.database import get_db
import datetime

def save_payment_request(user_id, username, wallet_address, amount=20.0):
    db = get_db()
    payment = PaymentRequest(
        user_id=user_id,
        username=username,
        wallet_address=wallet_address,
        amount=amount,
        status="pending",
        created_at=datetime.datetime.utcnow()
    )
    db.add(payment)
    db.commit()
    db.close()
