
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def plans_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⭐ اشتراك PRO - 10 USDT/شهر", callback_data="plan_pro")]
    ])
