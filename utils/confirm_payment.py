# utils/confirm_payment.py

from sqlalchemy import update, select
from models.database import Session
from models.payment_requests import PaymentRequest
from models.models import Subscription
import datetime

def confirm_payment_request(user_id):
    session = Session()

    # تحديث حالة الدفع إلى "confirmed"
    session.execute(
        update(PaymentRequest)
        .where(PaymentRequest.user_id == user_id)
        .values(status="confirmed")
    )

    # التأكد إذا المستخدم عنده اشتراك سابق
    existing = session.execute(
        select(Subscription).where(Subscription.user_id == user_id)
    ).scalar_one_or_none()

    if existing:
        session.execute(
            update(Subscription)
            .where(Subscription.user_id == user_id)
            .values(plan_type="pro", created_at=datetime.datetime.utcnow())
        )
    else:
        new_sub = Subscription(
            user_id=user_id,
            plan_type="pro",
            created_at=datetime.datetime.utcnow()
        )
        session.add(new_sub)

    session.commit()
    session.close()
