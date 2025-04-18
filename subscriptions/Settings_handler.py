from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def handle_settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🌐 تغيير اللغة", callback_data="change_language")],
        [InlineKeyboardButton("🔔 التنبيهات", callback_data="toggle_notifications")],
        [InlineKeyboardButton("🏠 العودة للقائمة", callback_data="main_menu")]
    ])

    text = (
        "⚙️ <b>إعدادات الحساب</b>\n\n"
        "اختر الإعداد الذي تريد تغييره:"
    )

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text=text, reply_markup=keyboard, parse_mode="HTML")
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def handle_change_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🇺🇸 English", callback_data="lang_en"),
            InlineKeyboardButton("🇸🇦 العربية", callback_data="lang_ar"),
            InlineKeyboardButton("🇪🇸 Español", callback_data="lang_es")
        ],
        [InlineKeyboardButton("🏠 العودة", callback_data="settings")]
    ])

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text="🌐 اختر لغتك المفضلة:",
        reply_markup=keyboard
    )
# حفظ اللغة المختارة مؤقتاً في context.user_data
async def handle_language_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    lang_code = query.data.split("_")[1]
    context.user_data["lang"] = lang_code

    lang_name = {"en": "English", "ar": "العربية", "es": "Español"}.get(lang_code, "English")

    await query.edit_message_text(
        text=f"✅ تم تغيير اللغة إلى: {lang_name}\n\n(التأثير الكامل سيتم تطبيقه قريبًا.)"
    )
from telegram import Update
from telegram.ext import ContextTypes
from .keyboards import settings_keyboard

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
    await update.callback_query.edit_message_text(text=text, reply_markup=keyboard, parse_mode="HTML")
