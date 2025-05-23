from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.keyboards import main_menu_keyboard

async def handle_stop_copying(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle stop copying action."""
    query = update.callback_query
    user_id = query.from_user.id  # جلب الآيدي

    await query.answer()
    await query.edit_message_text(
        text="Copying has been stopped.",
        reply_markup=main_menu_keyboard(user_id)  # تمرير الآيدي للكيبورد
    )
