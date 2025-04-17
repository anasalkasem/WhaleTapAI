from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("نسخ التداول", callback_data="copy_trade")],
        [InlineKeyboardButton("التداول التلقائي", callback_data="auto_trade")],
        [InlineKeyboardButton("إيقاف النسخ", callback_data="stop_copy")],
        [InlineKeyboardButton("المحفظة", callback_data="wallet")],
        [InlineKeyboardButton("إنشاء محفظة", callback_data="create_wallet")],
        [InlineKeyboardButton("تنبيهات", callback_data="alerts")],
        [InlineKeyboardButton("حد الخسارة", callback_data="stop_loss")],
        [InlineKeyboardButton("تغيير اللغة", callback_data="change_lang")],
        # --- القائمة السفلية ---
        [InlineKeyboardButton("⭐ اشتراك PRO - 20$", callback_data="subscribe_pro")],
        [InlineKeyboardButton("🆓 نسخة تجريبية", callback_data="subscribe_free")],
        [InlineKeyboardButton("📋 كيف يعمل البوت؟", callback_data="how_it_works")],
        [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)
