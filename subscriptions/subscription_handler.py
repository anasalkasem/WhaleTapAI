from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.keyboards import main_menu_keyboard  # استدعاء الكيبورد الصح

async def handle_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    keyboard = main_menu_keyboard(user_id)  # تمرير user_id هنا

    await query.answer()
    await query.edit_message_text(
        text="🏠 Main Menu:",
        reply_markup=keyboard
    )
