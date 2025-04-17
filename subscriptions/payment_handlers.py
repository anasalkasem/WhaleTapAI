
from telegram import Update
from telegram.ext import ContextTypes
from .keyboards import crypto_payment_keyboard
from .db_utils import save_payment
from .subscription_plans import PLANS

async def handle_subscription_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "subscribe_pro":
        await query.edit_message_text(
            "💰 يرجى اختيار وسيلة الدفع:",
            reply_markup=crypto_payment_keyboard("pro")
        )

    elif data == "subscribe_free":
        success = save_payment(
            user_id=query.from_user.id,
            plan="free",
            payment_method="auto",
            amount=0,
            status="active"
        )
        if success:
            await query.edit_message_text(
                "🎉 تم تفعيل اشتراكك المجاني (صفقة واحدة يوميًا).\n"
                "لترقية الاشتراك استخدم /upgrade"
            )
        else:
            await query.edit_message_text("⚠️ حدث خطأ أثناء التفعيل، يرجى المحاولة لاحقًا")
    else:
        await query.edit_message_text("🚫 خيار غير معروف")
