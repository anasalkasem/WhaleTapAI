from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.keyboards.main_menu_keyboard_v2 import main_menu_keyboard

async def handle_ai_trading(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="🤖 Welcome to AI Trading!\n\nOur AI system helps you copy smart trades automatically based on top whales and technical signals.\n\n🚀 Smarter. Faster. Easier.\n\n(This feature is currently experimental.)",
        reply_markup=main_menu_keyboard()
    )
