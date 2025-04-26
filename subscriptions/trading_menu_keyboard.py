from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def trading_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🛒 Buy", callback_data="buy"),
            InlineKeyboardButton("💰 Sell", callback_data="sell")
        ],
        [
            InlineKeyboardButton("✈️ Copy Trades", callback_data="copy_trades"),
            InlineKeyboardButton("🤖 Auto-Trading", callback_data="auto_trading")
        ],
        [
            InlineKeyboardButton("📊 Limit Orders", callback_data="limit_orders"),
            InlineKeyboardButton("⚙️ Manual/Auto Switch", callback_data="manual_auto_switch")
        ],
        [
            InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="main_menu")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
