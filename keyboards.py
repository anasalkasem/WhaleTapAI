from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def plans_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⭐ اشتراك PRO - 10 USDT/شهر", callback_data="pay_pro_usdt")],
        [InlineKeyboardButton("💎 اشتراك PRO - 10 SOL/شهر", callback_data="pay_pro_sol")]
    ])