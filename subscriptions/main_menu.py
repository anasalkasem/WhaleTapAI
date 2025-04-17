from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("شراء", callback_data="buy")],
        [InlineKeyboardButton("بيع", callback_data="sell")],
        [InlineKeyboardButton("نسخ التداول", callback_data="copy_trade")],
        [InlineKeyboardButton("التداول التلقائي", callback_data="auto_trade")],
        [InlineKeyboardButton("إيقاف النسخ", callback_data="stop_copy")],
        [InlineKeyboardButton("المحفظة", callback_data="wallet")],
        [InlineKeyboardButton("إنشاء محفظة", callback_data="create_wallet")],
        [InlineKeyboardButton("تنبيهات", callback_data="alerts")],
        [InlineKeyboardButton("حد الخسارة", callback_data="stop_loss")],
        [InlineKeyboardButton("تغيير اللغة", callback_data="change_language")]
    ]
    return InlineKeyboardMarkup(keyboard)
