from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def plans_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("⭐ اشتراك PRO - 20$", callback_data="subscribe_pro"),
            InlineKeyboardButton("🆓 نسخة تجريبية", callback_data="subscribe_free")
        ],
        [InlineKeyboardButton("📋 كيف يعمل البوت؟", callback_data="how_it_works")],
        [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
    ])

def crypto_payment_keyboard(plan: str):
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("💠 دفع بـ SOL", callback_data=f"pay_sol_{plan}"),
            InlineKeyboardButton("💎 دفع بـ USDT", callback_data=f"pay_usdt_{plan}")
        ],
        [InlineKeyboardButton("↩️ رجوع", callback_data="back_to_plans")],
        [InlineKeyboardButton("🏠 الرئيسية", callback_data="main_menu")]
    ])

def main_menu_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📈 نسخ صفقات الحيتان", callback_data="copy_trade"),
            InlineKeyboardButton("💳 اشتراك", callback_data="subscription_info")
        ],
        [
            InlineKeyboardButton("📊 إحصائياتي", callback_data="my_stats"),
            InlineKeyboardButton("⚙️ الإعدادات", callback_data="settings")
        ],
        [InlineKeyboardButton("ℹ️ المساعدة", callback_data="help")]
    ])
