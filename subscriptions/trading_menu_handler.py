from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.keyboards import main_menu_keyboard  # هذا لاستدعاء الكيبورد الرئيسي
from subscriptions.trading_menu_keyboard import trading_menu_keyboard  # هذا لاستدعاء كيبورد التداول

# التعامل مع واجهة التداول Trading Menu
async def handle_trading_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="🛒 Welcome to Trading Menu!\n\nChoose an option below:",
        reply_markup=trading_menu_keyboard()
    )

# التعامل مع العودة للقائمة الرئيسية Main Menu
async def handle_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id  # جلب الآيدي

    keyboard = main_menu_keyboard(user_id)  # تمرير اليوزر آيدي للكيبورد

    await query.answer()
    await query.edit_message_text(
        text="🏠 Main Menu:",
        reply_markup=keyboard
    )
