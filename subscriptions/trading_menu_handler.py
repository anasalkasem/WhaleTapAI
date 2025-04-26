# subscriptions/trading_menu_handler.py

from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.trading_menu_keyboard import trading_menu_keyboard

async def handle_trading_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """عرض قائمة التداول."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="🛒 Trading Menu:\n\nChoose an action below:",
        reply_markup=trading_menu_keyboard()
    )
