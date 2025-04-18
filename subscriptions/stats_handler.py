from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.keyboards import main_menu_keyboard

async def handle_my_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    text = (
        f"📊 <b>إحصائيات حسابك</b>\n\n"
        f"👤 المستخدم: {user.first_name}\n"
        f"🆔 معرف: <code>{user.id}</code>\n"
        f"✅ نوع الاشتراك: نسخة تجريبية\n"
        f"📈 صفقات منسوخة: 1\n"
        f"🕒 آخر صفقة: قبل 4 ساعات\n\n"
        f"💡 قم بالترقية للحصول على إحصائيات كاملة وتنبيهات مباشرة!"
    )

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text=text, reply_markup=main_menu_keyboard(), parse_mode="HTML")
