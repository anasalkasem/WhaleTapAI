# admin/confirm_payment_handler.py

from telegram import Update
from telegram.ext import ContextTypes
from models.database import get_db
from models.payment_requests import PaymentRequest
from models.models import Subscription

# معرف الأدمن الخاص بك (غيره إلى رقمك)
ADMIN_ID = 6672291052

async def handle_confirm_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.callback_query.from_user.id
    query = update.callback_query

    await query.answer()

    # تحقق أن المستخدم هو الأدمن فقط
    if user_id != ADMIN_ID:
        await query.edit_message_text("❌ You are not authorized to confirm payments.")
        return

    db = get_db()

    # البحث عن أول طلب دفع معلق
    payment = db.query(PaymentRequest).filter_by(status="pending").first()

    if payment:
        # تحديث حالة الدفع إلى confirmed
        payment.status = "confirmed"

        # تحديث الاشتراك إلى PRO
        subscription = db.query(Subscription).filter_by(user_id=payment.user_id).first()
        if subscription:
            subscription.subscription_type = "pro"
        else:
            # إذا لا يوجد اشتراك سابق، ننشئ واحد
            new_subscription = Subscription(user_id=payment.user_id, subscription_type="pro")
            db.add(new_subscription)

        db.commit()
        await query.edit_message_text("✅ Payment has been confirmed and PRO subscription activated!")
    else:
        await query.edit_message_text("ℹ️ No pending payment requests found.")

    db.close()
