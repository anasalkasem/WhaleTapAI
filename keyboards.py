from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def plans_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("PRO Subscription - 10 USDT/month", callback_data="plan_pro")]
    ])

def crypto_payment_keyboard(plan: str):
    buttons = [
        [InlineKeyboardButton("Pay with SOL", callback_data=f"pay_{plan}_sol")],
        [InlineKeyboardButton("Pay with USDT", callback_data=f"pay_{plan}_usdt")]
    ]
    return InlineKeyboardMarkup(buttons)
