from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("شراء", callback_data="buy"), InlineKeyboardButton("بيع", callback_data="sell")],
        [InlineKeyboardButton("نسخ التداول", callback_data="copy_trade"), InlineKeyboardButton("التداول التلقائي", callback_data="auto_trade")],
        [InlineKeyboardButton("أوامر الحد", callback_data="limit_orders")],
        [InlineKeyboardButton("العملات لدي", callback_data="my_tokens"), InlineKeyboardButton("المحفظة", callback_data="wallet")],
        [InlineKeyboardButton("المساعدة", callback_data="help")],
        [InlineKeyboardButton("المحفظة الذكية", callback_data="smart_wallet"), InlineKeyboardButton("امتداد", callback_data="extension")],
        [InlineKeyboardButton("الإعدادات", callback_data="settings"), InlineKeyboardButton("الإحالات", callback_data="referrals")]
    ]
    return InlineKeyboardMarkup(keyboard)
