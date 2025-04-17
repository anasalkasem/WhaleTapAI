from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def subscription_buttons():
    keyboard = [
        [
            InlineKeyboardButton("نسخة تجريبية 🆓", callback_data="subscribe_free"),
            InlineKeyboardButton("اشتراك PRO - 20$", callback_data="subscribe_pro"),
        ],
        [InlineKeyboardButton("كيف يعمل البوت؟ 📋", callback_data="how_it_works")],
        [InlineKeyboardButton("القائمة الرئيسية 🏠", callback_data="main_menu")],
    ]
    return InlineKeyboardMarkup(keyboard)
