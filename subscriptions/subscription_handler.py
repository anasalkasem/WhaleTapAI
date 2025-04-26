# subscriptions/main_menu_handler.py

from telegram import Update
from telegram.ext import CallbackContext
from subscriptions.keyboards import main_menu_keyboard

async def handle_main_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    if query:
        await query.answer()
        await query.edit_message_text(
            text="Welcome to WhaleTap!",
            reply_markup=main_menu_keyboard()
        )
    else:
        await update.message.reply_text(
            text="Welcome to WhaleTap!",
            reply_markup=main_menu_keyboard()
        )

async def handle_subscription_info(update: Update, context: CallbackContext):
    query = update.callback_query
    if query:
        await query.answer()
        await query.edit_message_text(
            text="Choose your subscription plan:",
            reply_markup=main_menu_keyboard()
        )
