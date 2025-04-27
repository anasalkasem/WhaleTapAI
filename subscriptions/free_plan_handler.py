from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.keyboards import main_menu_keyboard

async def handle_free_plan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle free plan subscription."""
    query = update.callback_query
    user_id = query.from_user.id  # جلب الآيدي

    await query.answer()
    await query.edit_message_text(
        text="✅ You have activated the Free Plan.\n\nEnjoy copying 1 trade per day!",
        reply_markup=main_menu_keyboard(user_id)  # تمرير الآيدي
    )
