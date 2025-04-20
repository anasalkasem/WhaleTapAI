from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.keyboards import settings_keyboard, language_selection_keyboard
from db_utils import set_user_language, get_user_language

# دالة عرض قائمة الإعدادات
async def handle_settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = get_user_language(user_id)

    if lang == "en":
        text = "⚙️ <b>Settings Menu:</b>\nYou can customize your preferences below."
    elif lang == "es":
        text = "⚙️ <b>Menú de configuración:</b>\nPersonaliza tus preferencias a continuación."
    else:
        text = "⚙️ <b>قائمة الإعدادات:</b>\nيمكنك تعديل تفضيلاتك من الخيارات التالية."

    keyboard = settings_keyboard(lang)

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text=text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )

# دالة عرض لوحة اختيار اللغة
async def handle_change_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text="🌐 اختر لغتك المفضلة:",
        reply_markup=language_selection_keyboard()
    )

# دالة حفظ اللغة المختارة في قاعدة البيانات
async def handle_language_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    selected_lang = query.data.replace("lang_", "")
    user_id = query.from_user.id
    set_user_language(user_id, selected_lang)

    await query.edit_message_text(
        text="✅ تم تغيير اللغة." if selected_lang == "ar" else
             "✅ Language changed." if selected_lang == "en" else
             "✅ Idioma cambiado.",
        reply_markup=settings_keyboard(lang=selected_lang)
    )

# دالة تفعيل/إلغاء التنبيهات
async def handle_toggle_notifications(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = get_user_language(user_id)

    current_status = context.user_data.get("notifications_enabled", True)
    context.user_data["notifications_enabled"] = not current_status

    if lang == "en":
        text = "🔔 Notifications have been turned " + ("off." if current_status else "on.")
    elif lang == "es":
        text = "🔔 Las notificaciones han sido " + ("desactivadas." if current_status else "activadas.")
    else:
        text = "🔔 تم " + ("إيقاف" if current_status else "تفعيل") + " التنبيهات."

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text=text)
