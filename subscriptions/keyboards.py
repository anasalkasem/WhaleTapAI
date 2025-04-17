from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def plans_keyboard():
    keyboard = [
        [InlineKeyboardButton("⭐ اشتراك PRO - 20$", callback_data="subscribe_pro")],
        [InlineKeyboardButton("🆓 اشتراك مجاني (1 صفقة/يوم)", callback_data="subscribe_free")],
        [InlineKeyboardButton("⏬ نسخ الصفقة الآن", callback_data="copy_trade")]  # تم التعديل هنا
    ]
    return InlineKeyboardMarkup(keyboard)


def crypto_payment_keyboard(plan: str):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💠 → دفع SOL", callback_data=f"pay_sol:{plan}")],
        [InlineKeyboardButton("💎 → دفع USDT", callback_data=f"pay_usdt:{plan}")]
    ])


def main_menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📈 نسخ صفقة الحوت", callback_data="copy_trade")],
        [InlineKeyboardButton("📋 حالة الاشتراك", callback_data="check_subscription")]
    ])
