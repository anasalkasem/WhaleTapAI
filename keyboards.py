from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def plans_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⭐ اشتراك PRO - 10 USDT/شهر", callback_data="plan_pro")]
    ])

def crypto_payment_keyboard(plan: str):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔷 دفع بـ SOL", callback_data=f"pay_{plan}_sol")],
        [InlineKeyboardButton("💎 دفع بـ USDT", callback_data=f"pay_{plan}_usdt")]
    ])