# subscriptions/insights_handler.py

from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.keyboards import main_menu_keyboard

async def handle_smart_insights(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle Smart Whale Insights action."""
    query = update.callback_query
    await query.answer()

    text = (
        "🧠 <b>Smart Whale Insights</b>\n\n"
        "Here are the latest notable whale activities:\n"
        "🔹 120,000 SOL purchased by wallet A1...2F.\n"
        "🔹 50,000 USDT transferred to Binance by wallet B9...C3.\n"
        "🔹 New whales joined the market today.\n\n"
        "Stay updated with real-time whale movements to make smarter decisions!"
    )

    await query.edit_message_text(
        text=text,
        parse_mode="HTML",
        reply_markup=main_menu_keyboard()
    )
