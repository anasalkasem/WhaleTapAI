from telegram import Update
from telegram.ext import ContextTypes
from .db_utils import save_payment

async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    data = query.data

    if data == "pay_pro":
        await query.edit_message_text(
            "✅ تم استلام طلب الاشتراك الخاص بك.\n"
            "سيتحقق المسؤول من الدفع ويُفعّل حسابك خلال وقت قصير."
        )
        # يتم حفظ الطلب بقاعدة البيانات بانتظار التفعيل اليدوي
        save_payment(user_id, "pro", "manual")

    elif data == "pay_free":
        await query.edit_message_text(
            "🎉 تم تفعيل اشتراكك المجاني المحدود (صفقة واحدة يوميًا)."
        )
        save_payment(user_id, "free", "auto")
