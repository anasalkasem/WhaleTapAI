from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def plans_keyboard():
    keyboard = [
        [InlineKeyboardButton("⭐ اشتراك PRO - 20$", callback_data="pay_pro")],
        [InlineKeyboardButton("🆓 اشتراك مجاني محدود (1 صفقة/يوم)", callback_data="pay_free")]
    ]
    return InlineKeyboardMarkup(keyboard)
