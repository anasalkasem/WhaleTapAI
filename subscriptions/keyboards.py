from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from models.database import has_pending_payment_request  # ✅ تعديل اسم الملف الصحيح

ADMIN_IDS = [6672291052]

def main_menu_keyboard(user_id):
    keyboard = [
        [
            InlineKeyboardButton("🛒 Trading", callback_data="trading"),
            InlineKeyboardButton("🤖 AI Trading", callback_data="auto_trading"),
            InlineKeyboardButton("💼 Wallet", callback_data="wallet"),
        ],
        [
            InlineKeyboardButton("⚙️ Settings", callback_data="settings"),
            InlineKeyboardButton("📊 Portfolio", callback_data="my_stats"),
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

    if user_id in ADMIN_IDS and has_pending_payment_request(user_id):
        keyboard.append(
            [InlineKeyboardButton("✅ Confirm Payment", callback_data="admin_confirm_payment")]
        )

    return InlineKeyboardMarkup(keyboard)
