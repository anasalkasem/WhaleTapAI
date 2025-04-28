# admin/confirm_payment_handler.py

from telegram import Update
from telegram.ext import ContextTypes
from models.database import get_db
from models.payment_requests import PaymentRequest
from models.models import Subscription
import datetime

# ID الأدمن
ADMIN_ID = 6672291052

async def handle_confirm_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    await query.answer()

    # السماح للأدمن فقط
    if user_id != ADMIN_ID:
        await query.edit_message_text("❌ You are not authorized to confirm payments.")
        return

    db = get_db()

    try:
        # البحث عن أول دفعة قيد الانتظار
        pending_payment = db.query(PaymentRequest).filter(PaymentRequest.status == "pending").first()

        if not pending_payment:
            await query.edit_message_text("ℹ️ No pending payment requests found.")
            return

        # تحديث حالة الدفع
        pending_payment.status = "confirmed"
        pending_payment.confirmed_at = datetime.datetime.utcnow()

        # تحديث أو إنشاء اشتراك PRO
        subscription = db.query(Subscription).filter(Subscription.user_id == pending_payment.user_id).first()
        if subscription:
            subscription.plan_type = "pro"
            subscription.created_at = datetime.datetime.utcnow()
        else:
            new_subscription = Subscription(
                user_id=pending_payment.user_id,
                plan_type="pro",
                created_at=datetime.datetime.utcnow()
            )
            db.add(new_subscription)

        db.commit()

        # إرسال رسالة تأكيد للأدمن
        await query.edit_message_text(f"✅ Payment confirmed for user ID: {pending_payment.user_id}")

        # إرسال رسالة للمستخدم
        try:
            await context.bot.send_message(
                chat_id=pending_payment.user_id,
                text="🎉 Your PRO subscription is now active. Enjoy unlimited access!"
            )
        except Exception as e:
            print(f"[Error] Failed to send message to user: {e}")

    except Exception as e:
        print(f"[Error] Exception during payment confirmation: {e}")
    finally:
        db.close()
