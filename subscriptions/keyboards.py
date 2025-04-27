from telegram import InlineKeyboardButton, InlineKeyboardMarkup

ADMIN_IDS = [6672291052]  # ضع معرفك كأدمن هنا

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
        ],
    ]

    # هنا الشرط: لو المستخدم هو الأدمن أضف زر تأكيد الدفع
    if user_id in ADMIN_IDS:
        keyboard.append(
            [InlineKeyboardButton("✅ Confirm Payment", callback_data="admin_confirm_payment")]
        )

    return InlineKeyboardMarkup(keyboard)
