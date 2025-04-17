from telegram import InlineKeyboardButton, InlineKeyboardMarkup

PLANS = {
    "pro": {
        "price": 10,
        "currency": "USDT",
        "duration": "شهري",
        "features": [
            "تتبع 10 محافظ حيتان",
            "تنبيهات فورية",
            "دعم فني مخصص"
        ],
        "crypto": ["USDT", "SOL"]
    }
}

def handle_subscription_buttons():
    keyboard = [
        [InlineKeyboardButton("🆓 نسخة تجريبية", callback_data="subscribe_free")],
        [InlineKeyboardButton("⭐ اشتراك PRO - 20$", callback_data="subscribe_pro")]
    ]
    return InlineKeyboardMarkup(keyboard)
