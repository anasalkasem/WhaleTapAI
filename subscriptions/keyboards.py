from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("🤖 Auto-Trading", callback_data="auto_trading")],
        [
            InlineKeyboardButton("📥 Copy Latest Trade", callback_data="copy_trade"),
            InlineKeyboardButton("🧠 Smart Whale Insights", callback_data="smart_insights"),
        ],
        [
            InlineKeyboardButton("🛑 Stop Copying", callback_data="stop_copying"),
            InlineKeyboardButton("📊 My Portfolio", callback_data="my_stats"),
        ],
        [
            InlineKeyboardButton("⚙️ Settings", callback_data="settings"),
            InlineKeyboardButton("💳 Upgrade to PRO", callback_data="subscription_info"),
        ],
        [InlineKeyboardButton("🆓 Free Plan", callback_data="subscribe_free")],
    ]
    return InlineKeyboardMarkup(keyboard)
