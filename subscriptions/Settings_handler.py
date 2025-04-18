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
