from telegram import Update
from telegram.ext import ContextTypes
from .main_menu import main_menu_keyboard

async def handle_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "⬇️ هذه هي القائمة الرئيسية:",
        reply_markup=main_menu_keyboard()
    )
