from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.keyboards import settings_keyboard, language_selection_keyboard

# عرض قائمة الإعدادات
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

# عرض اختيار اللغة
async def handle_change_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text="🌐 اختر لغتك المفضلة:",
        reply_markup=language_selection_keyboard()
    )

# حفظ اللغة المختارة
async def handle_language_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    lang_code = query.data.split("_")[1]
    context.user_data["lang"] = lang_code

    lang_name = {
        "en": "English",
        "ar": "العربية",
        "es": "Español"
    }.get(lang_code, "English")

    await query.edit_message_text(
        text=f"✅ تم تغيير اللغة إلى: {lang_name}\n\n(التأثير الكامل سيتم تطبيقه قريبًا.)"
    )
