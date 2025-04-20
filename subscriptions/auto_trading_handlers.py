from telegram import Update
from telegram.ext import CallbackContext
from subscriptions.auto_trading_keyboard import auto_trading_keyboard

# زر: 🤖 Auto-Trading
async def handle_auto_trading(update: Update, context: CallbackContext):
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text="⚙️ إعدادات التداول التلقائي:\n"
             "قم بتعديل المعايير أدناه لإنشاء أو تخصيص نمط التداول التلقائي الخاص بك.",
        reply_markup=auto_trading_keyboard()
    )

# زر: 🛑 Stop Copying
async def handle_stop_copying(update: Update, context: CallbackContext):
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text="🛑 تم إيقاف نسخ صفقات الحيتان مؤقتًا.\n"
             "يمكنك إعادة التفعيل من القائمة الرئيسية."
    )
await query.edit_message_text(
    text="⚙️ إعدادات التداول التلقائي:\nقم بتعديل المعايير أدناه لإنشاء أو تخصيص نمط التداول التلقائي الخاص بك.",
    reply_markup=auto_trading_keyboard()
)
