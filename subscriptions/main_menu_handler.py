from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


def main_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("📥 Copy Latest Trade", callback_data="copy_trade"),
            InlineKeyboardButton("🤖 Auto-Trading", callback_data="auto_trading")
        ],
        [
            InlineKeyboardButton("🛑 Stop Copying", callback_data="stop_copying"),
            InlineKeyboardButton("📊 My Portfolio", callback_data="my_portfolio")
        ],
        [
            InlineKeyboardButton("⚙️ Settings", callback_data="settings"),
            InlineKeyboardButton("🧠 Smart Whale Insights", callback_data="smart_insights")
        ],
        [
            InlineKeyboardButton("💳 Upgrade to PRO", callback_data="upgrade_pro"),
            InlineKeyboardButton("🆓 Free Plan", callback_data="free_plan")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


async def handle_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = main_menu_keyboard()
    text = "🚀 Welcome to WhaleTap!\nChoose an option below to get started."

    if update.message:
        await update.message.reply_text(text, reply_markup=keyboard)

    elif update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
