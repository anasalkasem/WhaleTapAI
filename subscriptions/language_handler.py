from telegram import Update
from telegram.ext import ContextTypes
from models.user_settings import set_user_language
from subscriptions.keyboards import main_menu_keyboard

async def handle_language_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    lang_code = query.data.split("_")[-1]  # "lang_en" → "en"
    await set_user_language(user_id, lang_code)

    keyboard = main_menu_keyboard(lang_code, user_id)
    await query.edit_message_text("✅ Language updated successfully!", reply_markup=keyboard)
