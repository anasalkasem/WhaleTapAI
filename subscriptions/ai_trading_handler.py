# subscriptions/ai_trading_handler.py

from telegram import Update
from telegram.ext import ContextTypes
from keyboards import main_menu_keyboard  # استيراد صحيح من ملف keyboards.py

async def handle_ai_trading(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        text="🤖 Welcome to AI Trading!\n\nHere you will soon be able to activate smart AI-powered trading strategies!",
        reply_markup=main_menu_keyboard()
    )
