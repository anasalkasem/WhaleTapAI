from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.keyboards import main_menu_keyboard
from models.user_settings import get_user_language

async def handle_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = await get_user_language(user_id)
    keyboard = main_menu_keyboard(lang)  # ✅ تم تصحيح هذا السطر
    await update.message.reply_text("Welcome to WhaleTap!", reply_markup=keyboard)
async def handle_subscription_info(update, context):
    await update.callback_query.answer()
    await update.callback_query.message.edit_text("Subscription Info: PRO = $20/month\nFree Plan = 1 trade/day")
