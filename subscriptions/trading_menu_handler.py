from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.trading_menu_keyboard import trading_menu_keyboard

async def handle_trading_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="📈 Trading Options:",
        reply_markup=trading_menu_keyboard()
    )
