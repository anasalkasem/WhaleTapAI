from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.main_menu import main_menu_keyboard

async def handle_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(
            "🚀 Welcome to WhaleTap!
Choose an option below:",
            reply_markup=main_menu_keyboard()
        )
    elif update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(
            "🚀 Welcome to WhaleTap!
Choose an option below:",
            reply_markup=main_menu_keyboard()
        )
