from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def plans_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⭐ اشتراك PRO - 20$", callback_data="pay_pro_usdt")],
        [InlineKeyboardButton("🆓 اشتراك مجاني - تجربة محدودة", callback_data="pay_free_usdt")]
    ])

def crypto_payment_keyboard(plan: str):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔷 دفع بـ SOL", callback_data=f"pay_{plan}_sol")],
        [InlineKeyboardButton("💎 دفع بـ USDT", callback_data=f"pay_{plan}_usdt")]
    ])

def main_menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📈 نسخ صفقة الحوت", callback_data="copy_trade")],
        [InlineKeyboardButton("🧾 حالة الاشتراك", callback_data="subscription_status")]
    ])
