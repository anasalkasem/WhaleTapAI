# subscriptions/settings_handler.py

from telegram import Update
from telegram.ext import CallbackContext
from subscriptions.keyboards import main_menu_keyboard

async def handle_settings(update: Update, context: CallbackContext) -> None:
    """Handle settings menu."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="⚙️ Settings:",
        reply_markup=main_menu_keyboard()
    )
