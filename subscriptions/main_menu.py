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
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("📥 Copy Latest Trade", callback_data="copy_trade"),
            InlineKeyboardButton("🤖 Auto-Trading", callback_data="auto_trading")
        ],
        [
            InlineKeyboardButton("🛑 Stop Copying", callback_data="stop_copying"),
            InlineKeyboardButton("📊 My Portfolio", callback_data="portfolio")
        ],
        [
            InlineKeyboardButton("⚙️ Settings", callback_data="settings"),
            InlineKeyboardButton("🧠 Smart Whale Insights", callback_data="whale_insights")
        ],
        [
            InlineKeyboardButton("💳 Upgrade to PRO", callback_data="upgrade_pro"),
            InlineKeyboardButton("🆓 Free Plan", callback_data="free_plan")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
