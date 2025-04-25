from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.keyboards import main_menu_keyboard, plans_keyboard
from models.user_settings import get_user_language

# عرض القائمة الرئيسية
async def handle_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = await get_user_language(user_id)
    keyboard = main_menu_keyboard(lang, user_id)
    await update.message.reply_text("Welcome to WhaleTap!", reply_markup=keyboard)

# عرض معلومات الاشتراك
async def handle_subscription_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.message.edit_text(
        "Subscription Info: PRO = $20/month\nFree Plan = 1 trade/day"
    )

# الرجوع إلى خطط الاشتراك
async def handle_back_to_plans(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = await get_user_language(user_id)
    keyboard = plans_keyboard(lang)
    await update.callback_query.answer()
    await update.callback_query.message.edit_text("اختر خطة الاشتراك:", reply_markup=keyboard)
