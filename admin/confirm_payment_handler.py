from telegram import Update
from telegram.ext import ContextTypes
from models.database import SessionLocal
from models.payment_requests import PaymentRequest
from models.user_subscriptions import UserSubscription  # تم التغيير هنا
import datetime

# ID الأدمن
ADMIN_ID = 6672291052

async def handle_confirm_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    await query.answer()

    if user_id != ADMIN_ID:
        await query.edit_message_text("❌ You are not authorized to confirm payments.")
        return

    db = SessionLocal()

    try:
        # الحصول على أول طلب دفع قيد الانتظار
        pending_payment = db.query(PaymentRequest).filter_by(status="pending").first()

        if not pending_payment:
            await query.edit_message_text("ℹ️ No pending payment requests found.")
            return

        # تحديث حالة الطلب
        pending_payment.status = "confirmed"

        # تحديث الاشتراك أو إنشاؤه
        subscription = db.query(UserSubscription).filter_by(user_id=pending_payment.user_id).first()
        if subscription:
            subscription.plan_type = "pro"
            subscription.created_at = datetime.datetime.utcnow()
        else:
            new_subscription = UserSubscription(
                user_id=pending_payment.user_id,
                plan_type="pro",
                created_at=datetime.datetime.utcnow()
            )
            db.add(new_subscription)

        db.commit()

        await query.edit_message_text(f"✅ Payment confirmed for user ID: {pending_payment.user_id}")

        try:
            await context.bot.send_message(
                chat_id=pending_payment.user_id,
                text="🎉 Your PRO subscription is now active. Enjoy unlimited access!"
            )
        except Exception as e:
            print(f"[Error] Failed to message user: {e}")

    except Exception as e:
        print(f"[Error] Payment confirmation failed: {e}")
    finally:
        db.close()
