from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("📥 Copy Latest Trade", callback_data="copy_trade"),
            InlineKeyboardButton("🤖 Auto-Trading", callback_data="auto_trading")
        ],
        [
            InlineKeyboardButton("🛑 Stop Copying", callback_data="stop_copying"),
            InlineKeyboardButton("📊 My Portfolio", callback_data="portfolio")
        ],
        [
            InlineKeyboardButton("⚙️ Settings", callback_data="settings"),
            InlineKeyboardButton("🧠 Smart Whale Insights", callback_data="whale_insights")
        ],
        [
            InlineKeyboardButton("💳 Upgrade to PRO", callback_data="subscribe_pro"),
            InlineKeyboardButton("🆓 Free Plan", callback_data="subscribe_free")
        ],
        [
            InlineKeyboardButton("📋 How It Works?", callback_data="how_it_works"),
            InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
