from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.keyboards import main_menu_keyboard

async def handle_smart_insights(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (
        "🧠 <b>Smart Whale Insights</b>\n\n"
        "📍 Highlighted whale activities over the past 24 hours:\n"
        "• Purchase of 120,000 SOL to wallet ...A1...\n"
        "• Transfer of 50,000 USDT to Binance from wallet ...B9...\n"
        "• New whales entering the market today.\n\n"
        "Stay updated with the smartest whale moves!"
    )

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text=text,
        parse_mode="HTML",
        reply_markup=main_menu_keyboard()
    )
