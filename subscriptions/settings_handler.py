from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.keyboards import settings_keyboard, language_selection_keyboard

# دالة عرض قائمة الإعدادات
async def handle_settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "ar")

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


# دالة حفظ اللغة المختارة مؤقتًا في context.user_data
async def handle_language_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # استخراج رمز اللغة من callback_data
    lang_code = query.data.split("_")[1]
    context.user_data["lang"] = lang_code

    # اسم اللغة لعرض رسالة التأكيد
    lang_name = {
        "en": "English",
        "ar": "العربية",
        "es": "Español"
    }.get(lang_code, "English")

    await query.edit_message_text(
        text=f"✅ تم تغيير اللغة إلى: {lang_name}\n\n(التأثير الكامل سيتم تطبيقه قريبًا.)"
    )
# دالة تفعيل/إلغاء التنبيهات
async def handle_toggle_notifications(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "ar")
    current_status = context.user_data.get("notifications_enabled", True)

    # تبديل الحالة
    context.user_data["notifications_enabled"] = not current_status

    if lang == "en":
        text = "🔔 Notifications have been turned " + ("off." if current_status else "on.")
    elif lang == "es":
        text = "🔔 Las notificaciones han sido " + ("desactivadas." if current_status else "activadas.")
    else:
        text = "🔔 تم " + ("إيقاف" if current_status else "تفعيل") + " التنبيهات."

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text=text)
