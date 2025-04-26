# subscriptions/stats_handler.py

from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.keyboards import main_menu_keyboard

async def handle_my_stats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle My Portfolio stats view."""
    query = update.callback_query
    await query.answer()

    text = (
        "📊 <b>My Portfolio</b>\n\n"
        "• Total copied trades: 0\n"
        "• Total profit: 0.00 USD\n"
        "• Current subscription: Free Plan\n\n"
        "Upgrade to PRO to unlock full portfolio features!"
    )

    await query.edit_message_text(
        text=text,
        parse_mode="HTML",
        reply_markup=main_menu_keyboard()
    )
