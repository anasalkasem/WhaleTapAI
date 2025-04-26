# subscriptions/settings_handler.py

from telegram import Update
from telegram.ext import CallbackContext
from subscriptions.keyboards import settings_keyboard

async def handle_settings(update: Update, context: CallbackContext) -> None:
    """Displays the settings menu"""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="⚙️ Settings:",
        reply_markup=settings_keyboard()
    )
