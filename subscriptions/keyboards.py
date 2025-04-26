from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🛒 Trading", callback_data="menu_trading"),
            InlineKeyboardButton("🤖 AI Trading", callback_data="ai_trading"),
            InlineKeyboardButton("🏦 Wallet", callback_data="menu_wallet"),
        ],
        [
            InlineKeyboardButton("⚙️ Settings", callback_data="settings"),
            InlineKeyboardButton("📈 Portfolio", callback_data="my_stats"),
        ],
        [
            InlineKeyboardButton("🧠 Smart Insights", callback_data="smart_insights"),
            InlineKeyboardButton("🛑 Stop Copying", callback_data="stop_copying"),
        ],
        [
            InlineKeyboardButton("💳 Subscribe PRO", callback_data="subscribe_pro"),
            InlineKeyboardButton("🆓 Free Plan", callback_data="subscribe_free"),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)
