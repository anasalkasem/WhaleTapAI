from telegram import Update
from telegram.ext import ContextTypes
from .main_menu import main_menu_keyboard

async def handle_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    if query:
        await query.answer()
        await query.edit_message_text(
            text="🚀 Welcome to WhaleTap!\n\nChoose an option below to get started:",
            reply_markup=main_menu_keyboard()
        )
    elif update.message:
        await update.message.reply_text(
            text="🚀 Welcome to WhaleTap!\n\nChoose an option below to get started:",
            reply_markup=main_menu_keyboard()
        )
    else:
        print("⚠️ No query or message found in update.")
from telegram import Update
from telegram.ext import ContextTypes

async def handle_copy_trade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        "📥 Copied the latest whale trade successfully!"
    )
