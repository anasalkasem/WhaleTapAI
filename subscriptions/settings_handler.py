# subscriptions/settings_handler.py

from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.keyboards import main_menu_keyboard

async def handle_settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle settings menu."""
    query = update.callback_query
    user_id = query.from_user.id  # <-- ضروري نجيب الآيدي

    await query.answer()
    await query.edit_message_text(
        text="⚙️ Settings:",
        reply_markup=main_menu_keyboard(user_id)  # <-- وتمريره هنا
    )
