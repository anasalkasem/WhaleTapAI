from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

# دالة عرض القائمة الرئيسية
async def handle_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = main_menu_keyboard()
    text = "🚀 Welcome to WhaleTap!\nChoose an option below to get started."

    if update.message:
        await update.message.reply_text(text, reply_markup=keyboard)
    elif update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=text, reply_markup=keyboard)


# === كيبوردات البوت ===

def main_menu_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📈 نسخ صفقات الحيتان", callback_data="copy_trade"),
            InlineKeyboardButton("💳 اشتراك", callback_data="subscription_info")
        ],
        [
            InlineKeyboardButton("📊 إحصائياتي", callback_data="my_stats"),
            InlineKeyboardButton("⚙️ الإعدادات", callback_data="settings")
        ],
        [InlineKeyboardButton("ℹ️ المساعدة", callback_data="help")]
    ])

def plans_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("⭐ اشتراك PRO - 20$", callback_data="subscribe_pro"),
            InlineKeyboardButton("🆓 نسخة تجريبية", callback_data="subscribe_free")
        ],
        [InlineKeyboardButton("📋 كيف يعمل البوت؟", callback_data="how_it_works")],
        [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
    ])

def crypto_payment_keyboard(plan: str):
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("💠 دفع بـ SOL", callback_data=f"pay_sol_{plan}"),
            InlineKeyboardButton("💎 دفع بـ USDT", callback_data=f"pay_usdt_{plan}")
        ],
        [InlineKeyboardButton("↩️ رجوع", callback_data="back_to_plans")],
        [InlineKeyboardButton("🏠 الرئيسية", callback_data="main_menu")]
    ])
