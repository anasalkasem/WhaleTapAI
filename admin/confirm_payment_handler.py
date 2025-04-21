from telegram import Update
from telegram.ext import ContextTypes
from utils.confirm_payment import confirm_payment_request

ADMIN_ID = 6672291052  # ← غيّره لو تغير رقمك لاحقًا

async def handle_confirm_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    if user_id != ADMIN_ID:
        await query.answer("❌ غير مصرح لك باستخدام هذا الأمر.", show_alert=True)
        return

    # مثال: استخدام user_id موجود مسبقًا (يمكنك لاحقًا تعديل الزر ليأخذ رقم محدد)
    confirm_payment_request(user_id)

    await query.answer("✅ تم تأكيد الدفع وتفعيل الاشتراك!", show_alert=True)
