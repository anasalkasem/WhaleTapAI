from telegram import Update
from telegram.ext import ContextTypes
from models.database import get_db
from models.payment_requests import PaymentRequest
from models.models import Subscription
import datetime

async def handle_confirm_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    admin_id = query.from_user.id

    await query.answer()

    db = get_db()

    # 1. البحث عن أول دفعة قيد الانتظار
    pending_payment = db.query(PaymentRequest).filter(
        PaymentRequest.status == "pending"
    ).first()

    if not pending_payment:
        await query.edit_message_text("❌ No pending payment requests found.")
        db.close()
        return

    # 2. تحديث حالة الدفع إلى 'confirmed'
    pending_payment.status = "confirmed"
    pending_payment.confirmed_at = datetime.datetime.utcnow()

    # 3. تحديث أو إنشاء اشتراك PRO للمستخدم
    subscription = db.query(Subscription).filter(
        Subscription.user_id == pending_payment.user_id
    ).first()

    if subscription:
        subscription.plan = "pro"
        subscription.active = True
        subscription.updated_at = datetime.datetime.utcnow()
    else:
        new_sub = Subscription(
            user_id=pending_payment.user_id,
            plan="pro",
            active=True,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow()
        )
        db.add(new_sub)

    db.commit()
    db.close()

    # 4. إرسال رسالة للأدمن بتأكيد العملية
    await query.edit_message_text(f"✅ Payment confirmed and PRO plan activated for user ID: {pending_payment.user_id}")

    # 5. إرسال رسالة للمستخدم مباشرة
    try:
        await context.bot.send_message(
            chat_id=pending_payment.user_id,
            text="🎉 Congratulations! Your PRO subscription is now active. Enjoy unlimited trading features!"
        )
    except Exception as e:
        print(f"Failed to send message to user: {e}")
