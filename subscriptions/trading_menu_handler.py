from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.keyboards import main_menu_keyboard
from subscriptions.main_menu_keyboard import main_menu_keyboard  # <-- اضفناه

async def handle_trading_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="🛒 Welcome to Trading Menu!\n\nChoose an option below:",
        reply_markup=trading_menu_keyboard()
    )

async def handle_main_menu(update, context):
    query = update.callback_query
    user_id = query.from_user.id

    keyboard = main_menu_keyboard(user_id)

    await query.answer()
    await query.edit_message_text(
        text="🏠 Main Menu:",
        reply_markup=keyboard
    )
