from models.database import get_db
from models.payment_requests import PaymentRequest

def has_pending_payment(user_id):
    db = get_db()
    pending_payment = db.query(PaymentRequest).filter(
        PaymentRequest.user_id == user_id,
        PaymentRequest.status == "pending"
    ).first()
    db.close()
    return pending_payment is not None
