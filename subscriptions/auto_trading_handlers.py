from telegram import Update
from telegram.ext import CallbackContext
from subscriptions.auto_trading_keyboard import auto_trading_keyboard  # أو auto_trading_keyboard_multilang

async def handle_auto_trading(update: Update, context: CallbackContext):
    user_lang = update.effective_user.language_code or "ar"  # كشف لغة المستخدم

    # تمرير اللغة للكيبورد
    keyboard = auto_trading_keyboard(lang=user_lang)

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text="⚙️ إعدادات التداول التلقائي:\n"
             "قم بتعديل المعايير أدناه لإنشاء أو تخصيص نمط التداول التلقائي الخاص بك.",
        reply_markup=keyboard
    )
async def handle_stop_copying(update: Update, context: CallbackContext):
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text="🛑 تم إيقاف نسخ صفقات الحيتان مؤقتًا.\nيمكنك إعادة التفعيل من القائمة الرئيسية."
    )
